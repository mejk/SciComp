#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# 

# 
# # Random numbers
# 
# ````{panels}
# :column: col-lg-12 p-2
# 
# <!--
# ```{image} ../../images/logos/Jupyter_logo.svg
# :alt: Jupyter
# :width: 150px
# :align: right
# ```
# -->
# 
# **Learning goals:** 
# 
# - To understand how random numbers are generated
# - To be able generate distributions of random numbers 
# - To become familiar with python's methods for random number generation
# 
# **Keywords:** random numbers
# 
# **Note:** Since Python and Jupyter are core components of the course, it is imperative that the installation works.
# 
# <!--
# **Associated material:** 
# 
# -->
# 
# **See also:**
# 
# - [Random number](https://en.wikipedia.org/wiki/Random_number) at Wikipedia.
# - [Random number generation](https://en.wikipedia.org/wiki/Random_number_generation) at Wikipedia.
# - [Pseudorandom number generator](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) at Wikipedia.
# 
# 
# ````

# In[ ]:





# 
# <div class="bg-light text-info border border-info">
# <small>
#     
# ```{epigraph} 
# *The generation of random numbers is too important to be left to chance.*
# 
# -- Robert R. Coveyou, Oak Ridge National Laboratory
# ```
#     
# </small></div>
#         
#         
# Almost all kinds of simulations in physics, chemistry, engineering, economics and social science use random numbers somewhere during the process. Random numbers are also needed in practical applications such as modelling he behavior of stock markets, machine learning and deep learning. Pehaps the most critical one is cryptography: Every time you use a computer or a mobile phone, you are using random numbers. The security of your on-line banking, purchases and messaging all depend on the random numbers.  
# 
# A precise mathematical definition of random numbers is difficult to give but let us start with an informal one, which contains the most important properties we demand from random numbers. First, we demand that the random numbers are evenly distributed in interval (0,1); as the preceding indicates, random numbers are assumed to be real. This is also how your computer's intrinsic RNG produces random numbers. The random numbers should be random. How can we define random? Intuitively, an arbitrarily long sequence of numbers should "look" random. That means that no sub-interval within (0,1) should be preferred, and there should be no recurring patterns or sequences of numbers. To be more precise, there should be no correlations between successive random numbers or sequences of of random numbers. We will return to this topic later and define some statistical and physical measures as how to study randomness. 
# 
# You may ask if it really matters or if it is really so hard to define what is random. As for the first question, it is easy to convince yourself if you think of, for example, a very practical and important problem of data encryption. If your random numbers have predictable correlations or repeating patterns, it may become very easy to break the encryption, which, in practice, could lead, for example, to unsafe transmission of you credit card information with on-line purchases. As for the second question, try to come up with a definition of randomness! Is the sequence {1,1,1,1} more random than {2190,9,1,14,276}? If you picked one over the other, what is your criterion and can be it applied generally? 
# 
# 
# 
# 
# ## Historical tidbits
# 
# As John von Neumann joked, "Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin." 
# 
# ## Random numbers vs Pseudo-random numbers
# 
# <blockquote>
# 'Random' numbers chosen by humans:
#  In a recent study it was shown that 17 is the most common 'random number' 
# when people were asked to choose a random number between 1 and 20. 
# </blockquote>
# 
#     
# As indicated above, our aim is to generate random numbers using deterministic algorithms. That sounds almost like an oxymoron: how can we produce random numbers using a deterministic algorithm? 
# 
# Let us first classify random numbers in the following two categories 
# 1. True random numbers and 
# 2. Pseudo-random numbers. 
# 
# True random numbers are produced by a physical process such as radioactive decay. These numbers are truly random in the sense that there are no correlations present and that the successive numbers are totally unpredictable.
# 
# Those numbers are tabularized and may then be used. The problem is, however, that that method is very impractical. To overcome that difficulty, several algorithms have been developed  to produce sequences of pseudo-random numbers which mimic the true random numbers as well as possible. The goodness, i.e., quality, of these pseudo-random numbers can be tested in various ways as will be discussed below. When we discuss random numbers, we actually mean pseudo-random numbers unless otherwise mentioned. 
# 
# Development of random number generators has been a very active field of research since (and already before) the invent of modern computers and remains to be so even today.
# 
# ### Can humans produce random numbers?
# 
# The answer is no: In a recent study it was shown that 17 is the most common ’random number’ when people were asked to choose a
# random number between 1 and 20.
# 
# 
# ## Requirements for a good Random Number Generator
# 
# 1. Randomness 
# 2. Long period. 
# 3. RNG should be portable from one CPU architecture to another 
# 4. The algorithm should be fast and use little memory 
# 5. The algorithm should be parallelizable 
#     
# ## Uniform Random Numbers
# When talking about random numbers, we typically mean uniformly distributed random numbers. Typically we mean that random numbers are uniformly distributed between 0 and 1. It is then possible to generate other distributions from thos uniform distribution, e.g., using the Box-Müller method. 
# 
# ### Linear Congruential Generator (LCG)
# 
# Linear Congruential Generator are the one of the oldest and most common types of pseudo-random number generator. They are very easy to implement, they are fast, and use minimal amount of memory. They are also very portable, but the downside is that they do not produce high-quality random numbers.  Thus, when randomness is critical, LCGs should not be used. Such applications include calculation of critical exponents in continuous phase transitions and cryptography. 
# 
# LCG generators are defined by
# 
# \begin{equation}
# x_{i+1} = (ax_i + c )\, \mathrm{mod} \, m
# \end{equation}
#         
# The above is a recurrence relation and numbers $\{x_i \}$ form a set of pseudo-random numbers. Notice also the above equation is defines line with a modulo operation added. The modulo operation means that the result is wrapped if it exceeds the limit set by $m$ since the modulo operation returns the remainder of $(ax_i + c)/m$. LCG generator is said to be of full period if the period is exactly $m$. 
# 
# The parameters are defined as follows 
# - $a$: multiplier. $1<a<m$.  
# - $c$: increment. $0 \le c < m$.  
# - $m$: period. The operation is even faster if $m$ is chosen to be a power of 2. 
# 
# 
# 
# 
# In addition, one needs a seed ($x_0$) to start the random number generator. The seed has to be supplied when the RNG is called the first time. Using the above parameters, the following notation is typically used for LCGs: 
# 
# \begin{equation}
# \mathrm{LCG}(a,c,m)
# \end{equation}
# 
# It has been well established that LCGs are very sensitive to the choice of $a$, $c$, and $m$. Generators with $c=0$ are called multiplicative congruential generators (MCG). Sometimes generators with $c \> 0$ are called mixed. For MCG's $0 < s < m$. It has been shown \cite{xx} that MCGs  are never full period. For MCGs, typical notation is thus 
# 
# \begin{equation}
# \mathrm{LCG}(a,m).
# \end{equation}
# 
# Note on choosing $a$, $c$, and $m$: First of all, using a larger value for $m$ (for a 32-bit computer one typically has $m=2^{32}$) gives a long period as it goes through all accessible numbers. That is not enough, but $a$ and $c$ have to be chose carefully as well. That is somewhat of an art and there are tables listing 'safe' numbers $a$, $c$, and $m$. 
# 
# LCGs have also the widely known property that the rightmost digits contain correlations. 

