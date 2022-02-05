#!/usr/bin/env python
# coding: utf-8

# In[1]:



from IPython.display import Markdown as md
from IPython.core.magic import register_cell_magic


@register_cell_magic
def markdown(line, cell):
    return Markdown(cell.format(**globals()))# Diffusion 


# In[2]:




get_ipython().run_line_magic('matplotlib', 'inline')
#import markdown
a = "bla"
b = 0.21
print(b)
#%config InlineBackend.figure_format = 'svg'
#set_matplotlib_formats('svg')
from IPython.core.display import SVG
from IPython.display import Markdown as md

## TEST


# {{ b }}

# In[3]:


from datetime import datetime
#from IPython.display import Markdown as md
updated = datetime.now()
now = updated.strftime("%A, %B %d %Y at %H:%M" )


# # Diffusion - a brief introduction

# In[4]:


md(f"-Last updated on {now}")


# 
# Linear response theory for concentration becoming equlibrated by molecular motions. 
# 
# Latin: __diffundere__ "to spread out".
# 
# <!-- 
# ## Random notes:
# 
# Diffusion in other languages:
# 
# |  |  |  |
# | --- | --- | --- |
# | ENG: Diffusion | GER: Diffusion | FRA: Diffusion |
# | ESP: Difusión  | FIN: Diffuusio | SWE: Diffusion  |
# | RUS: Диффу́зия  | | |
# 
# Brownian motion:
# 
# |  |  |  |
# | --- | --- | --- |
# | ENG: Brownian motion | GER: Brownsche Bewegung | FRA: Mouvement brownien |
# | ESP: Movimiento browniano  | FIN: Brownin liike | SWE: Brownsk rörelse  |
# | RUS: Броуновское движение  | | |
# 
# -->
# 
# ## Brief history of diffusion: First observations and landmarks
# 
# - Around 60 BC: [Lucretius](https://en.wikipedia.org/wiki/Lucretius) (Rome) wrote in a poem "*Observe what happens when sunbeams are admitted into a building and shed light on its shadowy places. You will see a multitude of tiny particles mingling in a multitude of ways... their dancing is an actual indication of underlying movements of matter that are hidden from our sight... It originates with the atoms which move of themselves*". This is sometimes seen as the first description of Brownian motion and statement for the existence of atoms.  
# - 1785: [Jan Ingenhousz](https://en.wikipedia.org/wiki/Jan_Ingenhousz) (NED). Powdered charcoal on an alcohol surface. He is more known for discovering photosynthesis.
# - 1827: [Robert Brown](https://en.wikipedia.org/wiki/Robert_Brown_(botanist,_born_1773)) (SCO). Pollen particles (of _Clarkia pulchella_) on a water surface. Also known for classification of plants and discovering the cell nucleus.
# - 1856: [Adolf Fick](https://en.wikipedia.org/wiki/Adolf_Eugen_Fick) (GER). Fick's law of diffusion.
# - 1880: [Thorvald N. Thiele](https://en.wikipedia.org/wiki/Thorvald_N._Thiele) (DEN). Probably the first mathematical model for Brownian motion. The theory was in a paper discussing the method of least squares and he used cumulants and likelyhood function.
# - 1900: [Louis Bachelier](https://en.wikipedia.org/wiki/Louis_Bachelier) (FRA; student of Poincaré) studied stock market fluctuations and in his thesis (titled *Théorie de la spéculation*) developed a theory for Brownian motion. In particular, he stated that probability could diffuse the same way as heat does. One of the first mathematical models for Brownian motion. 
# - 1905: [Albert Einstein](https://en.wikipedia.org/wiki/Albert_Einstein) (GER/SUI/USA). Theory of Brownian motion. One of Einstein's *annus mirablis* papers - _"Über die von der Theorie molekularkinetischen Theorie  der Wärme geforderte Bewgung von in ruhenden  Flüssigkeiten suspendierten Teilchen"_. Importantly, Einstein's work provides a method to determine Avogadro's constant and hence the existence of atoms. 
# - 1905: [William Sutherland](https://en.wikipedia.org/wiki/William_Sutherland_(physicist)) (SCO/AUS)
# - 1905: [Karl Pearson](https://en.wikipedia.org/wiki/Karl_Pearson) (UK): The term *random walk*
# - 1906: [Karl Pearson](https://en.wikipedia.org/wiki/Karl_Pearson) (UK) and [Lord Rayleigh](https://en.wikipedia.org/wiki/John_William_Strutt,_3rd_Baron_Rayleigh) (UK)
# - 1906: [Marian von Smoluchowski](https://en.wikipedia.org/wiki/Marian_Smoluchowski) (POL). Independent (of Einstein) theory for Brownian motion - _"Zur kinetischen Theorie der Brownschen Molekularbewegung und der Suspensionen"_ 
# - 1908: [Paul Langevin](https://en.wikipedia.org/wiki/Paul_Langevin) (FRA)
# - 1908: [Jean Perrin](https://en.wikipedia.org/wiki/Jean_Baptiste_Perrin) (FRA): experimental verification of Einstein's theory
# - 1914: Ivar Nordlund (SWE). Time resolved measurements using a moving plate. This allowed for measurements over long times.
# - 1926: Nobel Prize in Physics to Jean Perrin "[for his work on the discontinuous structure of matter](https://www.nobelprize.org/prizes/physics/1926/perrin/facts/)"
# - 1931: Eugen Kappler (GER). Time resolved measurements. First to experimentally measure the Gaussian Boltzmann distribution.
# <!--
# - 1996: Crocker and Grier: 
# -->
# 
# <b>Note:</b> The [existence](https://en.wikipedia.org/wiki/History_of_molecular_theory) of atoms was not accepted until well into the 20th century. It was strongly opposed by such notables as [Ernest Mach](https://en.wikipedia.org/wiki/Ernst_Mach) and [Wilhelm Ostwald](https://en.wikipedia.org/wiki/Wilhelm_Ostwald) (Nobel Prize in Chemistry 1909).

# ## Fick's laws and the diffusion equation 
# 
# Normal diffusion is often called Fickian diffusion whereas anomalous diffusion referes to non-Fickian diffusion. __Fick's first__ law assumes a steady state and it is given in terms of a flux ($\vec{j}(\vec{x},t)$), concentration ($n(\vec{x},t)$) and the diffusion coefficient ($D$) as
# 
# $$ \vec{j}(\vec{x},t) = -D \nabla n(\vec{x},t).$$
# 
# When combined with the continuity equation
# 
# $$ \frac{ \partial n(\vec{x},t)}{ \partial t } = - \nabla \vec{j}(\vec{x},t), $$
# 
# one obtains __Fick's second law also known as the diffusion equation__:
# 
# $$
# \frac{ \partial n(\vec{x},t)}{ \partial t } = D \nabla^2  n(\vec{x},t) 
# $$
# 
# Using $\Delta \equiv \nabla^2$, the above can be given as
# 
# \begin{equation}
# \frac{ \partial n(\vec{x},t)}{ \partial t } = D \Delta  n(\vec{x},t).
# \label{eq:diffusion}\tag{1}
# \end{equation}
# 
# The diffusion equation given in Eq. (\ref{eq:diffusion}) is a _parabolic PDE_ describing a time-dependent process. It is an initial-value problem. 
# 
# 
# ### Analogous laws
# <!--    
# #### Ohm's law - electrical conductivity
# -->
# <!-- 
# #### Darcy's law - fluid flow in porous medium
# -->
# 
# #### Fourier's law - heat conduction (Fourier 1822)
# 
# $$
# \frac{\partial T (\vec{x},t)}{\partial t} = \alpha \nabla^2 T (\vec{x},t)
# $$
# 
# $\alpha$ is thermal conductivity.
# 
# 

# ## Solution of the diffusion equation
# 
# 
# We consider the diffusion problem in one dimension in a domain of length $L$ to solve for concentration $n(x,t)$. Both initial (concentration at $t=0$) and boundary (concentration at $x=0$ and $x=L$) conditions are required. There are several options for boundary conditions.

# ### Options for boundary conditions
# 
# There are several possibilities for boundary conditions depending on the physical situation.
# 
# 1. **Dirichlet boundary conditions**: We set  $n(0,t)$ and $n(L,t)$ to constant values.
# 
# * If  $n(0,t) = n(L,t) = C$, then we have *homogeneous Dirichlet boundary conditions*.
# 
# * If $n(0,t) = C_1$,  $n(L,t) = C_2$, and $C_1 \ne C_2$ we have *inhomogeneous Dirichlet boundary conditions*.
# 
# 1. **Von Neumann boundary conditions**: We set  $\partial_x n(0,t)$ and $\\partial_x n(L,t)$ to constant values. If $\partial_x n(0,t) = \partial_x n(L,t) = 0$, then there is no flux across the boundary. This means that the ends are insulated: For diffusion it means that particles cannot diffuse past the boundary and in the case of heat conduction this means that no heat can flow through the boundary.

