# Off By One
Difficulty: ★★★☆☆☆☆☆☆☆	&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Solved by: codestube (youstube_)  
![chall-img](media/chall.png)  

## Details:
- Author: Connor Chang
- Category: Forensic
- Score acquired: 497

## Description:
>i hid a qr inside a qr
>
>[hidden.png](files/hidden.png)

## Write up:
We were given an QR code image:
![QR-code](files/hidden.png)

I went straight to some [online QR-Code Scanner](https://qrscanner.net/) and scanned the QR code to see what it is. You probably could've guessed it.

![result](media/scan-result.png)&emsp;&emsp;<sub> youtube link with dQw4... why am I not surprised...</sub>

Being an obvious rick-roll attempt <sub>(yes you didn't get me Connor, not this time)</sub>, I started to look into the image itself.

When the image is opened on my browser, it shows the image dimensions as well. It is a `963 x 964` .png image file, tying back to the title of this challenge (<b>Off By One</b>).

![dimension](media/dimension.png)

Surely there is something in that hidden in that `1 x 963` pixel line right? Upon my ***microscopic*** inspections, nothing seems to be out of the ordinary, until I tried using the eyedropper (color select) tools on my image editing software (Here I am using [Aseprite](https://www.aseprite.org/)). by selecting it pixel to pixel, I can check if there are different colors that just looks similar.

https://github.com/user-attachments/assets/b184480b-4433-4fe9-8abb-4349131cf77d


**Bingo!** We have found another "Off By One" reference :D

Seems like that top line's "white" color is off by 1b value in RGB.Let's try to extract that whole line and see if its the same for others!

## My Solution:
First, I use bucket fill tool to fill all outer white colors with black (or any other colors) to better highlight the top line.

https://github.com/user-attachments/assets/ad308457-79fe-4f4f-9dc0-2dd95f76fe78

Then, I select that single line of pixels and extract it.
**![single-line](media/single-line.png)**

At first, I though this looked a lot like morse codes, with some dots and dashes, but referring back to the description of the challenge `"hid a qr inside a qr"`, with the inconsistent dash and stop length, I suspect this is somehow another QR code.

**BUT HOW!?** how could this 963 pixel one-liner be a QR code? 

Looking at it closely, some length of the long "dashes" had the same pixel length, of 7 pixels. Almost as if it could be corners of a QR code... **THAT'S IT!**

**This one-liner image is just a X * Y image split to a single line!!** The question is what's the size.. or is it? <sub>*insert vsauce sound*</sub>

See, looking at this `1 x 963` image, you can see the trailing 122 black pixels, which seems very weird considering there is almost 0 chance a QR code has a full black LINES. So we can safely assume that thats just padding.

After removing that, while we could just brute every dimension possible, we can take a guess on the dimension based on the square root of the total pixel (since the dimension of a QR code is always a square).
$$\sqrt{963 - 122} = 29$$
And that, ladies and gentlemen, is the original QR code length. Now all we have to do is write a [simple python script](files/solve.py) to make the `1 x 963` one-liner image to a `29 x 29` QR Code.
<details>
<summary>Click to toggle code</summary>

```
from PIL import Image

im=Image.open("single-line.png")
w,h=im.size

cropped=im.crop((0,0,w-122,1))

px = list(cropped.getdata())[:841]
resized = Image.new("RGBA", (29, 29))
resized.putdata(px)
resized.save("final-qr.png")
```
</details>
Here is the final QR Code (Resized to view better):

![final-image](media/resized-final-qr.png)
![flag](media/flag.png)

> FLAG!! WOOHOO YAY I FOUND IT!!

## Final flag:
`scriptCTF{qrqrqrc0d3s}`

## Conclusion
This challenge was not hard at all, the fact that the chall title already gave clues on what the player should look for is a nice touch. While I want to be respectful and all, I think most player who solved this chall would agree that this is not a 497-point chall 💀 Even the author himself didn't believe in it as well. Anyway great chall and CTF by them! ![author's word](media/author.png)

## Shoutout
- [ScriptSorcerers](https://ctftime.org/team/284260) (The Organizers)
- Connor Chang (The author)
- ChatGPT (for giving me the script)

<br>
<sub>
	Tags: Forensic, scriptCTF, Image, QR code, Python
</sub>
