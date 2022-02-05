# On computation and codes


<div class="bg-light text-info border border-info">
<small>

```{epigraph}
Debugging is twice as hard as writing the code in the first place. 
Therefore, if you write the code as cleverly as possible, you are, 
by definition, not smart enough to debug it.
    
-- B.W. Kernighan & P.J. Plauger in The Elements of Programming Style.
```
</small>
</div><p></p>

Before we start discussing modelling and implementing the different algorithms and methods, let us briefly list a few general issues on design, programming, computing and codes. The remarks below do not depend on the programming language.

## Well-written programs: Desirable properties 

Independent of the chosen programming language, there are several matters that should be considered. It is impossible to write an exhaustive checklist, but the purpose of the short lists below is to bring some of the important issues to the reader's attention. In all programming, one should be careful and pay attention to detail, and remember debug, debug, and debug. 

- __Portability:__ Codes should be written in such a way that they are portable, i.e., they must work correctly on different computer architectures 
- __Parallelizability:__ A good code should be parallelizable. Here, we will not focus on that issue, though. 
- __Readability:__ A good code should include comments.
- __Simplicity:__ The purpose is to solve problems, not to write the most beautiful code.

## Programming languages
   
<div class="bg-light text-info border border-info">
<small>

```{epigraph}
 There are only two kinds of languages: the ones people 
 complain about and the ones nobody uses.

-- Bjarne Stroustrup, The C++ Programming Language     
```
</small>
</div><P></p>

There are many, many programming languages. There is no ultimate language, but one has to choose the language based on pragmatic arguments. However, Python has become a very popular language for a great number of tasks as well as scientific computing, and C/C++ has become the most common general purpose language. For web-based solutions, javascript is extremely common. 

    
## A few notes on coding and related matters

Perhaps to most important piece of advice is the following quote:



<div class="bg-light text-info border border-info">
<small>

```{epigraph}
First, solve the problem. Then, write the code.

--John Johnson.
```
</small>
</div><P></p>

In brief, the above is the essence of good design: Do your background work, solve the problem, find the important determinants and constraints, find analytical solutions that you can use as your benchmarks. If your code fails to reproduce them, either your program, your algorithm or/and your general approach to solve it is/are wrong. Find what is essential to your problem, do not try to include everything possible (=avoid irrelevant details): If your task is to optimize the wind resistance of a new car model, its shape is the major factor. Including color options or the interior have no role and should not be considered. As another example, consider a database for course grades: The essential information consists of names, students numbers, grades and comparable, but including details such as hair color, height and weight are irrelevant. Apply the 

- KISS (keep it simple, stupid) and 
- YAGNI (your aren't gonna need it) principles

Good design consists of finding the essential parameters and variables and avoiding unnecessary complexity. Beginning programmers and computer modellers often try to include too Remember: Garbage in, garbage out (GIGO).   

Below are some practical hints to speed up programming and design: 

1. __Pseudocode:__ Write out the details of the algorithm you wish to implement as pseudocode. It makes tracing of errors much easier and programming much faster. Pseudocode is *independent* of the chosen programming language. 
1. __Modularize:__ Write subroutines (=subprograms) for self-contained routines. These subroutines are then called by the main program to perform their tasks. These subroutines may be tested and verified individually, which is a great advantage. 
1. __Clarity:__ In general, try to program in a clear manner avoiding unnecessary complications. 
1. __Variable names:__ Use descriptive variable names. It makes your code much for readable. Do not recycle variables which have been named in a descriptive fashion as that will make following the code really hard. You can easily recycle variables such as loop indices (*i*, *j*, *k*). It is often a good idea to call temporary variables as `temp` or something like that. 
1. __Comments:__ Include generous and precise comments in your code. What does this subroutine do? What are the main variables? Have any tricks been applied? It is also clearer to comment blocks of code and avoid line-by-line commenting as it decreases readability. 
1. __Status:__ Mark the status of your codes clearly. Is the program, subroutine or function fully functional or tested. How has it been tested? When? By whom? 
1. __Print:__ Print out results, also intermediate results, as they can be used later for comparison and to help to debug the code. 
1. __Keep a lab-book:__ Keep notes when you program and test your codes. Print out the results, and keep a diary - a lab-book - in which you detail what kind of changes you did and what was the reason for those changes or corrections and their effect. Proper logging will save enormous amount of time afterwards. 
1. __Debug:__ Debug, debug, debug, and even after that, debug. It is often quicker to write the first version of a code than to debug it. Even the best of programmers do, however, produce certain number of errors. It has been quoted that the 'industry average' for professional programmers is 15-50 errors per 1,000 lines of code. 
1. __Test cases:__ Test your code against known results whenever possible. In particular, pay attention to boundary conditions. 
1. __Program libraries:__ Use program libraries when possible. They have usually been tested tested by numerous users, and typically optimized for performance and accuracy. Keep in mind, though, that using them is not always straightforward (e.g., wrapping in the case FFTs is sometimes somewhat involved) and one should always perform one's own tests and verifications. 




<div class="bg-light text-info border border-info">
<small>

```{epigraph}
On two occasions I have been asked, "Pray, Mr. Babbage, if you put into the machine wrong figures, will the right answers come out?" ... I am not able rightly to apprehend the kind of confusion of ideas that could provoke such a question.

-- Charles Babbage, Passages from the Life of a Philosopher.
```
</small></div><p></p>

## A few additional details for efficient programming 


In addition to the above design issues, here are a few often overlooked practical issues

__Summations:__ One can minimize roundoff errors if summations are performed in the order of increasing magnitude (add smaller numbers first). 

__Avoid mixing of types:__ Do not add floating point numbers and integers. Instead,  use a type conversion (functions such as `REAL` in Fortran) when performing such an operation. `REAL(i)` converts an integer *i* into a floating point number and it can then be used in operations with other floating point numbers. Although Python does not have type declarations, this issue still matters: For example, consider the difference between 1/2 and 1.0/2.0.

__Memory access:__ Make sure you access computer memory in the most efficient way. For example, in the case nested loops, the first index runs fastest in Fortran, whereas in C/C++ and Python it is the last one. This can make a huge difference in performance. 