# ### Diffusion equation with homogeneous Dirichlet conditions in 1-d
# 
# We start by considering a one-dimensional system of length $L$ using homnogeneous Dirichlet boundary conditions. The goal is the solve the diffusion equation for the concentration $n(x,t)$. The solution requires both spatial boundary conditions and temporal initial conditions. The problem is determined as
# 
# \begin{equation}
# \frac{ \partial n(x,t)}{ \partial t } = D \Delta  n(x,t) \mathrm{\,\,\,with\,\,\,}
# t>0 \mathrm{\,\,\,and\,\,\,}  0 \le x \le L
# \label{eq:1ddiff}\tag{1ddiff}
# \end{equation}
# 
# with the initial concentration ($t=0$) given as
# 
# $$
# n(x,0) = f(x) \mathrm{\,\,\,where\,\,\,}  0 \le x \le L
# $$
# 
# where $f(x)$ is some given function and
# 
# $$
# n(0,t) = n(L,t) = 0 \mathrm{\,\,\,for\,\,\,} t> 0. 
# $$
# 
# Thus, we are using homogeneous Dirichlet boundary conditions. In the following, we are looking for a non-trivial ($f(x) \ne 0$) solution.
# 
# #### Solution using separation of variables
# 
# When using separation of variables, one makes the _ansatz_ that the solution can be written as product of single variable functions. Note that this is just an ansatz, there is no guarantee that it is correct and one must check its validity when possibile. In this case we have two variables and the ansatz is 
# 
# $$
# n(x,t) = X(x)T(t)
# $$
# 
# Let $X \equiv X(x)$ and $T \equiv T(t)$. Then, direct substitution in Eq. (\ref{eq:1ddiff}) gives
# 
# $$
# XT'  = D X''T
# $$
# or
# $$
# \frac{X''}{X} = \frac{1}{D}\frac{T'}{T}
# $$
# 
# At least superficially, separation of variables seems to be a reasonable assumption. To proceed, we introduce the separation constant $\lambda$. This reduces the original PDE two homogeneous ODEs:
# 
# $$
# X'' + \lambda X = 0 \mathrm{\,\,\,\,and\,\,\,\,} T' + \lambda DT =0.
# $$
# 
# $$
# X'' + \lambda X = 0 \mathrm{\,\,\,\,with\,\,\,\,} X(0) = X(L) = 0.
# $$
# 
# We must first solve for the boundary conditions, that is, use the spatial part. Then, with the solution to the boundary value problem, proceed to the initial value problem and combine the two for the full solution.
# 
# __The Boundary Value Problem: The spatial part__:
# 
# Notice that equations above define an _eigenvalue problem_: Solutions (nontrivial ones; the trivial one is obviously $X(x) = 0$) exist only for discrete values, that is, eigenvalues  $\lambda$. The non-trivial solutions are the corresponding eigenfunctions. 
# 
# The general solution depends on the sign of the eigenvalue $\lambda$. Thus, we must consider three cases: $\lambda > 0$, $\lambda < 0$ and $\lambda = 0.$
# 
# <u>1. __Case__ </u> $\lambda > 0$: Define $\lambda = \mu^2$. Then, we search for a solution to
# 
# \begin{equation}
# X'' + \mu^2 X = 0.
# \label{eq:lge0}\tag{a}
# \end{equation}
# 
# The general solution is 
# 
# $$
# X(x) = A \cos (\mu x) + B \sin (\mu x)
# $$
# 
# To find $A$ and $B$, we apply the boundary conditions:
#  - $x=0$: 
#    $$
#    X(0) = A \cos (0) + B \sin (0) = 0 \Rightarrow A=0.
#    $$
#  - $x=L$:    
#    $$
#    X(L) = A \cos (\mu L) + B \sin (\mu L) = B \sin (\mu L) = 0.
#    $$
#  or 
#    $$
#    B \sin (\mu L) = 0.
#    $$
#    Since we cannot have $B=0$,
#  
#    $$
#    \sin (\mu L) = 0.
#    $$
#    
#    This is satisfied when $\mu L = n \pi$, where $n$ is an integer, that is,
# 
#   $$
#   \mu = n \frac{\pi}{L} \mathrm{\,\,where\,\,} n= 1, 2, 3,...
#   $$
# 
# With the above, the set of eigenvalues for $\lambda > 0$ is given as
# 
# \begin{equation}
# \lambda_n = \left(\frac{n  \pi }{L} \right)^2 \mathrm{\,\,} n=1, 2, 3, ...
# \label{eq:lgn}\tag{aa}
# \end{equation}
# 
# and the corresponding eigenfunctions are
# 
# \begin{equation}
# X_n = \sin \left( \frac{n \pi x}{L}\right)
# \label{eq:lgsol}\tag{aaa}
# \end{equation}
#   
#   
# <u>2. __Case__ </u>  $\lambda < 0$: We use the same strategy as above an define $\lambda = - \mu^2$ and look for a general solution to 
# 
# $$
# X'' - \mu^2 X = 0.
# $$
# 
# The general solution is 
# 
# $$
# X(x) = A \cosh (\mu x) + B \sinh (\mu x)
# $$
# 
# <!--
# Could also use $e^{\mu x}$ and $e^{- \mu x}$
# instead of $\cosh$ and $\sinh$
# -->
# 
# To find $A$ and $B$, we apply the boundary conditions:
#  - $x=0$: 
#     $$
#    X(0) = A \cosh (0) + B \underbrace{\sinh (0)}_{=0} = 0 \Rightarrow A=0.
#    $$
#    
#  - $x=L$:    
#    $$
#    X(L) = \underbrace{A}_{But A=0} \cosh (\mu L) + B \sinh (\mu L) = B \sinh (\mu L) = 0.
#    $$
#    
#  The only solution ($\mu \ne 0$) is $B=0$.   
# 
# 
# 
# The above means that there is no non-trivial solution in the case  $\lambda < 0$.
# 
# <u>3. __Case__ </u> $\lambda =0$:
# The original equation is now simplified to the form
# 
# $$
# X'' = 0.
# $$
# 
# The general solution is
# 
# $$
# X(x) = A + Bx.
# $$
# 
# As above, we apply the boundary conditions:
#  - For both $x=0$ and $L=0$: 
# 
#   $$
#    X(0) = X(L) = 0.
#    $$
# 
#  This yields $A = B = 0$.
# 
# The above means that there is no non-trivial solution in the case  $\lambda = 0$.
# 
# We have now applied the boundary conditions. Next, we must use the initial value for $T(t)$.
# 
# __Time dependence__:
# 
# As seen above, the only non-trivial solution is the case of $\lambda > 0$, that is, we must use the eigenvalues given as Eq.~\ref{eq:lgn}. Doing that gives
# 
# $$
# T' + \left(\frac{n  \pi }{L} \right)^2 D T = 0.
# $$
# 
# The solution is
# 
# \begin{equation}
# T_n \propto e^{-n^2 \pi^2  D  t / L^2}.
# \label{eq:lgt}\tag{t}
# \end{equation}
# 
# __Full solution: Apply the initial condition__:
# 
# Now we are in position to present the full solution. We combine the only non-trivial spatial solution provided by Eq. \ref{eq:lgsol} and the only non-trivial temporal solution as given by Eq. \ref{eq:lgt}. This gives
# 
# \begin{align}
# n_i(x,t) 
# & = X(x)T(t) \\
# & = \sin \left( \frac{n \pi x}{L}\right) e^{-n^2 \pi^2  D  t / L^2} 
# \mathrm{\,\,\,\,for\,\,\,\,} i= 0,1,2,... 
# \label{eq:nsum}\tag{nsum}
# \end{align}
# 
# Notice that this is the solution for any positive integer $n$. In the context of heat condution, the above equation is sometimes called the _fundamental solution of the heat conduction problem_.
# 
# To give the full solution, we must apply the superposition principle. This means that we need to account for all values of $n$ as well as the initial condition. To include the former, we have:
# 
# \begin{align}
# n(x,t) 
# & = \sum_{n=1}^{\infty} b_n n_n(x,t) \\ 
# & = \sum_{n=1}^{\infty} b_n \sin \left( \frac{n \pi x}{L}\right) e^{-n^2 \pi^2  D  t / L^2}.
# \label{eq:nsol}\tag{nsol}
# \end{align}
# 
# 
# But at $t=0$ we have $n(x,0) = f(x)$. Thus,
# 
# \begin{align}
# f(x)  
# & = n(x,0) \\ 
# & = \sum_{n=1}^{\infty} b_n n_n(x,0) \\ 
# & = \sum_{n=1}^{\infty} b_n \sin \left( \frac{n \pi x}{L}\right) e^{0} \\
# & =  \sum_{n=1}^{\infty} b_n \sin \left( \frac{n \pi x}{L}\right).
# \label{eq:f0}\tag{f0}
# \end{align}
# 
# 
# But this is a Fourier sine series for an odd function of period of $2L$. Using the properties of the Fourier sine series, the coefficients $b_n$ are given as
# 
# \begin{equation}
# b_n = \frac{2}{L} \int_0^L \, f(x) \,\sin \frac{n \pi x}{L} \,dx.
# \label{eq:bn}\tag{bn}
# \end{equation}
# 
# 
# Now we have the full solution: It is given by Eq. (\ref{eq:nsol}) with the coefficient defined by Eq. (\ref{eq:bn}) 

