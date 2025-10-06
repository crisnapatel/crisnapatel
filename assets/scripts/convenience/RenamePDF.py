'''
This scripts takes all the pdf in the pwd and renames them according to the title of the pdf found in its metadata
'''

import os
import PyPDF2
import glob
import re



# Get the list of all the pdf files
pdfFiles = glob.glob("*.pdf")

# Iterate over all the pdf files
for filename in pdfFiles:
    # Create a PdfReader object
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # Get document info
    docInfo = pdfReader.metadata

    # Get title of the pdf document
    title = docInfo.title

    # Check if title is present
    if title is not None and title != '':
        # Replace special characters with underscore
        title = re.sub(r'[^\w\s-]', '_', title)
        # Rename the file with title name
        os.rename(filename, title + '.pdf')
    else:
        print(f"No title found for file {filename}, skipping...")

