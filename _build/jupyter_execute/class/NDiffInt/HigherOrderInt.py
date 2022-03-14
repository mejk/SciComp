#!/usr/bin/env python
# coding: utf-8

# ## Higher Order Integration Schemes
# 
# The composite trapezoidal rule is functional, but not all that accurate.  At this point, the only method we have to improve accuracy is to divide the interval into smaller segments.  We can, however, use results for different step sizes $h$ to improve both results by eliminating the lowest order error.  To illustrate, consider the trapezoidal rule for a step $h_1=(b-a)$ and then $h_2=(b-a)/2$,  
# 
# $$
# \begin{align}
# I_1 &=\int_a^b f(x) dx = \frac{h_1}{2}\left[f(a)+f(b)\right] - (b-a)\frac{h_1^2}{12} f''(\eta_1),\\
# I_2 &=\int_a^b f(x) dx = \frac{h_2}{2}\left[f(a)+2f(a+h)+f(b)\right] - (b-a)\frac{h_2^2}{12} f''(\eta_2).
# \end{align}
# $$
# 
# The problem with attempting to use these two equations to eliminate the error term lies in the fact that $\eta_1$ and $\eta_2$ are not likely to be the same.  However, it is possible to show that, for a suitably smooth function, the error term can be replaced by a power series om even powers of $h$, namely
# 
# $$
# E(h) = - (b-a)\frac{h^2}{12} f''(\eta_1) = \sum_{j=1}^n K_j h^{2j} + \mathcal{O}(h^{2n+2}),
# $$
# 
# where the $K_j$ are constants, independent of the division $h$. Using this, and $h_2=h_1/2$ we can rewrite the two trapezoidal methods above as
# 
# $$
# \begin{align}
# I_1 &= \frac{h_1}{2}\left[f(a)+f(b)\right] + K_1 h_1^2 + K_2 h_1^4+ \mathcal{O}(h_1^6),\\
# I_2 &= \frac{h_2}{2}\left[f(a)+2f(a+h_2)+f(b)\right] + K_1 h_2^2 + K_2 h_2^4 + \mathcal{O}(h_2^6),\\
# &= \frac{h_1}{4}\left[f(a)+2f(a+h_2)+f(b)\right] + K_1 \frac{h_1^2}{4} + K_2 h_2^4+\mathcal{O}(h_1^6).
# \end{align}
# $$
# 
# Now note that
# 
# $$
# \int_a^b f(x) dx=\frac{4 I_2 - I_1}{3} = \frac{h_2}{3}\left[f(a) + 4 f(a+h_2) + f(b) \right] - \frac{12}{3} K_2 h_2^4 + \mathcal{O}(h_2^6).
# $$
# 
# The resulting numerical integration scheme is known as *Simpson's Rule* and the error is now $\mathcal{O}(h^4)$ rather than the $\mathcal{O}(h^2)$ for the (composite) trapezoidal rule.
# 
# This technique of eliminating error terms using results from two step sizes is generally referred to as Richardson's extrapolation.  We can also use this method to get rid of higher order error terms as well which brings us to *Romberg's Method*.
# 
# ## Romberg's Method
# 
# We start by using the composite trapezoidal rule for $m_1=1,\, m_2=2,\, m_3=4,\,\cdots m_n=2^{n-1}$ subintervals with regularly spaced points $h_k=\frac{b-a}{m_k}$ apart. In particular, when we do this we don't want to recompute $f(x)$ any more than necessary so we need to write the trapezoidal rule for the different intervals in such a way that we use our previous work:
# 
# $$
# \begin{align}
# R_{1,1} &= \frac{h_1}{2}\left[f(a)+f(b)\right],\\
# R_{2,1} &= \frac{h_2}{2}\left[f(a)+f(b) + 2 f(a+h_2)\right],\\
# &= \frac{1}{2}\left[ \frac{h_1}{2}\left\{ f(a)+f(b)\right\} + 2h_2 f(a+h_2)\right],\\
# &= \frac{1}{2}\left[ R_{1,1} + h_1 f(a+h_2)\right],\\
# R_{3,1} &= \frac{h_3}{2}\left[f(a)+f(b) + 2\left\{f(a+h_3)+f(a+2 h_3) + f(a+3 h_r)\right\}\right],\\
# &= \frac{1}{2}\left[ R_{2,1} + h_2 \left\{ f(a+h_3)+ f(a+3 h_r)\right\}\right],\\
# &\vdots \\
# R_{k,1} &= \frac{1}{2}\left[ R_{k-1,1}+h_{k-1} \sum_{i=1}^{2^{k-2}} f(a+(2i-1)h_k) \right].
# \end{align}
# $$
# 
# We now apply the extrapolation technique to refine our results using
# 
# $$
# R_{k,2}=\frac{4 R_{k,1}-R_{k-1,1}}{3},
# $$
# 
# on each successive pair of our previous results.
# 
# We then apply the extrapolation technique to successivly higher orders using
# 
# $$
# R_{i,j} = \frac{4^{j-1}R_{i,j-1}-R_{i-1,j-1}}{4^{j-1}-1},\qquad j=2,3,\cdots,n.
# $$
# 
# 
# **Example**  Suppose we want to compute $\int_0^\pi \sin x\, dx$  (which in this case we know is $2$).  We construct the following tableau:  
# 
# $$
# \begin{align}
# {\begin{array}{ccccccc}
#     R_{1,1}    &         &         &         &         & &\\
#     \downarrow & \rangle & R_{2,2} &         &         & &\\
#     R_{2,1}    &         &         & \rangle & R_{3,3} & &\\
#     \downarrow & \rangle & R_{3,2} &         &         & \rangle & R_{4,4}\\
#     R_{3,1}    &         &         & \rangle & R_{4,3} & &\\
#     \downarrow & \rangle & R_{4,2} &         &         & &\\
#     R_{4,1}    &         &         &         &         &\\
#   \end{array} } 
# \end{align}
# $$
# 
# With actual numbers, this translates to
# 
# 
# $$
# \begin{align}
# {\begin{array}{ccccccc}
#     0    &         &         &         &         & &\\
#     \downarrow & \rangle & 2.094... &         &         & &\\
#     1.57079...    &         &         & \rangle & 1.9985... & &\\
#     \downarrow & \rangle & 2.0045... &         &         & \rangle & 2.0000055...\\
#     1.896...    &         &         & \rangle & 1.999983... & &\\
#     \downarrow & \rangle & 2.00026... &         &         & &\\
#     1.974...    &         &         &         &         &\\
#   \end{array} } 
# \end{align}
# $$
# 
# We see that even though the underlying composite trapezoidal rule results in the first column are not all that accurate, extrapolation of those results to the fourth column gives  six digits of accuracy.  It should also be clear that we can get an estimate for our (forward) error by comparing the difference between our best two results, in this case $R_{4,4}$ and $R_{4,3}$ where $|R_{4,4}-R_{4,3}|\sim 2\times 10^{-5}$.  Here, this is the error in $R_{4,3}$ and so an overestimate of the error for $R_{4,4}$.  
# 
# While these are fairly easy to code up yourself, there are also scipy versions of all of these integration routines as illustrated below where we use the various schemes to integrate $\frac{1}{\sqrt{\pi}}e^{-x^2}$ from $0$ to $2$.  We start with the results of the cumulative trapezoidal and cumulative Simpson's rule with our interval divided into eight segments:

# In[1]:


import numpy as np

def f(x):
   return 1/np.sqrt(np.pi) * np.exp(-x**2)

x = np.linspace(0, 2, num=9, endpoint=True)
print("sample points: ",x)

y = f(x)
from scipy import integrate
I1 = integrate.trapezoid(y, x)
I2 = integrate.simpson(y, x)
print("trapezoidal = ",I1, ", Simpsons = ",I2)


# The accuracy of these results is difficult to judge, other than by comparing them which gives us an estimate for the trapezoidal rule.  In contrast, the Romberg integration keeps adding a row to the tableau until the results converge:

# In[14]:


from scipy import integrate

normaldist = lambda x: 1/np.sqrt(np.pi) * np.exp(-x**2)
result = integrate.romberg(normaldist, 0, 2, show=True)


# Our previous results from the trapezoidal and Simpson's rule correspond to the first two results in the fourth row. 

# In[ ]:




