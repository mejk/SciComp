#!/usr/bin/env python
# coding: utf-8

# ## Gaussian Integration
# 
# So far, we have focussed on integration schemes where the function is sampled at regular intervals.  These are very useful for data that comes to us in this form, but if we wish to integrate a known function as accurately as possible it is better to take advantage of the freedom we have to choose our nodes, just as we did for interpolation where selecting Chebyshev points was optimal.
# 
# Consider that quadrature formulas are typically of the form
# 
# $$
# \int_a^b f(x) dx = \sum_{i=0}^{n-1} c_i f(x_i) + error,
# $$
# 
# which has $2n$ parameters (note for this section we are stopping the sum at $n-1$ rather than $n$ as this is conventional for Gaussian quadrature formulas).  The idea of Gaussian integration is that with these $2n$ parameters it should be possible to chose them to ensure that we can integrate all polynomials of degree less than or equal to $2n-1$ *exactly*.  
# 
# Before we do this, it is useful to first transform to a standard interval, namely $y$ in $[-1,1]$, from the original $x$ in $[a,b]$.  Similar to what we did with the Chebyshev interpolation, we use the change of variables
# 
# $$ x = \frac{b-a}{2}y+\frac{b+a}{2}. $$
# 
# We must also remember to perform the appropriate change of the integral measure,
# 
# $$\int_a^b f(x) dx = \int_{-1}^1 f\left(\frac{b-a}{2}y+\frac{b+a}{2}\right) \frac{dx}{dy} dy,$$
# 
# with $\frac{dx}{dy}=\frac{b-a}{2}$.  The $n-$point Gaussian quadrature routine will then result in
# 
# $$\int_a^b f(x) dx \approx \frac{b-a}{2}\sum_{i=0}^{n-1} c_i f\left(\frac{b-a}{2}y_i+\frac{b+a}{2}\right).$$
# 
# So, we will focus on integration over $[-1,1]$ below.
# 
# **Theorem** Suppose $\{x_0,x_1,\cdots,x_{n-1}\}$ are the roots of the $n$th Legendre polynomial $P_n(x)$ and 
# 
# $$ c_i=\int_{-1}^1 L_i^{n-1}(x) dx,\quad i=0,1,\cdots,n-1$$
# 
# where $L_i^{n-1}(x)$ is the Lagrange polynomial (from interpolation).  Then if $p(x)$ is any polynomial of degree less than or equal to $2n-1$, then
# 
# $$ \int_{-1}^1 p(x) dx = \sum_{i=0}^{n-1} c_i p(x_i),$$
# 
# exactly.
# 
# **Proof:**  First look at the case where the degree of $p(x)$ is less than $n$.  Then
# 
# $$ p(x) = \sum_{i=0}^{n-1} L_i^n(x) p(x_i) $$
# 
# is an exact interpolation of $p(x)$ (the [interpolation error](../InterpFit/InterpErrors) involves $\frac{d^n p(x)}{dx^n}$ which is zero for a polynomial of degree less than $n$).  Hence,
# 
# $$\int_{-1}^1 p(x)dx = \int_{-1}^1 \sum_{i=0}^{n-1} L_i^n(x) p(x_i) = \sum_{i=0}^{n-1} c_i p(x_i),$$
# 
# as claimed in the theorem.  Now suppose that the degree of $p(x)$ is at least $n$ but less than or equal to $2n-1$.  Then we can write 
# 
# $$p(x) = q(x)P_n(x) + r(x),$$
# 
# where $P_n(x)$ is the $n$th Legendre polynomial (which has degree $n$) and $q(x)$ and $r(x)$ are polynomials of degree less than $n$.  (To construct $q(x)$ you pick its coefficients so that $q(x)P_n(x)$ has coefficients that match coefficients of $p(x)$ for terms $x^{2n-1}$ to $x^n$.  $r(x)$ is then whatever is left over).  Now,
# 
# $$ p(x_i) = q(x_i)P_n(x_i) + r(x_i) = r(x_i),$$
# 
# where the last step follows from the fact that the $x_i$ are the roots of $P_n(x_i)$.  As a result,
# 
# $$\sum_{i=0}^{n-1} c_i p(x_i) = \sum_{i=0}^{n-1} c_i r(x_i).$$
# 
# Also,
# 
# $$
# \begin{align}
# \int_{-1}^1 p(x) dx &= \int_{-1}^1\left(q(x)P_n(x) + r(x)\right)dx,\\
# &= \int_{-1}^1 q(x)P_n(x) dx + \int_{-1}^1  r(x) dx.
# \end{align}
# $$
# 
# Now $q(x)$ has degree less than $n$ so can be written using the Legendre polynomials as a basis (they are an orthogonal basis set for polynomials), i.e.
# 
# $$
# q(x) = \sum_{i=0}^{n-1} a_i P_i(x),
# $$
# 
# for some constants $a_i$.  As a result,
# 
# $$
# \int_{-1}^1 q(x)P_n(x) dx = \sum_{i=0}^{n-1} a_i \int_{-1}^1 P_i(x)P_n(x) dx =0,
# $$
# 
# as $P_n(x)$ is orthogonal to all the $P_i(x)$ with $i<n$.  As a result, we now have
# 
# $$
# \begin{align}
# \int_{-1}^1 p(x) dx&=\int_{-1}^1  r(x) dx,\\
# &= \sum_{i=0}^{n-1} c_i r(x_i),
# \end{align}
# $$
# 
# where the last step is exact as $r(x)$ is of degree less than $n$ (and we showed this was exact for such polynomials in the first step of the proof above).  
# 
# --------
# 
# A general formula for the weights and nodes for Gauss-Legendre integration is not available.  However, the first few have all been tabulated and are listed below for reference :
# 
# | Number of nodes, $n$ | Points, $x_i$ | weights, $w_i$  |
# | :------------------: | :-----------: | :-------------: |
# | 1                    | 0             | 2               |
# | 2                    | $\pm \frac{1}{\sqrt{3}}$ | 1     |
# | 3                    | 0,            | $\frac{8}{9},$    |
# |                      | $\pm \sqrt{\frac{3}{5}}$ | $\frac{5}{9}$ |
# | 4                    | $\pm \sqrt{\frac{3}{7}-\frac{2}{7}\sqrt{\frac{6}{5}}},$ | $\frac{18+\sqrt{30}}{36},$ |
# |                      | $\pm \sqrt{\frac{3}{7}+\frac{2}{7}\sqrt{\frac{6}{5}}}$| $\frac{18-\sqrt{30}}{36}$ |
# | 5                    | 0,             | $\frac{128}{225},$ |
# |                      | $\pm \frac{1}{3}\sqrt{5-2\sqrt{\frac{10}{7}}},$ | $\frac{322+13\sqrt{70}}{900},$ |
# |                      | $\pm \frac{1}{3}\sqrt{5+2\sqrt{\frac{10}{7}}}$ | $\frac{322-13\sqrt{70}}{900}$ |
# | 7                    | 0,             | 0.41795 91836 73469, |
# |                      | $\pm$0.40584 51513 77397, | 0.38183 00505 05119, |
# |                      | $\pm$0.74153 11855 99394, | 0.27970 53914 89277, |
# |                      | $\pm$0.94910 79123 42759  | 0.12948 49661 68870  |
# 
# 
# SciPy has an implementation of Gauss-Legendre integration illustrated in the example below:

# In[1]:


import numpy as np
from scipy import integrate
normaldist = lambda x: 1/np.sqrt(np.pi) * np.exp(-x**2)
print("n=1 result = ",integrate.fixed_quad(normaldist, 0.0, 2.0, n=1))
print("n=2 result = ",integrate.fixed_quad(normaldist, 0.0, 2.0, n=2))
print("n=3 result = ",integrate.fixed_quad(normaldist, 0.0, 2.0, n=3))
print("n=4 result = ",integrate.fixed_quad(normaldist, 0.0, 2.0, n=4))
print("n=5 result = ",integrate.fixed_quad(normaldist, 0.0, 2.0, n=5))
print("n=7 result = ",integrate.fixed_quad(normaldist, 0.0, 2.0, n=7))


# We also integrated this same function in our example for [Romberg integration](./HigherOrderInt).  The accuracy of our result for $n=7$ here (so 7 function evaluations) was only obtained in the row for 16 steps (17 function evaluations) using Romberg integration!   

# In[ ]:




