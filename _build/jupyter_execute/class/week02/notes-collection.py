#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Visualization

# \begin{equation}
# \vec{F}_{i}=m_{i}\ddot{\vec{r}}_{i}
# \end{equation}
# 
# \left\{ \begin{array}{ll}
# \dot{\vec{r}}_{i}=\frac{\vec{p}_{i}}{m_{i}} \\
# \dot{\vec{p}}_{i}=\vec{F}_{i} \end{array} \right. ,
# \end{equation}
# where the forces are given as
# \begin{equation}
# \vec{F}_{i}=-\frac{\partial{U}(\vec{r}_{i})}{\partial\vec{r}_{i}},
# \end{equation}
# where $m_{i}$ stands for the mass of the particle and $\dot{\vec{r}}_{i}$ denotes the derivative of $\vec{r}_{i}$ with respect to time $t$.

# \subsection{Verlet algorithm}
# The Verlet algorithm [40] is obtained by addition of Taylor expansions about $\vec{r}(t)$ in two different time directions.
# It reads as follows
# \begin{equation}
# \vec{r}_{i}(t+\Delta{t})=2\vec{r}_{i}(t)-\vec{r}_{i}(t-\Delta{t})+\frac{1}{m}\vec{F}_{i}(t)(\Delta{t})^2.
# \end{equation}
# The Verlet algorithm uses the position and force at time $t$ and the position at time $(t-\Delta{t})$ to calculate the new position at time $(t+\Delta{t})$. So at $t=0$ the position at time $(-\Delta{t})$ is needed. This problem is usually solved by using a Taylor expansion about $\vec{r}(t)$.
# The velocity, which does not appear explicitly in the Verlet algorithm, can be obtained from the finite difference formula
# \begin{equation}
# \vec{v}_{i}(t)=\frac{\vec{r}_{i}(t+\Delta{t})-\vec{r}_{i}(t-\Delta{t})}{2\Delta{t}}
# \end{equation}
# In this algorithm the velocity term is always a step behind the position term.
# 

# \subsection{Leapfrog algorithm}
# The leapfrog algorithm [42] is a modification of the Verlet algorithm. Eliminating the velocity from this algorithm shows that it is algebraically equal to the Verlet algorithm.
# It reads as
# \begin{eqnarray}
# \vec{v}_{i}\left(t+\frac{\Delta{t}}{2}\right) &=& \vec{v}_{i}\left(t-\frac{\Delta{t}}{2}\right)+\frac{1}{m_{i}}\vec{F}_{i}(t)\Delta{t} \nonumber\\
# \vec{r}_{i}(t+\Delta{t}) &=& \vec{r}_{i}(t)+\vec{v}_{i}\left(t+\frac{\Delta{t}}{2}\right)\Delta{t} \nonumber\\
# \end{eqnarray}
# The leapfrog algorithm uses the position and the force at time $t$ and velocity at half a time step $\left(t-\frac{\Delta{t}}{2}\right)$ to update the positions and velocities. The velocity leaps over the coordinate to give the next half-step value of the velocity, which is then used to calculate the new positions. That is where the name of this algorithm comes from.
# The velocity at a full time step is obtained as follows
# \begin{equation}
# \vec{v}_{i}=\frac{\vec{v}_{i}\left(t+\frac{\Delta{t}}{2}\right)+\vec{v}_{i}\left(t-\frac{\Delta{t}}{2}\right)}{2}.
# \end{equation}
# The advantage of programming the equation in the form of the leapfrog algorithm is that the velocity appears explicitly. But it would be desirable to obtain the velocity at the same time step as the position directly from the algorithm without further calculations.

# The van der Waals interaction between atom $i$ and $j$ is most commonly modelled by the Lennard-Jones potential
# \begin{equation}
# \label{eq:LJ}
# U_\mathrm{LJ}(r_{ij}) = 4 \varepsilon
# \left[
# \left(
# \frac{\sigma}{r_{ij}}
# \right)^{12}
# -
# \left(
# \frac{\sigma}{r_{ij}}
# \right)^6,
# \right]
# \end{equation}
# where $\varepsilon$ is the value of the potential at its minimum and $\sigma$ is the atomic diameter.
# The repulsive $r^{-12}$ part in the Lennard-Jones potential cannot be derived from first principles and 
# in principle any rapidly diverging term for $r \rightarrow 0$ is possible. The above form is the most commonly
# used one.  The origin of the $r^{-12}$ is in the Pauli exclusion principle, i.e., it has a quantum mechanical origin.

