# VMD selections


VMD has very powerful tools for selecting atoms and molecules based 
on a number of different criteria. Here is a brief summary.


## Name, residue etc.-based selection


| COMMAND  | EXPLANATION |
|---------|-------|
|<img width=400/>|<img width=300/>|
| `name CA` | select all $\alpha$-carbons |
| `name CA and resname ALA` |  select all $\alpha$-carbons in ALA residues|
| `resid 35` | |
| `resid 35 to 40` | |
| `backbone not protein` | |
| `name "C.*"` | |

## Distance-based selection

Note: In VMD distances are measured in Å. In Gromacs, for example, distances 
are measured in nanometers.

| COMMAND  | EXPLANATION |
|---------|-------|
|<img width=400/>|<img width=300/>|
| `z < 6 and z > 3` ||
| `within 5 of name FE` ||
| `protein within 5 of nucleic` ||
| `water within 3 of protein` ||

## Mass-based selection

| COMMAND  | EXPLANATION |
|---------|-------|
|<img width=400/>|<img width=300/>|
| `mass < 5` ||

## Charge-based selection

| COMMAND  | EXPLANATION |
|---------|-------|
|<img width=400/>|<img width=300/>|
| `abs(charge) > 1` | |

## Bond-based selection

| COMMAND  | EXPLANATION |
|---------|-------|
|<img width=400/>|<img width=300/>|
| `numbonds = 2` ||



Alpha carbons
Residue 35
Residues 35–40
Alanine alpha carbons
Protein backbone atoms
Any atom not in a protein
Carbon atoms
Atoms heavier than 5 a.u.
Atoms bonded to 2 other atoms
Atoms with a large net charge
Atoms between 3 and 6 Å in z
Atoms within 5 Å of iron atoms
Protein atoms close to nucleic acids
Water close to proteins


## Selection in one frame vs in every frame of a trajectory

## Periodic boundaries: Lines/bonds all over the place

–Atoms are bonded across periodic boundary conditions (PBC).
–Trajectory post-processing is required to make molecules whole.


## More information

https://docs.computecanada.ca/wiki/VMD
