# Endless
Difficulty: ★★★★★★★★★☆	&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Solved by: youstube_ & BlitzHack  
![chall-img](media/chall.png)  

## Details:
- Author: blackth0rns
- Category: OSINT
- Score acquired: 498

## Description:
> The keyword is "AUTHOR".

> Its more than just a keyword. It's where you'll find the challenge itself. Go for it and search for it.

## Write up:
<b>
Fair warning: This is a longggggggg write-up of it, you should open a subway surfer clip on the side.
</b>

We were first told that this challenge would consist over 24 stage. So I'm gonna write this quick then refine it later on.

### 1st Stage: AUTHOR
With the keyword being author, the first query is the author themselves.  
Looking up blackth0rns on google returns a X, Middle, TikTok, Pinterest account. The correct one was the [Pinterest](https://in.pinterest.com/rottenpetals00/_created) (I think). ![pinterest-img](media/pinterest.png)  

### 2nd Stage: Pinterest
Looking at the only image that isnt wolf, it's a photo of a person standing towards sunlight. Reverse image searching it results in a [LinkedIn account](https://in.linkedin.com/in/shubhampundir?trk=public_post_feed-actor-image) with a guy wearing the same shirt called  Shubham Pundir.  
![reverse-search-img](media/reverse-search.png)  

### 3rd Stage: LinkedIn
In the LinkedIn account, you see a base64 string (it's not there anymore)
![linkedin-img](media/linkedin.png)

`WdB1jUEtLf9qsaF3SsUJC2RBuNhrUteDKUJPFMApRhasKWpRRCvAMe9OYzyRu3zgJbReuL9LuErcYy5WWPN0k1rgMXUrpOBINCvEefOLHeFHNgziTXGZrMpRFATQMdeyHUIrwsz5EWrbY2F2PjDckKDyNgGoHzb2M25Vr2IIOf8=`

### 4th Stage: Decipher
Initially decoding it will return nothing readable, but using vigenere with the key mentioned in the description `AUTHOR` and decoding it with base64 2 times, then reversing it returns a [Google doc link](https://docs.google.com/document/d/1j3P3sAMjv4-Z0NaDSpKk9e7TwLBWA96riVvyqaK4e_U/edit?usp=sharing). ([See cyberchef](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('AUTHOR')From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)Reverse('Character')&input=V2RCMWpVRXRMZjlxc2FGM1NzVUpDMlJCdU5oclV0ZURLVUpQRk1BcFJoYXNLV3BSUkN2QU1lOU9ZenlSdTN6Z0piUmV1TDlMdUVyY1l5NVdXUE4wazFyZ01YVXJwT0JJTkN2RWVmT0xIZUZITmd6aVRYR1pyTXBSRkFUUU1kZXlIVUlyd3N6NUVXcmJZMkYyUGpEY2tLRHlOZ0dvSHpiMk0yNVZyMklJT2Y4PQ&ieol=CRLF&oeol=NEL))

### 5th Stage: Google doc
Reading through the doc, we see there are many presumable reddit username (reddit username convention with underscore and 4 numbers at the end) in the doc, with the title being "ONE OF THEM IS RIGHT".

<details>
<summary>Click to see the distinct usernames</summary>

```
Patient_Diamond2316
Patient_Diamond1632
Patient_Diamond1236
Patient_Diamond2163
Patient_Diamond2631
Patient_Diamond2613
Patient_Diamond2361
```
</details>

### 6th Stage: Reddit user
So I tested each of them as reddit username, and [`Patient_Diamond2361`](https://www.reddit.com/user/Patient_Diamond2361/) returned a valid account. In their account, there is a [cryptic post](https://www.reddit.com/user/Patient_Diamond2361/comments/1mnm0kd/code/) about code, along a vanity url `/DNP83nftRTK/`  
![reddit-img](media/reddit3.png)

### 7th Stage: Instagram
As the post said this is a code for a post, I assume it's referring to Instagram. So I went ahead to [that post](https://www.instagram.com/p/DNP83nftRTK/).  
![instagram-img](media/instagram4.png)

### 8th Stage: metamorphosis_manga
At this point we were stuck, so asking the author, he send me this:
```
i wanted to set a point of view through this stage. 
metamorphosis manga (about which ive heard from reddit and insta) has a very sad ending where girl kinda suicides.
metamorphosis novel(also about which ive heard from reddit) has a very sad story which depicts how a man was treated throughout the story.

both of them has same name and their stories align with topic of bad influence emitted by society and how society made both of them drive mad. 

So this message

metamorphosis_manga: you dont want to know   
metamorphosis_novel: youll eventually know


depicts that manga one is something which is so disturbing you dont want to know about it while novel depicts a story which you'll know about in future because of the way society operates
```

From this, it seems the manga one is something we should know about (since they don't want us to know about it). Running sherlock on `metamorphosis_manga` reveals it has a [pastebin account](https://pastebin.com/u/metamorphosis_manga) along with 2 pastebin post.
### 9th Stage: Pastebin  
[1st post](https://pastebin.com/jkSzNxEH)
```
FeT-g/Y7xIiZB]+^J6Q&YHWBE;H.A(gND8^V
 
hmm?
```
[2nd post](https://pastebin.com/tbdghChq)  
`85 and 92 are my favorite number might as well use them somewhere.`

From these post and the unique encoded string, I [decoded it with base92](https://gchq.github.io/CyberChef/#recipe=From_Base92()&input=RmVULWcvWTd4SWlaQl0rXko2USZZSFdCRTtILkEoZ05EOF5W&ieol=CRLF&oeol=NEL), which decoded to a discord link.  
`https://discord.gg/vE69axXaeb`

### 10th Stage: Discord
From the discord server link, there is a text channel `#whatisit` with the message:  
`what do we call a cat full of boxes?? 🤔 Oh no wait it's box full of cats silly me (its a website)`  
Asking ChatGPT, it said that the website would be https://catbox.moe, a file upload website. Additionally, in the `#general` text channel, there was a pinned message: `2kbvac.png`  

From this, I suspect we need to check the png using the catbox website. So first I uploaded a random file up to the website, and looked at the URL. Realizing the upload server is at `https://files.catbox.moe/{filename}`, I changed the last part of the website to the pinned message text, returning a [QR code](https://files.catbox.moe/2kbvac.png).  
![telegram-qr-img](https://files.catbox.moe/2kbvac.png)

### 11th Stage: Fixing QR
In the middle of the QR code, you can 2 letters - tg, but we cant seem to scan it normally. This means this QR is broken in some way. Looking at the corners you see it's kinda "broken" with the circles not lining up. So we fixed the QR code just by "removing" the 3 corner squares, and rebuilding the smaller 3 corner circular squares, revealing a Telegram group invite.
![fixed-qr-img](media/fixed-qr.png)
> https://t.me/+lUPwRZ_lAd80YWE1

### 12th Stage: Telegram
In the Telegram group, there is a message from TheOneWhoSlays:  
![telegram-img](media/telegram.png)  
Due to my low attention span, I didn't read all of that, and only see keywords like YouTube, Cuco and phoenixsp7. So I search on youtube for a `Cuco phoenixsp7`, where the 1st result returned [this video](https://www.youtube.com/watch?v=Ka6boboYYXI&list=RDKa6boboYYXI&start_radio=1). 

### 13th Stage: YouTube
In the video comment section, a [link to another catbox.moe file](https://files.catbox.moe/j3eiz0.png) was given. 
![blur-img](https://files.catbox.moe/j3eiz0.png)

### 14th Stage: Reading / Decoding the text
This blurry text is hard to see, but not hard to read. We can make out some character that looks like `MJWGCY3UGA===` (I thought the 3 was a J, wrongly decoding the string and rabbit-holed for a bit, but luckily @demonster corrected me).  
This looked like a base32 encoded text, so naturally putting through [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base32('A-Z2-7%3D',true)&input=TUpXR0NZM1VHQT09PQ&ieol=CRLF&oeol=NEL) return the decodeD string `blact0`, seemingly similar to `blackth0rns`

### 15th Stage: blact0
Since from here, we don't have a lead on what this could mean, so I ran sherlock on it again, and found out they had a [pastebin account](https://pastebin.com/u/Blact0) again. There, [another post](https://pastebin.com/13cQNp3x) was created.

### 16th Stage: Pastebin
From [the post](https://pastebin.com/13cQNp3x), it writes:
```
28.6699053,77.193373
a restaurant which closes at 10:30 PM
///mystified.rare.begun (this is the additional code incase they ask you for secret)
```
Which is obvious that it is a coordinate to a place (The bottom line is a what3word location as well).

### 17th Stage: Google map
Pasting the coordinates to [Google map](https://www.google.com/maps/place/28%C2%B040'11.7%22N+77%C2%B011'36.1%22E/@28.66991,77.1907927,17z/data=!3m1!4b1!4m4!3m3!8m2!3d28.6699053!4d77.193373?entry=ttu&g_ep=EgoyMDI1MDkxMC4wIKXMDSoASAFQAw%3D%3D), it shows a random location in Delhi, India. We need to find a restaurant which closes at 10:30 PM (according to the post in pastebin).  
Clicking the restuarnt button and zooming closer to the given coords shows around 6 restaurants. From there we manually click on each restaurant until we found [this restaurant](https://www.google.com/maps/place/BTT+BITE+TONGUE+TINGLING/@28.6698569,77.1920899,18.59z/data=!4m11!1m3!2m2!1sRestaurants!6e5!3m6!1s0x390d03bdce300d85:0x9a158f1b51a66993!8m2!3d28.6698508!4d77.1933137!15sCgtSZXN0YXVyYW50c1oNIgtyZXN0YXVyYW50c5IBFGZhc3RfZm9vZF9yZXN0YXVyYW50mgEjQ2haRFNVaE5NRzluUzBWSlEwRm5UVVIzY1RSUFdrZDNFQUWqAUQQASoPIgtyZXN0YXVyYW50cygAMh4QASIa4iedZWtQTBEhPBWiwUE7GKzd5slXHymgamgyDxACIgtyZXN0YXVyYW50c-ABAPoBBAgAECY!16s%2Fg%2F11frnkm3hc?entry=ttu&g_ep=EgoyMDI1MDkxMC4wIKXMDSoASAFQAw%3D%3D), with the closing hour exactly at 10:30pm.

### 18th Stage: The restaurant
From the restaurant on Google map, we see a review by a familiar person, PhoeNiXSP7! They have placed a review on this specific restaurant:  
![review-png](media/review.png)  
```
musashi_the_one: bro i couldn't understand it
other: we studied AI together dude how can you not understand it.

BTW about food - food is not as good as it used to be, the quantity and quality is reduced ;-;
```

<sub>btw food is not as good, quantity and quality worsen, and you still gave 4 star... what else was in the restaurant :face_with_raised_eyebrow: </sub>

### 19th Stage: musashi_the_one
From the review, you can see a reference to a person / username musashi_the_one. So we ran sherlo- nah we were tired asf at this point, and sherlock always give false positives, so I just suggest to manually brute all known social media instead. We tried [Instagram](https://www.instagram.com/musashi_the_one) first, didn't work; tried [X (formerly known as Twitter)](https://x.com/musashi_the_one), and aha!

### 20th Stage: Twitter (now known as X)
In this Twitter account, there is [a post](https://x.com/musashi_the_one/status/1954847766170993014)
with a random UUID:
```
Hmm? What is it? How can I see your messages using this?

`6899c110-2de8-8010-81d0-6203517f8464`
```
This seemed weird at first, since UUID is an universally unique identifier that should b- unless?  

### 21th Stage: UUID
Thanks to my teammates (5h1kh4r & others) with their quick thinking (and perhaps using AI too much), they knew this was a share UUID for a chat log from a user using ChatGPT right away.  
So we quickly made [a random chat log](https://chatgpt.com/share/68c827b6-a634-8004-bb2c-c7bf74d5d0b7) and edited the last part to the particular UUID.

### 22th Stage: ChatGPT
Using [that link](https://chatgpt.com/share/6899c110-2de8-8010-81d0-6203517f8464) we just edited, it reveals a chat conversation from Anonymous and ChatGPT.
```
You said:
hmmmm wonder what dc3bfae33610 could be

ChatGPT said:
dc3bfae33610 looks like a hexadecimal string — specifically 12 hex characters (6 bytes).

A few possibilities for what it could represent:
- A MAC address fragment — 6 bytes is exactly the size of a MAC address, often written as dc:3b:fa:e3:36:10.
- You said:A raw binary value — could be part of a hash, a key, or an identifier.
- You said:An integer in hex — in decimal, 0xdc3bfae33610 = 241430711289232.
- Part of a cryptographic hash — could be the start or end of something like SHA1/SHA256 output.
- A timestamp — if interpreted in certain binary formats, though 6 bytes is unusual for Unix time.

If you tell me where you found it (log file, network packet, file header, etc.), I can narrow it down and maybe even decode it into something human-readable.

Where did you see dc3bfae33610?

You said:
probably its your rival.. haha lets just not talk about it now have a good day

ChatGPT said:
Haha, fair enough — I’ll let that mystery sit in the shadows for now.
You too — have a good one!
```

And from this conversation, we got `dc3bfae33610`, and when asked `"Where did you see dc3bfae33610?"`, the person replied `"probably its your rival"`, suggesting it's from another AI / LLM model.

### 23th Stage: GuessCT- wait no, its GuessLLM
Since ChatGPT released GPT-5, their previous rivals have been unmatched. However, there were always a few notorious candidates that was somewhat a contender to GPT, that includes the China Supreme DeepSeek AI, the MechaHitler Grok (@grok is this true?), the coding agent Claude; and so on. You know which AI ISN'T a rival to ChatGPT? **GOOGLE GEMINI**<sub> this is my own personal beef with it. i just think Gemini is a ragebaiting AI. </sub>  
Anyways! So I tried all different AI except for Gemini, but none of them had similar UUID that's in hex... and well...

### 24th Stage: Google Gemini
Launching Gemini's website and generating [a share link](https://g.co/gemini/share/7c7a190ac879) to a random chat log, then replacing the random hash to the one from the ChatGPT chat log, resulting in [this chat](https://gemini.google.com/share/dc3bfae33610):  
![gemini-img](media/gemini.png)

## My Solution:
Visually saw that flag, copied it, and pasted in the corresponding challenge submission flag input box.

Flag: `07CTF{b33n_4_l0ng_j0urn3y_1snt_it}`
## Conclusion:
This was one hell of a challenge, where me and my whole team actually participated together on a voice chat, while literally yawning and burning our lifes to not sleep. However, I do want to thank the author of this chall a lot as I bothered him way too much with this chall due to my incompetence and lack of understanding. Great chall overall! :fire:  

>Fun fact: This chall is not solvable in Hong Kong, Macau, or China due to restriction access of AI / LLM, and if you know me, I'm from Hong Kong :)
## Shoutout:
- blackth0rns / rottenp3tals (Author)
- BlitzHack (My team who helped me on this chall)
- 0bscuri7y (Organiser)
- ProtonVPN (For allowing me to use ChatGPT and Gemini)

<br>
<sub>
	Tags: OSINT, YouTube, X, Pastebin, Discord, Telegram, Reddit, Pinterest, QR code fixing, stegnography, AI, ChatGPT, Gemini, Google Map
</sub>