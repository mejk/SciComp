
# Quantum level methods

````{panels}
:column: col-lg-12 p-2

**Learning goals:** 
- Basic terminology of quantum simulations

**Keywords:** Density functional theory (DFT), *ab initio*, electronic structure, Sch\"ordinger equation, force field, interactions, Car-Parrinello, Born-Oppenheimer, semi-empircal methods

<!--
**Associated material:** Cheat sheet of the most common Linux commands.
-->

````

```{epigraph}
“All that glitters may not be gold, but at least it contains free electrons.”

-- John Desmond Bernal (Irish physicist) in a Lecture at
 Birkbeck college, University of London, 1960.
 ```

## Background

### Schr\"odinger equation

\begin{equation}
i \hbar \frac{\partial}{\partial t} \Psi (\vec{r}, t) =
\left[
- \frac{\hbar^2}{2m}\nabla^2 + V(\vec{r},t)
\right] \Psi(\vec{r},t)
\end{equation}


\begin{equation}
\left[
- \frac{\hbar^2}{2m}\nabla^2 + V(\vec{r})
\right] \Psi(\vec{r})
= E \Psi(\vec{r})
\end{equation}


## Geometry optimization

## Born-Oppenheimer molecular dynamics (BOMD)

## Car-Parrinello molecular dynamics (CPMD)

The method is due to two Italian physicists, [Michele Parrinello](https://en.wikipedia.org/wiki/Michele_Parrinello) and [Roberto Car](https://en.wikipedia.org/wiki/Roberto_Car) who published the method in their article titled *Unified Approach for Molecular Dynamics and Density Functional Theory* in 1985. Parrinello is also known for the [Parrinello-Rahman barostat]() (with [Aneesur Rahman](https://en.wikipedia.org/wiki/Aneesur_Rahman)) and [Metadynamics](https://en.wikipedia.org/wiki/Metadynamics) (with [Alessandro Laio](https://people.sissa.it/~laio/).

**More:**

- [Editorial: a tribute to Michele Parrinello: from physics via chemistry to biology](http://onlinelibrary.wiley.com/doi/10.1002/cphc.200500427/pdf)

### Software for CPMD

- CPMD
- CP2K

## Semi-empirical electronic structure methods


### Hartree-Fock methods

### M{\o}ller-Plesset perturbation theory

### Coupled cluster methods

### Configuration interaction methods


<!--

Saad et al:


When it comes to methodology and algorithms, the biggest steps forward were made in the six-ties with the advent of two key new ideas. One of them isdensity functional theory, which enabledone to transform the initial problem into one which involvesfunctions of only one space variablesinstead ofNspace variables, forN-particle systems in the original Schr ̈odinger equation. Insteadof dealing with functions inR3N, we only need to handle functions inR3. The second substantialimprovement came withpseudopotentials.  In short pseudopotentials allowed one to reduce thenumber of electrons to be considered by constructing special potentials, which would implicitlyreproduce the effect of chemically inert core electrons andexplicitly reproduce the properties ofthe chemically active valence electrons .  With pseudopotentials, only valence electrons, those onthe outer shells of the atom, need be considered,e.g., a Pb atom is no more complex than a C atomas both haves2p2valence con£gurations.  This leads to substantial gains bothin memory and areduction of computational complexity.

In the case where the material studied with DFT is in contact with a solvent, which mightalso contain electrolyte, the explicit description of the electrolyte solution can be computa-tionally prohibitive due to the large number of solvent and electrolyte molecules and the needto average over all possible degrees of freedom.  Often, the focus area or the region of interestis the solute, or solid side of the interface, and one only wants to estimate the mean field effectof the electrolytic solution.  Hence, an explicit or discrete representation of the electrolytesolution can be replaced by a dielectric continuum with a continuously varying charge den-sity of the mobile electrolyte ions.  Hybrid quantum-mechanical/continuum solvation modelstreat the solute quantum mechanically and the surrounding solution at a classical continuumlevel.5The quantum problem deals with the determination of the electronic density (ρe) ofa  given  arrangement  of  nuclei  in  the  presence  of  an  external  potential  (ν)  by  solving  theKohn-Sham equations.  The classical problem deals with finding the electrostatic potential(ν) given the total charge density by solving a Poisson-Boltzmann equation (P-BE) (whichincludes  the  charge  density  due  to  mobile  electrolyte  ions).   This  is  a  non-linear  coupledformalism which requires the simultaneous solutions of both equations.

Neese:

In order to predict quantities that can not be measured (example: short lived intermediates that never accumulate enough for experimental studies)•In order to interpret the outcome of experiments (example: complex NMR or EPR spectra)•In order to obtain insight in the regularities of data (example: understand the key factors that contribute to reactivity trends in a series of related molecules)•In order to predict the outcome of future experiments (example: Design of materials - how do i have to change the molecule in order to optimize a given property)•Have fun with computers, study algorithms, approximations and other „inner theoretical reasons to do it“, ..

Popper:

.. but I shall certain admit a system is empirical or scientific only if it is capable of being tested by experience. These considerations suggest that not verifiability but the falsifiability of a system is to be taken as a criterion of demarcation. The logic of scientific discovery (1959).

Neese

The  BO  Hamiltonian  -  despite  its  (apparent)  simplicity  -  is  a  great  achievement:  it describes 99% of all chemistry correctly. Exceptions are: ★The BO Hamiltonian does not contain terms that describe the interactions of nuclei and electrons with external electric and magnetic fields ★ The BO Hamiltonian misses many small terms that are associated with the electron and nuclear spins★ The BO Hamiltonian does assume a point like nucleus ★ The BO Hamiltonian breaks down in situations where the separation of nuclear and electronic movements is no longer well separated. For example in Jahn-Teller systems.★The Born-Oppenheimer Hamiltonian needs to be party replaced or supplemented with relativistic terms if heavy elements are involved.Only   for   the   description   of   more   advanced   spectroscopies,   such   as   EPR spectroscopy,   do   we   need   to   proceed   beyond   the   Born-Oppenheimer approximation


Neese: Partial charges

As (bio)chemists we want to think of „polar groups“ and „partial charges“ and „ionic character“ and all that. Hence, we have a desire to divide the total electron density such that parts of it are „assigned“ to individual atoms. This  is  the  subject  of  „population  analysis“.  It  is  never  unique  and  hence  very many different schemes exist. The easiest is due to Mulliken: NA=PμνAASμνAAμν∈A∑+PμνABSμνABμ∈Aν∈B∑B≠A∑QA=ZA−NARefined Schemes are the „Natural Population Analysis“ (NPA) and the „Atoms in Molecules (Bader)“ Analysis. NOTE: Since partial charges are NOT observables there is no „best“ charge. One should stick to one scheme and then look at trends

Kuhne: Classes of basis sets

Extended basis sets, PW : condensed matter Localised basis sets centred at atomic positions, GTO Mixed (GTO+PW) to take best of two worlds, GPW Augmented basis set, GAPW:  separated hard and soft density domains

-->
