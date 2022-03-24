# Sources of Errors in Scientific Computing

Errors can come from a number of sources and it is helpful to categorize these sources first:

1. **Blunders**.  This includes *syntax errors* and *logic errors* in your code.  The first are relatively easy to find, especially if you use a compiled language such as C/C++ and learn how to read the error messages from the compiler/interpreter.  The second are much harder to find but are probably most likely when your code gives results that don't seem to make sense.

2. **Data errors from measurements**.  The old saying "garbage in = garbage out" is relevant here.  This is can be a significant problem in data sciences.  It includes "over-fitting" where the misguided researcher fits not just the signal in a measurement but also the noise.  Another example we will examine in more detail in the section on interpolation is the "Runge Phenomenon".  This is an error that arises from using polynomial interpolation on equally spaced data points that can cause huge errors near the boundaries of the fitted domain.  It is also something that is common in extrapolation which is rarely successful just fitting data without an underlying model that you have strong reason to believe is valid outside the fitted domain.

3. **Truncation or discretization errors**.  We will discuss this in more detail later in this chapter.  These arise from the fact that our models and algorithms usually only try to approximate the solution.  

4. **Finite precision arithmetic**.  These stem from the fact that we cannot represent all possible real numbers on a computer.  This leads to issues of over/underflow and roundoff errors which we will explore in more detail in this chapter.
5. **Attempting to solve the wrong problem**.  This is much more common that you would think.  An example is trying to predict whether or not it will rain in a certain location 60 days from now (i.e. yes or no).  This is a poorly conditioned problem.  However, if you change the problem slightly and ask for the probability that it will rain in a certain location 60 days from now, this new problem is now solvable within reasonably well-defined error bounds.  

The first of these sources of errors are the sort of thing that is usually addressed in a computer science course and we will not spend much time here discussing it.  However, when you sit down to do the exercises this is likely to be the primarily source of errors that will consume your time.  Good coding practise and ensuring you understand the algorithm you are trying to implement before trying to code it up are the best way to avoid spending too much time on blunders.

While we will return to data errors later in the course when we discuss interpolation and regression, they are not the main focus of a numerical analysis course.  A good understanding of probability and statistics will help you in knowing how significant these sorts of errors may be in the problem you are trying to solve.

The last three sources of error will be something we will cover in detail in this course and by completion you should be adept at avoiding them.  


## Quantifying Error

To quantify error we need to first define what we mean.
If $p^*$ is an approximation to $p$, then:

-the *absolute* error is $|p-p^*|$,

-the *relative* error is $\frac{|p-p^*|}{|p|}$,

-and the number of *significant digits* is $t$ if $t$ is the largest positive integer with $\frac{|p-p^*|}{|p|} \leq 5 \times 10^{-t}$.

The advantage of the relative error is that it is scale invariant.  For example, if you measure the length of a pencil with a ruler to be $16$ cm with an absolute error of $0.5$ mm.  This absolute error depends on the unit of measurement.  If you measure in nm, then it is huge.  If you measure in parsecs, it is minuscule.  However, the relative error is $0.003$ independent of the units of measurement.  Note that the formula above actually says the relative error is $0.003125$, but we typically only quote errors to one significant digit.

