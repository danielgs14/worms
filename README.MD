# Taxonomic breakdown using World Register of Marine Species
This is a simple python script that reads a CSV file written with a list of ***animal*** species, requests the unique identifier AphiaID from the World Register of Marine Species (WoRMS) and returns a taxonomic breakdown of the species. This is finally stored in a Pandas dataframe that is then written into a csv file. 

## How to run this script  
The script to run is named ``worms_taxa.py``, placed inside a *scripts* folder. The structure of the repository has a folder named *files* in which csv files are stored for reading and writing. The desired list of species can be copied in this folder and the *sample_data.csv* name in the script should be changed. After running the script, you will get a file named *worms_output.csv* with many columns:

* AphiaID
* url
* scientificname
* authority
* status
* unacceptreason
* taxonRankID
* rank
* valid_AphiaID
* valid_name
* valid_authority
* parentNameUsageID
* kingdom
* phylum
* class
* order
* family
* genus
* citation
* lsid
* isMarine
* isBrackish
* isFreshwater
* isTerrestrial
* isExtinct
* match_type
* modified

You can modify the script to remove columns using pandas to create a data subset if you would rather keep less columns. 

## Test it

A sample data file is included to test the script. It consists of a single row with a header and nine different taxa (species, genus, family).

## Take in mind
* This script is not as efficient as it could be. Going through hundreds of entries can take minutes. For about ~430 taxa, it has taken about 7 minutes. Higher taxonomic ranks like orders and families take longer to process. 

* Some names can return errors like *Holothuria thomasi*, as its accepted name includes the subgenus: *Holothuria (Thymiosycia) thomasi*. After running the script, you will see a list of errors in the console. Look up those names in WoRMS to make sure you are not missing anything. 

* There are names that have changes, like *Chromis atrilobata* now being placed in the *Azurina* genus. The output will have a column named **valid_name** in which you will see the accepted *Azurina atrilobata*. I suggest using this field for any following analytics. 

* Heading and trailing blank spaces can produce errors. Make sure you are adding a word (Echinometridae) or the scientific name correctly (*Arbacia stellata*). As an example, I am adding underscores to where there should not be any blank spaces:
    * *Arbacia__stellata*
    * *Arbacia stellata_*
    * *_Arbacia stellata*