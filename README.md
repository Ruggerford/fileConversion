# Background
(why do this in the first place?)
- I wrote many Matlab programs at Uni, and I didn't want to loose the knowledge I got from them even though I no longer have Matlab.
- I want to import them into Obsidian so that it is easy to reference them.

# Problem
Moving them one by one is very slow and they need appropriate header info for Obsidian to organise them correctly, so I can't just bulk rename them.

# Goal 
- Edit text files to add a header and save them with a different extension

# Approach
- Load each (text-based) file in a given folder one after another
- Add a header and footer to each file
- Save each file in a new folder with the specified new extension
- User can then move the new files directly into Obsidian