# Physics
# ### Diffusion equation with inhomogeneous Dirichlet conditions 
# 
# Assume that one end the (one dimensional) system is maintained at a constant concentration of $C_1$ and the other end at a constant concentration of  $C_2$. The boundary conditions are then given by
# 
# $$
# n(0,t) = C_1 \mathrm{\,\,and\,\,} n(0,L) = C_2 \mathrm{\,\,\,\,for\,\,\,\,} t>0.
# $$
# 
# Only the boundary conditions have changed, the initial condition remains the same as above, that is, at $t=0$ the concentration is given as
# 
# $$
# n(x,0) = f(x) \mathrm{\,\,\,\,for\,\,\,\,}  0 \le x \le L
# $$
# 
# where $f(x)$ is some given function or the problem needs to be converted to an appropriate form.
# 
# #### Solution using separation of variables
# 
# That is, using ansatz
# 
# $$
# n(x,t) = X(x)T(t)
# $$
# 
# from above.
# 
# __Boundary value problem: Spatial part__
# 
# Let's apply the boundary conditions as above:
# 
# $$
# n(0,t) = X(0)T(t) = C_1
# $$
# 
# This implies that 
# 
# $$
# X(0) = \frac{C_1}{T(t)}
# $$
# 
# and contradicts the ansatz of separation of variables. Other types of solution must be  sought.
# 
# #### Straightforward separation doesn't work, need a different solution
# 
# __Use physical conditions__:
# Straighforward separation of variables does not work on this case, but it is possible to transform the problem into a problem with homogeneous boundary conditions. The strategy is this: We make an assumption (based on physics), that after a long time there will a stationary distribution that is independent of time. This is reasonable since after a very long time (technically speaking $t \rightarrow \infty$) the distribution must reach a steady-state. We denote this steady-state concentration by $g(x)$. This means that seprate the time-dependent part from the $t \rightarrow \infty$ stationary distribution by splitting the concentration into two parts, that is,
# 
# $$
# n(x,t) = g(x) + h(x,t).
# $$
# 
# We consider the stationary part ($g(x)$ first. It must satisfy the diffusion equation, 
# 
# $$
# \frac{ \partial g(x)}{ \partial t } = D \nabla^2  g(x)  \mathrm{\,\,\,\,for\,\,\,\,} 0 < x < L
# $$
# 
# but since $g(x)$ does not depend on time, we have 
# 
# $$
# \nabla^2 g(x) = 0 \mathrm{\,\,\,\,for\,\,\,\,} 0 < x < L.
# $$
# 
# The general solution is 
# 
# $$
# g(x) = A + Bx,
# $$
# where $A$ and $B$ are constants.
# 
# __Solve the stationary part using the boundary conditions__:
# We can solve $A$ and $B$ by using the boundary conditions. Direct substitution gives
# 
# $$
# g(0) = A = C_1
# $$
# and
# \begin{align}
# g(L) 
# & =  A +BL \\ 
# & = C_1 + BL = C_2
# \end{align}
# from which
# $$
# B= \frac{(C_2 - C_1)}{L}.
# $$
# 
# With these, stationary distribution $g(x)$ is given by the linear function
# 
# $$
# g(x) = C_1 + \frac{(C_2 - C_1)}{L}x.
# $$
# 
# 
# __The time-dependent (transient) part + boundary conditions:__ This is where things get a bit tricky. Above, we split $n(x)$ into two parts,
# 
# $$
# n(x,t) = g(x) + h(x,t).
# $$
# 
# The full solution is given as a combination of the asymptotic long-time solution and a solution to the transient part ($h(x,t)$). Since we have already solved for $g(x)$, we must now focus on $h(x,t)$ since
# direct substitution into the diffusion equation leaves the transient parts only,
# 
# 
# Taking the time derivaties leaves the transient parts only,
# 
# \begin{align}
# \frac{\partial }{\partial t} 
# \left[\underbrace{g(x)}_{\mathrm{\partial_t g=0}} + h(x,t) \right] 
# & = D \nabla^2 \left[ g(x) + h(x,t) \right]\\
# \frac{\partial }{\partial t}  h(x,t)  
# % &= D \nabla^2 \left( g(x) + h(x,t) \right) \\
# &= D \left(\underbrace{\nabla^2 g(x)}_{\mathrm{=0}} + \nabla^2 h(x,t) \right)\\
# \frac{\partial }{\partial t}  h(x,t)
# & = D \nabla^2 h(x,t).
# \end{align}
# 
# 
# The transient must satisfy the boundary conditions
# At $x=0$:
# 
# \begin{align}
# n(0,t) & = g(0) + h(0,t) \\
# h(0,t) & = n(0,t) - g(0) \\
# h(0,t) & = C_1 - C_1 = 0
# \end{align}
# 
# At $x=L$:
# \begin{align}
# n(L,t) & = g(L) + h(L,t) \\
# h(L,t) & = n(L,t) - g(L) \\
# h(L,t) & = C_2 - C_2 = 0
# \end{align}
# 
# We have now transformed the problem to one with _homogeneous_ boundary conditions! 
# 
# __Important:__ This strategy is not limited to this particular problem but can be applied to other problems with inhomogenous boundary conditions and where splitting the original function to stationary and transient parts can be done (usually based on physical arguments).
# 
# __Use the initial values__:
# What is left now is to use the initial condition and combine the stationary and the transient solutions.
# 
# Let's use direct substitution:
# 
# \begin{align}
# n(x,0) & = g(x) + h(x,0) \\
# h(x,0) & = n(x,0) - g(x) \\
# h(x,0) & = f(x) - C_1 - \frac{(C_2 - C_1)}{L}x.
# \end{align}
# 
# This defines now the initial condition for the transient function $h(x,t)$ in terms of the full initial condition ($f(x)$) and the time-independent part ($g(x)$). We are now ready to give the full solution to the diffusion problem with _inhomogeneous_ Dirichlet conditions: We can use directly the results obtained for the case of _homogeneous_ Dirichlet boundary conditions above. For completeness we repeat the formulas here. 
# 
# The full solution solution given in Eq.(\ref{eq:nsol}) as
# $$
# n(x,t) = \sum_{n=1}^{\infty} b_n \sin \left( \frac{n \pi x}{L}\right) e^{-n^2 \pi^2  D  t / L^2}
# $$
# is replaced by
# \begin{align}
# n(x,t) & = g(x) + h(x,t) \\
# & = C_1 + \frac{(C_2 - C_1)}{L}x + h(x,t) \\
# & = \underline{\underline{C_1 + \frac{(C_2 - C_1)}{L}x + \sum_{n=1}^{\infty} b_n \sin \left( \frac{n \pi x}{L}\right) e^{-n^2 \pi^2  D  t / L^2}}}.
# \end{align}
# 
# The Fourier coefficients $b_n$ given in Eq.~(\ref{eq:bn}) as
# 
# $$
# b_n = \frac{2}{L} \int_0^L \, f(x) \,\sin \frac{n \pi x}{L} \,dx,
# $$
# become
# 
# \begin{align}
# b_n & = 
# \frac{2}{L} \int_0^L \, h(x,0) \,\sin \frac{n \pi x}{L} \,dx \\
# & = 
# \frac{2}{L} \int_0^L \, (n(x,0) - g(x)) \,\sin \frac{n \pi x}{L} \,dx \\
# & =
# \frac{2}{L} \int_0^L \, \left[
# f(x) - C_1 - \frac{(C_2 - C_1)}{L}x
# \right] \,\sin \frac{n \pi x}{L} \,dx
# \end{align}
# 
# End the initial condition $f(x)$ given in Eq.(\ref{eq:f0}) as
# 
# \begin{align}
# f(x)  
# & = n(x,0) \\ 
# & = \sum_{n=1}^{\infty} b_n n_n(x,0) \\ 
# % & = \sum_{n=1}^{\infty} b_n \sin \left( \frac{n \pi x}{L}\right) e^{0} \\
# & =  \sum_{n=1}^{\infty} b_n \sin \left( \frac{n \pi x}{L}\right).
# %\label{eq:f0}\tag{f0}
# \end{align}
# 
# becomes replaced by
# 
# \begin{align}
# h(x,0)  
# %& = h(x,0) \\ 
# & = \sum_{n=1}^{\infty} b_n h_n(x,0) \\ 
# & = \sum_{n=1}^{\infty} b_n (n_n(x,0)- g(x)) \\ 
# %
# % & = \sum_{n=1}^{\infty} b_n \sin \left( \frac{n \pi x}{L}\right) e^{0} \\
# & =  \sum_{n=1}^{\infty} b_n \sin \left( \frac{n \pi x}{L}\right).
# %\label{eq:f0}\tag{f0}
# \end{align}
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# 
# ### Diffusion equation with homogeneous von Neumann conditions 
# 
# The Dirichlet boundary conditions state that the ends are kept at a constant value. The homogeneous von Neumann conditions, on the other hand, state that there is no flux through the ends. In other words, the ends are capped. This can be stated as
# 
# \begin{align}
# \left. \frac{\partial n(x,t)}{\partial x}\right|_{x=0} & = 0 
# \mathrm{\,\,\,and \,\,\,} \\
# \left. \frac{\partial n(x,t)}{\partial x}\right|_{x=L} & = 0 
# \mathrm{\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,for \,\,\,}
# t>0.
# \end{align}
# 
# __Physical justification for the boundary conditions:__ Fick's law as derived above in a linear response theory for concentration.  becoming equlibrated by molecular motions. The same idea applies in the context of heat transfer and it is known as Newtonian cooling. One should also note that linear response itself is an approximation (although a good one in many cases).
# 
# #### Separation of variables
# 
# Let's again make the same  ansatz that the solution can be written as product of single variable functions,
# 
# $$
# n(x,t) = X(x)T(t).
# $$
# 
# As before, we let $X \equiv X(x)$ and $T \equiv T(t)$ and direct substitution in the diffusion  equation ($\partial_t n(x,t) = D \Delta n(x,t)$) gives
# 
# $$
# \frac{X''}{X} = \frac{1}{D}\frac{T'}{T}
# $$
# 
# We proceed as above: We introduce the separation constant $\lambda$, the boundary value problem is considered first (spatial part) and we then complete the problem by using the initial value (temporal part). 
# 
# <!--
# NOTE: It is possible to show that for non-trivial solutions to exist, $\lambda \ne R$.
# -->
# 
# __Boundary value problem: spatial part__
# 
# The boundary conditions are now on the derivative part,
# 
# $$
# X'' + \lambda X = 0 \mathrm{\,\,\,\,\,\,with\,\,\,\,\,\,} X'(0) = X'(L) = 0.
# $$
# 
# This is again an eigenvalue problem and we must consider three cases as was done in the csae of Dirichlet boundary conditions: 1) $\lambda >0$, 2) $\lambda<0$ and 3) $\lambda=0$. 
# 
# <u>1. __Case__ </u> $\lambda > 0$: Define $\mu^2 = \lambda$. Then, the general solution is again
# 
# The general solution is 
# 
# $$
# X(x) = A \cos (\mu x) + B \sin (\mu x).
# $$
# 
# Since the boundary conditions are on the derivative, we must differentiate the above,
# 
# $$
# X'(x) = - \mu A \sin (\mu x) + \mu B \cos (\mu x)
# $$
# 
# First, apply the condition $X'(0) = 0$. This gives
# 
# \begin{align}
# X'(0) 
# & = - \mu A \sin (\mu 0) + \mu B \cos (\mu 0 ) \\
# & = B \mu = 0 \\
# & \Rightarrow B=0.
# \end{align}
# 
# The other boundary condition $X'(L) = 0$ gives
# 
# \begin{align}
# X'(L) 
# & = - \mu A \sin (\mu L) + \mu B \cos (\mu L ) \\
# & = - \mu A \sin (\mu L) = 0.
# \end{align}
# 
# Ruling out the trivial solution ($A=0$) leaves the condition
# 
# \begin{align}
# \sin (\mu L) & = 0 \\
# \Rightarrow \mu & = \frac{n \pi }{L} \mathrm {\,\,\,where\,\,\,} n \in Z_+
# \end{align}
# 
# Since $\lambda  = \mu^2  >0$, we have the eigenvalues
# 
# $$
# \lambda_n = \left( \frac{n \pi }{L} \right)^2 \mathrm {\,\,\,\,\,\,with \,\,\,\,\,\,} n = 1, 2, 3,...
# $$
# 
# Since $B=0$, we have the corresponding eigenfunctions determined as
# 
# $$
# X_n = \cos \left( \frac{n \pi x}{L}\right) \mathrm {\,\,\,\,\,\,with \,\,\,\,\,\,} n = 1, 2, 3,...
# $$
# 
# <u>2. __Case__ </u> $\lambda < 0$: Define $\mu^2 = - \lambda$. 
# The general solution is, as above with homogeneous Dirichlet boundary conditions, we have
# 
# $$
# X'' - \mu^2 X = 0
# $$
# 
# with the general solution
# 
# $$
# X(x) = A \cosh (\mu x) + B \sinh (\mu x).
# $$
# 
# We must again take the derivative to apply the boundary conditions,
# 
# $$
# X'(x) = \mu A \sinh (\mu x) + \mu B \cosh (\mu x).
# $$
# 
# Using the boundary condition $X'(0) = 0$ gives
# 
# \begin{align}
# X'(0) 
# & = \mu A \underbrace{\sinh (\mu x)}_{=0} + \mu B \cosh (\mu x)\\
# & = \mu B \underbrace{ \cosh (\mu x) }_{\ne 0} = 0 \\
# & \Rightarrow B= 0.
# \end{align}
# 
# 
# The boundary condition $X'(L) = 0$ yields
# 
# $$
# X'(L) = \mu A \sinh (\mu x)  =  0.
# $$
# 
# Since $\mu \ne 0$, the only solution is $A=0$. This means that there is no non-trivial solution for $\lambda < 0$.
# 
# 
# <u>2. __Case__ </u> $\lambda = 0$:
# 
# The original equation is now simplified to the form
# 
# $$
# X'' = 0
# $$
# 
# and the general solution is
# 
# $$
# X(x) = A + Bx.
# $$
# 
# Taking the derivative gives
# 
# $$
# X'(x) = B.
# $$
# 
# Using the boundary condition $X'(0) = 0$ gives $X'(0) = B = 0$. The boundary condition $X'(L) = 0$ gives the same answer, $X'(L) = B = 0$. That is, the boundary conditions are trivially satisfied. Neither of the boundary conditions determines $A$. The above means that $\lambda = 0$ is an eigenvalue. The corresponding eigenvalue is $X_0(x)=1$
# 
# But $A$ is still undetermined. Using 
# 
# \begin{align}
# & T' + D \lambda T = 0 \\
# & T' = 0 
# \end{align}
# 
# states that $T(t)$ must be a constant. If we use $\lambda = 0$, we have
# 
# $$
# n(x,t) = \underbrace{X(x)}_{1}\underbrace{T(t)}_{constant} = \underbrace{\mathrm{constant}}_{A}
# $$
# 
# 
# 
# __Initial value problem: Temporal part__
# 
# The non-trivial solution was the case of $\lambda > 0$. That gives (as above)
# 
# $$
# T' + \left(\frac{n  \pi }{L} \right)^2 D T = 0.
# $$
# 
# The solution is
# 
# $$
# T_n = e^{-n^2 \pi^2  D  t / L^2} \mathrm{\,\,\,for \,\,\,} n=1,2,3,...
# $$
# 
# __Full solution__
# 
# The full solution is given as the product of the two parts,
# 
# $$
# n_n(x,t) = X_n(x) T_n(t).
# $$
# 
# As above, using the superposition principle gives the general solution,
# 
# \begin{align}
# n(x,t) 
# & = \sum_{n=0}^{\infty} c_n n_n(x,t) \\
# & = \underbrace{\frac{a_0}{2}}_{c_0} + \sum_{n=1}^{\infty} \underbrace{a_n}_{\equiv c_n} 
# \cos \left(\frac{n \pi x}{L} \right) e^{-n^2 \pi^2 D t / L^2}.
# \end{align}
# 
# Finally, the solution has to satisfy the initial condition
# 
# $$
# n(x,0) = f(x) \mathrm{\,\,\,where\,\,\,}  0 \le x \le L.
# $$
# 
# This yields
# 
# $$
# f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos \left( \frac{n \pi x }{L} \right)
# $$
# 
# This is Fourier cosine seriesfor an even function with period $2L$. The Fourier coefficient are given by
# 
# $$
# a_n = \frac{2}{L} \int_0^L\, f(x) \cos \left( \frac{n \pi x }{L} \right) \,dx.
# $$