# In[ ]:





# ### Fibonacci Method
# 
# LCGs can be improved by adding more multipliers, i.e., we obtain the form
# 
# $$
# x_i = (a_1 x_{i-1}+ \cdots a_r x_{i-r}) \, \mathrm{mod} \, m.
# $$
# 
# Here we must have $r >1$  and $a_r \ne 0$. If we choose $r=2$, $a_1=1$  and $a_2=1$, we obtain the so-called Fibonacci generator
# 
# $$
# x_i = (x_{i-1}+ x_{i-2}) \, \mathrm{mod} \, m.
# $$
# 
# 
# The name of the method comes from Fibonacci numbers (this sequence was know to Indian mathematicians even earlier, but Fibonacci introduced it in Europe in 1202) which are defined as a sequence
# 
# $$
# x_n =  \left\{
# \begin{array}{ll }
#       0 & \, \mathrm{if \,}\,  n=0    \\
#       1 &    \, \mathrm{if \,}\, n=1 \\
#       x_{n-1} + x_{n-2}  & \, \mathrm{if \,}\, n>1.
# \end{array}
#  \right. 
# $$
# 
# 
# 
# Given the two 'seeds', each number is a sum of the two immediately preceding numbers. Fibonacci sequence looks like this 
# 
# $$
# \begin{array}{| l| l | l | l | l | l | l | l | l | l | l |} \hline
#       x_0 & x_1 & x_2 & x_3 & x_4 & x_5 & x_6 & x_7 & x_8 & x_9 & x_{10}    \\ \hline
#       0     &  1     & 1    &  2     &  3    & 5     & 8      & 13   &  32   & 34  & 55 \\  \hline
# \end{array}
# $$
# 
# As such, this method for random number generation does not have particularly good properties. LCGs are typically preferred over them. The Fibonacci generator can be improved, however. 

