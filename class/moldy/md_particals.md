# Molecular Dynamics: How it is done

This module focuses on  particle simulations using the molecular dynamics (MD) method. The aim is to learn the what particle simulations and MD are, and what can be done with them. MD is mainly used in physics, chemistry, chemical engineering and pharmaceutical research. It is, however, a versatile method and has found use in many other fields as well. 
As this is an introduction to particle simulations, the aim is not to provide  complete description, but rather to be practical in the sense that basic concepts and terminology are introduced. 



````{panels}
:column: col-lg-12 p-2

```{image} ../../gallery/dmpc-headgroup.png
:alt: VMD
:class: bg-primary
:width: 250px
:align: right
```

**Learning goals:** 
- To be able to program time dependent simulations. Here, we use molecular dynamics as the simple example
- To learn how particle simulations are done.
- To learn how to generate and handle data.
- To understand the importance and utility of visualizing time-dependent data.

**Keywords:** Particle simulations, molecular dynamics, data analysis

````


<hr>
 
 
MD is the evolution of Newton’s equations motion in time. 
In short, the problem is simlpy to solve numerically F=ma.


It is important that energy conservation is fulfilled, i.e., E=T+V. This may look trivial, but that is not the case. When we solve the equations of motion numerically, we are hampered by practical problems. For example, integration method has to be selected carefully and the potential energy of needs to be truncated for distance shorter than some cutoff radius.

## The basics

Pick particles, masses and potential (i.e. the forces)

Initialize positions and momentum. (boundary conditions in time)

Solve  F = m a  to determine r(t), v(t).

Compute properties along the trajectory

Estimate errors.

Try to use the simulation to answer physical questions.


Also we need boundary conditions in space.  
Real systems are not isolated!
What about interactions with walls, stray particles?
How can we treat 1023 atoms?


## Newtons equation of motion

## Integration of the equation of motion

## Pseudocode for molecular dynamics

```
program MolDy
call initialize
do i=1,nmax
	call force
	call integrate
	call observables
enddo
end program MolDy
```

Pick particles, masses and potential (i.e. the forces)

Initialize positions and momentum (boundary conditions in time)

Solve  F = m a  to determine r(t), v(t).

Compute properties along the trajectory

Estimate errors.

Try to use the simulation to answer physical questions.


Potentials are highly non-linear with discontinuous higher derivatives either at the origin or at the box edge. 

Small changes in accuracy lead to totally different trajectories (the mixing or ergodic property). We cannot use long-time information.

We need low accuracy because the potentials are not very realistic. Universality saves us: A badly integrated system is probably similar to our original system. This is not true in the field of non-linear dynamics or, in studying the solar system. 

CPU time is totally dominated by the calculation of forces.  We do not want to compute higher-order derivatives.

Memory limits are (often) not too important.

Energy conservation is important; roughly equivalent to time-reversal invariance: Allow 0.01kT fluctuation in the total energy. 

## Reduced units vs physical units

$$
u^* = u /\epsilon
$$

$$
\rho^* = \rho \sigma^3
$$

## Forces

## Integration of the equations of motion

### Euler



### Verlet and velocity-Verlet

## A few words of warning

## What is conserved and what is not

## Visualization

## Data analysis



## Summary

This section introduced a number of concepts related particle modelling. In the next sections, we will make these concepts more quantitative and put them into practise when we set up and analyze simulations and simulation data.

## Bibliography

```{bibliography} ../../references.bib
    :filter: docname in docnames
    :style: plain
```
