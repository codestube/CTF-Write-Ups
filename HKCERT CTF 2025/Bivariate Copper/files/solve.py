#!/usr/bin/env python3
import re
import math
import mpmath as mp
from Crypto.Util.number import long_to_bytes
from sympy import symbols, Poly, expand, Integer, Matrix
from sympy.ntheory import factorint
from sympy.matrices.normalforms import hermite_normal_form

x, y = symbols('x y')

# ---------- custom LLL (mpmath float GS) ----------
def lll_reduction(B, delta=mp.mpf(3)/4, dps=250):
    mp.mp.dps = dps
    n = len(B)
    m = len(B[0])
    B = [list(map(int, v)) for v in B]

    mu = [[mp.mpf(0) for _ in range(n)] for __ in range(n)]
    Bstar = [[mp.mpf(0) for _ in range(m)] for __ in range(n)]
    Bnorm = [mp.mpf(0) for _ in range(n)]

    def compute_gs(start=0):
        for i in range(start, n):
            b_i = [mp.mpf(val) for val in B[i]]
            for j in range(i):
                num = mp.mpf(0)
                for a, bs in zip(B[i], Bstar[j]):
                    num += mp.mpf(a) * bs
                mu[i][j] = num / Bnorm[j]
                if mu[i][j] != 0:
                    for k in range(m):
                        b_i[k] -= mu[i][j] * Bstar[j][k]
            Bstar[i] = b_i
            norm = mp.mpf(0)
            for val in Bstar[i]:
                norm += val * val
            Bnorm[i] = norm
            mu[i][i] = mp.mpf(1)

    compute_gs(0)
    k = 1
    while k < n:
        # size reduction
        for j in range(k - 1, -1, -1):
            q = int(mp.nint(mu[k][j]))
            if q != 0:
                for t in range(m):
                    B[k][t] -= q * B[j][t]
                for l in range(j):
                    mu[k][l] -= mp.mpf(q) * mu[j][l]
                mu[k][j] -= mp.mpf(q)

        # Lovasz condition
        lhs = Bnorm[k]
        rhs = (delta - mu[k][k - 1] ** 2) * Bnorm[k - 1]
        if lhs >= rhs:
            k += 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            compute_gs(k - 1)
            k = max(k - 1, 1)

    return B

# ---------- parse instance from chall.py pasted output ----------
def parse_params_from_chall_py(path):
    data = open(path, "r", encoding="utf-8", errors="ignore").read()
    m = re.search(r"'''(.*?)'''", data, re.S)
    if not m:
        raise RuntimeError("No pasted output block (''' ... ''') found in chall.py")
    block = m.group(1).replace("\r", "")
    names = ["e", "N", "c", "k", "r1", "r2", "leak1", "leak2"]
    out = {}
    for name in names:
        mm = re.search(rf"\b{name}\s*=\s*([0-9]+)", block)
        if not mm:
            raise RuntimeError(f"Missing {name} in pasted output block")
        out[name] = int(mm.group(1))
    return out

# ---------- build polynomial f(x,y) congruent 0 mod p ----------
def build_f(p, k, r1, r2, leak1, leak2, shift_bits=244):
    X = 1 << shift_bits
    A1 = leak1 * X
    A2 = leak2 * X
    # f(x,y) = (r1-r2)(A1+x)(A2+y) - k((A2+y)-(A1+x))  == 0 (mod p)
    f_expr = (r1 - r2) * (A1 + x) * (A2 + y) - k * ((A2 + y) - (A1 + x))
    f_poly = Poly(expand(f_expr), x, y, domain="ZZ")
    # reduce coefficients mod p to centered reps to stabilize lattice
    terms = {}
    for mon, coef in f_poly.terms():
        c = int(coef) % p
        if c > p // 2:
            c -= p
        terms[mon] = c
    f_mod = sum(Integer(c) * (x ** mon[0]) * (y ** mon[1]) for mon, c in terms.items())
    return A1, A2, X, Poly(f_mod, x, y, domain="ZZ")

