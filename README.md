# ebc-neuro

See neurodocking protocol pdf for detailed descriptions on how to run files.

## File Descriptions:
```
create_configs.py
```
When run in a folder with a PDBQT for each receptor and a PDBQT for the ligand, creates config files (.txt) and a shell script (.sh) to quickly run all files in a SLURM-based supercomputer system. Note that all receptors should have binding pockets around the same area in 3D space since they will use the same grid, so they will likely have to be based on the same template model.
```
compare_sets.py
```
Simple, rather inelegant script to compare outputs of create_configs.py with different settings. Make sure to put both sets in separate folders, then put the script in a folder that contains both folders. Helps calculate if there is a significant difference based on exhaustiveness levels and other settings.
```
read_results.py
```
Script to read output PDBQT files from Autodock Vina and compile docking energies across multiple unique receptors using the same template. Creates a compact CSV file for later data analysis.
```
get_tree.py
```
Creates a radial phylogenetic tree using the NCBI taxonomy database and color-codes it (heatmap) according to binding affinities of the receptor normalized to each other. Input is a csv file with no headings with the first column being the taxonomic ID number and the second being the binding affinity.
```
create_plots.py
```
Simple script to create a boxplot figure with jitter data points to show distribution of binding affinities. Note that data and graph parameters must be entered manually.
