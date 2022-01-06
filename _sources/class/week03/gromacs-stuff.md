# The index file should contain the groups for which VELACC is computed.
#
# Note: VACFF decays in scales < 1 ps. Output must include velocities and
# be sampled often enough (for example every 10 fs or so). On the other hand
# only a short run (<100 ps is needed; AFTER the system has been fully equilibrated -> best
# to do this after the production run).

# Possible index file:

gmx make_ndx -f dmpc128-autocorr.gro -o P8.ndx

# Some useful options: 
#  -mol: compute VACF for molecules
#  -os (xvg): compute spectrum
#  -P (number): Legendre polynomial of order (number)
#  -fitfn (choice): none (def), exp, axep, exp_exp. Not very useful but can be used to check the data

gmx velacc -f file.trr -s file.tpr -mol -n file.ndx -o vacf.xvg