# 
# 
# 
# ## Diffusion of colloids, Debye rotation

# ## Mathematical methods for studying diffusion
# 
# Fokker-Planck equation
# 
# Generalized Langevin equation
# 
# Diffusion with time dependent diffusion coefficient
# 
# Percolation models

# ## Fokker-Planck equation
# 
# The Fokker-Planck equation describes the evolution of the probability distribution $P(s,t)$, where $s$ is the state of the system and $t$ is time.
# 
# 
# $k_\mathrm{B}$ is the Boltzmann constant.
# 
# The stationary solution of the Fokker-Planck equation, that is,
# 
# $$
# \frac{\partial P(s,t)}{\partial t} = 0
# $$
# describes equlibrium. 
# 
# <!-- DPD stuff --> 

# 

# 

# ## Mean squared displacement

# ### Van Hove correlation function

# In[ ]:





# **Exercise:** Measure MSD using the van Hove correlation function
# 
# **Exercise:** Fit the van Hove correlation function to a Gaussian. Compute the moments of the van Hove distribution. Is it Gaussian?
# 

# **Movies**
# 
# - diffusion in cold and hot water
# - salad dressing

# ## Random Walks
# 
# *Random walk* in other languages:
# 
# |  |  |  |
# | --- | --- | --- |
# | ENG: Random walk | GER: Zufallsbewegung | FRA: Marche aléatoire |
# | ESP: Paseo aleatorio  | FIN: Satunnaiskävely | SWE:   |
# | RUS: Случайное блуждание  | | |
# 
# As the name suggests, the term *random walk* refers to a process that is random or stohastic by its nature. The term *random walk* is due to Karl Pearson who in his 1905 16-line communication to the journal Nature requested for information from the readers to the following problem:
# 
# > A man starts from a point $O$ and walks $l$ yeards in a straight line; he then turns through any angle whatever and walks another $l$ yards in a second straight line. He repeats this process $n$ times. I require the probability that after these $n$ stretches he is at a distance between $r$ and $r_\delta r$ from his starting point, $O$.
# 
# Lord Rayleigh responded in the next issue by saying that he has already solved the problem in a different context and that the solution in the case of large $n$ is 
# 
# $$
# \frac{2}{n}e^{-r^2/n}r\,dr.
# $$
# 
# Given the way how Pearson posed the problem, this is often called *drunkards walk*.
# 
# <table>
# <tr>
#     <td>
#         <img src="./img/drunkards-walk-1.png" width="50%"/>
#     </td>
# <td>
#     <img src="./img/drunkards-walk-2.png" width="50%"/>
#     </td>
#     </tr>
#     <tr>
#         <td colspan="2">
#         Figures from [2](https://chinookjargon.com/2019/08/26/the-drunkards-walk-from-chinuk-wawa-to-upper-chehalis/) abd [1](https://medium.com/@mooneyse/a-drunkards-walk-20bbb6045522)
#         </td>
#     </tr>
# </table>
# 
# While there are several possible definitions for random walk, the most common way is to define *simple random walk* or *discrete random walk* as follows:
# 
#  1. Steps take place at *discrete time intervals*.
#      - In other words: Random walk is a *discrete-time process* (rather than a continous-time process). It takes place at integer times $i$. If we denote the random walk by $S$, then the walk can be given as
#      $$
#      S_t = X_0 + X_1 + ... + X_t
#      $$
#      Here, the *random variables* $X_i$ are independent. 
#  2. In the case of a *simple random walk*, the steps are always of the same *discrete* length. Here, we a
#  re assuming a 1-dimensional random walk.
#  3. Probability is taken from a uniform distribution with the probability $p$ moving to the right and $q=1-p$ to the left.
#      - Only two possible outcomes are possible (with probabilities $p$ and $q$, respectively)
#      - There is no memory: At each time, the new probability is independent of the previous ones.
#      - If $p = q = \frac{1}{2}$, the *simple random walk* is called *symmetric* or *isotropic* depending on the context.
# 4. The previous point can be easily generalized to higher dimensions. Fr example, in a 2-dimensional square lattice, the walker can take steps to left, right, up and down. In the case of a *symmetric random walk* the probabilities for each of the directions equal to $1/4$     
# 5. The steps are independent of each other. That is to say that there is no memory in the system. This also implies that the random walk is a *Markov process*.
# 
# **Mathematical defintion:**
# 
# Sequence $\{S_n\}$ with $S_0 = 0$
# \begin{align}
# S_n = \sum_{i=1}^N X_i
# \end{align}
# 
# \begin{equation}
#     X_i =
#     \begin{cases}
#       +1, & \mathrm{if}\ p \\
#       -1, & \mathrm{otherwise\,\,} q=1-p
# \end{cases}
# \end{equation}
# 
# 
# <table>
# <tr>
#     <td>
#         <img src="./img/simple-random-walk-1d.svg" width="80%"/>
#     </td>
#     <tr>
#         <td colspan="1">
#         Figure: 1-dimensional random walk starting from position $x=0$ at time $t=0$. The walker takes steps of length $\pm 1$ at equally spaced discrete time intervals. The probability for step $+1$ is $p$ and $q=1-p$ for step $-1$. For a <i>symmetric</i> random walk $p=q=\frac{1}{2}$. A few possible steps are shown as an example. 
#         </td>
#     </tr>
# </table>
# 
# 
# 
# 

# 
# **Side note, Bernoulli process:** The random walk is closeley related to what is called  a [*Bernoulli process*](): (infinite) sequence of independent binary ($0$ or $1$; zero means failure and 1 means success) outcomes where the probability of success in a single trial is $p$ and the probability of failure is $q=1-p$. Coin flip is the perfect example of this. The random variable $X$ is then the number of success. The Bernoulli process is often denoted as $X \sim Be(p)$
# 
# - Probabilities: $p+q =1$
# - The total number of outcomes ($N$) is the sum of the two possible outocomes ($n_1$ and $n_2$): $N = n_1 + n+2$
# 

# ### Terminology: Random walk vs Brownian motion vs Wiener process
# 
# The terms Brownian motion and Wiener process are used more or less synonymously. 
# 
# The important differences between the Random walk and Brownian motion
#  - Random walk is a *discrete-time process* but Brownian motion is a *continous-time process*.
#  
# How about the Wiener process? In a strict sense, *Brownian motion* refers to the physical situation of a particle executing random motion due to thermal fluctuations whereas the term *Wiener process* is the mathematical formulation for such systems.

# #### Martingale
# - [Wikpedia: Martingale](https://en.wikipedia.org/wiki/Martingale_(probability_theory))

# ### Random variables

# ### Polya

# ### Law of large numbers

# ### Central limit theorem

# In[5]:


#=================================================================================
# Bernoulli process
#
# - the scipy module gives the statistical properties
#=================================================================================

from scipy.stats import bernoulli
import matplotlib.pyplot as plt

# We need to give the probability of success (p)

p = 0.5

mean, var, skew, kurt = bernoulli.stats(p,moments='mvsk')

print('Mean:', mean)


# 
# #### Motivation: why should we be interested in random walks?
# 
# - How atoms/molecules move in a liquid or a gas? 
# - How neutrons move in radiactive decay?
# - Stock market predictions.
# 
# #### Examples:
# 
# - Polymers: One of the simplest model for polymers is the so-called *freely jointed chain* - a random walk in three dimensions. Despite its simplicity, it displays lot of properties and also provides a starting point for more realistic polymer models.

# 

# ### The simplest case: Random walk in one dimension

# In[6]:


SVG(filename='./img/random-walk-1d.svg')


