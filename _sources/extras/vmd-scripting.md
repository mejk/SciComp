# VMD scripting

Tcl/TK

Python

## What is Tcl/Tk

## Tk console

It is available under `Extensions`.

## Running scripts

Calling a script from the tcl/Tkwindow:

% source <script file>

•From command line:

>> vmd–dispdevtext <coordinate file> <topology file> < <script> [&> <log file> &]

## VMD specific commands

atomselect top {name “[O.*]”}
measure center
measure minmax
measure rgyr
measure sasa
measure angle/bond/dihed

## Dynamical

proc do_time {args} {
     display_time_bar 1.0 50.0 "fs" 0
	 }
set mol [molinfo top]
trace variable vmd_frame($mol) \
w do_time



## Colorization shall indicate deformation of C60 molecules

- [Kohlmeyer](http://www.jncasr.ac.in/ccms/sbs2007/lecturenotes/6day12nov/vmd-advanced.pdf)
- [From RUB](http://www.theochem.rub.de/~legacy.akohlmey/cpmd-vmd/part1.html)


set mol [molinfo top]
set left  [atomselect $mol {index < 60}]
set right [atomselect $mol {index>= 60}]
set nf [ molinfo $mol get numframes ]
for {set i 0} {$i < $nf} {incr i} {
$left frame $i
set com [measure center $left]
set dlist ""
foreach c [$left get {x y z}] {
lappend dlist [veclength [vecsub $c $com]]}$left set user $dlist# repeat for second molecule...
}
