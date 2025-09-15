# Insanity (Blooded) (will add image in the future)
Difficulty: ★★★★★★★☆☆☆	&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Solved by: youstube_, .vedved, .inv1s1bl3  
![chall-img](media/chall.png)  

## Details:
- Author: bhavya_32
- Category: OSINT
- Score acquired: 499 (First blood)

## Description:
> QdwK8gcJ2a

> Flag format - 07CTF{part1_part2_part3}

## Write up:
My teammate .vedved found out the description is a Discord server invite ID , so putting this into the end of a Discord Server invite link (or just put the ID in Discord, left side `+` sign).  
In the Discord there is an event. telling me if im "Stuck?? Take help from @please_fiind_me" looking in the discord there isn't a user with that name, so I looked on x (since twitter have an @ in usernaemes as well) and found https://x.com/@please_fiind_me.  

They have bio of:  
`Here is the part 1 - "Tenebris". Easy huh? part 2 and 3 won't be this generous. Find the remaining two, and the doors shall open!!`

Part 2 was tricky. In the secret Discord server, for some reason there is a ticket bot. Even the bot's message is "Why even is a ticketing bot here?". So naturally I opened a ticket. and saw this ‌‌‌‌‍  
`‬‬‌‌‌‌‌‍﻿‍‌Welcome! ‌‌‌‌‍﻿‍‌‌‌‌‌‍﻿‌‌You‌‌‌‌‍﻿‌﻿ ‌‌‌‌‌﻿‬‬‌‌‌‌‌‬﻿﻿need‌‌‌‌‌‬﻿﻿ ‌‌‌‌‍‬‍‌‌‌‌‌‍﻿‌‬‌‌‌‌‍‬‬‍help?‌‌‌‌‍﻿‍‬‌‌‌‌‍‬‍‍‌‌‌‌‌‬﻿‬‌‌‌‌‍‬‍﻿‌‌‌‌‍‬﻿﻿ ‌‌‌‌‍‬﻿﻿‌‌‌‌‍‬‍﻿‌‌‌‌‍‬﻿‌‌‌‌‌‍‬‍‍‌‌‌‌‌‬﻿‬‌‌‌‌‍‬‌﻿‌‌‌‌‍‬﻿﻿‌‌‌‌‍‬﻿‍Here ‌‌‌‌‌‬﻿﻿is‌‌‌‌‍‬‍‌ ‌‌‌‌‍﻿‌‬the‌‌‌‌‍‬‬‍‌‌‌‌‍﻿‍‬ ‌‌‌‌‍‬‍‍‌‌‌‌‌‬﻿﻿‌‌‌‌‍‬‍‬fla‌‌‌‌‍‬﻿﻿‌‌‌‌‍‬﻿‌‌‌‌‌‍‬‍‌‌‌‌‌‍‬‍‍.‌‌‌‌‍﻿‌‬.‌‌‌‌‍﻿‌﻿‌‌‌‌‌‬﻿﻿.‌‌‌‌‌﻿‌‍ ‌‌‌‌‍﻿‌‍nvm‌‌‌‌‍‍‬‌‌‌‌‌‍‍‌﻿,‌‌‌‌‍‬‍‬ ‌‌‌‌‍‍‍‬‌‌‌‌‍‍‌‌‌‌‌‌‍‍‌﻿here‌‌‌‌‍﻿‍﻿ ‌‌‌‌‍‬﻿‌‌‌‌‌‌﻿‍﻿‌‌‌‌‍‌﻿﻿is‌‌‌‌‍‌‌﻿‌‌‌‌‍﻿‍﻿‌‌‌‌‍﻿‍‌‌‌‌‌‍‬﻿﻿ ‌‌‌‌‍﻿‍﻿a ‌‌‌‌‍‌‍‬clue‌‌‌‌‍﻿‍‌‌‌‌‌‍‍‍﻿ ‌‌‌‌‍‬‍‌‌‌‌‌‌﻿‬‌‌‌‌‌‍‬‌﻿‌‌‌‌‍﻿‌‍‌‌‌‌‌﻿‌﻿‌‌‌‌‍‍‌‍to ‌‌‌‌‍‌﻿‍‌‌‌‌‍‌‍‬get‌‌‌‌‌﻿‬‍‌‌‌‌‍‍‌‌ ‌‌‌‌‍‍‍‍the‌‌‌‌‍‬﻿﻿‌‌‌‌‌﻿‍‍‌‌‌‌‌﻿﻿﻿‌‌‌‌‍﻿‍‍ ‌‌‌‌‍﻿‌﻿‌‌‌‌‍﻿‌‌flag‌‌‌‌‌﻿﻿‍‌‌‌‌‍﻿‌﻿‌‌‌‌‍‬‬‌‌‌‌‌‍‬‌‍‌‌‌‌‍﻿‌‬‌‌‌‌‍‬‬‍‌‌‌‌‍‬﻿‬.‌‌‌‌‍‬‍﻿`  

