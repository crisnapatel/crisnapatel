---
layout: page
title: Tools & Scripts
description: "Collection of practical Python, Perl, and Bash scripts for molecular dynamics simulations and data processing."
permalink: /tools/
---

A curated collection of scripts and tools I've developed to streamline molecular dynamics workflows. Each tool is designed to solve specific challenges in MD simulation data processing and conversion.

## [Pragrammatic Interaction](https://github.com/crisnapatel/Pragrammatic-Interaction)

A comprehensive repository of utilities for MD simulation data processing and conversion. All scripts are open-source and contributions are welcome.

### Data Parsing & Analysis

**LAMMPS Log Parsing**
- Extract thermodynamic properties from LAMMPS simulation logs
- Jupyter notebook for interactive analysis
- Returns data as pandas DataFrames for easy downstream processing
- Handles multiple files and property filtering
- [View on GitHub →](https://github.com/crisnapatel/Pragrammatic-Interaction/tree/main/lammps_log_parsing)

### Format Conversion

**XSD to LAMMPS Data File Converter**
- Convert Materials Studio XSD files to LAMMPS data format
- Extracts atoms with coordinates, charges, and element types
- Automatically detects and preserves bond connectivity
- Handles complex bond types based on atom elements and bond order
- Batch conversion utility for high-throughput workflows
- [View on GitHub →](https://github.com/crisnapatel/Pragrammatic-Interaction/tree/main/XSD_to_LAMMPS_Converter)

**Trajectory Export Tools**
- Perl scripts for converting Materials Studio trajectory files to LAMMPS dump format
- Export full trajectories or specific atom sets
- Output compatible with OVITO and other visualization tools
- Supports Materials Studio 2020.1v forcite trajectories
- [View on GitHub →](https://github.com/crisnapatel/Pragrammatic-Interaction/tree/main/trajectory_export)

### HPC & Simulation Management

**HPC Utilities**
- Scripts optimized for high-performance computing environments (IIT Delhi HPC)
- LAMMPS simulation management and monitoring tools
- Job submission templates and automation scripts
- [View on GitHub →](https://github.com/crisnapatel/Pragrammatic-Interaction/tree/main/hpc_iitd)

**Log Visualization**
- Streamlit-based interactive app for visualizing LAMMPS simulation data
- Real-time monitoring of simulation progress
- [View on GitHub →](https://github.com/crisnapatel/Pragrammatic-Interaction/tree/main/lammps_log_reader_streamlit_app)

---

## Requirements

- Python 3.x with pandas
- Perl 5.x (for some trajectory conversion tools)
- LAMMPS (for generating and analyzing log files)
- OVITO (optional, for trajectory visualization)

## Getting Started

Each tool has its own README with specific usage instructions and examples. For detailed documentation, visit the [main repository](https://github.com/crisnapatel/Pragrammatic-Interaction).

## Contributing

Found a useful script? Have improvements? Contributions, bug reports, and feature requests are welcome on GitHub!
