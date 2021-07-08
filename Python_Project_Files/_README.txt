***CRISPR File Generator***

**How to**
-Open the Python_Project_Input.csv file
-Fill in the 2 fields
	--The Gene you want to target and generate files for
		---Please give the gene name by its designated 4-digit genome number
			i.e. if the gene is notated as either Kpha#### or GQ67_0####,
			then just report the #### portion. Otherwise, the gene won't be located!
	--The resistance marker you want in the R-Vector plasmid file
		---This Column takes ONLY the abbreviated inputs "kan", "nrs", and "zeo" without the quotes

-Run the script
	--fill in the prompted inputs appropriately
		*NOTE the active directory should be the folder in which you've stored all of the files for this program.
		i.e. C:\Users\User\Desktop\Python_Project_Files for a Windows System
	 	    /Users/User/Desktop/Python_Project_Files for a Unix System
		*NOTE the Output Directory is the folder in which you want all output files to be stored on your system. 
		Make sure this location exists prior to running the program, it will not create the direcotry.
		Make sure all directories are copied and pasted carefully, or the program will crash!

-Wait as the magic happens
	-- in the designated Output Directory, folders will be created and filled for each target Gene.
		These folders will contain the R-Vector plasmid Genbank Files, the deathstar ins Genbank files,
		and the list of primers that will need to be ordered.

-Order your primers. Not part of the program, just don't forget.
	