# Understanding Key-Exchange Systems: An elementary example.
Author: Mike Zeng, West Computing Club

This textfile is a background for new users to complete this project. Today, we are going to approach public and private key communication with an elementary systems problem.

## Problem - Adding SAT scores
Maria has a SAT score of 900. John has a SAT score of 1000. At the start of class, neither of them know each others SAT score. Their parent Jane can hear everything that Maria and John say. Jane wants them to report to her the sum of their SAT scores.

How should Maria and John do this?

## Solution & Analysis
Maria tells John her number (900), John then sums up his number (1000) with the number he recieved (900) to get (1900). He reports it (1900) to Jane and solves the problem.

This problem is trivial. Due to unlimited constrainsts for John and Maria's communication, they can communicate directly with numbers to each other. We will see how limiting this make this system unfeasible.

## Problem 2 - No single score.
Jane does not want to hear a SAT score of below 1200. She will tolerate the sum being more than 1800, but if any one of them mentions a SAT below 1200, both of them will be punished. Jane can hear everything Maria and John say, so neither John or Maria should say their SAT score to each other. How should John and Maria proceed?

## Solution & Analysis for single score
Maria, instead of telling John her number, tells John a string. She also tells John a method of turning the string back into a number. The method is to use [a-j] to replace [0-9]. When John recieves the string, he uses the method Maria gave him to turn it into a number. He sums the numbers and tells Jane their summed number.

Due to the transformation of the number into a string, Jane does not hear a score below 1200. While Maria and John's communication was hindered by the fact that they couldn't directly tell each other, John and Maria were still able to cleverly use transformations of their number to prevent Jane from hearing. The 3rd modification will be signficantly harder; We will see what happens to our system if Jane becomes intelligent.

## Problem 3 - Intelligent Jane
Jane is intelligent. She can do all calculation John can, and is actively listening between John and Maria to find a way to sniff what one of their SAT scores are. If Maria gave instructions out to John, Jane can utilize those to crack their string and punish both of them. How should John and Maria proceed?

## Solution & Analysis for intelligent Jane
Attempt to solve this problem on your own before consulting the solution. This solution will highlight the main concepts in key-exchange.

## Solution Part 1: Understanding what is happening
In our case, we know that Maria needs to send a value V that is not her SAT score to John (since she can't say SAT score). However, the value V makes no sense to John. He cannot do anything with this value with his value (1000).

Let's play around with the old scenario to see how they might play out:
- Maria tries to give John the formula to transform V back to number. This fails because Jane will transform V herself and get Maria's SAT, which will get both of them punished.

Why is it failing? It's failing because Jane understood John!
- Jane is using information transfered between John and Maria to transform V back into a number.

## Solution Part 2: Stop Jane from understanding!

Let's think about this for a second. How might we solve this?
- What if we prevented Jane from transforming V back into a number?

This would help the problem a lot! If Jane couldn't transform V back into a number, then she can't detect what Maria communicates to John!

But this is problematic. If Maria doesn't send the information, John has no idea how to transform V back into a number either. We are back to square one. How should we proceed? We're stuck!

Failing to draw meaningful conclusions, we try to re-examine what we have to try to remove V->number from what is mentioned. Maria's always doing so much with all her transform and whatnot. John can do some work too. Why don't we try making John do some work? How might we make John work?

Oh.

What if John told Maria how to transform a number into V? Maria then transforms her number to V and sends it. Jane never hears about how to transform the number back into V, so she can't understand. John, having recieved V, uses the undisclosed "how to transform the number" to transform Maria's string back? He can then sum them up and tell Jane. Solved!

But wait. We said Jane was intelligent. Our number transformation is pretty easy to reverse. [0-9] -> [a-j] is pretty easy to transform back, you just run [a-j] -> [0-9]. Oh no, Jane now has the score of 900 or 1000, and both of them are punished.

Did our solution fail? Is there any way to create a function that is not reversible?

### Solution Part 3: One-way Transformation (Warning: Number Theory)
#### Some background in number theory.
It turns out, number theory is extremely significant in these one way communications. A lot of systems behave in a manner that is one way.

A strong example is product and multiplication. 2 \* 3 \* 4 = 1 \* 4 \* 6. Given 3 factors [2,3,4], we can combine them in a way such that it is irreversible to 3 numbers as [1,4,6] or [1,1,24] work. In a sense, we can denote the merging of [2,3,4] to 24 as a **one-way** transformation. 

Another example is modular arithmetic. Given that 8 mod 3 = 17 mod 3, it is impossible to reverse modules.

Due to the destructive nature of these operations, there is no way to change the number back. However, we can wrap these in complex systems to create a saving method fix this. More details on this will be explained later in real life systems.

## Relavancy to real world.
In real life, people communicate on computers in the Internet. Critical information is sent to each other all the time, ranging from passwords to credit card information. 

The Internet is insecure. While it's not always the case that Jane can hear everything, the worst case is that Jane can. Taking the chances with information such as your passwords that you may input on a daily basis is dangerous.

In real life, some people are like initial Jane. They don't care what information goes on between person 1 and person 2. Some people are like modified Jane, where they do listen but are too lazy to do anything.

But the realistic case of people who gain access to listen on networks is final Jane form, an intelligent being that sniffs for important information. They will bypass weak data transformations, jump around loopholes. 

That brings us to modern protocols that prevent this. Most notably, there is HTTPS and SSH. HTTPS is a protocol to encrypt information between your browser and a web server. SSH is a protocol to allow two computers to execute instructions on each other.

Let's tie in our terms from the problem to real world. In real world, there is a **public key** and **private key**. These are analogous to our **number->string** and **string->number** respectively. There is also a **requester** and **sender**, which in our example would be  **John** and **Maria** respectively. 

Private keys are **never** sent over the web, just like show John's **string->number** is not sent to Maria. Instead, John sends Maria the **number->string** key, which is essentially the **public key**. Maria then transforms her data that she wants to send and sends it to John. John after recieving it uses his **private key** to transform the string back into normal data, similar to how the **string->number** works.

## Concluding Remarks
Congraduatlations on your completion of this background reading. You should have:
- A general understanding of why public-private keys exist
- An understanding of how public keys are implemented.
