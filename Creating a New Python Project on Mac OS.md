
# Creating a new Python project on MacOS

## Assumptions

This note assumes that both Python and VSCode are installed.

Confirm the presence of VSCode using Spotlight Search - start entering "Visual" and you should see Visual Studio Code as a choice. If it is not present, follow the direction found [here](./Installing%20Python%20on%20Mac%20OS.md).

Confirm the presence of the right version of Python by entering the Terminal and typing:

```text
python3 --version
```

You should get something like:

```text
Python 3.7.5
```

If you do not, follow the same link given above.

## Creat a new directory

### From finder

Upon opening a Finder window, you should be in your home directory. Click the "Action" gear. Click on "New Folder" and give the new folder a name. Try to avoid spaces, using underscores or dashes instead.

### From Terminal

Upon opening a Terminal window, you should be in your home directory. Type: 

```text
mkdir chooseafoldername
```

Try to avoid spaces, using underscores or dashes instead.

## Open VSCode

Use Spotlight Search, or click the VSCode icon in the Dock. From the Terminal (if you added the appropriate `alias` type: `code`.

## Open the folder you made

Select menu File --> Open... This command can also be executed by hitting `⌘o` (using the keyboard is typically faster than using the mouse or trackpad).

Navigate to the folder you created above and click "Open".

## Create a new Python file

This assumes you need to create a new Python file. If the one you want to edit already exists, double click on it after exposing the Explorer (potentially by clicking the top left icon).

To create a new file, you can either do File --> New File or `⌘n`.

Type `#` just to get something in the file. The octothorp introduces a Python comment. Anything past the octothorp is ignored by Python.

Hit 	`⌘s` to save the file or select File --> Save. Specify the name of the file - end with `.py`.

If this is the first Python file you've ever made, a dialog will appear in the bottom right of the window. It will say "The \'Python\' extension is recommended for this file type." Click the button that says "Install"

After the install is complete, you will get two new dialogs. The one that begins with "Tip" you can simply click "Got It!"

The remaining dialog says "Linter pylint is not installed." Click Install. Some warnings will be generated. Ignore them.

Down in the bottom left of the VSCode window it should say "Python 3.7.5 64-bit". The actual number may be different but it *must* begin with **3**.

 


> Written with [StackEdit](https://stackedit.io/).