# ### Fundamental properties of symmetric random walks in 1-d
# #### Displacement and variance after $N$ steps
# 
# Some of the fundamental properties that we are interested in are the average displacement and variance of a random walker. 
# 
# *Displacement*: Tells how far from the origin the particle has drifted. Average displacement, or expectation value of the displacement, is an important characteristic. 
# 
# *Variance:* Variance is the expectation value of the squared distance,  or squared displacment, from its mean (average displacement). It is the square of standard deviation (typically denoted by $\sigma$).
# 
# *Why?* In the essence, variance measures how for a quantity has spread from its mean value. Since we need a measure for the spread, or distance, that cannot not depend on the direction. This means that we have to have a squared quantity. We also need a reference point and mean is the most natural one and it doesn't depend on the system or the coordinate system. 
# 
# **Reminder:** Variance, or standard deviation squared, of a quantity $x$ is given as
# 
# \begin{align}
# \sigma^2 & = \langle \Delta x^2 \rangle  \\
#          & = \langle (x -  \langle x \rangle )^2 \rangle\\
#          & = \langle x^2 - 2 x \langle x \rangle + \langle x \rangle^2  \rangle \\
#          & = \langle x^2 \rangle - 2  \langle x \rangle^2 + \langle x \rangle^2  \rangle \\
#          & = \langle x^2 \rangle - \langle x \rangle^2,
# \end{align}
# 
# where the angular brackets denote averaging
# 
# Below, we will be compute variance and related to diffusion. 
# 
# **Static collection vs time dependence**
# 
# While taking the mean is simple, variance sometimes causes some misunderstandings. Let's look at the last line of above formula again:
# 
# \begin{align}
# \sigma^2 & = \langle x^2 \rangle - \langle x \rangle^2.
# \end{align}
# 
# If the random variable $x$ depends on time, then $x \equiv x(t)$ and $\langle x \rangle \equiv \langle x(t) \rangle $ is the time average. If we have a static collection of points rather than a time dependent quantity, then $x \equiv x_i$ and 
# $\langle x \rangle \equiv \langle x_i \rangle $, the latter simply means averaging over the whole collection. Figure illustrates the two scenarios (for clarity, the static points are given in 2d). 
# As we will see in connection to diffusion, we may also be interested in taking the avarage over a collection random walkers, that is, we take a average and an ensemble average.
# 
# <table>
# <tr>
#     <td>
#         <img src="./img/random-points-demo.svg" width="49%"/>
# <!--</td>
#        <td>
# -->
#         <img src="./img/random-walks-demo.svg" width="49%"/>
#     </td>
#     </tr>    
#     <tr>
#         <td colspan="1">
#         Figure: Left: Static collection of points (integers; distributed using a uniform integer distribution such that each $x_i \in [-10,10]$ and $y_i \in [-10,10]$). Right: Five time-dependent trajectories of a single symmetric random walker (step length is equal to unity) in 1d starting from zero. Position along the $x$-axis is show with respect to time.
#         </td>
#     </tr>
# </table>
# 
# 
# **Let's have the following definitions:**
# - At any time $i$ the random walker can take steps ($s_i$) in two directions: $s_i = \pm \ell$
# - The step length is constant: $|s_i| = \ell \,\,\, \forall \,\, i$
# - Probabilities for moving to the positive or negative directions are given by $p$ and $q=1-p$, respectively. 
#   - The case in which $p = q = \frac{1}{2}$ is called *isotropic* or *symmetric*.
#   - In contrast, when $p \ne q $ then the random walk is called *biased*, *anisotropic* or *asymmetric*. Note that $p+q = 1$ by the above definition.

# In[7]:


#================================================================================================================
#
# Generate a plot of a 1D random walk + a collection of
# static points
#----------------------------------------------------------------------------------------------------------------
#
#
#================================================================================================================

import random 
import numpy as np 
import matplotlib.pyplot as plt 

import matplotlib.pyplot as plt                            # For plotting
import seaborn as sns
from matplotlib import rc


#---- This allows the use of LaTeX + the use sans-serif fonts also for tick labels:

rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')

# There are 5 presents for background: darkgrid, whitegrid, dark, white, and ticks
# Define how ticks are placed and define font families

sns.set_style("ticks")
sns.set_style("whitegrid", 
 {'axes.edgecolor': 'black',
 'axes.grid': True,
 'axes.axisbelow': True,
 'axes.labelcolor': '.15',
 'grid.color': '0.9',
 'grid.linestyle': '-',
 'xtick.direction': 'in', 
 'ytick.direction': 'in',
 'xtick.bottom': True,
 'xtick.top': True,
 'ytick.left': True,
 'ytick.right': True, 
 'font.family': ['sans-serif'],
 'font.sans-serif': [
  'Liberation Sans',
  'Bitstream Vera Sans',
  'sans-serif'],})

step       = [-1.0,1.0]
#p          = 0.5
#q          = 1.0-0.5
n_steps    = 100

# Create M random walks:

M = 5

for i in range(M):
    
    moves       = np.random.choice(step, n_steps, p=[0.50, 0.5]) 
    positions   = np.cumsum(moves)
    positions   = np.concatenate((positions[:0], [0.0], positions[0:]))

    plt.plot(positions)#,'.')#,'o') 

plt.xlabel('time step')
plt.ylabel('position along the x-axis')

#plt.savefig('random-walks-demo.svg')
plt.show() 

#print(type(positions),positions[0])
#print(positions, positions[-1],len(positions))
#plt.loglog(delay,msd,'x')
#print('avg', np.average(moves),'theor (=0): ', '<x^2(N)> = N*l**2:', np.sum(moves)**2,n_steps)

#\len(positions)


# In[8]:


#================================================================================================================
#
# Generate  a collection of static ranodm points
#----------------------------------------------------------------------------------------------------------------
#
#
#================================================================================================================

import random 
import numpy as np 
import matplotlib.pyplot as plt 

import matplotlib.pyplot as plt                            # For plotting
import seaborn as sns
from matplotlib import rc


#---- This allows the use of LaTeX + the use sans-serif fonts also for tick labels:

rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')

# There are 5 presents for background: darkgrid, whitegrid, dark, white, and ticks
# Define how ticks are placed and define font families

sns.set_style("ticks")
sns.set_style("whitegrid", 
 {'axes.edgecolor': 'black',
 'axes.grid': True,
 'axes.axisbelow': True,
 'axes.labelcolor': '.15',
 'grid.color': '0.9',
 'grid.linestyle': '-',
 'xtick.direction': 'in', 
 'ytick.direction': 'in',
 'xtick.bottom': True,
 'xtick.top': True,
 'ytick.left': True,
 'ytick.right': True, 
 'font.family': ['sans-serif'],
 'font.sans-serif': [
  'Liberation Sans',
  'Bitstream Vera Sans',
  'sans-serif'],})

# Use NumPy to generate random integers

lower_limit = -10
upper_limit = 10
amount      = 100

values_x = np.random.randint(lower_limit, upper_limit, amount)
values_y = np.random.randint(lower_limit, upper_limit, amount)

# print(values_x, values_y)


plt.xlim(lower_limit,upper_limit)
plt.ylim(lower_limit,upper_limit)

plt.plot(values_x,values_y,'o',)#,'.')#,'o') 

plt.xlabel('x')
plt.ylabel('y')

#plt.savefig('random-points-demo.svg')
plt.show() 


# With the above definitions, we have
# 1. the displacement of the walker after $N$ steps is given by the sum
# $$
# x(N) = \sum_i^N s_i,
# $$
# 2. and the displacement squared (with some extra forms for it) is given as
# $$
# x^2(N) = \left( \sum_{i=1}^N s_i \right)^2 
# = \left( \sum_{i=1}^N s_i \right) \left( \sum_{j=1}^N s_j \right) 
# = \sum_{i=1}^N \sum_{i=j}^N s_i s_j
# = \sum_{i=1}^N s_i^2 + \underbrace{\sum_{i,j=1}^N}_{i\ne j}s_i s_j
# $$

# We can use the above definitions to calculate some fundamental properties of random walks. After finding the theoretical predictions, we will write a short computer simulation to see how well or if the predictions hold.

# **Property 1: Average displacement of a random walker**
# 
# \begin{align}
# \langle x(N) \rangle    & = \langle \sum_{i=1}^N s_i \rangle \\
#                         & = \sum_{i=1}^N \langle s_i \rangle \\
#                         & = \sum_{i=1}^N \ell p + (-\ell)q 
#                         \mathrm{\,\, or\,\,} =  \sum_{i=1}^N \ell p + (-\ell)(1-p) \\
#                         & = \underline{\underline{N \ell (2p-1)}}.
# \end{align}
# 
# In the *isotropic* (or symmetric) case $p= q=  \frac{1}{2}$ and hence $\langle x(N) \rangle = 0$. This means that the mean, or average, position of an isotropic walker will be at the origin. How should one interpret this? Although the mean position as at the origin, it does not mean that the particle (or walker) is always found at the origin. However, it means that the probability of finding the walker anywhere in space is *centered* around the origin.  
# 
# In the *biased* (or asymmetric) case $p \ne q$ and the the mean value is non-zero. Thus, the probability of finding the walker is no longer centered around the origin but drifts in the direction of the bias. This bias could be, for example, an external force.
# 
# In both the *isotropic* and *biased* cases the probability distribution itself becomes wider as time progresses. This can be measured by the variance ($\sigma_x^2$) or the standard deviation ($\sigma_x = \sqrt{\sigma^2_x}$). 

# In[9]:


#================================================================================================================
#
# Generate a plot of a 1D random walk + a collection of
# static points
#----------------------------------------------------------------------------------------------------------------
#
#
#================================================================================================================

import random 
import numpy as np 
import matplotlib.pyplot as plt 

import matplotlib.pyplot as plt                            # For plotting
import seaborn as sns
from matplotlib import rc


#---- This allows the use of LaTeX + the use sans-serif fonts also for tick labels:

rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')

# There are 5 presents for background: darkgrid, whitegrid, dark, white, and ticks
# Define how ticks are placed and define font families

sns.set_style("ticks")
sns.set_style("whitegrid", 
 {'axes.edgecolor': 'black',
 'axes.grid': True,
 'axes.axisbelow': True,
 'axes.labelcolor': '.15',
 'grid.color': '0.9',
 'grid.linestyle': '-',
 'xtick.direction': 'in', 
 'ytick.direction': 'in',
 'xtick.bottom': True,
 'xtick.top': True,
 'ytick.left': True,
 'ytick.right': True, 
 'font.family': ['sans-serif'],
 'font.sans-serif': [
  'Liberation Sans',
  'Bitstream Vera Sans',
  'sans-serif'],})

step       = [-1.0,1.0]
#p          = 0.5
#q          = 1.0-0.5
n_steps    = 1000
0
# Create M random walks:

M = 100

avg = 0.0

for i in range(M):
    
    positions = []
    moves     = []
    moves       = np.random.choice(step, n_steps, p=[0.50, 0.5]) 
    positions   = np.cumsum(moves)
    positions   = np.concatenate((positions[:0], [0.0], positions[0:]))
#    print('Mean displacement:', np.mean(positions))
    plt.plot(positions)#,'.')#,'o') 
    avg = np.mean(positions) + avg

print('Ensemble average:', avg)

variance = np.arange(0,n_steps,1)
plt.xlabel('time step')
plt.ylabel('position along the x-axis')
#plt.plot(positions)

# sigma: 68%, 2 sigma: 95%, 3 sigma: 99.7%
# p=0.05 corresponds to 2 sigma