#  In polymer modelling, it is often necessary to modify the Lennard-Jones potential in such a 
#  away that both good and bad solvent conditions can be be modelled. Good solvent conditions 
#  can be modelled by the purely repulsive so-called truncated and shifted Lennard-Jones potential,
# % 
#  \begin{equation}
# \label{eq:lennardjones}
# U_{\rm LJ-ts} (r_{ij}) = \left\{
# \begin{array}{ll}
# 4\,\epsilon \left[ \left(\frac{\sigma}{r_{ij}}\right)^{12}
#                  - \left(\frac{\sigma}{r_{ij}}\right)^{6} + \frac{1}{4}
#                 \right]
#    & ,\, r_{ij} \leq r_c \\
# 0  & ,\, r_{ij} > r_c
# \end{array}
# \right .
# \end{equation}

# The electrostatic interaction between two charged atoms $i$ and $j$ is represented by Coulomb's law 
# \begin{equation}
# \label{ }
# U(r_{ij}) =  \frac{q_i q_j}{4 \pi \varepsilon r_{ij}} 
# \end{equation}
# where $q_i$ are the charges and $\varepsilon$ is the dielectric constant

# \subsection{Reaction field method}
# 
# The next improvement is to consider the far field using a mean-field approximation.
# The basic idea is to treat all electrostatic
# interactions explicitly within the cutoff distance $r_{\text{cut}}$.
# For larger distance, the system is described by a mean-field approximation,
# typically based on the Poisson-Boltzmann equation. This approach is based on
# Onsager's reaction-field idea dating back to 1936~\cite{Onsager_L_36}. 
# In the reaction-field approximation,
# the continuum
# part is described by a dielectric constant  $\epsilon$, 
# and one has to treat the boundary between the explicit and
# continuum descriptions with some care. This is particularly so
# in inhomogeneous systems and systems having surfaces. That is easier
# to understand if one
# considers the following example: the dielectric
# constant of water is about 78 whereas in the lipid bilayer 
# core it is about 2-5~\cite{Koehorst:04vg}. This change occurs over a very short distance,
# and in practice there is a dielectric discontinuity at the water-bilayer
# interface.
# 
# For
# $r>r_{\text{cut}}$
# the system is treated on a mean-field level and is thus completely
# described by its dielectric constant
# $\epsilon$. The
# potential is
# \begin{equation}
# 	\mathcal{V}(r)=\frac{q_i q_j}{4\pi\epsilon_0 r}
# 	\left[ 1 + \frac{\epsilon -1}{2\epsilon+1} 
# 	\left(\frac{r}{r_{\text{cut}}}\right)^3 \right] \\
# 	- \frac{q_i q_j}{4\pi\epsilon_0 r_{\text{cut}}}
# 	\frac{3\epsilon}{2 \epsilon+1}
# 	\quad\text{for}\quad r\le r_{\text{cut}}\;.
# 	\label{eqReactionField}
# \end{equation}
# The second term makes the potential vanish at $r=r_{\text{cut}}$. 

# The total electrostatic energy of N particles and its periodic images can be represented as the following sum 
# \begin{equation}
# \label{ }
# U = \frac{1}{2} \sum_{\vec{n}} \left[
# \sum_{i=1}^N
# \sum_{i=1}^N q_i q_j | \vec{r}_{ij} + \vec{n}|^{-1}
# \right]
# \end{equation}
# where $q_i$, $q_j$ are the charges including the electric constants and factors.  $\vec{n} = N_xL,n_yL,n_zL)$ 
# is the box vector, where $L$ is the box length and $n_x$, $n_y$ and $n_z$ are integers. 
# In the sum above, the case where $i=j $for   needs to be excluded. 
# This sum is only conditionally convergent. 
# 
# The idea of the Ewald sum is to screen each charge of the neighboring charges 
# by a radial Gaussian charge distribution of equal magnitude than the original charge, but of opposite sign 
# 
# \begin{equation}
# \label{ }
# \rho_i(\vec{r}) = q_i \kappa^3 \exp \left( 
# - \frac{\kappa^2 r^2}{\pi^{3/2}}
# \right)
# \end{equation}
# 
# Here, $q_i$ and$ q_j$ are the two charges, $\alpha$ is Ewald parameter, ${\bf k}$ is the reciprocal
# lattice vector. $V =L_x \times L_y \times L_z$ is the volume of the system. The system was periodic
# in the x-y -plane and we chose $L_x =L_y$. The last term in Eq.~(\ref{eq:2dewald}) is the correction
# term that accounts for the non-periodicity in z-direction. It depends on the geometry used for the
# Ewald summation ($P$) and the total dipole moment (${\bf M}$) of the system.
# 

