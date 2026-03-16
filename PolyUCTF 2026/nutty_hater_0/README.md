# nutty_hater_0

Difficulty: ★★☆☆☆☆☆☆☆☆  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Solved by: codestube (youstube_)  
![chall-img](media/chall.png)  
![blood-img](media/blood.png)

## Details

- Author: Ryan
- Category: OSINT
- Score acquired: 50 (110 Solves) (First blood)

## Description

> A recent intel obtained by NuttyShell Intelligence Agency revealed that the notorious "Hater" has been spotted on the internet.  
> Identify the target's social media account from the image provided.  
> If the account's handle were "@forbes.com", the flag would be "PUCTF26{@forbes.com}".  
>
> Flag Format: `PUCTF26{@[A-Za-z0-9_.]{3,25}}`

## Write up

We were first given an image to inspect.  
![dist-img](files/nutty_hater_0.jpg)

From this image, we can gather a few information that could lead us to finding the target's social media account. Here are the highlighted area for better understanding:
![detail-img](media/details.png)

${\textsf{\color{yellow}YELLOW}}$: From the `🔁Reposted by` wordings, we can tell this is either X (formerly known as Twitter) or Bluesky. Judging by the UI color not being entirely black and some sort of UI element that uses a much deeper blue above the `🔁Reposted by`, it is definitively Bluesky.

${\textsf{\color{red}RED}}$: With the aforementioned clue concluding that this is Bluesky, the word `GIFS GALOR..` is most definitely their display name.

${\textsf{\color{lime}GREEN}}$: The captions of this post made by the account: `NATURE/SEASCAPE.GIF`

${\textsf{\color{pink}In addition}}$, we can see a sneak-peek of a profile picture that doesn't match the above account whom is being reposted from, and there is no repost symbols (nor a div) above it. This means that this icon is the account's profile picture.

With the above clues layed out fully, we can start looking for the target's social media account.  
> [!NOTE]  
> It is important to note that there have been instances where searching on Bluesky while not logged in the platform could cause issue.

## My understanding

I started by going to [Bluesky](https://bsky.app/), and looking up someone named `GIFS GALOR` in the search bar;  
![prof-search-img](media/prof-search.png)  
This profile icon matches the one from the challenge, meaning this is the [right profile](https://bsky.app/profile/gifs-bot.bsky.social). Now we have to find the post with the caption `NATURE/SEASCAPE.GIF`. Using [search filtering on Bluesky](https://bsky.social/about/blog/05-31-2024-search), we can filter post by this account and look for a post with that caption.  
![post-search](media/post-search.png)  
<sub> A little fun fact: At the time, I actually just scrolled the entire profile and `CTRL + F` the caption instead of using this method. Minor time loss for me but still got to blood it :trollface:</sub>  

There seems to be a few repeating posts with the same image made by this account. Without much info to go off of, we will have to manually check each post's reposters and see if there's one account that has the same profile picture that we saw on the challenge image.  
We can click on the [first post](https://bsky.app/profile/gifs-bot.bsky.social/post/3mfgvztdc3f26) and check who has [reposted](https://bsky.app/profile/gifs-bot.bsky.social/post/3mfgvztdc3f26/reposted-by) the post:  
![click-me-waga](media/click.png)  
> [!WARNING]  
> TW: There are profiles that displays NSFW materials or bios. Please check at your own risk. Readers discretion is advised.  

## My Solution

After scrolling a bit, you'll find this profile with similar looking profile picture along with a username with the word `nutty` in it, further proving that this is probably the right account. Checking their feed could further prove that this is who we're looking for.  
![found-img](media/found.png)  
![found-prof-img](media/found-prof.png)  

From here, we can craft the flag with the user's handle.  
Flag: `PUCTF26{@nuttychud.bsky.social}`

## Conclusion

I wrote this as detailed as possible in hopes of beginners who stumble upon this writeup can understand how to solve challenges like this and how to pick up on clues faster. However, this is only 1/5 so it might take a lot of attention span to keep up. My apologies :p

## Shoutout

- Ryan (Author)
- NuttyShell (Organizer)
- Internet (for not dying)  
<!-- [Next episode~]("../nutty_hater_1/README.md") -->
<h2 align="right">
  <a href="../nutty_hater_1/README.md"><strong>Next Writeup~</strong></a>
</h2>
<br>
<sub>
 Tags: OSINT, PolyUCTF, 2026, Bluesky, repost, NuttyShell, First Blood
</sub>