plt.plot(np.sqrt(variance))
plt.plot(-np.sqrt(variance))
plt.plot(2.0*np.sqrt(variance))
plt.plot(-2.0*np.sqrt(variance))
plt.plot(3.0*np.sqrt(variance))
plt.plot(-3.0*np.sqrt(variance))


#plt.savefig('random-walks-demo.svg')
plt.show() 

plt.hist(moves, density=False, facecolor='g', alpha=0.75)

plt.show()
#print(type(positions),positions[0])
#print(positions, positions[-1],len(positions))
#plt.loglog(delay,msd,'x')
#print('avg', np.average(moves),'theor (=0): ', '<x^2(N)> = N*l**2:', np.sum(moves)**2,n_steps)

plt.loglog(np.sqrt(variance))
plt.show()

#\len(positions)


# **Property 2: Variance of a random walker**
# 
# Variance is defined as 
# 
# \begin{align}
# \langle \Delta x^2  \rangle & = \langle (x- \langle x \rangle)^2  \rangle \\
#                             & = \langle x^2 \rangle - \langle x \rangle^2 \\ 
# \end{align}
# 
# Notice that this defintion describes the moment of inertia of the probability with the mean value as the reference point.
# 
# With the above definition, the variance after $N$ steps is given as
# 
# \begin{align}
# \langle \Delta x^2 (N) \rangle & = \langle x^2(N) \rangle - \underbrace{\langle x(N) \rangle^2}_{N^2 \ell^2 (2p-1)^2} \\ 
# \end{align}
# 
# Since we have already calculated $\langle x(N) \rangle $, we have the second term as
# 
# \begin{align}
#  \langle x(N) \rangle^2  & = \underline{N^2 \ell^2 (2p-1)^2} \\ 
# %                         & =  \underline{N^2 \ell^2 (4p^2 - 4p + 1)}.
# \end{align}
# 
# Let's calculate the first term:
# \begin{align}
# \langle x^2(N) \rangle  & = \langle \sum_{i=1}^N s_i^2 \rangle + \langle \underbrace{\sum_{i,j=1}^N}_{i\ne j}s_i s_j \rangle \\ 
# %                        & = \left( \sum_{i=1}^N \underbrace{(\ell)^2p + (-\ell)^2 (1-p)}_{\ell^2}\right) 
# %                        +  \sum_{i,j=1\\ i\ne j}^N \langle s_i \rangle \langle s_j \rangle \\ 
#                         & = \underline{N\ell ^2 +  (N^2-N)\ell^2(2p-1)^2}
# \end{align}
# 
# Lets put the terms together to get the variance:
# 
# \begin{align}
# \langle \Delta x^2 (N) \rangle & = \langle x^2(N) \rangle - \langle x(N) \rangle^2 \\ 
# %                                & = N\ell ^2 +  (N^2-N)\ell^2(2p-1)^2 - N^2 \ell^2 (2p-1)^2 \\
# %                                & = N\ell ^2 + N^2\ell^2(2p-1)^2 - N\ell^2(2p-1)^2 - N^2 \ell^2 (2p-1)^2 \\
# %                                & = N\ell ^2 - N\ell^2(2p-1)^2 \\
# %                                & =  N\ell ^2 - N\ell^2 (4p^2 - 4p +1) \\
# %                                & = N\ell ^2 - N\ell^2 4p^2 + N\ell^2 4p - N\ell^2 \\
#                                 & = 4 N\ell ^2 p(1-p)\\
#                                 & = \underline{\underline{4 N\ell ^2 pq}}
# \end{align}
# 
# In the *symmetric* case when $p=q=\frac{1}{2}$, $\langle \Delta x^2 (N) \rangle = N\ell ^2$. This describes the spread around the origin; notice the radial symmetry: $\ell$ appears as a square and hence directions $-\ell$ and $\ell$ are treated as equal. In the *biased* case when $p \ne q$ this symmetry is broken. 
# 
# We can now connect this result to a simulation. If we have a simulation with time step $\delta t$, then the simulation time after $N$ steps is $t = N \Delta t$. With this we can write the variance as 
# 
# \begin{align}
# \langle \Delta x^2 (N) \rangle  & =  4 N\ell ^2 pq \\
#                                 & = 4 pq t \frac{\ell^2 }{ \Delta t}.
# \end{align}
# 
# Since the walker can move in two directions ($+x$ and $-x)$, we can write the above as
# 
# \begin{align}
# \langle \Delta x^2 (N) \rangle  & =  4 N \ell ^2 pq \\
#                                 & = 2 \underbrace{2 pq \frac{\ell^2 }{\Delta t}}_{D} t \\
#                                 & = \underline{\underline{2 D t}}, \mathrm{\,\,where\,\,}D\mathrm{\,\,is\,\,the\,\,diffusion\,\,coefficient.}
# \end{align}
# 
# In the special case of isotropic walkers ($p=\frac{1}{2}$), we have
# 
# \begin{align}
# \langle \Delta x^2 (N) \rangle  & =  4 N \ell ^2 pq \\
#                                 & = 2 t 2pq \frac{\ell^2 }{\Delta t} \\
#                                 & = 2t \underbrace{\frac{1}{2}\frac{\ell^2 }{\Delta t}}_{D} \\
#                                 & = 2 Dt.
# \end{align}
# 
# **Exercise:** Prove equations X and Y.

# ### Simulation of Random Walk in 1-d
# 
# Let's test the above prediction by a simple computer simulation. The code that is needed is very simple:
# - assign step length $\ell$. For simplicity, $\pm \ell = \pm 1$.
# - set the origin to zero.
# - assign probabilities $p$ and $q$. 
# - generate uniformly distributed random numbers such that $r \in [0,1)$.
#     - If $r < p$ take a step to the positive direction
#     - Else move to the negative direction
# - store the result
# - repeat $M$ times
# - report the results for the mean and variance, compare with the theoretical predictions.
# 
# In the essence, this is a simple Monte Carlo simulation.
# 
# **Exercise:** Write a simple code to simulate 1-d random walk. 
# 
# **Exercise:** Write a simple code to simulate 1-d random walk. 
# 
# **Exercise:** Study how sensitive average and variance are to $p$ and $q$. 
# 

# In[10]:


#================================================================================================================
#
# 1D random walk + MSD
#----------------------------------------------------------------------------------------------------------------
#
#
#================================================================================================================

import random 
import numpy as np 
import matplotlib.pyplot as plt 

import matplotlib.pyplot as plt                            # For plotting
import seaborn as sns
from matplotlib import rc


# Pretty plots:

sns.set()
rc('text', usetex=True)
# 5 presents: darkgrid, whitegrid, dark, white, and ticks
sns.set_style("whitegrid")
sns.set_style("ticks")
sns.set_style("whitegrid", {'axes.edgecolor': 'black',
 'axes.grid': True,
 'axes.axisbelow': True,
 'axes.labelcolor': '.15','grid.color': '0.9',
 'grid.linestyle': '-',"xtick.direction": "in", 'ytick.direction': 'in','xtick.bottom': True,
 'xtick.top': True,
 'ytick.left': True,
 'ytick.right': True, 
 'font.family': ['sans-serif'],
 'font.sans-serif': [#'Arial',
#  'DejaVu Sans',
  'Liberation Sans',
  'Bitstream Vera Sans',
  'sans-serif'],})
sns.set_context("paper", font_scale=1.5, rc={"lines.linewidth": 2.0})
#sns.set_palette("husl")
# deep, colorblind, dark, bright, muted, pastel
#current_palette = sns.color_palette("colorblind")
#sns.palplot(current_palette)

def msd1(vector):
    # Take all possible intervals:
    intervals = np.arange(len(vector))
    msd       = np.zeros(intervals.size) 
#    print('intervals:', intervals)
#    print('msd:', msd)
#    print(enumerate(intervals))

    # loop over all possible shifts
    for i, shift in enumerate(intervals):
        diffs  = vector[:-shift if shift else None] - vector[shift:]
        x2     = np.square(diffs).sum(axis=0)
        msd[i] = x2.mean()
#        print(i,diffs,x2,msd[i])
        
    return msd

step       = [-1.0,1.0]
n_steps    = 50
msd        = np.zeros(n_steps+1)
# Create M random walks:

final_position = []

x_avg = 0.0
x_2   = 0.0
#final_position = 0.0

M = 100

for i in range(M):
    
    moves       = np.random.choice(step, n_steps, p=[0.50, 0.5]) 
    positions   = np.cumsum(moves)
    positions   = np.concatenate((positions[:0], [0.0], positions[0:]))
#    positions_2 = positions**2 
#    plt.plot(positions)#,'.')#,'o') 
#    print(np.average(moves),np.average(positions),np.average(positions_2),n_steps )    
    x_avg = x_avg + positions[-1]
    x_2 = x_2  + positions[-1]**2
#    final_position[i] = positions[-1]
    final_position = np.append(final_position,positions[-1])
#    print(positions)
#    print(i,final_position, len(final_position))

    msd = msd + msd1(positions)
    
# Print on screen:

msd = msd/M

plt.xlabel('time')
plt.ylabel('msd')
plt.axvline(x=len(positions)/2)
plt.axvline(x=len(positions)/3)
plt.axvline(x=len(positions)/4)
plt.axvline(x=len(positions)/10)



plt.loglog(msd)
plt.show() 

print('Average over',M,'random walks of length',n_steps)
print('Average position after N steps:', x_avg/M)
print('Variance after N steps:', x_2/M - (x_avg/M)**2, 'Theoretical value:', n_steps)

# plot the last trajectory:

plt.xlabel('time step')
plt.ylabel('position along the x-axis')

plt.plot(positions)
plt.show() 

plt.plot(final_position)
plt.show() 

# the histogram of the data
#n, bins, patches = plt.hist(final_position, 50, density=True, facecolor='g', alpha=0.75)
plt.hist(final_position, 20, density=False, facecolor='g', alpha=0.75)
#print(len(final_position))

#print(type(positions),positions[0])
#print(positions, positions[-1],len(positions))
#plt.loglog(delay,msd,'x')
#print('avg', np.average(moves),'theor (=0): ', '<x^2(N)> = N*l**2:', np.sum(moves)**2,n_steps)

#\len(positions)


# In[11]:


#================================================================================================================
#
# 1D random walk + MSD
#----------------------------------------------------------------------------------------------------------------
#
#
#================================================================================================================

import random 
import numpy as np 
import matplotlib.pyplot as plt 
  
def mean_square_displacement(positions,delay):
    # loop over the time delays
    # compute MSD using np.roll and shifting the arrays
    # normalize

    # initialize arrays. not really necessary, but clearer
    msd     = np.empty(0)
    sqd     = np.empty(0)
    delayed = np.empty(0)
        
    for tau in delay:
        shift   = len(positions)-tau
        delayed = np.roll(positions, -tau)[0:shift]
        sqd     = np.square(positions[0:shift] - delayed)
        msd     = np.append(msd,np.sum(sqd)/len(sqd))
        
    return msd