# \subsection{Routes to coarse graining}
# 
# The methods that have been developed to achieve
#   coarse grained descriptions of physical systems in general -- and
#   soft materials in particular -- can be roughly divided into five
#   categories:
# 
# 
# \begin{enumerate}
# \item Phenomenological methods such as dissipative particle dynamics or Ginzburg--Landau type approaches
# \item Analytical approaches based on the operator projection formalism
# \item Construction of
# coarse grained potentials by matching structure or forces between the two tiers of
# resolution
# %\item Free energy methods such as configurational analysis
# \item The analysis of the occurrence rates of different processes
# \item Techniques such as self-organizing maps to coarse grain molecular representations
# \end{enumerate}
# 
# 
# \textbf{
# Some approaches for selecting the coarse-grained degrees of freedom have already been proposed. Some of these methods are based on the analysis of a single structure, either using  rigidity \cite{gohlke06} or topology \cite{arkhipov06:capsids} to define the interacting units. Another class of methods uses dynamic information from the detailed model, either in the form of normal modes \cite{zhang08} or representing the detailed model as a complex network \cite{gfeller08}. Here, we discuss a somewhat different approach based on analysis of the conformations produced by the simulation.
# }
# 

# \subsection{Henderson theorem -- relation to density functional theory \label{sec:henderson}}
# 
#   The Henderson theorem, powerful as it is, is remarkably simple to
#   prove.  Let us summarize here the essence of the argument.
#   Uniqueness of the potential follows as a beautiful application of
#   the Gibbs-Bogoliubov inequality 
#   (also referred to as
#   Gibbs-Bogoliubov-Feynman or Feynman-Kleinert variational principle~\cite{feynman:86xx}
#   depending on the context). 
#   For two systems with Hamiltonians
#   $H_1$ and $H_2$ the following inequality holds for their free
#   energies:
# \begin{equation}
# F_1 \le F_2 + \langle H_2-H_1\rangle_1 \ , \label{eq:GibbsBogoliubov}
# \end{equation}
# where $\langle\cdots\rangle_1$ denotes the (canonical) average
# appropriate for $H_1$. 
#   The
# key point is that equality holds \emph{if and only if} $H_1-H_2$ is
# independent of all degrees of freedom, which implies that the pair
# potentials can differ only by a constant.  Consider now two systems
# which are identical in all respects except that the pair potential in
# one is $u_1$ and the pair potential in the other is $u_2$. The
# corresponding two particle distributions are $g_1$ and $g_2$. The
# uniqueness theorem asserts that if $g_1\equiv g_2$ then $u_1-u_2$ is a
# constant. Now, if $u_1$ and $u_2$ differ by more than just a constant,
# the same holds for $H_1$ and $H_2$, and thus equality in
# Eq.~(\ref{eq:GibbsBogoliubov}) cannot hold, i.e., we have $F_1 < F_2 +
# \langle H_2-H_1\rangle_1$, or more explicitly
# \begin{equation}
# f_1<f_2+\frac{1}{2}n\int {\rm d}^3r\;\big[u_2(r)-u_1(r)\big]\,g_1(r) \ . \label{eq:inequality1}
# \end{equation}
# where the $f_i$ are the free energies per particle and $n$ is the
# average particle density.  The clue is that the above argument can be
# repeated with system 1 and 2 interchanged, which leads to
# \begin{equation}
# f_2<f_1+\frac{1}{2}n\int {\rm d}^3r\;\big[u_1(r)-u_2(r)\big]\,g_2(r) \ . \label{eq:inequality2}
# \end{equation}
# If we now use the fact that $g_1\equiv g_2$ and add the inequalities
# (\ref{eq:inequality1}) and (\ref{eq:inequality2}), we obtain the
# contradiction $0<0$. This proves that the initial assumption that
# $u_1$ and $u_2$ differ by more than a constant must be wrong.
# 
# \textbf{
# Uniqueness of the pair potential is thus an almost trivial matter.
# The same does not hold, however, for its \emph{existence}.  Much
# more work needs to be done in order to find out, whether the search
# for a pair potential that reproduces a desired $g(r)$ is a quest worth
# beginning.  Luckily, the answer is in the affirmative, as Chayes \textit{et al.}
# have proven in their important papers from 1984 \cite{chayes84a,chayes84b}.
# The rigorous proof for the existence  \cite{chayes84a,chayes84b} is rather lengthy and will not be reproduced here. Basically, if the given RDF is a two-particle reduction of any admissible $N$-particle probability distribution, there always exists a pair potential that reproduces it \cite{chayes84b}. Admissible in this case refers to certain finiteness conditions. In addition, the above theorem holds even if the Hamiltonian of the system contains a fixed $N$-particle interaction term $W(x_1,\ldots,x_N)$ (satisfying certain conditions): any such $W$ can be augmented by a pair potential such that the system reproduces the given RDF.
# }
# 

