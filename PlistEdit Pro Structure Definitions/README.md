# Autopkg Recipe Structure Definition for PlistEdit Pro

With [AutoPkg](https://github.com/autopkg/autopkg) and [Munki](https://github.com/munki/munki) you are juggling property list files all the time. Sometimes using a text editor is the best choice, other times you want a graphical representation of the property list. Xcode can be used for that, but launching Xcode for a humble plist always seems overkill… and slow. My preferred tool of choice for this is [FatCat Software’s PlistEdit Pro](https://www.fatcatsoftware.com/plisteditpro/).

[AutoPkg recipes have a well defined format](https://github.com/autopkg/autopkg/wiki/Recipe-Format). Creating them from scratch in an editor can be boring and error prone. PlistEdit Pro offers [a feature called ‘Structure definitions’](https://fatcatsoftware.com/plisteditpro/Help/property%20list%20structure%20definitions.html) which… well… allows you to define the structure of a property list. Best thing is you can create your own, though the documentation on their website is a bit outdated.

## Installation

If you want to do this, use this definition file and put it in ~/Library/Application Support/PlistEdit Pro/Structure Definitions. Then restart PlistEdit Pro. Finally, go to “Preferences > Definitions”, select the “AutoPkg Recipe” in the list and add ‘recipe’ as a file extension.

## Usage

Now when you open a .recipe file, it will know to use this definition. This will help with some steps of managing recipes. For example when you create a new element in the Process array, it will automatically be set to be a dict and pre-filled with a Processor string element and a Arguments array element. It will also warn when you try to delete mandatory elements.

When you create a new empty file and change the definition from the ‘Definition’ menu, it will pre-fill your new file with the right keys for a recipe. Enjoy!
