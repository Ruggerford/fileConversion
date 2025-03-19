# Background
(why do this in the first place?)
- I wrote lots of Matlab programs at Uni, and I didn't want to lose the knowledge in them even though I no longer have Matlab.
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

# Notes
- This program isn't limited to just converting Matlab to markdown files. By swapping a few values, you could probably convert pretty much any text-based file into another text-based file.
- I am fully aware that there are far more robust programs that already exist to do this task.
- This was just a hobby project to help me to learn python, and it succeeded in converting the files I wanted it to.
- Use at your own descretion, I am _very_ unlikely to fix any issues.
