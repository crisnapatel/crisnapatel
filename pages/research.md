---
layout: page
title: Research
permalink: /research/
description: "Overview of Krishna Patel's molecular dynamics research at IIT Delhi."
subtitle: "Molecular simulations for energy storage and soft matter."
---
## Current focus areas

I explore how nanoscale interactions influence emergent properties of polymers and carbon-based materials. The themes below capture my ongoing and near-term work.

### Polymer–graphene interfaces in solution
- Quantifying changes in chain conformation (radius of gyration, end-to-end distance) for polystyrene oligomers in toluene.
- Comparing NVT and NVE ensembles to understand equilibration pathways near graphene and graphene-oxide surfaces.
- Designing reproducible GPU-enabled LAMMPS workflows and validation steps.

### Hydrogen adsorption on modified carbon allotropes
- Studying oxidation, decoration, and curvature effects on graphene and CNTs for gravimetric/volumetric capacity.
- Combining grand canonical Monte Carlo insertion with post-run energy decomposition in Python.
- Validating force fields (ReaxFF, AIREBO) against available experimental observables.

### Simulation automation and analysis
- Building analysis pipelines with MDAnalysis, pandas, and OVITO for stress–strain and adsorption metrics.
- Maintaining reusable templates for job submission on IIT Delhi HPC clusters (MPI and CUDA builds).
- Creating RAG-style knowledge bases to search simulation logs and literature.

## Selected collaborations & support
- Schrödinger Institute scholarship for *Molecular Modeling for Materials Science Applications: Organic Electronics* (Oct 2023).
- Internal collaborations with the Soft Matter Lab, IIT Delhi.

## Resources for collaborators
The following helper scripts reside in the repository under `assets/scripts/`. They are shared as-is for colleagues and students.

| Script | Purpose |
| --- | --- |
| [RenamePDF.py]({{ '/assets/scripts/convenience/RenamePDF.py' | relative_url }}) | Rename downloaded PDFs to their embedded titles for quick literature triage. |
| [gpu_usage.py]({{ '/assets/scripts/convenience/gpu_usage.py' | relative_url }}) | Capture and plot GPU utilization while benchmarking GROMACS runs. |
| [plot_lammps_log_file.py]({{ '/assets/scripts/convenience/plot_lammps_log_file.py' | relative_url }}) | Generate thermodynamic trend plots directly from LAMMPS log files. |
| [xtc_convert_to_dcd.py]({{ '/assets/scripts/convenience/xtc_convert_to_dcd.py' | relative_url }}) | Convert trajectories between XTC and DCD formats for cross-tool analysis. |
| [MD tools JSON]({{ '/assets/scripts/md-related/MD_related_Codes.json' | relative_url }}) | Metadata list of domain-specific utilities maintained for MD projects. |

If you reuse these materials, please double check dependencies and adapt paths to your environment.
