# buhtig
Difficulty: ★★★★☆☆☆☆☆☆	&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Solved by: youstube_  
![chall-img](media/chall.png)  

## Details:
- Author: bhavya_32
- Category: OSINT
- Score acquired: 495 (7 solves)

## Description:
> linus-r8000
 

## Write up:
We were only given a description of `linus-r8000`. Reading the title `buhtig` I realized it's just github spelt backwards, so naturally I went to github and search for this person.

[Click here for the Github Profile](https://www.github.com/linus-r8000)
![repo-img](media/repo.png)

From there we can see there is a repository from them called [`the-final-checkpoint`](https://github.com/linus-r8000/the-final-checkpoint), with a [README.md](https://github.com/linus-r8000/the-final-checkpoint/blob/main/README.md) and a [don't open this.jpeg](https://github.com/linus-r8000/the-final-checkpoint/blob/main/don't%20open%20this.jpeg).

However, it just looks like red herring as there doesn't seem like anything special. So I divert my attention to other parts of their Github.

Looking this accounts [project page](https://github.com/linus-r8000?tab=projects), there is a [closed project](https://github.com/users/linus-r8000/projects/4).

![project-img](media/projects.png)

Click on it reveals a view sheet with morse code.  
```-. . ...- . .-./--. --- -. -. .-/--. .. ...- ./-.-- --- ..-/..- .--. --..--/-. . ...- . .-./--. --- -. -. .-/.-.. . -/-.-- --- ..-/-.. --- .-- -.```  
I'll leave the decoding to you guys :> Moving on...  

Checking out the project detail, we see there is there is a weird README for it.
![projdesc-img](media/projdesc.png)  
This screamed ROT8000 characters (I use cyberchef way too much), so I put this to [cyberchef with ROT8000 parameter](https://gchq.github.io/CyberChef/#recipe=ROT8000()&input=57GZ57Gq57G857G857KA57G457G757GtIOexsuexvCDnsbXnsZ3nsbPnsZXnsZznsZ3nsYrnsZbnsoDnsbHnsYznsZ0&oenc=65001&ieol=CRLF&oeol=NEL), and it decoded to this:  
`Password is lTjLSTAMwhCT`

Password? where would I be able to use a password?  
At this point, I struggled looking for a place to use a password. I tried logging into the account with the password, using steghide with the passphrase on the red herring image, but to no avail. Asking the author in desperation, they said everything is within the Github (hence the name of the challenge).  

So I continue to search for anything I missed in the Github.

Moving back to the Github repository (`the-final-checkpoint`) from `linus-r8000`, it doesn't sit right with me that it's just a red herring. There has to be something I missed. So I dug deeper, and clicked on [activity for the repository](https://github.com/linus-r8000/the-final-checkpoint/activity). Bingo.
![activity-img](media/activity.png)  

Now we see there were deleted branches which we couldn't see before. Clicking on the latest act of deleting branch `xmain`, and comparing the changes, we see there is a [commit message](https://github.com/linus-r8000/the-final-checkpoint/commit/c0290e6b1577478b78491552a99bde11f5432bc8) to the delete commit.  

![commit-img](media/commit.png)  
A [cryptpad.fr](https://cryptpad.fr/pad/#/2/pad/view/pfGQ11vUPCXfuMmEb6-QBdk36dIBItyFPkN1gCTyxak/p/embed/) link. This has to be where to use the password! <sub>hehehe</sub>

## My Solution:
Going to [the url](https://cryptpad.fr/pad/#/2/pad/view/pfGQ11vUPCXfuMmEb6-QBdk36dIBItyFPkN1gCTyxak/p/embed/), it asked for a password.  
![crypt-img](media/crypt.png)  
Putting the password `lTjLSTAMwhCT` in reveals a text file with the flag  
![flag](media/flag.png)

Flag: `07CTF{d4n6l1n6_c0mm17_r3v34l5_l057_533cr375}`

## Conclusion:
Fun chall, short OSINT, and didn't know about Github project before. Just wish I didn't tunnel visioned at the viewsheet for that long. Could've blooded this :sob:
## Shoutout:
- bhavya_32 (Author)
- BlitzHack (My team)
- 0bscuri7y (Organizers)

<br>
<sub>
    Tags: Github, OSINT, Commit, Project
</sub>
