# Lab 2, part 2/2: Visualization of molecules using VMD


**The tasks below are part of Assignment 3. You can download it from OWL.**


Create yourself a work directory (name it as you please; it may be good to put it under the course directory that you have already created and to use a descriptive name for the subdirectory). 

1. Visualizations for the human islet polypetide are shown in Fig. 1.5 in the lecture material. Download the corresponding PDB file and try to recreate the visualizations as closely as possible. Which ones are the most informative? Use Tachyon rending to produce a high-quality image as discussed in the VMD section.

**For tasks 2-5 do the following:** The VMD section of lecture material contains an example of `.gro` file that contains 5 water molecules.

Create yourself a work directory (name it as you please; it may be good to put it under the course directory that you have already created and to use a descriptive name for the subdirectory) for this part  and create a file called `spc5.gro` in there. 

Once done, open the file in VMD. If you encounter problems, first examine very carefully that the file is exactly in the format as given in the example. 

2. Try to recreate the visualization shown in the lecture notes in connection with the file (Inside the Example of the .gro format tab). For this, you will have to try different representations for the molecule. Then render the molecule. Use Tachyon rending to produce a high-quality image as discussed in the VMD section.

3. Color each of the oxygens with a different arbitrary color and render.

4. Use a different representation for each of the water molecules and render. 

5. List all the residue names, names and elements present in the system.

6. Examine the keywords `residue` and `resid`. What is the difference between them?


<!--

Load from 


1. Load the file `dmpc128-200ns.gro`

Create a high resolution rendering (1024 x 1024 px) of the system with the following specifications:

- Show the headgroup phosphorous and nitrogen atoms using van der Waals representation
- Show the water molecules that are closer than 0.5 nm from the phosphate atoms using CPK representation
- Show all the carbons (the hydrocarbon tails of the lipids) using line representation and gray color. 
- Show all the oxygens except the water oxygens using van der Waals representation
- Show lipids number 1 and 128 in licorice representation

Note: You may want to tune the size of vdW and CPK atoms for clarity and rotate the scene such that all of the above features are illustrated

The quality and clarity of the representation will be part of the evaluation.



1. Load a trajectory for the `.gro` file. 

- In `Graphical Representations`, select the representation you have and turn off displaying waters (speeds up the process)
  ```
  Selected Atoms -> not water
  ```
- Activate the molecule dmpc128-200ns.gro in the `VMD Main` window by clicking it.
- Then load the trajectory (`.trr`) file for the `.gro` file:

```
File -> Load Data Into Molecule -> Browse -> dmpc128-200ns.trr -> Load
```

Notice the selector at the bottom of the `VMD Main` window for `Loop`, `Once`, `Rock`

Load the file dmpc128-200ns.gro


-->