# ## Phase field models               
# 
# The above description does not include time dependence. 
# How time dependence can be added is to use linear response 
# theory and assume relaxational dynamics, i.e., the system 
# is dissipative and it is driven to equilibrium, see 
# Fig.~\ref{fig:doublewell}. The resulting models are often 
# described as models A, B, C and so on depending on their 
# symmetry properties, dimensionality of the order parameter 
# and conservation laws~\cite{hohenberg77a}.
# 
# 
# Being the simplest, model A serves as an example. It is 
# a non-conserved system and the equation of motion can 
# be given as
# % 
# \begin{equation}
# \frac{\partial \Psi(\vec{x},t)}{\partial t} = - \Gamma
# \frac{\delta {\cal F}[\Psi(\vec{x},t)]}{\delta \Psi(\vec{x},t)}
# + \eta(\vec{x},t),
# \label{eq:modelA}
# \end{equation}
# % 
# where we have included thermal fluctuations as Gaussian 
# random noise with the first and second moments defined as 
# % 
# \begin{equation} 
# \langle \eta(\vec{x},t) \rangle = 0 
# \end{equation}
# % 
# and 
# % 
# \begin{equation} 
# \langle \eta(\vec{x},t)  \eta(\vec{x}',t')
# \rangle = 2 \Gamma k_\mathrm{B} T\delta(\vec{x}-\vec{x}') \delta(t-t').
# \end{equation}
# % 
# The angular brackets denote an average and $\Gamma$ is 
# a kinetic coefficient describing the relaxation rate. 
# An example of the evolution of a system described by model A 
# is given in Fig.~\ref{fig:modelA}.
# 
# 
# Other models can be obtained by including conservation 
# laws, e.g., the dynamical equation of motion for a conserved 
# order parameter is given by model B,
# % 
# \begin{equation}
# \frac{\partial \Psi(\vec{x},t)}{\partial t} = \Gamma \nabla \left[
# \frac{\delta {\cal F}[\Psi(\vec{x},t)]}{\delta \Psi(\vec{x},t)} 
# + \eta(\vec{x},t) \right].
# \label{eq:modelB}
# \end{equation}
# % 
# This can be derived using the continuity equation. 
# 
# 
# The system may have several order parameters that are 
# coupled, thus leading to more complicated free energies 
# and equations of motion, see  Ala-Nissila et al. 
# \cite{softsimu:tapio} and references therein. 
# 
# 
# It is rather surprising that this type of approach has, 
# thus far, had only limited attention in soft matter and 
# biological modeling. There are a few notable exceptions, 
# though. Shore et al. \cite{shore96:a,shore97:a} coupled 
# a phase-field model to Navier--Stokes equation including 
# viscoelasticity to melt fracture in polymer extrusion 
# experiments. The details of that model are beyond this 
# review but it suffices to note that the study of Shore 
# et al. is a good example of the power of the phase-field 
# approach as it provides physical insight into, in this case 
# instabilities, both fundamentally and industrially 
# important problems. 
# 
# 
# Other examples of the use of field theoretical models in 
# soft matter include the OCTA software package which in 
# one of its parts uses self-consistent field theory from 
# the Nagoya group \cite{doi02:a,doi03:a}. Self-consistent 
# field theory has been used in the theoretical description 
# of polymers for a long time. A very recent example of the 
# developments in that field is the elegant study of tetrablock 
# copolymers by Drolet and Fredrickson~\cite{drolet99:a}.   
# 
# 
# Another major effort to build modeling software around 
# field-theoretical ideas is the MESODYN project of the 
# Leiden group \cite{maurits98,fraaije:1997}. They use the 
# Ginzburg--Landau approach and density functional theory 
# to build a systematic and computationally tractable system 
# for polymer melts. A detailed description is again beyond 
# this review, but with their approach it is possible to 
# study phase separation even in three dimensional systems. 
# This approach is closely related to model B of critical 
# dynamics \cite{hohenberg77a} as discussed above.
# 
# 
# 
# 
# 
# \section{Methodological issues in molecular simulations
#          \label{sec:methodological_issues}}
# 
# 
# One of the intriguing issues in science is indeed that there 
# is the artistic side, too. The art of doing science. In the 
# field of molecular simulations and computational sciences, this 
# is largely related to the inventions and new ideas of seeing things 
# done in an accurate but efficient manner. This brings us to the 
# methodological side of doing molecular simulations. In this Section, 
# we consider a few aspects related to both atomistic and coarse-grained 
# descriptions of molecular systems that illustrate the importance 
# of developing the methodology. 
# 
# 
# We discuss three highly important 
# methodological issues whose role for the reliability and 
# accuracy of molecular simulations is particularly significant.  
# First, especially for molecular dynamics simulations of 
# biologically relevant soft matter systems on atomic level, 
# the treatment of long-range electrostatic interactions is 
# a major issue. If this is not handled with care, the 
# interpretation of simulation results may be very problematic due 
# to the underlying artifacts caused by the mistreatment of 
# electrostatics. Second, as all stochastic simulation methods are 
# based on the use of noise produced by so-called pseudorandom 
# number generators, the quality of pseudorandom number sequences 
# is of prominent importance in all cases where they are 
# employed to generate the dynamics for the systems under study. 
# Since pseudorandom number generators produce deterministic 
# rather than unpredictable sequences of numbers, the ``randomness'' 
# of pseudorandom numbers is a very subtle issue and should never 
# be taken for granted. Finally, third, we discuss an old issue 
# that has been thought to be overcome several years ago: 
# the artifacts due to integration schemes that yield the 
# dynamics for systems governed by Newton's equations of 
# motion. In contrast to classical MD, where this issue is 
# well under control, in stochastic simulation techniques 
# such as dissipative particle dynamics the case is more 
# subtle. Here we discuss most recent developments in this 
# field and show how the problems can be overcome in an 
# efficient and reliable fashion. 
# 
# 
# 
# 