# ### Lagged Fibonacci Generator (LFG)
# 
# LFG is based on a generalization of the above Fibonacci  sequence, but now a lag is defined by two integers $q$ and $r$ such that 
# 
# $$
# x_i = (x_{i-q} \otimes x_{i-r}) \mathrm{\,mod\,} m.
# $$
# 
# Here, $q>r$ and operation $ \otimes $ is one of the following binary operations:
# 
# $$
# \begin{array}{ll}
#      + & \, \mathrm{addition}    \\
#       - &  \, \mathrm{subtraction} \\
#       \times & \,  \mathrm{multiplication} \\
#       \oplus &  \, \mathrm{XOR\,\, \mathrm{(exclusive\,\, OR)}\, if\,\,}\, m\, \mathrm{is\, a \,power\, of\, two.}   
# \end{array}
# $$
# 
# Notation for LFG generators is then the following:
# 
# $$
# \mathrm{LFG}(q,r,\otimes).
# $$
# 
# Initialization of an LFG generator requires $q$ seeds which can be produced using another RNG. LFGs have a long period, and they seem to have good properties. They have not been studied to such extent as the LCGs have. An example of a fairly commonly used LFG generator is RAN3 from Numerical Recipes. The exact form of RAN3 is LFG(55,24,-). 
# 

# <!-- 
# Generalized Feedback Shift Register Generators (GFSR)
# -->

# <!-- 
# Mersenne Twister
# -->

# ### Few words on implementation
# 
# Although the above methods look simple, one has to pay attention to their implementation. Vattulainen \cite{xx} has pointed out that that using single precision instead of double precision in the case of an LFG can lead to a decrease in period by a factor of about $10^7$. 

# ## How to produce different distributions 
# 
# So far we have only discussed uniformly distributed random numbers. There is a good reason to this - random numbers in any other distribution are almost always generated starting from random numbers distributed uniformly between 0 and 1. Data, however, often comes in many other forms than uniformly distributed. For example, the peaks in various spectra have a Gaussian or Lorentzian shape, the decay of a radioactive sample follows an exponential function, and so on. The practical question is: How to produce random numbers following a pre-defined distribution using random numbers which are evenly distributed in $(0,1)$. Why should evenly distributed random numbers be used as a starting point? 
# 
# There are two basic approaches to generate other distributions than the uniform. The first is the analytical one, the other the numerical von Neumann rejection method. 

# ### Gaussian distribution: The Box-Müller algorithm
# 
# In the [Box-Müller method](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform), two Gaussian distributions in 2D are considered. Their joint distribution is 
# 
# $$
# f(x,y)= \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}x^2} \frac{1}{\sqrt {2 \pi}} e^{-\frac{1}{2}y^2} = \frac{1}{2 \pi} e^{-\frac{1}{2}x^2+y^2}.
# $$
# 
# Switching to polar coordinates, and remembering that the surface element transforms as $dx \,dy = r \, dr \,d \phi$ we get the polar density distribution function as
# 
# $$
# g(r, \phi) = f(x,y) r = \frac{1}{2 \pi} e^{- \frac{1}{2}r^2}
# $$
# and
# 
# \begin{eqnarray}
# g_1 & = & \sqrt{-2 \ln (r_1) \cos ( 2 \pi r_2)} \\
# g_2 & = &  \sqrt{-2 \ln (r_1) \sin ( 2 \pi r_2)}
# \end{eqnarray}
# 
# Algorithmically this method is fine, there is no wasted effort in terms of misses or something like that. But in terms of computational efficiency, it leaves much to be hoped for. It requires computation of the functions such a square root, $\log$, $\sin$ and $\cos$. Calculating all of these, and especially the last three ones, is excruciatingly slow compared to the simple arithmetic operations - it would be nice to have a more efficient routine. 
# 

