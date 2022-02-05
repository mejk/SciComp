## Roundoff Error Amplification

In addition to accumulation with each floating point operation, roundoff errors can be magnified by

1. Multiplication by a large number or division by a small number.  
2. Adding numbers of very different magnitude.  
3. Subtractive cancellation (subtraction of numbers of similar magnitude).

If we can possibly do something to avoid these magnification events or mitigate their effects it is usually worthwhile.  The issue with how multiplication by a large number or division by a small number can turn a small error into a large one should be fairly clear.  To illustrate the other ideas, we will look at a number of examples.

*Example 1.  Adding numbers of very different magnitude.*

Suppose you want to do a simulation of ocean waves.  Before you start, you have a couple of very basic decisions to make: (1) what units should you use and (2) where to place the origin (the zero).  Possible units could be miles, feet, kilometers, meters, or millimeters.  Hopefully you have enough science background to realize you should avoid miles and feet (NASA's [Mars climate orbiter](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) is a clear example of why to avoid imperial units).  The remaining choices may seem to be arbitrary.  However, let's assume you plan on storing the height of the ocean surface using 32-bit floating point numbers.  Conceptually, suppose you decide it makes sense for these "heights" to always be positive so the origin should be at the bottom of the ocean, which at its deepest point is about 11 km below sea level.  If you decide to use units of meters, then most of your numbers of ocean height will then be around 11 000 m.  Suppose, in your simulation, wind starts a wave of initial height 1 mm (you have to start somewhere) which is easily measured in reality.  However, 1 mm = 0.001 m and if your code then has to execute $ 11 000.000 + 0.001$ you will get back $11 000.00$ (i.e. there will be no change) because there are only about 6 digits of precision with 32-bit floating point numbers and this calculation would require at least 8 to be peformed without roundoff.  If instead, you accepted both positive and negative heights for your ocean surface and measured the ocean surface height from sea level, then most of your heights will be around 0 m.  A  change of 1 mm is now easily accomodated without being affected by roundoff errors as $0.000+0.001$ will now give $0.001$ with no loss in precision from roundoff at the seventh digit.  Here, you will note I have chosen the unit meters rather than mm or km.  Why is this the better choice?  In this case, waves are typically of the order of meters so this choice makes our heights of order 1 in magnitude.  As indicated, the real world measurements would typically have a resolution of 1 mm = 0.001 m so mm would not be a terrible choice here either.  However, km would not be a good choice as our heights would then be of order 0.001 and our resolution would be 0.000001.  Typing numbers in your code with a bunch of zeros or requiring explicitly filled in exponents is introducing a lot of opertunities for typos that may be very difficult to debug later.  In summary, pick units and an origin so that floating point numbers are, on average, of order one as much as possible.  This reduces both possibilities of roundoff errors and typos that might be hard to find.

*Example 2.  Adding numbers of very different magnitude.*

Suppose you want to sum the series  

$$\sum_{n=1}^\infty \frac{1}{n^2}$$  

to as high an accuracy as possible.  The exact answer here is $\pi^2/6 \approx 1.64493$.  Again, let's assume we are storing intermediate results of our sum using 32-bit floating point arithmetic so again have only 6 decimal digits or precision.  Obviously you cannot sum an infinite number of terms so you decide to cut it off at 1 million terms, i.e. evaluate  

$$\sum_{n=1}^{10^6} \frac{1}{n^2}.$$  

The conventional way to evaluate this would be in order (so $1+1/2^2+1/3^2+...+1/(10^6)^2$).  If you do this you will get the result $1.64393$, so an absolute error of $0.001$.  This is much less than the roundoff error in a single computation so you might think there is nothing you can do about this.   However, if you evaluate the sum in *reverse* order (i.e. $1/(10^6)^2 + ...+ 1/3^3 + 1/2^2 +1$) you will get an answer close to the machine epsilon from the "exact" answer of $1.64493$.  Why does this occur?  It turns out that if you sum the terms in order, roundoff errors mean that every term past $n=1000$ will end up contributing nothing to the sum.  This is again because the term we want to add, $1/1000^2 = 0.000001$, is being added to a number $1.64393$ and the difference in magnitude of these numbers cannot be accomodated with the 6 digits of decimal precision we have with 32-bit floats.  However, when we sum the terms in reverse we only ever add terms of similar magnitude and this gives the very small later terms a chance to add together to build a larger number as we get to the point where we are adding the larger terms. 

*Example 3. Subtractive cancellation.*  

Subtractive cancellation is the converse problem to adding numbers of very different magnitude.  For example, suppose in Example 1 above we  had decided to use the bottom of the ocean as our origin so that our ocean height numbers were typically around 11 000.  Now we are were interested in computing the slope of the ocean surface at neighboring points where the actual difference in height is zero.  However, perhaps due to previous roundoff errors, one measurement is 11 000.02 m and the other is 10999.99 m.  The difference between these two values is 0.03 m = 3cm, much bigger than our desired resolution of mm, and even large if we assumed a resolution of 1 cm.  The solution in this case is again to use a sensible origin such as the average sea level so that the roundoff errors will be of the order of $10^{-6} m$ so that any differences due to roundoff will be below our 1 mm resolution.

*Example 4. Division by a small number and Subtractive cancellation.*  

Suppose you want to compute  

$$f(x) = \frac{1-\cos x}{\sin x}.$$  

and we will assume $x\in [0,2\pi]$.  When $x$ is small this formula suffers from two issues that can magnify roundoff errors: division by a small number ($\sin x \approx 0$ when $x$ is small) and subtractive cancellation ($\cos x \approx 1$ when $x$ is small).  A simple mathematical transformation that often allows you to eliminate subtractive cancellation is to multiply by the sum of the two terms in question in both a numerator and denominator of a fraction (so effectively multipying by one) and then rearranging the terms to eliminate the subtraction:  

$$\begin{align}
f(x) & = \frac{1-\cos x}{\sin x} \times \frac{1+\cos x}{1+\cos x}&\\
& = \frac{1-\cos^2 x}{(1+\cos x)\sin x}&\\
& = \frac{\sin x}{1+\cos x},
\end{align}$$

where we have used the trig identity $1-\cos^2 x = \sin^2 x$ to get the final result.  The resulting formula is mathematically equivalent to the original but no longer has either the division by a small number of the subtractive cancellation near $x=0$.  However, this formula *will* have issues near $x=\pi$ as $\cos x \approx -1$ near $x=\pi$ which will again lead to subtractive cancellation and division by the resulting small number.  To solve both these issues one should first test $x$ to decide if it is closer to $0$ or $\pi$ and then pick either the modified formula (when $x$ is closer to zero) or the original (when $x$ is closer to $\pi$).

*Example 5. Subtractive cancellation.*  

Recall that the roots of $ax^2 + bx + c=0$ are  

$$
\begin{align}
x_1 &= \frac{-b + \sqrt{b^2-4ac}}{2a},&\\
x_2 &= \frac{-b - \sqrt{b^2-4ac}}{2a}.
\end{align}
$$

Note that if $b^2 \gg 4ac$ then $\sqrt{b^2-4ac} \approx |b|$ so

- if $b>0$ then $x_1$ involves subtraction of similar numbers ($x_2$ is fine though),  
- if $b<0$ then $x_2$ involves subtraction of similar numbers ($x_1$ is fine though).

If we again apply the trick of multiplying by a fraction where denominator and numberator are both the sum of the terms in question we get for the $b>0$ case where we need to rewrite $x_1$:  

$$
\begin{align}
x_1 &= \frac{-b + \sqrt{b^2-4ac}}{2a} \frac{-b - \sqrt{b^2-4ac}}{-b - \sqrt{b^2-4ac}},&\\
&= \frac{-2c}{b + \sqrt{b^2-4ac}}.
\end{align}
$$  

where a small amount of algebra is used to similify the final expression which no longer has the problem of subtracting similar numbers.  Note that you should only use this formula for $x_1$ when $b>0$.  When $b<0$ you should use the original formula for $x_1$ and apply a similar transformation for $x_2$ instead.


