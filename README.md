CONTENTS OF THIS FILE
--------------------------

	- Introduction
	- Requirements
	- Configuration
	- Instructions
	- Troubleshooting


INTRODUCTION
-----------------

	This authorship program is run to analyze multiple text files and return the closest approximation for the author of the file. The program is launched by running the main file using python3. The main file for this document is TextAnalysisMain.py. 


REQUIREMENTS
-----------------

	This program requires the following modules to run:

		- python 3.5
		- pandas
		- numpy
		- matplotlib
		- sklearn


CONFIGURATION
------------------

	The user interface module is enabled when the main file, TextAnalysisMain.py, is run. 
	The user will be prompted to enter the number of files he/she will be analyzing. 
	This number will affect the user interface that is displayed. Disabling the module by closing the python file will result in the program ending and a return of None.


INSTRUCTIONS
----------------

	To run this program:

		- Run TextAnalysisMain.py with Python3

		- The program will prompt the user to enter the number of files that he/she wishes to analyze
			- Enter a number greater than zero to represent the number of files you want analyzed

		- The user interface will launch

		- All document text entries should be filled in with document names in the .txt format

		- The year and genre text entries are optional to fill in
			- Year should be filled in with an int representing the year of the document
			- The genre should be filled in with text depicting the genre of the document

		- The Text Filters text entry can be filled in with filters that you would like applied to each document
			- Filters should be listed in the order they are to be applied to the document
			- Filters should be entered exactly as designated, separated by commas, with no spaces anywhere
			- Available Filters:
				- "normalizeWhitespace"
				- "normalizeCase"
				- "stripNullCharacters"
				- "stripNumbers"
				- "stripCommonWords"
			- For Example: 
				To normalize white space, then strip numbers, and then strip null characters, enter:
					"normalizeWhitespace,stripNumbers,stripNullCharacters"

		- The check boxes can be checked if you would like the respective functions to be carried out on each document

		- The final step is to click the button corresponding to the analysis method you would like to use to analyze the documents


TROUBLESHOOTING
----------------------

	* If the appropriate number of text inputs does not appear after entering the number of files, check the following:

		- Was the user input a number?
		- Was the number entered greater than zero?

	* If the documents are not assigned the correct year, check the following:

		- Was the input a number?

	* If the documents are not filtered correctly, check the following:
		
		- Were the filter names spelled correctly?
		- Were there any spaces in the text? There should no be any.
		- Were there commas between each filter name? There should be one comma between each filter.