# 19## Force fields in classical molecular dynamics
# 
# The {\it force field} is the heart of molecular 
# computer simulations. It describes the internal energy 
# of the system at any moment of time, and obviously 
# consists of a number of terms, each of which describes 
# some physical process. Generally speaking, for a system 
# of $N$ particles whose coordinates are given by $\{\vec{r}_i\} $, 
# one can write down the force field as follows: 
# % 
# \begin{equation} 
# V = \sum_{i} v_1(\vec{r}_i) + 
#     \sum_{i} \sum_{j > i} v_2(\vec{r}_i,\vec{r}_j) + 
#     \sum_{i} \sum_{j > i} \sum_{k > j > i} 
#          v_3(\vec{r}_i,\vec{r}_j,\vec{r}_k) + \cdots . 
# \end{equation} 
# % 
# The potential energy of the system is therefore divided into 
# terms describing one-body, two-body, and three-body interactions, 
# and other higher-order interactions that have not been listed 
# here. The one-body interaction ($v_1$) can be as simple as the 
# action of a uniform electric field on a single atom. Two-body 
# interactions ($v_2$) are obviously those between two 
# interacting particles, and are usually divided into bonded 
# and non-bonded interactions. Bonded two-body interactions 
# such as bond stretching are usually those between particles 
# that are bonded by a covalent bond, while non-bonded 
# interactions such as Coulombic interactions are between 
# those atoms that are not bonded, such as atoms in different 
# molecules. Higher order interactions such as three- ($v_3$) 
# and four-body interactions include bond bending, torsional 
# interactions, etc. 
# 
# 
# In practice, a simple force field typically used for biologically 
# 
# relevant molecules can look like the following: 
# % 
# \begin{eqnarray} 
# \label{eq:forcefield}
# V & = & \sum_{\mathrm{bonds}} 
#     \frac{k_i^\mathrm{b}}{2}(l_i - l_i^{\mathrm{ref}})^2 +
#     \sum_{\mathrm{angles}}\frac{k_i^\mathrm{a}}{2}
#          (\theta_i - \theta_i^{\mathrm{ref}})^2 +
#     \sum_{\mathrm{torsions}}\frac{V_T}{2}
#          (1 + \cos(n\omega - \gamma)) + \\ \nonumber 
#   & &  \sum_{i=1}^{N-1} \sum_{j=i+1}^{N} 
#       \left( 4\epsilon_{ij}
#           \left[ 
#              \left( \frac{\sigma_{ij}}{r_{ij}}\right)^{12} - 
#              \left( \frac{\sigma_{ij}}{r_{ij}}\right)^6 
#           \right] + 
#           \frac{q_i q_j}{4\pi \epsilon_0 r_{ij}}
#       \right)  . 
# \end{eqnarray} 
# % 
# Here the first term on the right-hand side describes the 
# interaction due to bond stretching for a pair of bonded particles, 
# whose reference distance is chosen to be $l_i^\mathrm{ref}$. 
# The interaction in the present case is harmonic, thus it is 
# best justified for small fluctuations. As a remark, note that 
# $l_i^\mathrm{ref}$ is not the equilibrium distance because 
# that depends on thermodynamic conditions as well as the 
# composition of the system. Rather, $l_i^\mathrm{ref}$ should 
# be regarded as the distance that two particles will adapt to 
# in the absence of any other interactions in a system. The 
# second term in Eq.~(\ref{eq:forcefield}) is the (harmonic) 
# bending interaction for three consecutive particles 
# (A\,--\,B\,--\,C) in the same chain-like piece of a molecule, 
# the reference value of the valence angle being 
# $\theta_i^\mathrm{ref}$. The torsional interaction 
# presented third is a four-body term, while a short-range 
# Lennard-Jones 6\,--\,12 potential is often used to describe 
# the steep repulsion due to the Pauli-exclusion principle 
# as well as van der Waals interactions due to dispersion 
# forces. Finally, there is an electrostatic term for long-range 
# Coulombic interactions for a pair of charged particles 
# whose distance from each other is $r_{ij}$. 
# 
# 
# For clarity, let us emphasize here that, to define a force 
# field, one must specify not only the set of potential energy 
# functions in a force field but also the force-field parameters 
# (as well as other practical details such as cutoff distances 
# used in truncating long-range interactions) used in the 
# calculations. If one of the parameters is changed, then 
# the force field is also changed. 