# The times at which MSD is evaluated:

delay = [1,2,3,10,20,30,50,100,200,500,1000,2000,3000,5000,6000,10000,15000,20000]

step       = [-1.0,1.0]
n_steps    = 1000000

# Create N random walks:

for i in range(5):
    
    positions  = np.empty(0)
    
# In case you want to use a predefined seed.
#    np.random.seed(1)

    moves      = np.random.choice(step, n_steps, p=[0.5002, 0.4998]) 
    positions  = np.cumsum(moves)

    msd = mean_square_displacement(positions,delay)
    plt.plot(positions)#,'.')#,'o') 

    
# Plot:

plt.xlabel('time step')
plt.ylabel('position')
plt.xlim(0,10)
plt.ylim(0,10)

#plt.plot(positions)#o') 
plt.show() 

# Fit:

#z = np.polyfit(delay,msd,1)
#slope, intercept = z
#diffusion_constant = slope/2.0# / coefficient
#print(delay)
#np.int(delay)*diffusion_constant
#gg = np.array(delay)*diffusion_constant + intercept
#plt.loglog(delay,gg,'*')
#print(diffusion_constant)
#plt.plot(delay,10.0*np.sqrt(delay),'o|')
#plt.plot(delay,msd,'x')
plt.loglog(delay,msd,'x')
print('avg', np.average(moves),'theor (=0): ', '<x^2(N)> = N*l**2:', np.sum(moves)**2,n_steps)

#\len(positions)


# In[12]:


step = [-1,1]
a=np.random.choice(step, 10000, p=[0.5, 0.5])
plt.plot(np.cumsum(a))


# In[13]:


b=np.arange(10)
#b=np.array([1.0,2.0,1.0,3.0,1.0])
c=b[1::2]
#b.astype(int)
print(b)
delay = 1
#print(np.diff(c))


# In[14]:


bb=np.roll(b, -delay)[0:4]
print(bb)


# In[15]:


b-np.roll(b, -delay)
#indices = [0:3] 
#a[indices].sum()
#import itertools as ite
shift = len(b)-delay
print(b[0:shift])
print(bb[0:shift])
#np.square
cc = np.cumsum(np.square(b[0:shift] -bb))
print(b[0:shift] -bb)
print(cc)
np.sum(cc)/len(cc)
#g=b[0:2]
#print(len(g))


# In[256]:


delay = [1,2,3,4]
positions = b
#msd = np.empty([len(delay)])
msd = []
for tau in delay:
    shift   = len(positions)-tau
#    print(len(positions),shift)
    delayed = np.roll(b, -tau)[0:shift]

#    print(positions[0:shift])
#    print(delayed[0:shift])

    sqd = np.cumsum(np.square(positions[0:shift] -delayed))
#    print('displ',sqd)
    np.sum(sqd)/len(sqd)
    msd = np.append(msd,np.sum(sqd)/len(sqd))

#    print(np.sum(sqd)/len(sqd),len(sqd),msd)
plt.plot(delay,msd)


# In[185]:


c=(b-np.roll(b, -1))**2
print(c)
cc=[1,2,3,4,4]
d=ite.islice(cc, 2,3)
print(d)
d


# In[155]:


np.cumsum(c)


# In[189]:


print(c)
c.cumsum(axis=0)[0:2]


# In[139]:


plt.plot(np.cumsum(a))


# In[61]:


plt.hist(final_position, 30, density=False, facecolor='g', alpha=0.75)


# #### Random walk in 3-dimensions. Freely jointed chain model for polymers.
# \begin{align}
# \langle \vec{r} \rangle    &= \langle \sum_{i=1}^N \vec{a}_i \rangle \\
#                            &=(x+y)(x^2+2xy+y^2)\\
#                            &=x^3+3x^2y+3xy^3+x^3.
# \end{align}

# ### 2d random walk

# **Exercise:** Write a code for a random walk in 2d.

# In[169]:


#================================================================================================================
#
# 2D random walk 
#----------------------------------------------------------------------------------------------------------------
#
#
#================================================================================================================

import random 
import numpy as np 
import matplotlib.pyplot as plt 

import matplotlib.pyplot as plt                            # For plotting
import seaborn as sns
from matplotlib import rc


# Pretty plots:

sns.set()
rc('text', usetex=True)
# 5 presents: darkgrid, whitegrid, dark, white, and ticks
sns.set_style("whitegrid")
sns.set_style("ticks")
sns.set_style("whitegrid", {'axes.edgecolor': 'black',
 'axes.grid': True,
 'axes.axisbelow': True,
 'axes.labelcolor': '.15','grid.color': '0.9',
 'grid.linestyle': '-',"xtick.direction": "in", 'ytick.direction': 'in','xtick.bottom': True,
 'xtick.top': True,
 'ytick.left': True,
 'ytick.right': True, 
 'font.family': ['sans-serif'],
 'font.sans-serif': [#'Arial',
#  'DejaVu Sans',
  'Liberation Sans',
  'Bitstream Vera Sans',
  'sans-serif'],})
sns.set_context("paper", font_scale=1.5, rc={"lines.linewidth": 2.0})
#sns.set_palette("husl")
# deep, colorblind, dark, bright, muted, pastel
#current_palette = sns.color_palette("colorblind")
#sns.palplot(current_palette)

step       = [-1.0,1.0]
n_steps    = 10000

# Create M random walks:

x_avg = 0.0
x_2   = 0.0

y_avg = 0.0
y_2   = 0.0

M = 20000

for i in range(M):
    
    moves_x       = np.random.choice(step, n_steps, p=[0.50, 0.50]) 
    moves_y       = np.random.choice(step, n_steps, p=[0.50, 0.50]) 
    
    positions_x   = np.cumsum(moves_x)
    positions_y   = np.cumsum(moves_y)
    
    positions_x   = np.concatenate((positions_x[:0], [0.0], positions_x[0:]))
    positions_y   = np.concatenate((positions_y[:0], [0.0], positions_y[0:]))    
#    positions_2 = positions**2 
#    plt.plot(positions)#,'.')#,'o') 
#    print(np.average(moves),np.average(positions),np.average(positions_2),n_steps )    
    x_avg = x_avg + positions_x[-1]
    x_2   = x_2  + positions_x[-1]**2
    
    y_avg = y_avg + positions_y[-1]
    y_2 = y_2  + positions_y[-1]**2    
    
    
# Print on screen:

print('Average over',M,'random walks of length',n_steps)
print('Average position after N steps:', x_avg/M, y_avg/M, (x_avg/M)**2 + (y_avg/M)**2)
print('Variance after N steps:', x_2/M - (x_avg/M)**2,y_2/M - (y_avg/M)**2, 'Theoretical value:', n_steps)

# plot the last trajectory:

plt.xlabel('time step')
plt.ylabel('position along the x-axis')

plt.plot(positions_x,positions_y)
plt.show() 

#print(type(positions),positions[0])
#print(positions, positions[-1],len(positions))
#plt.loglog(delay,msd,'x')
#print('avg', np.average(moves),'theor (=0): ', '<x^2(N)> = N*l**2:', np.sum(moves)**2,n_steps)

#\len(positions)


# ### 3d random walk

# **Exercise:** Download the trajectory data from AAA. The data is from an MD simulation of XX water molecules at XX degrees. Examine if the molecules execute 3d random walk.

# ### Summary: 1d vs 2d vs 3d random walks

# ## Diffusion: Microscopic vs macroscopic description

# ## Microscopic derivation of the Diffusion Equation
# 
# [//]: # "
# Master equation
# \begin{align}
# \frac{\partial p_i}{\partial t} & = -
# \sum_{j=1}^N \left ( w_{ij} p_i - w_{ji} p_j \right) 
# \end{align}
# 
# Transition rates
# \begin{align}
# w_{ij} & = \frac{p_{ij}}{\tau} 
# \end{align}
# Steady state:
# \begin{align}
# \frac{\partial p^*}{\partial t} & = 0
# \end{align}
# "