What the helly? where is the help? If you read this on the surface, it looks like a normal message, but when copy the message, you'll see there is [hidden ASCII characters](files/hidden_character.txt), specifically `U+200C`(ZWNJ), `U+200D`(ZWJ), `U+202C`(PDF) and `U+FEFF`(BOF). 
<details>
<summary>Click to view the hidden ASCII character</summary>

```
⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWJ⟩⟨ZWNJ⟩Welcome!•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩You⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨BOM⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨BOM⟩⟨PDF⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩need⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨PDF⟩⟨ZWJ⟩help?⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWJ⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨PDF⟩⟨BOM⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨PDF⟩⟨BOM⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨ZWJ⟩Here•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩is⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨ZWNJ⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨PDF⟩the⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨PDF⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWJ⟩⟨PDF⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨PDF⟩fla⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨ZWJ⟩.⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨PDF⟩.⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩.⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWJ⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWJ⟩nvm⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨BOM⟩,⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨PDF⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨BOM⟩here⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWJ⟩⟨BOM⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨BOM⟩⟨BOM⟩is⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWJ⟩⟨BOM⟩a•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩clue⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨BOM⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨BOM⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWJ⟩to•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩get⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨BOM⟩⟨PDF⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWJ⟩the⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨BOM⟩⟨BOM⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWJ⟩⟨ZWJ⟩•⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩flag⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨BOM⟩⟨BOM⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨BOM⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨BOM⟩⟨ZWNJ⟩⟨PDF⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨PDF⟩⟨ZWJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨BOM⟩⟨PDF⟩.⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWNJ⟩⟨ZWJ⟩⟨PDF⟩⟨ZWJ⟩⟨BOM⟩
```
</details>

This was obviously a stego of some sort. So I tried mapping it by the last 2 hexcode of the ASCII character (0C, 0D, 2C, FF), but quickly realized this is not correct since 3 of them starts with 20, but `FEFF` is not. so I tried to map it by 0 1 2 3, and decode with base4, but that doesn't seem right as well.  

Ultimately, I cleaned the text to only contain the [hidden characters](files/processed_hidden_character.txt), and resorted to mapping those 4 characters to 00, 01, 10, and 11, and decoded it with binary. Bingo! ([See cyberchef here](https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Regex','string':'%E2%9F%A8ZWNJ%E2%9F%A9'%7D,'00',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%E2%9F%A8ZWJ%E2%9F%A9'%7D,'01',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%E2%9F%A8PDF%E2%9F%A9'%7D,'10',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%E2%9F%A8BOM%E2%9F%A9'%7D,'11',true,false,true,false)From_Binary('Space',8)Remove_null_bytes()&input=4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqFBERuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hCT03in6nin6haV0rin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqEJPTeKfqeKfqFBERuKfqeKfqFBERuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoUERG4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6hQREbin6nin6hCT03in6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqFBERuKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hCT03in6nin6haV0rin6nin6hQREbin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6hQREbin6nin6hCT03in6nin6hQREbin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqEJPTeKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hQREbin6nin6hCT03in6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6hQREbin6nin6hCT03in6nin6hQREbin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldOSuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hQREbin6nin6hCT03in6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6hQREbin6nin6hCT03in6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqFBERuKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hCT03in6nin6haV0rin6nin6hQREbin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6hQREbin6nin6hCT03in6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqEJPTeKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hQREbin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6hQREbin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoUERG4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV0rin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6haV0rin6nin6haV05K4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6haV0rin6nin6haV0rin6nin6hQREbin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hCT03in6nin6haV0rin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6hCT03in6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqEJPTeKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqEJPTeKfqeKfqFpXSuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqEJPTeKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqEJPTeKfqeKfqFBERuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldOSuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV0rin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqEJPTeKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6hCT03in6nin6hQREbin6nin6haV0rin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqEJPTeKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6hCT03in6nin6hCT03in6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldK4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqEJPTeKfqeKfqFpXTkrin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqEJPTeKfqeKfqEJPTeKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoQk9N4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqFBERuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hCT03in6nin6haV05K4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXSuKfqeKfqFBERuKfqeKfqFBERuKfqeKfqFpXSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV0rin6nin6hQREbin6nin6hCT03in6nin6hQREbin6nin6haV05K4p%2Bp4p%2BoWldOSuKfqeKfqFpXTkrin6nin6haV05K4p%2Bp4p%2BoWldK4p%2Bp4p%2BoUERG4p%2Bp4p%2BoWldK4p%2Bp4p%2BoQk9N4p%2Bp&ieol=CRLF&oeol=NEL))

