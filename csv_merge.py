#!/usr/bin/python
#############################################
#  Script to merge multiple csv files       #
#  Author: DDD Team                         #
#  version 1.0                              #
#############################################

import pandas as pd, argparse, glob, os.path, sys

# Arguments for the source and destination folders
# To be specified by the user

parser = argparse.ArgumentParser(description='Script to Merge unique columns from multiple csv Files')
parser.add_argument("input", help='SOURCE_FOLDER_PATH')
parser.add_argument("output",help='DESTINATION_FOLDER_PATH')
args = parser.parse_args()

## Validate the Source & Destination folders exist
## Read the raw csv files
## Validate to ensure the files exists and are readable
if os.path.isdir(args.input) and os.path.isdir(args.output):
	files =  glob.glob(args.input + "/*.csv")
	if not files:
		sys.exit("No csv files exists in [%s]"% args.input)
	else:		
		for file in files:
			if os.access(file, os.R_OK):
		  		csv_list = [pd.read_csv(file, keep_default_na=False, na_values=[""]) for file in files]
		  		combined_csv = pd.concat(csv_list, axis=1)
		  		combined_csv.to_csv(args.output + '/Combined.csv')
		  		file_with_no_duplicates = combined_csv.T.drop_duplicates().T
		  		file_with_no_duplicates.to_csv(args.output + '/Expected_results.csv')
		  	else:
		  		sys.exit("File [%s] not readable" %file)
else:
	print "Either paths [%s] and/or [%s] is not existing!"% (args.input,args.output)

      # Write the trimmed output into path specified
