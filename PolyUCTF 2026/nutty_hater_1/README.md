# nutty_hater_1

Difficulty: ★★★★☆☆☆☆☆☆ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Solved by: youstube_  
![chall-img](media/chall.png)  
![blood-img](media/blood.png)

## Details

- Author: Ryan
- Category: OSINT
- Score acquired: 111 (94 Solves)

## Description

> In one of the "Hater"'s posts, he posted images of his gameplay and ranted about other players.
>
> Identify the amount of damage he dealt to other players in the game and the amount of damage he took in the same game shown in the images.
>
> If the "Hater"'s dealt damage is 12345 and taken damage is 67890, the flag would be "PUCTF26{12345_67890}".
>
> Flag Format: `PUCTF26{\d{0,16}_\d{0,16}}`

## Write up

Previously on nutty_hater_0, we discovered the target social media account which was [`@nuttychud.bsky.social`](https://bsky.app/profile/nuttychud.bsky.social). We can then check out posts they have posted that relate to this challenge.  
We would see [this post](https://bsky.app/profile/nuttychud.bsky.social/post/3mfoh6dstuk2h) that has `images of his gameplay`:  
![post-img](media/post.png)  

If this is not obvious <sub>kudos to you</sub> , this is the game [League of Legends](https://www.leagueoflegends.com/), an extremely popular multiplayer online battle arena video game developed and published by Riot Games.  
Let's take a closer look at the two images:
![first-img](files/given_1.png)![second-img](files/given_2.png)

## My understanding

Let's go back to what details does the challenge want:  
> The hater's dealt damage and taken damage  

With that in mind, we are going to have to dig up the match detail of the match shown for the 2 images. This may seem difficult at first for non-gamers, but if you have played any competitive games in the past, a term called **`Tracker`** should be pretty familiar to you :>  

With a simple Google search, you would find several stat trackers for League of Legends, including [tracker.gg](https://tracker.gg), [op.gg](https://op.gg). For these trackers we would need to provide a name for it to lookup. Luckily, if we take a closer look at the images given, we would find the name `camenana`. We can use that as our entrypoint.

<sub>
  Sidenote: you can kinda guess the name of the player on the first image. If you've played League before, you would know that the blue bar above their character are "your" teammates, not "yourself". In the first image, the green bar is "you". Since we can see the ending character of your name is "..ud", you can take a wild guess and get their name to be nuttychud, exactly the name of this Bluesky account.
</sub>

## My Solution

We can use the tracker [op.gg](https://op.gg/) and lookup the player camenana:  
![search-img](media/search.png)  
![result-img](media/result.png)  

Here we can search the character that she was playing in the match. Thanks to my teammate ~~being a degen~~ with experience of the game, he told me that they are playing a champion called ***Syndra***. <sub> You can also just use AI to identify that character. </sub>
![syndra-img](media/syndra.png)  

**TA-DAAA!** We found the match that had our "hater's" account! `nuttychud`! Now we just click the down arrow and view [the details of that match.](https://op.gg/lol/summoners/tw/camenana-727/matches/ZP-GJLOl5EA0JfnbHbcYcbfUHYqD0bUm/1770559517000)  
![damage-img](media/damage.png)  
> Red indicates dealt damage, Indigo indicates taken damage

Here we can craft the flag!!  
Flag: `PUCTF26{12586_42999}`

## Conclusion

This is such a ~~degen~~ niche challenge it's funny. Also I had to force my teammate to stop whatever he was solving and answer me which character was that :trollface: Initially I had a tough time looking for the matches that had another player named `黑武藏` (shown blurly on the image), but I quickly diverted to op.gg since that was leading to nowhere. Anyway, this was a quick challenge and happy to have blooded it.

## Shoutout

- Ryan (Author)
- NuttyShell (Organizer)
- owo_wowowo (My teammate for answering)

<br>
<sub>
 Tags: OSINT, NuttyShell, PolyUCTF, 2026, LoL, op.gg, first blood, bluesky
</sub>
