# Taxonomic breakdown using World Register of Marine Species

This is a simple python script that reads a CSV file written with a list of species, requests the unique identifier AphiaID from the World Register of Marine Species (WoRMS) and returns a taxonomic breakdown of the species. This is finally stored in a Pandas dataframe that is written into a csv file. 


## How to run this script  
The script to run is named ``worms_taxa.py``. The structure of the repository has a folder named *files* in which csv files are stored for reading and writing. The desired list of species can be copied in this folder and  the *sample_data.csv* name in the script should be changed. 

A sample data file is included to test the script. It consists of a single row with a header and nine different taxa (species, genus, family).