# 
# - 1973: Pomeau et al: Square lattice → not symmetric enough
# - 1983: Pomeau et al: for Lattice Gas Automata to Lattice Boltzmann
# 

# In[1]:


from IPython.display import IFrame
from IPython.display import FileLink
from IPython.display import display_pdf
from IPython.display import display_markdown

from IPython.core.display import display
#import os



#report_path = "/home/mkarttu/jp-2020-07546k_Proof_hi_backup.pdf"
#rel_report_path = os.path.relpath(report_path)

#display(IFrame('https://yle.fi/aihe/tekstitv?P=201', '100%', '600px'))
#display(IFrame('/home/mkarttu/jp-2020-07546k_Proof_hi_backup.pdf', '100%', '600px'))
#IFrame(rel_report_path, width=900, height=650)
#display(IFrame('jp-2020-07546k_Proof_hi_backup.pdf', width=1000, height=650))
#local_file = FileLink("diffusion.md")
#display_markdown(local_file)
#display_markdown("./diffusion.md")
#display_pdf('jp-2020-07546k_Proof_hi_backup.pdf')


# 

# ## Density Functional Theory (DFT)
# 
# Understanding of many-body interacting system of electrons and nuclei re-
# quires electronic structure methods such as Density Functional Theory for the
# description of electronic and structural properties of systems. This chapter
# introduces the many-body particle Hamiltonian of a system of interacting elec-
# trons and nuclei and reviews the essential definitions and formulations that
# yield the single particle Kohn-Sham equations. 
# 

