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