# Let's consider the *symmetric* random walk, that is, $p=q=\frac{1}{2}$. We now introduce the probability for the walker to be at lattice site $i$ after taking $N$ steps. We denote this by
# 
# \begin{align}
# p(i,N)
# \end{align}
# 
# There are two possible ways for the walker to have arrived at site $i$ after $N$ steps: After $N-1$ steps it must have been either at site $i-1$ or $i+1$. Since we have a *symmetric* random walk, the probabilities of the two two sites are equal ($p=q=\frac{1}{2}$). With this, the probability for the walker to be at site $i$ after $N$ steps is given as the sum of the two probabilities $p(i-1,N-1)$ and $p(i+1,N-1)$   as
# 
# \begin{align}
# p(i,N) = \frac{1}{2} p(i+1,N-1) +
#          \frac{1}{2} p(i-1,N-1).
#          \label{eq:pin}
# \end{align}
# 
# This is a discrete formulation of the problem. While this is useful on its own, we need to have a contiuum formulation as well. That can be done by a change variables and taking the continuum limit at which the discrete time step and step length approach zero. To be able to do that, let's give the time $t$ and position $x$ in terms of a discrete time step of length $\Delta t$ and lattice size of $\ell$ as
# 
# [//]: # "If we have a simulation of $N$ time steps of length $\Delta t$ on a lattice that has lattice size $\ell$, then we can say that after $N$ time steps the walker is at site $i$. Using these definitions, we can write"
# 
# \begin{align}
#  t & = N \Delta t \\
#  x & = i \ell
# \end{align}
# 
# 
# With this, we write Eq.\ref{eq:pin} as
# 
# 
# \begin{align}
# p\left( \frac{x}{\ell},\frac{t}{\Delta t}\right)  = 
# \frac{1}{2}  p \left( \frac{x}{\ell} 
# + 1, \frac{t}{\Delta t}-1 \right) 
#          + \frac{1}{2} p \left( \frac{x}{\ell}-1,\frac{t}{\Delta t}-1 \right).
#          \label{eq:p_discr}
# \end{align}
# 
# To be able to proceed, there is one important property that we must notice: The probility $p$ does not depend on our choice of time and length scales, that is $\ell$ and $\Delta t$. This has the consequence that if we can arbitrarily scale the position and time. In other words, we can multiply the position and time by arbitrary constants. Furthermore, position and time are independent variables.
# Before applying, let's examine this a bit further. The probability 
# 
# \begin{align}
# p\left( \frac{x}{\ell},\frac{t}{\Delta t}\right)
# \end{align}
# 
# We can then write separately for the position and time coordinates
# 
# \begin{align}
# p\left( \xi \frac{x}{\ell},\frac{t}{\Delta t}\right) & = 
# \xi p\left( \frac{x}{\ell},\frac{t}{\Delta t}\right)\\
# p\left( \frac{x}{\ell}, \tau \frac{t}{\Delta t}\right) & =
# \tau p\left( \frac{x}{\ell},\frac{t}{\Delta t}\right)\\
# \end{align}
# 
# and simulataneous application then gives
# 
# \begin{align}
# p\left( \xi \frac{x}{\ell}, \tau \frac{t}{\Delta t}\right) & = 
# \tau \xi p\left( \frac{x}{\ell},\frac{t}{\Delta t}\right).
# \end{align}
# 
# We can now apply this to Eq.\ref{eq:p_discr} and scale by the lattice size $\ell$ and time step $\Delta t$ - these are arbitrary parameters. 
# 
# 
# \begin{align}
# \ell \Delta t \,
# p\left( \ell \frac{x}{\ell}, \Delta t \frac{t}{\Delta t}\right) & = 
# \frac{1}{2} \ell \Delta t \, 
# p \left(\ell \left( \frac{x}{\ell} 
# + 1\right), \Delta t \left( \frac{t}{\Delta t}-1 \right) \right) 
#          + \frac{1}{2} \ell \Delta t \, 
#          p \left(\ell \left( \frac{x}{\ell}-1 \right ), \Delta t \left( \frac{t}{\Delta t}-1 \right) \right) \\
#  & = \frac{1}{2} \ell \Delta t \,  p \left(x + \ell , t- \Delta t  \right) 
#          + \frac{1}{2} \ell \Delta t \,  p \left(x - \ell , t- \Delta t  \right)  \\      
#          & \mathrm{\,\,\,...divide\,\,by\,\,}\ell \Delta t... \\
#  p\left( x,t\right) & = \frac{1}{2}  p \left(x + \ell , t- \Delta t  \right)
#  + \frac{1}{2}  p \left(x - \ell , t- \Delta t  \right)
#           \label{eq:p_discr2}
# \end{align}
# 
# This is a very useful form: Subtracting $ p\left( x,t - \Delta t \right )$ gives
# 
# \begin{align}
# p\left( x,t \right) - p\left( x,t - \Delta t \right) & = 
#  \frac{1}{2} \left[ 
# p \left(x + \ell , t- \Delta t  \right)
#  + p \left(x - \ell , t- \Delta t  \right)
#  -2  p\left( x,t - \Delta t \right)
# \right]
# \end{align}
# 
# There are a few possible ways as how to proceed. If we notice that that the left hand side looks very similar to the the definition of the derivative (needs $\Delta t$) and the right hand side looks very much lke the second order derivative (needs $\ell^2$), we can bring in the necessary missing parts: Multiply both sides by $\ell^2/\Delta t \ell^2/$ and group the terms:
# 
# \begin{align}
# \frac{1}{\Delta t}\left[p\left( x,t \right) - p\left( x,t - \Delta t \right) \right] & = 
#  \frac{\ell^2 }{2\Delta t}  \frac{1}{\ell^2} \left[ 
# p \left(x + \ell , t- \Delta t  \right)
#  + p \left(x - \ell , t- \Delta t  \right)
#  -2  p\left( x,t - \Delta t \right)
# \right]
# \end{align}
# 
# 
# Now, we have differential forms on both sides, and we are ready to take the limits $\Delta t \rightarrow 0$ and $\ell \rightarrow 0$   but the term $\frac{\ell^2 }{2\Delta t}$ looks problematic. However, that term must approach a constant, that is
# 
# \begin{align}
# \lim_{\Delta t \rightarrow 0\\ \ell \rightarrow 0} \frac{\ell^2 }{2\Delta t} = \mathrm{constant}
# \end{align}
# 
# We can now identify this is as the *diffusion coefficient* $D$ and we can write
# \begin{align}
# \frac{\partial p(x,t)}{\partial t} = D \frac{\partial^2 p(x,t)}{\partial x^2}
# \end{align}
# 
# This is the *diffusion equation* for a single walker (or particle) in one dimension. The single particle diffusion is also called *tracer diffusion*.
# 
# The generalization to higher dimensions is straighforward:
# 
# \begin{align}
# \frac{\partial p(x,y,z,t)}{\partial t} = D \nabla^2 p(x,y,z,t)
# \end{align}
# 
# 

# #### Generalization of single particle diffusion to a finite density of particles 
# 
# Let's assume that the system in homogeneous. To describe a number of particles, we use the number density $n(\vec{r},t)$, where $\vec{r} = [x,y,z]$.
# 
# Collective diffusion tensor:
# \begin{equation*}
# \underline{D}^c = 
# \begin{bmatrix}
# D_{xx}^c & D_{xy}^c & D_{xz}^c \\
# D_{yx}^c & D_{yy}^c & D_{yz}^c \\
# D_{zx}^c & D_{zy}^c & D_{zz}^c
# \end{bmatrix}
# \end{equation*}
# 
# Now we have the general diffusion equation:
# 
# \begin{align}
# \frac{\partial n(\vec{r},t)}{\partial t} = \nabla \cdot \underline{D}^c \cdot \nabla n(\vec{r},t)
# \end{align}
# 
# If the the diffusion tensor is constant and isotropic,
# 
# \begin{align}
# \frac{\partial n(\vec{r},t)}{\partial t} = {D}^c \nabla^2 n(\vec{r},t)
# \end{align}
# 

# ### Note on Laplace transforms
# 
# The Laplace transform is defined as
# 
# \begin{align}
# \mathcal{L} \{ f(t) \} &= \int_{0^-}^{\infty} dt\, e^{-st} f(t)
# \end{align}
# 
# The variable $s$ is a complex one.
# 
# Poles on the real axis are purely dissipative whereas poles on the imaginary axis are oscillatory in the sense that an impulse as the input will lead to oscillatory response without any dissipation.
# 
# **In condensed matter and plasma physics** one typically uses 
# 
# \begin{align}
# \mathcal{L} \{ f(t) \} &= \int_{0^-}^{\infty} dt\, e^{i\omega t} f(t)
# \end{align}
# 
# as the kernel instead of the above. In **electrical engineering** 
# 
# \begin{align}
# \mathcal{L} \{ f(t) \} &= \int_{0^-}^{\infty} dt\, e^{-i\omega t} f(t)
# \end{align}
# 
# is often used.

# The diffision equation is a linear *parabolic partial differential equation.* To solve it, initial condition is needed for time and two boundary conditions are needed for the spatial part.

# ### The fundamental solution
# 
# 

# ### Continuum limit of a Random Walk: Wiener process

# In[ ]:





# In[62]:


48*112


# ### Hydrodynamic modes
# 
# We can now use the formulation for collective diffusion to study fluctuations which provides us with the hydrodynamic modes. To do that, we notice two things: 1) The time dependence is an *initial value problem* and 2) spatial depenence is a *boundary value problem*. This means that mathematically, we Fourier transform the spatial part and Laplace transfor the temporal part:
# 
# \begin{align}
# n(\vec{k},t) & = \int_{-\infty}^{\infty} d\vec{r} \, e^{-i \vec{k} \cdot \vec{r}} n(\vec{r},t)\\
# n(\vec{k},s) & = \int_{0}^{\infty} d\vec{t} \, e^{st} n(\vec{k},t)
# \end{align}
# 
# We need to convert the diffusion equation accordingly. The *Laplace transform* of a derivative is given as
# 
# $$
# \mathcal{L}\left\{\frac{df(x)}{dx}\right\} = s F(s) - f(0^-)
# $$
# 
# and the *Fourier transform* of the Laplacian is given as
# 
# $$
# F
# $$
# 
# This gives
# \begin{align}
# n(\vec{k},s) = \frac{i}{z + i D^c k^2} n(\vec{k},t=0)
# \end{align}
# 
# where we have identified the 

# In[ ]:





# In[2]:


import pandas as pd
import numpy as np
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')


# In[ ]:





# ## Lipid diffusion: to do:
# 
# - Vary the delay time and measure the displacement distribution. 
#   * Hsieh et al: Two-component Gaussian fit (using 1 ms delay; statistcs: 10,000 steps or 5,000 per direction, bin size: 1.9 nm). 
#      - "a sum of two Gaussian functions corresponding to distinct diffusion coefficients of $D_1= 0.19 \pm  0.01$ $\mu m^2/s$ and $D_2= 0.028 \pm 0.005$ $\mu m^2/s$ with weighting factors $0.78 \pm 0.04$ and  $0.22 \pm 0.04$, respectively. Here, and refer to the fractions of time that the particle undergoes diffusion at the corresponding mobilities."
# - Hsieh et al. used a two-component distribution function for fitting:
# 
# \begin{align}
# P(r^2, \Delta t) & = 1 - \epsilon_1 e^{-r^2/4D_1 \Delta t} - \epsilon_2 e^{-r^2/4D_2 \Delta t}; \epsilon_1+ \epsilon_2 = 1
# \end{align}
# 
# Fit using $D_i$ and $\epsilon_i$.
# 
# General:
# 
# \begin{align}
# P(r^2, \Delta t) & = 1 - \sum_{i=1}^N 
# \epsilon_i e^{-r^2/4D_i \Delta t}; \sum_{i=1}^N \epsilon_i = 1
# \end{align}
# 
# 

# [Tracking single particles on supported lipid membranes:
# multi-mobility diffusion and nanoscopic confinement](https://arxiv.org/abs/1312.6736)
# Chia-Lung Hsieh, Susann Spindler, Jens Ehrig, Vahid Sandoghdar

# "the diffusion of single gold nanoparticles (GNPs) with diameter of 20 nm attached to GM1 ganglioside or DOPE lipids at different concentrations in supported DOPC bilayers"
# 
# - Diffusion of GM1 on supported DOPC (not) DOPE
# - Single-particle tracking (SPT) method: interferometric scattering microscopy (iSCAT)
# - 1.9 nm spatial precision at 1 ms temporal resolution
# - transient confinements within domains as small as 20 nm
# - deviations of the trajectory from the expectations of normal diffusion
# - 1,000 frames/sec
# - Short time nanoconfinements. 
#   * The problem: analysis averages them out. 
#   * solution: Add theird mobility component
#   
# \begin{align}
# \mathrm{MSD} (\Delta t) = 4 D_{\alpha} \Delta t^{\alpha}
# \end{align}
# as a function of delay
# 
# Result: $D_\alpha = 0.18 \mu m^2/s$ and $\alpha = 1.02$
# 
# **Nanoconfinement analysis:** Transient MSD
# 
# \begin{align}
# \mathrm{MSD}_\mathrm{trans}  & =  \langle MSD (\Delta t) \rangle_T (t) \\
#                     & = \frac{1}{T-\Delta t} \sum_{t=\tau}^{t+T - \Delta t} 
#                     \left(
#                     \vec{r}(\tau ) - \vec{r}(\tau + \Delta t)
#                     \right)^2
# \end{align}