# 

# The question of how to describe a system of many-body interacting electrons
# traces back to decades ago [38, 37]. The difficulty is not because the related
# equations of motions are not known, but in how to solve them. The non-
# relativistic Hamiltonian of a system of interacting electrons and nuclei can be
# written as
# 

# The obstacle is how to solve the time-independent Schrödinger equation
# for a system of N + Nn interacting particles in which the number of electrons
# and nuclei is of the order of Avogadro’s number ∼ 1023:
# [Hˆ
# n + Hˆ
# el]Ψ({r}, {R}) = EΨ({r}, {R}). (3.2)
# where E is the eigenvalue and Ψ({r}, {R}) is the eigenfunction of the coupled
# electronic-nuclear system which is a function of all electronic ({r} = r1, r2, . . . ,
# rN ) and nuclear ({R} = R1, R2, . . . , RNn
# ) variables. E gives the total energy
# of the system and Ψ({r}, {R}) yields the electron distribution.
# One way out of this dilemma is to simplify the Hamiltonian

# ### Born-Oppenheimer approximation
# 
# The Born-Oppenheimer (BO) approximation uses the fact that electrons are much lighter than the nuclei (protons and neutrons). 
# The mass of an electron is $m_e \approx 9.1094 \times 10^{-31}$ kg, while proton weighs $m_p \approx 1.6726 \times 10^{-27}$ kg and neutron $m_n \approx 1.6749 \times 10^{-27}$ kg. Thus, the difference between $m_e$ and $m_p$ is about four orders of magnitude. This very large difference in masses means that electrons move much faster than the nuclei and if the nuclei moved / are displaced, the electrons respond my adjusting almost instantaneously. For the same reason, the opposite is not true: the nuclei are not influenced by the motion of the electrons and they can be seen as remaining fixed from the electrons' perspective. This allows the separation of motions to electronic and nuclear, that is, they are treated as independent of each other. This is called the *Born-Oppenheimer approximation*. It was originally proposed by [Max Born](https://en.wikipedia.org/wiki/Max_Born) and [J. Robert Oppenheimer](https://en.wikipedia.org/wiki/J._Robert_Oppenheimer) in their article titled *Zur Quantentheorie der Molekeln* in 1927.
# 
# #### Born-Oppenheimer molecular dynamics
# 
# First the positions of the nuclei are assumed to be fixed and the Schr�dinger equation is solved under this assumption, resulting the energy states of the electrons. Then the Schr�dinger equation is solved for the nuclear motion by using the electronic ground states are used as the potential energy. 
# 
# #### Relation to classical molecular dynamics
# 
# When developing a force field for the classical representation of atoms the Born-Oppenheimer approximation to the potential energy with respect to the nuclei can be seen as the function representing the potential and the electrons as implicit variables of the potential. By treating the atoms in a classical way, computation time is saved and larger systems can be simulated for a longer time span. So in classical MD a coarse-grained model of an atom is used, where the nucleus and the electrons are combined in one particle.
# 
# This is also the basis of classical molecular dynamics.
# 
# #### Relation to other fields
# 
# - Spectroscopy
# 
# #### More detailed view of the BO approximation
# 
# 
# 

# ### Kohn-Sham Equations
# The electronic Schrödinger equation within the Born-Oppenheimer approximation, eq. 3.3 is not exactly solvable because of electron-electron interactions.
# Several quantum chemistry approaches have been proposed in order to solve it.
# Methods include Hartree [73], Hartee-Fock [74], configuration interaction [75]
# method, variational Monte Carlo [76, 77], etc. which are based on optimizing
# many-body wave-functions. These methods severely suffer from the dimen-
# sionality bottleneck as the computational cost grows as ∼ N4−6 with system
# size N. Furthermore, exchange and electron correlations are not considered in
# the Hartree method. Electron correlations are not included in Hartree-Fock
# method, however, the exchange effects are included in terms of a single Slater
# determinant to account for the Pauli exclusion principle. All these approaches
# aim to predict and explain experimental measurements and, therefore, one
# needs to calculate the expectation values of observables. For this the know-
# ledge of the full wave-function is not mandatory [68, 69, 70, 71].
# DFT is based on the original works of Hohenberg and Kohn [38, 37] in
# which they indicate that all the information of the correlated many-body
# system can be described as a functional of the ground state density. The
# Hohenberg-Kohn theorems [38, 37] for a system of N interacting fermions are
# the following:
# 
# 1. There is a one-to-one correspondence between the ground state density
# n0(r) and external potential Vext(r) applied to a system of interacting
# fermions.
# 2. The energy of a system of interacting particles is a universal functional
# of its density n(r), E[n(r)], and the exact ground state energy of thesystem is the global minimum of this energy functional.

