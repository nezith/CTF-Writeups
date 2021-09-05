# Challenge

Decipher this string!

>617a316a5a6d526a4d44466c4f54526d5a4463794f4445354d5455354f444d77593255344e54646d597a45354d437870505446684f57526c5a6a6b344e57457a4d7a49334e6a59784d6d49314d6a4532596a5a6a5a6a4e6b4d5755344c4449774f5446685a444d325a444d324d574d344f475131597a4d794d444a6c4d7a5a6b4f546331595441314e4455314e5464694e4455775a44566d5a47466d5954466b4e6a49774e7a6c6d4d5749324e6a677a59544a6b4e574e6c595459335a5759774f47557a4d6d4533595445314f4755315932526b4d7a67304f44557a5a413d3d


# Solution

[CyberChef](ttps://gchq.github.io/CyberChef) was a big help in solving this challenge

1. I noticed that the string was comprised of only numbers and lower case letters which was consistent with hex. So I converted from hex to get the below string:

>az1jZmRjMDFlOTRmZDcyODE5MTU5ODMwY2U4NTdmYzE5MCxpPTFhOWRlZjk4NWEzMzI3NjYxMmI1MjE2YjZjZjNkMWU4LDIwOTFhZDM2ZDM2MWM4OGQ1YzMyMDJlMzZkOTc1YTA1NDU1NTdiNDUwZDVmZGFmYTFkNjIwNzlmMWI2NjgzYTJkNWNlYTY3ZWYwOGUzMmE3YTE1OGU1Y2RkMzg0ODUzZA==


2. This new string looked like base64 denoted by the equal sign at the end so I converted from base64 to obtain the below string:

>k=cfdc01e94fd72819159830ce857fc190,i=1a9def985a33276612b5216b6cf3d1e8,2091ad36d361c88d5c3202e36d975a0545557b450d5fdafa1d62079f1b6683a2d5cea67ef08e32a7a158e5cdd384853d


3. At this point I felt like I was on the right track. This string was separated by commas and seemed to have a key, an initialization vector and a payload of sorts. I figured the key would be used somehow to decrypt the string but wasn't sure how exactly at first. I did some reading up on AES decryption and realized that it was exactly what I needed, this was reinforced by the name of the challenge 'Twisty seA', 'seA' being AES rearranged.

>AES Decrypt

>key = cfdc01e94fd72819159830ce857fc190 (as hex)
>IV = 1a9def985a33276612b5216b6cf3d1e8 (as UTF-8)
>String to decrypt/payload = 2091ad36d361c88d5c3202e36d975a0545557b450d5fdafa1d62079f1b6683a2d5cea67ef08e32a7a158e5cdd384853d

>Mode: CBC
>Input: Hex
>Output: Raw


4. After decrypting using AES, the flag was mine:
**GPSCTF{208E5f02Dc1EEe20DE59F8dfcA2bd06e}**