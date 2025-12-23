# solve.py

from PIL import Image
import struct
from pathlib import Path

AVIF_PATH = "sus.avif"


# -------------------------
# Part 1: stylesuxx LSB decode (32-bit length + payload bits in RGB LSBs)
# -------------------------
def bits_from_image_rgb_lsb(img: Image.Image):
    if img.mode != "RGB":
        img = img.convert("RGB")
    for r, g, b in img.getdata():
        yield r & 1
        yield g & 1
        yield b & 1


def read_u32_be_from_bits(bit_iter):
    v = 0
    for _ in range(32):
        v = (v << 1) | next(bit_iter)
    return v


def read_bytes_from_bits(bit_iter, nbytes):
    out = bytearray()
    for _ in range(nbytes):
        b = 0
        for _ in range(8):
            b = (b << 1) | next(bit_iter)
        out.append(b)
    return bytes(out)


def decode_stylesuxx_first(avif_path: str) -> str:
    img = Image.open(avif_path)
    it = bits_from_image_rgb_lsb(img)
    n = read_u32_be_from_bits(it)
    msg = read_bytes_from_bits(it, n)
    return msg.decode("utf-8", errors="replace")


# -------------------------
# Part 2: AVIF/MP4 stts covert channel (sample_delta 2-value RLE -> bits -> bytes)
# -------------------------
def u32be(buf: bytes, off: int) -> int:
    return struct.unpack(">I", buf[off : off + 4])[0]


def u64be(buf: bytes, off: int) -> int:
    return struct.unpack(">Q", buf[off : off + 8])[0]


def iter_boxes(buf: bytes, start: int, end: int):
    pos = start
    while pos + 8 <= end:
        size = u32be(buf, pos)
        typ = buf[pos + 4 : pos + 8].decode("latin1")
        hdr = 8

        if size == 1:
            size = u64be(buf, pos + 8)
            hdr = 16
        elif size == 0:
            size = end - pos

        if size < hdr or pos + size > end:
            return

        yield pos, size, typ, hdr
        pos += size


CONTAINERS = {
    "moov", "trak", "mdia", "minf", "stbl",
    "meta", "dinf", "udta", "moof", "traf", "mfra",
    "ipro", "sinf", "schi", "edts", "mvex", "tref", "stsd"
}


def find_all_boxes(buf: bytes, boxtype: str):
    out = []
    stack = [(0, len(buf))]
    while stack:
        s, e = stack.pop()
        for pos, size, typ, hdr in iter_boxes(buf, s, e):
            if typ == boxtype:
                out.append((pos, size, hdr))
            if typ in CONTAINERS:
                stack.append((pos + hdr, pos + size))
    return out


def bits_to_bytes_msb(bits):
    out = bytearray()
    for i in range(0, (len(bits) // 8) * 8, 8):
        b = 0
        for j in range(8):
            b = (b << 1) | bits[i + j]
        out.append(b)
    return bytes(out)


def decode_stts_last(avif_path: str) -> str:
    buf = Path(avif_path).read_bytes()
    stts_list = find_all_boxes(buf, "stts")
    if not stts_list:
        raise RuntimeError("stts box not found")

    pos, size, hdr = stts_list[0]
    o = pos + hdr

    entry_count = u32be(buf, o + 4)
    o += 8

    entries = []
    for _ in range(entry_count):
        sample_count = u32be(buf, o)
        sample_delta = u32be(buf, o + 4)
        o += 8
        entries.append((sample_count, sample_delta))

    uniq = sorted({sd for _, sd in entries})
    if len(uniq) != 2:
        raise RuntimeError(f"expected exactly 2 distinct sample_delta values, got {uniq}")

    lo, hi = uniq[0], uniq[1]

    bits = []
    for sc, sd in entries:
        bit = 0 if sd == lo else 1
        bits.extend([bit] * sc)

    msg = bits_to_bytes_msb(bits)
    return msg.decode("utf-8", errors="replace")


# -------------------------
# Glue
# -------------------------
def main():
    first_msg = decode_stylesuxx_first(AVIF_PATH)      # "first part:hkcert25{..._"
    last_msg = decode_stts_last(AVIF_PATH)            # "last part: ...}"

    first_part = first_msg.split("first part:")[1]
    second_part = last_msg.split("last part: ")[1]
    flag = first_part + second_part

    print("Extracted messages:")
    print(first_msg)
    print(last_msg)
    print("flag:", flag)


if __name__ == "__main__":
    main()
