## Finite Precision

A transcendental number like $\pi$ has an infinite number of digits.  Clearly, a computer is capable of only storing a finite number of these digits.  We are familar with the idea that rational numbers like $1/3 = 0.333333...$ in base 10, or $0.0101010101...$ in binary, must typically be truncated.  However, it is important to remember that computers store numbers in base 2 (binary) so that numbers like $1/10 = 0.1$ in base 10, is $0.000110011001100...$ have an infinite number of digits in binary and will have to be truncated when represented in a computer.  In this section we will discuss the impact of the computer's finite precision on numerical algorithms.

### Precision versus Accuracy

It is important to distinguish what we mean by precision versus what we mean by accuracy.  In numerical computation we typically have 32 or 64 binary digits of *precision* in our calculations (which translates to roughly 8 or 16 decimal digits).  This does not mean we have anything like this amount of accuracy (as measured by absolute or relative errors).  In high school you may have been taught to discard any digits that were not accurate by keeping only significant digits in calculations.  This philosophy places value only on accuracy and none on precision.  However, there is also value in precision even if it far exceeds the accuracy of the numbers involved.

An example of the value of precision, even in the absense of accuracy, was in the [Hubble space telescope](https://www.nasa.gov/content/hubbles-mirror-flaw).  The Hubble was a complete embarassment for NASA when it was first launched.  It was ground to the wrong specifications due to a calibration error.  As a result, it produced fuzzy images.  Fortunately, it was ground to a very high precision (with poor accuracy).  The high precision allowed NASA to install corrective lenses to cancel the error (the poor accuracy) resulting in the amazing clear images you are now familar with.

As we will discuss below, the finite precision of floating-point numbers can result in a loss of accuracy as they lead to errors that can not just propogate but be significantly magnified by arithmetic operations.  The easiest, but not necessarily the best, way to deal with these errors is to increase the number of digits used to store numbers.  Over the years, this has lead to the number of binary digits used to store numbers increasing from 16-bit, to 32-bit, and then to 64-bit.  In addition, typically CPUS use 80-bit registers (at time of writing in 2022) to store intermediate results for 64-bit floating point calculations.  However, many computationally intensive calculations are now moving to GPU-computing (graphics processing unit) which are either limited to 32-bit floating point numbers, or perform significantly faster in 32-bit rather than 64-bit mode.  In addition, many of the typical "shortcuts" done for performance can often lead to a [reproducability problem](https://www.intel.com/content/dam/develop/public/us/en/documents/fp-consistency-121918.pdf) (ie. the program may give slightly different results from one run to the next).  The best way to avoid these problems is to have a firm understanding of the origin of errors originating from finite precision arithmetic and design your algorithm and code in such a way to avoid them, or at least minimize their effects.

### Under/Over-flow

As we mentioned, numbers have a finite precision in order to be stored in a computer.  Different types of numbers have different precision.  The table below gives the number of digits and range of several types of numerical types.

| mathematical type | C-style code type | number of binary digits | range        | decimal precision |
|-------------------|-------------------|-------------------------|--------------|-----------|
| integer           | 'short'           | 16-bit                  | $-2^{15}=-32 768$ to $2^{15}-1=32 767$ | - |
|                   | 'int'             | 32-bit                  | $-2^{32}=-2 147 483 648$ to $2^{32}-1$ | - |
|                   | 'long'            | 64-bit                  | $-2^{64}$ to $2^{63}-1$ | - |
| real number       | 'float'           | 32-bit                  | `1.2E-38` to `3.4E+38` | 6 digit|
|                   | 'double'          | 64-bit                  | `2.3E-308` to `1.7E+308` | 15 digit |
|                   | 'long double'     | 80-bit                  | `3.4E-4932` to `1.1E+4932` | 19 digit |

Overflow (too big) or underflow (too small) occur whenever you attempt to store a number outside the possible range shown in the table (sometimes both are just called "overflow").  This occurs most frequently when an arithmetic operation results in a value outside the possible range.  In this case your program may, or many not, crash.  In either case it is not likely you will get what you intended.  

A spectacular example of the consequences of overflow was the [Ariane 5 test flight](https://esamultimedia.esa.int/docs/esa-x-1819eng.pdf) which exploded (along with the 7 billion dollars it cost to make) 40 seconds after launch.  The cause was determined to be a sensor reporting a large acceleration (this tends to happen when rockets launch) that caused an overflow in the inertial guidance program.  The overflow occured when a 64-bit floating point number, larger than 65536, was converted to a 16-bit signed integer (largest allowed value being $2^{32}=65536$).  

It should be clear that avoiding overflow is important.  To do so, we need to be aware of where it occurs.  Some potential operations that can lead to overflow are:  
- variable type conversion, especially implicit type conversions.  In some computer languages you can ask the compiler to warn you about implicit type conversions.  In addition you should carefully consider the types of all variables in any arithmetic operation, as well as the variable the result is being assigned to.  Ask yourself if the range of all of these variables is consistent with what could be possibly encountered when the code is running.
- division by a real number close to zero can cause overflow.  If you have a variable that *could* be zero, or very small, this should be tested before performing the arithmetic operation that could cause overflow.
- don't undersize variables.  You may be tempted to use `float` instead of `double` to be "economical".  However, except in rare circumstances (such as gpu computing) this is rarely going to do anything helpful.  On most CPUs the calculations will be done using 64-bit `double` anyway, even if you only ask for `float`.  Similarly, there is typically little to no advantage to using a `short` integer versus a normal 32-bit `int`.
- if you are certain your integers will always be positive, you may wish to use `unsigned` types which will double the maximum value possible before overflow.

It is important to note that in some cases, the compiler may actually do integer range checking and may deal with an overflow by applying a modulo operation, or some other not always defined solution.  In this case you will not get the answer you expect which is another important reason to detect the overflow even when your program doesn't crash as a result.

A very similar issue to overflow that is often a problem in numerical codes is array indices going out of bounds.  This can actually be a very difficult bug to detect as it will often not cause an immediate crash.  For example, suppose we have a function defined at $N$ equally spaced set of points, $\Delta x$ apart, whose values are stored in an array `F` of type `double`.  We might want to compute the derivative of this function using a finite difference.  In practice, this will involve differences like $(F[i+1]-F[i])/\Delta x$.  Evaluating this expression for all elements of the array will cause the array index $i+1$ to go out of bounds when $i= N-1$ (assuming array indices are numbered from $0$ to $N-1$).  These end cases will require special consideration.  Some languages automatically do bounds checking, but others like C do not.  There is also a performance cost to doing bounds checking every time you index into an array.  A reasonable compromise for high performance computing can be using something like the [Boost libraries](https://www.boost.org/) which have C-style array types where bounds checking can be turned on/off using a compiler flag.  In this case, extensive testing can be performed with array bounds checking and then, when you are convined the code is working properly, you can turn off the bounds checking for production runs.


### Round-off Errors

Round-off errors occur when we perform arithmetic operations with floating-point numbers. These errors can accumulate and become amplified by subsequent operations leading to catastrophic results.  A tragic example of this occured in 1991 in the "first" Gulf War when an [American Patriot missle failed to track an Iraqi Scud missle](https://www.gao.gov/assets/imtec-92-26.pdf).  Instead, it hit an army barracks, killing 26 people.  The cause was determined to be related to [measuring time in tenths of a second](https://web.archive.org/web/20080801202418/http://www.mc.edu/campus/users/travis/syllabi/381/patriot.htm).  $1/10$ cannot be represented exactly in binary, and particular in the 24-bit floating point numbers used at the time.  A poorly designed algorithm that did not account for this consistently caused an accumulation of these errors leading to the disaster.

To understand how these errors occur and accumulated, we first need to examine how floating-point numbers are stored.  We can represent any number in the form

$$ \pm 0.\underbrace{d_1 d_2 d_3 d_4...}_\text{mantissa} \times \beta^n, $$

where $\beta$ is the base and $n$ is the exponent.  To reduce the number of digits that need to be stored, we normalize (ie. adjust the exponent) so that $d_1 \neq 0$.  For a computer, we use base 2 (binary) so $\beta=2$ and we store numbers with a finite precision (fixed number of digits in the mantissa).

Inside most computers, a 64-bit real number is stored as:

```{figure} ./img/IEEE_754_Double_Floating_Point_Format.svg  
:alt: floating-point-format
:width: 700px
:align: left

*<sub><sup>Based on [this source](https://commons.wikimedia.org/wiki/File:IEEE_754_Double_Floating_Point_Format.svg) </sup></sub>* 
```

If we call this number $x$, it can be converted back to decimal via

$$ x = (-1)^s(1+f)2^{c-1023} $$

where $s$ is the sign bit, $c$ is the 11-bit exponent, and $f$ is the mantissa.  Note that nonzero numbers are normalized to that the first digit in the mantissa is nonzero.  In binary this means that this digit must be 1 so does not need to be stored,  thus explaining the addition of 1 to $f$ in the formula. There are a few special cases such as when $c=0$ and $f=0$ being a "signed" zero and $c$ having all digits 1 idicating infinity if $f=0$ and the imfamous NaN if $f\neq 0$.  That later (and $c=0$ with $f\neq 0$) is generally an indicator of overflow/underflow.  This allows your code a means for checking for over/underflow and take corrective action.  However, if you do not do this the code will likely continue running and crash at a later point when these values are used blindly.

Of particular interest is the smallest value you can add to unity and get a computationally discernably different number.  This is called the [*machine epsilon*](https://en.wikipedia.org/wiki/Machine_epsilon) and its value for 64-bit floating point numbers is

$$ \epsilon = 2^{-25} \approx 10^{-16}. $$

In order to fully implement floating point numbers, one also needs to decide hwo intermediate results terminate the mantissa at 64 bits.  Two standard methods are

- **chop** : just delete the extra digits
- **round** : add 5 to the first "extra" digit and then chop.

Note that the later is equivalent to the normal rounding operation.  The chop operation is faster and what you will often get if you compile your code with full "optimization".  However, the second is slightly more accurate and is part of the IEEE standard for floating point numbers.
What this does mean, however, is that we have the potential to lose at least 1 binary digit or accuracy with each arithemtic operation.  In fact, you might be suprised to learn that you can actually lose many more than just one digit.  We will illustrate this with a few examples, along with some strategies to avoid the worst of these effects.

While a good knowledge of binary numbers is crucial for designing hardware, it is not the goal here.  Here we want to understand how roundoff can be avoided or at least minimized.  Strategies for this are independent of the actual base used so we will illustrate our examples with an imaginary decimal computer with $k$ digits in the mantissa.  This separates the concept of avoiding roundoff errors from the vagaries on binary numbers.

```{image} ./img/styleatthetime.jpg
:alt: the Style at the time
:width: 200px
:align: right
```

Our first example of the accumulation of roundoff effors comes from the [Vancouver stock exchange](https://en.wikipedia.org/wiki/Vancouver_Stock_Exchange) (now defunct, this wasn't its only problem).  In 1982 the exchange instituted a new index initialized to a value of 1000.000 (having 7 digits was part of the index's definition and is what is usually quoted for stock exchange indices.  At that time 32-bit floating point numbers were the "state-of-the-art" at the time and as we noted above these only have about 7 decimal digits.).  Note that the index is just the total value of the companies that trade on the exchange.  To provide continuous updates for the index you could recalcuate the index by adding up all the stock values for all companies at fixed intervals, or you could just add the net change of a given stock after each trade.  Mathematically both should give the same value, but the second should generally be much faster to compute as it only involves one stock.  For an individual operation the difference between a chop and a round is very small.  However, these computations in question were done in floating point using a chop (this predated the current IEEE standard) and were done about 3000 times each day.  Note that the chop operation biases results down.  The accumulated truncations resulted in an erroneous drop of around 25 points per month until it was noticed and corrected almost two years later .  This resulted in a Friday close of 524.811 being corrected to 1098.892 on Monday morning, a change of over 50% !.