# ---------- build standard bivariate Coppersmith lattice ----------
def build_lattice_total_degree(p, f_poly, m=2, d=2, X=1<<244, Y=1<<244):
    # monomials of total degree <= d*m
    monoms = []
    for total in range(d*m + 1):
        for a in range(total + 1):
            b = total - a
            monoms.append((a, b))
    scales = [(X ** a) * (Y ** b) for a, b in monoms]

    polys = []
    for kpow in range(m + 1):
        bound = d * (m - kpow)
        for i in range(bound + 1):
            for j in range(bound - i + 1):
                g = (x ** i) * (y ** j) * (f_poly.as_expr() ** kpow) * (p ** (m - kpow))
                polys.append(Poly(expand(g), x, y, domain="ZZ"))

    # coefficient rows
    rows = []
    for poly in polys:
        dct = {mon: int(coef) for mon, coef in poly.terms()}
        row = [dct.get((a, b), 0) * scale for (a, b), scale in zip(monoms, scales)]
        rows.append(row)

    # IMPORTANT: compute Z-basis of row-lattice via HNF of transpose (column lattice)
    A = Matrix(rows)      # (many x dim)
    Ht = hermite_normal_form(A.T)  # gives square basis for column lattice
    B = Ht.T  # row basis matrix (dim x dim)
    basis_rows = [[int(v) for v in B.row(i)] for i in range(B.rows)]
    return monoms, scales, basis_rows

def vec_to_poly(v, monoms, scales):
    expr = 0
    for (a, b), scale, val in zip(monoms, scales, v):
        val = int(val)
        if val == 0:
            continue
        q, r = divmod(val, scale)
        if r != 0:
            # not expected; keep rational
            q = val / scale
        expr += Integer(q) * (x ** a) * (y ** b)
    return Poly(expr, x, y, domain="ZZ")

# ---------- attempt extraction and solve ----------
def try_solve(chall_py_path):
    P = parse_params_from_chall_py(chall_py_path)
    e = P["e"]
    N = P["N"]
    c = P["c"]
    k = P["k"]
    r1 = P["r1"]
    r2 = P["r2"]
    leak1 = P["leak1"]
    leak2 = P["leak2"]

    # factor N (q is 25-bit)
    fac = factorint(N)
    qs = [q for q in fac.keys() if q.bit_length() <= 30]
    if not qs:
        raise RuntimeError("Could not find small q")
    q = qs[0]
    p = N // q

    # decrypt message (hint)
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    msg = pow(c, d, N)
    print("[+] decrypted message:", long_to_bytes(msg))

    # build f
    A1, A2, Xb, f = build_f(p, k, r1, r2, leak1, leak2, shift_bits=244)
    X = 1 << 244
    Y = 1 << 244

    # lattice
    monoms, scales, basis_rows = build_lattice_total_degree(p, f, m=2, d=2, X=X, Y=Y)
    print("[+] lattice dim:", len(basis_rows))

    # LLL
    red = lll_reduction(basis_rows, delta=mp.mpf(3)/4, dps=260)

    # try first few vectors -> polynomials; search for small root by brute resultant strategy
    polys = [vec_to_poly(v, monoms, scales) for v in red[:8]]

    # check candidates by solving pairwise resultants over small primes + CRT is omitted here
    # Instead, we directly try to solve by elimination with sympy for each pair (may work if exact)
    from sympy import resultant
    for i in range(len(polys)):
        for j in range(i+1, len(polys)):
            pi = polys[i]
            pj = polys[j]
            if pi.total_degree() == 0 or pj.total_degree() == 0:
                continue
            # eliminate y
            R = resultant(pi.as_expr(), pj.as_expr(), y)
            Rx = Poly(R, x, domain="ZZ")
            # try to find an integer x root by scanning small factors of Rx mod small primes is better,
            # but here we use sympy factor and check linear factors
            fac = Rx.factor_list()[1]
            for fct, exp in fac:
                if fct.degree() == 1:
                    a, b = map(int, fct.all_coeffs())
                    if a != 0 and (-b) % a == 0:
                        x0 = (-b) // a
                        # solve y from pi
                        yi = Poly(pi.as_expr().subs(x, x0), y, domain="ZZ")
                        facy = yi.factor_list()[1]
                        for fy, _ in facy:
                            if fy.degree() == 1:
                                ay, by = map(int, fy.all_coeffs())
                                if ay != 0 and (-by) % ay == 0:
                                    y0 = (-by) // ay
                                    if 0 <= x0 < X and 0 <= y0 < Y:
                                        # verify with original congruence
                                        t1 = A1 + x0
                                        t2 = A2 + y0
                                        if ((r1-r2)*t1*t2 - k*(t2-t1)) % p != 0:
                                            continue
                                        m1 = (k * pow(t1, -1, p) - r1) % p
                                        m2 = (k * pow(t2, -1, p) - r2) % p
                                        if m1 != m2:
                                            continue
                                        flag = long_to_bytes(m1)
                                        print("[+] FLAG:", flag.decode())
                                        return

    print("[-] Did not extract the root. Increase LLL strength / adjust basis.")

if __name__ == "__main__":
    try_solve("./chall.py")
