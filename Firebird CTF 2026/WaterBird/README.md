# WaterBird
Difficulty: ★★★★☆☆☆☆☆☆	&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Solved by: codestube (youstube_)  
![chall-img](media/chall.png)  


## Details:
- Author: 650
- Category: Miscellaneous
- Score acquired: 103 (35 Solves)

## Description:
> My friend is on a trip and sent me this photo. He said he will bring me on his next trip if I can find where this photo is taken! Can you help me find this place?

>The flag is in the format of firebird{<latitude>,<longitude>}, where latitude and longitude are coordinates in degree, rounded off to 3 decimal places. For example if the answer is Sydney Opera House at -33.856764, 151.215302, the flag would be firebird{-33.857,151.215}.

>

## Write up:
We were given this image:  
![given-img](media/WaterBird.jpg)  
<sub>funny how they named this challenge waterbird cuz... you know, firebird, waterbird? :D okay let's continue..</sub>  
So long story short, we have to figure out where this place is, and what better way to do this than to, you guessed it, ***Reverse image search*** it!  
![ris-img](media/GoogleRSI.png)
Huh, so we figured out that it could be in eastern China, Russia, and Japan (taken with a grain of salt since it's Gemini Overview <sub>I still hate it</sub>). Now how can we pinpoint the location of this place though...

We can see that picture does have hints of Japan / China according the the post above the gate, as well as the utility poles and the hill structure. Looking at the hut behind, the style of it is kind of leaning towards Japanese-vibe (with the slanted roof design thingy). So we can rule Russia out for now. In addition, the "bridge" and that "shop" the bird is covering has to be somewhat recognizable, or at the very least RIS-able, right? I really want to select / search the part behind the bird. However, can the AI STOP LOOKING AT THE BIRD AND FIGURE THE BACK OF THE BIRD? EVERY TIME I DO RIS IT GIVES ME INFORMATION ABOUT THE BIRD!!11  
![analysis-img](media/anaylsis.png)  
...

...

wait... could I just... draw the bird out?  
and I tried that. The RIS now looks at the black bird instead.  
![drawingout-img](media/WaterBirdless.jpg)  
Then it clicked for me. Instead of manually removing the bird, how about I just nano-banana the bird out of existence?
## My Amazing Solution
The one time I actually wanted Gemini to help me the most, is when Nano Banana is actually goated with image generation.  
![aichat-img](media/convo.png)
![gemini-img](media/Gemini_Generated_Image.png) * thanos snapped *  
and then we do our good ol' RIS technique:  
![result](media/result.png)  
The first result is exactly what we want! Now just slowly navigate to the shop, and where the dock is. After some careful navgiation you should find [this](https://maps.app.goo.gl/9K5dzQnz8Z7LRiGm8)!  
![finalpos-img](media/finalpos.png)  
Then just right click on the map to get the coords and round them to get the flag!

Flag: `firebird{35.670,135.277}`
## Conclusion:
Overall, this was a simple challenge, but the way I solved it actually amazed both myself and some other contestants as well (post-vc). I never thought that I would somehow have the bright idea of using Gemini to manip an image just for an OSINT chall, and I thought the solve was pretty funny so I decided to write this. Anyway huge shoutout to Firebird for org-ing this event, had a fun time! (Please invite flagaholic next year :pray:)
## Shoutout:
- Firebird (Organizer)
- Gemini Nano Banana (snap the bird)
- Myself (with that brilliant idea)

<br>
<sub>
	Tags: misc, osint, gemini, AI
</sub>