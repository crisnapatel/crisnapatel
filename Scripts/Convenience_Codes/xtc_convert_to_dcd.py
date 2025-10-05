# Convert xtc to dcd formate

# Import the MDTraj library
import mdtraj as md

# Load every frame from the .xtc file along with the corresponding topology file (.gro, .pdb, etc.)
trajectory = md.load('nvt.xtc', top='nvt.gro', stride=1)

# Create an atom slice for indices 1 to 968 (or use a selection string)
subset_traj = trajectory.atom_slice(range(1, 968))  # or use trajectory.topology.select("resname GRA")

# Save all but the last frame of the subset trajectory in .dcd format
subset_traj[:-1].save_dcd('nvt_subset.dcd')

# Save the last frame as a PDB file for topology
subset_traj[-1].save_pdb('nvt_subset.pdb')

# That's it! Your .xtc file has been converted to .dcd with stride and atom selection, and a PDB file has been created for topology.

