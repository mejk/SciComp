#!/usr/bin/env python
# coding: utf-8

# # Horner's algorithm
# 
# ## Example: Evaluating polynomials
# 
# To illustrate the affect of accumulation of roundoff errors let's imagine a decimal computer that does floating point arithemetic using a 3-digit chop.  Let's use this to compute the value of a polynomial written in the standard monomial basis:
# 
# $$ p(x) = x^3-6x^2+3x-0.147 $$
# 
# at the point $x=4.71$.  Using exact arithmetic
# 
# $$ p(4.71) = -14.634489. $$
# 
# Let $\mathcal{fl}(.)$ denote the 3 digit chop operation and note that this imaginary computer must do this recursively (i.e. after every arithemtic operation) so an expression like  $\mathcal{fl}(6 x^2)$ is evaluated as $\mathcal{fl}(6 \mathcal{fl}(x^2))$.  In particular, $ \mathcal{fl}(4.71^2)=\mathcal{fl}(22.1841)=22.1$ and $\mathcal{fl}(6 \mathcal{fl}(4.71^2))=\mathcal{fl}(6\times 22.1)=\mathcal{fl}(132.6)=132$.  Doing this for every arithmetic operation leads to  
# 
# $$ p^* = \mathcal{fl}(p(4.71)) = -14.0 $$  
# 
# Clearly we have lost a full digit of accuracy here (so only have 2 significant digits).  In this case, the result is not significantly improved using a rounding operation instead of a chop.  The question is:  Can we do any better or is this something we have to accept as part of not doing exact arithemtic?  The answer is that we can do better by rewriting the polynomial into a different, but mathematically equivalent form.  In this case, a nested multiplication:  
# 
# $$ \bar{p}(x) = ((x-6)x+3)x-0.147). $$  
# 
# It should not be too hard to see that $\bar{p}(x)$ is mathematically equivalent to our original polynomial $p(x)$.  If we evaluate this expression as written we get  
# 
# $$ \bar{p}^* =  \mathcal{fl}(\bar{p}(4.71)) = -14.5, $$  
# 
# much closer to the exact result (and still retaining 3 significant digits).  Why?  It turns out that $\bar{p}(x)$ requires fewer arithmetic operations to compute than $p(x)$ and this results in a smaller accumulation of roundoff errors.    
# 
# Let's generalize this to a generic polynomial in an [algorithm usually attributed to William Horner](https://en.wikipedia.org/wiki/Horner%27s_method#:~:text=In%20mathematics%20and%20computer%20science%2C%20Horner%27s%20method%20%28or,hundreds%20of%20years%20to%20Chinese%20and%20Persian%20mathematicians.).  There is evidence, however, that it is actually much older.
# 
# ## Horner's Algorithm (a.k.a. "nested multiplication")
# 
# To evaluate the polynomial  
# 
# $$p(x) = a_{n-1} x^{n-1} + a_{n-2} x^{n-2} + ... + a_1 x + a_0,$$  
# 
# first rewrite it in the form:  
# 
# $$p(x) = ((...((a_{n-1} x + a_{n-2})x+a_{n-3})x+...)x+a_1)x + a_0.$$
# 
# Note that, without loss of generality and in anticipation of coding this up, the coefficiencts have been labelled from $0$ to $n-1$ rather than $0$ to $n$.  This can now be easily turned into a short python code as follows.

# In[29]:


# Use Horner's algorithm to compute and return the polynomial
#    p(x) = a[0] + a[1] x^1 + a[2] x^2 + ... + a[n-1] x^(n-1)
# evaluated at x.
def horners(a, x):
    result = a[len(a)-1]
    for i in range(len(a)-2, -1, -1):
        result = result*x + a[i]
    return result
 
# Let's use the horners function defined above to evaluate the polynomial from the example above
coefficients = [-0.147, 3., -6., 1.]
x = 4.71

print("p(x) = ", horners(coefficients, x))


# To analyze the efficiency of algorithms like this, one usually counts the number of flops.  
# 
# **flop**: floating point operation consisting of one * and one + (i.e. $a*x+b$ is 1 flop).
# 
# Comparing Horner's algorithm with the evaluation using the monomial basis it is not too hard to see  
# 
# | method   |   number of flops |  
# |----------|----|  
# | Horner   |    $n$ |  
# | monomial basis | $2 n -1$ |    
# 
# The fewer flops involved, the lower the chance for the accumulation of roundoff errors plus you get the bonus of a faster and more efficient program.
# 
