# MATLAB to Markdown file converter

# Loads each (text-based) file in folder one after another
# Adds a header and footer to each file
# Saves each file in a new folder with the specified new extension
# Ready to be copied into Obsidian

# Import necessary modules
import os

# Define the filepath to the relevant folders
oldfilefolder = '/.../Aa_processingFolder/' # (replace with actual filepath)
requiredFileExtension = '.m' # use TRUE if you don't care

newfilefolder = '/.../Aa_processingFolder/processCompleted/' # (replace with actual filepath)
newFilePrefix = 'matlab_' # add this to the beginning of the new filename
newFileExtension = '.md'

# Define the headerTxt to be added at the top of each file (in this case, metadata and formatting for Obsidian)
# headerTxt = ''
headerTxt = """---
backlinks:
- "[[matlab coding]]"
tags:
- codepage
- codingmatlab
---
# Description:

# Code:
```matlab

"""

# Define the footerTxt to be added at the bottom of each file
# footerTxt = ''
footerTxt = """

```
"""

# Get all items in the directory (files and folders)
for filename in os.listdir(oldfilefolder):
    # Get the old file path and the new filepath
    oldpath = oldfilefolder + filename
    [filename_noExt,oldExt] = os.path.splitext(filename)
    newFilename= newFilePrefix + filename_noExt + newFileExtension
    newpath = newfilefolder + newFilename
    print('-----------')
    print(oldpath)
    print(newpath)
    
    # Check if the item is a file & that the file ends with the required extension
    if os.path.isfile(oldpath) & (oldExt == requiredFileExtension):
        print(oldpath)
        # Open the file in read mode
        with open(oldpath, 'r') as fread:
            # Read the lines of the file
            content = fread.readlines()
        
        # Add the headerTxt & footerTxt to the content
        new_content = [headerTxt] + content + [footerTxt]
        
        # Write the modified content back to the file
        with open(newpath, 'w',) as fwrite:
            fwrite.writelines(new_content)
        
            
print('Conversion complete.')