Decoded text: `https://drive.google.com/drive/folders/1qXSfVPSwl7OCwtowFtWd8cq3QMF9PUo5?usp=sharing`

Going to the [Google drive link](https://drive.google.com/drive/folders/1qXSfVPSwl7OCwtowFtWd8cq3QMF9PUo5) reveals a Red Herring.png, and reading the description of the folder reveals the 2nd part.  
`Nice, here is the part 2 - "susurrrat".`

3rd part is also tricky. I first theorized there could be stickers or emoji the server uses since we still haven't found "IT" (according to the server name). So I check the emoji from this server. Bingo. 3 animated emojis, where one is called :IT: as well. ![IT-webp](media/IT.webp) << This is the emoji.

So I extracted the emoji's webp file (Ctrl+Shift+I in discord, and inspect the animated emoji), and write a [short python script](files/frame.py) to export the webp frame by frame: 

<details>
<summary>Click to toggle code</summary>

```
import os
import sys
import subprocess
import shutil

def extract_webp_frames(webp_path: str):
    """
    Extracts all frames from an animated WebP file into a directory
    named after the file.
    
    Args:
        webp_path (str): The full path to the animated WebP file.
    """
    # 1. Check if the anim_dump command is available
    if not shutil.which("anim_dump"):
        print("Error: 'anim_dump' command not found.")
        print("Please install the 'webp' or 'libwebp-tools' package.")
        print("  - On Debian/Ubuntu: sudo apt-get install webp")
        print("  - On macOS (Homebrew): brew install webp")
        print("  - On Fedora/CentOS: sudo dnf install libwebp-tools")
        sys.exit(1)

    # 2. Validate input file path
    if not os.path.isfile(webp_path):
        print(f"Error: File not found at '{webp_path}'")
        sys.exit(1)

    # 3. Create the output directory
    dir_path = os.path.dirname(os.path.abspath(webp_path))
    filename = os.path.basename(webp_path)
    output_dir_name = os.path.splitext(filename)[0]
    full_output_path = os.path.join(dir_path, output_dir_name)

    print(f"Creating output directory at: {full_output_path}")
    os.makedirs(full_output_path, exist_ok=True)

    # 4. Construct and run the command
    command = ["anim_dump", "-folder", full_output_path, webp_path]
    
    print(f"Extracting frames from '{filename}'...")
    try:
        process = subprocess.run(
            command, 
            check=True, 
            capture_output=True, 
            text=True
        )
        if process.stdout:
            print(process.stdout)
        if process.stderr:
            print("Errors:", process.stderr)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during extraction for {filename}:")
        print(e.stderr)
        sys.exit(1)
    except FileNotFoundError:
         print(f"Error: Could not find the '{command[0]}' executable.")
         sys.exit(1)


    print("✅ Extraction complete!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_webp_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    extract_webp_frames(input_file)
```
</details>

Extracting the [frames](media/IT), we can see in one particular frame where something pops up.  
![frame-img](media/IT/dump_0013.png)  
`p3- "veritatem"`


## My Solution:
Combining these 3 parts, and wrapping it in 07CTF{}  
Flag: `07CTF{Tenebris_susurrrat_veritatem}`
## Conclusion:
Fun fact, if you actually look through the secret Discord server, there is a channel called `#whisper-of-the-void`, where in the original challenge, you needed to send these three words like a secret passphrase to get a role (`get if if you can`), and view a hidden channel `#get-your-flag`. However, due to some misconfiguration of the bot, the message didn't delete as quickly as it should've, so the whole channel was restricted and instead used the passphrase as flag instead. I pointed this out to the author and was surprised they didn't know until mid-ctf :joy: A nice blood overall.
## Shoutout:
- bhavya_32 (Author)
- .vedved & inv1s1bl3 (My teammate)
- BlitzHack (My team)
- 0bscuri7y (Organizer)

<br>
<sub>
	Tags: Misc, OSINT, Discord, Stegnography, Hidden Character, frame extraction
</sub>