# Challenge

We have deciphered the Secret Service's daily color code! Every day, the Secret Service wears a special identifying pin that is the "color of the day." They use a specific algorithm to determine what the color for that day is. Can you guess what the color will be 815 days after today? Here are the clues:

    The colors are: Plum, Peach, Teal, Cerulean, Black, Gold, Gray, and Cyan in that order.
    The in the list above, "Plum" is 0, "Peach" is 1, and so on. Starting with the highest number, they add up the date (for example, 2018-10-26 would be added to 2054) and divide it by that number. If the modulus is 0, that is the color of the day. If not, they decrement by one until they reach a modulus of 0.




# Solution

1. I did this challenge on August 13, 2021. 815 days after this date is November 6, 2023.
2. Adding up this future date (2023 + 11 + 6) = 2040
3. Dividing 2040 by the number of colours (8) starting from the highest number and decrementing until the modulus is 0.
4. 2040 % 8 is 0 therefore no decrementing was necessary in this scenario (but if it was then I would decrement to 7 and if the modulus still was not equal to zero then decrement to 6 and so on).
5. The 8th colour is Cyan which was the answer

I created a python script to calculate the correct colour on a given day by calculating the modulus of the sum of the date and the number of colours. I used this script to obtain the flag:
**GPSCTF{952a1af38062c22b7187c97a52ac9bec}**