# ### Density Functional Theory in Practice
# 
# <table class="lblue" style="float: right" width="680">
#   <tr>
#     <td>
#        <img src="./img/kohn-sham-sc.svg" width="680px" />     
#      </td>
#     </tr>    
#     <tr>
#      <td colspan="1">
#          Figure: Some common computer simulation methods and typical their time scales. Rough idea of systems sizes in terms of atoms and lengths is given when appropriate. The typical time steps in classical molecular dynamics and coarse-grained MD are also shown.
#      </td>
#    </tr>
# </table>  
# 
# 3.6.1 Norm-conserving pseudopotential
# There is another term in the KS Hamiltonian which includes the electron-
# nuclear Coulomb interactions and this is Vext(r). Electron-nuclear Coulomb
# interactions are singular near the nuclear core. However, core electrons are
# localized around each atom and they have a weak interaction with the core
# electrons of other atoms. Therefore, the external potential generated by the
# core electrons behave like a nucleus core. One can replace the external po-
# tential of the original all electron problem, including those of nucleus and the
# core electrons by a smooth non-singular potential known as pseudopotential
# which only acts on the valence electrons. Then, the Kohn-Sham calculations
# become limited to valence electrons
# 
# Once core electrons are removed, pseudo wave-functions are nodeless in the
# core region (no zero in the core region) and outside that region the pseudopo-
# tential and pseudo wave-functions are the same as the all-electron ones. An
# empirical or a semi-empirical pseudopotential is based on fitting the effective
# potential or its ionic components to empirical data and is not transferable to
# different chemical environments. Norm conserving pseudopotential is a set
# of ab initio pseudopotential that are not fitted to experimental data and are
# transferable. Such a pseudopotential is constructed to satisfy the following
# conditions [69]:
# 1. The eigenvalues resulting from the pseudopotential are identical to the
# all-electron eigenvalues.
# 2. Outside a cut-off region the pseudopotential is equal to the all-electron
# potential.
# 3. Outside the cut-off region the pseudo wave-function is the same as the
# all-electron one. At the cut-off the logarithmic derivatives of pseudo
# wave-function and the all electron one is the same.
# 4. Inside the cut-off region the charge from pseudopotential calculations
# and all-electron calculations coincide.
# The cut-off region controls the accuracy of the pseudopotential. The pseudo-
# potential is more transferable if the cut-off is smaller [69].
# By removing the core electrons a considerable part of total energy is dis-
# regarded and hence only differences in total energy due to the valence charge
# readjustment are meaningful in pseudopotential calculations [68, 69, 88].
# 
# 
# 

# Basis sets
# By choosing the appropriate exchange-correlation functional and pseudopoten-
# tial, HKS is defined and one can solve the Kohn-Sham equations numerically.
# For this purpose one needs to use a set of basis functions in order to represent
# the single-particle wave-functions. The basis functions are chosen depending
# on several factors, e.g. ease of implementation, computational cost, precision
# and geometry of the system [88]. In general the basis sets are either local-
# ized in k space, like the plane-wave basis, or localized in real space. In this
# work [48, 49], we employed Gaussian basis sets. Accordingly, we restrict our
# discussion to Gaussian basis sets.
# Gaussian functions are localized in Fourier space and real space. Gaussian
# orbitals either can be given in polar coordinates or Cartesian coordinates as

# In[2]:


m_ele = 9.1094*10**(-31)
m_pro = 1.6726*10**(-27)
m_neu = 1.6749*10**(-27)
ratio = m_ele/m_pro
print(ratio)