# ### How to test Random Number Generators
# 1. Statistical tests 
# > - [Kolmogorov-Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test) 
# > - [$\xi^2$ test](https://en.wikipedia.org/wiki/Chi-squared_test) 
# > - [Spectral tests](https://en.wikipedia.org/wiki/Spectral_test) 
# 2. Bit-wise tests (if the RNG uses integer arithmetics) 
# 3. Visual tests 
# 4. Physical tests 

# <!-- 
# ## Final remarks 
# 
# Now, when generators tend to be at least fairly decent, the following opinion is probably close to the truth (at least in a male-chauvinistic worldview): 
# 
# <blockquote>
# A random number generator is much like sex: 
# when it is good it is wonderful and when it is bad 
# it is still pretty good.<br>
# - George Marsaglia 
# </blockquote>
# 
# -->

# ## Random numbers using Python
# <!-- To verify: Numpy uses Mersenne twister -->
# 
# NumPy includes a package called `random`. That is what we will use. 

# In[1]:


import numpy as np


# There is no need to define the seed. But sometimes it is a good idea to do so as using the same seed can be used for reproducibility:

# In[2]:


seed = 182828
np.random.seed(seed)


# ### Uniform random numbers
# Single random number can drawn from a uniform distribution $x_i \in [0.0,1.0)$ the following way:
# 

# In[3]:


print(np.random.random())
print(np.random.rand())


# Array of random numbers (from a uniform distribution $x_i \in [0.0,1.0)$) of length 2:
# 

# In[4]:


np.random.rand(2)


# ### Gaussian random numbers
# 

# In[5]:


np.random.standard_normal()


# ### Integer(s) within given limits
# 
# A single random number between 0 and 100:

# In[6]:


np.random.randint(low = 0, high = 100)


# The following gives an array of 5 random numbers between 0 and 100:

# In[7]:


np.random.randint(low = 0, high = 100, size = 5)


# In[8]:


## The above combined:

import numpy as np
seed = 182828

np.random.seed(seed)
a = np.random.random()
b = np.random.rand()
c = np.random.rand(2)
d = np.random.standard_normal()
e = np.random.randint(low = 0, high = 100)
f = np.random.randint(low = 0, high = 100, size = 5)

print('One random number from a uniform distribution:', a)
print('One random number from a uniform distribution:', b)
print('Array of two random numbers from a uniform distribution:', c)
print('One random number from a Gaussian distribution:', d)
print('One random integer between 0 and 100:', e)
print('Array of five random integers between 0 and 100:', f)


# ### What else `np.random` has?

# In[9]:


help(np.random)


# ### Is numpy really faster?
# 
# There are other methods, such as the generic python module `random`, to generate random numbers. Let's test the two methods. We have already imported `numpy` but let's do that again for completeness, and let's define `N` as the number of random numbers we want to generate

# In[10]:


import random
import numpy as np
N=1000000


# In[ ]:





# Let's test the two methods by simply summing up the random numbers. In the case of the generic `random`, we must use a loop:

# In[11]:


get_ipython().run_cell_magic('time', '', '\ny = 0      \nfor i in range(N):\n    x = random.uniform(0, 1)\n    y += x')


# With `numpy`, no loop is needed:

# In[12]:


get_ipython().run_cell_magic('time', '', '\nx = np.random.uniform(0, 1, N)\ny = np.sum(x)')


# As the results show, `numpy` is about an order of magnitude faster! The difference becomes even larger if a more complex operation than simle addition is performed.

# 
