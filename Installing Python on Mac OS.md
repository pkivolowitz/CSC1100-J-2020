
# Installing Python on MacOS

## Terminal

You will be using the MacOS terminal a great deal. It would be best if you glued the terminal to your dock. Use Spotlight Search and enter "terminal" without the quotes. Then, right click on the terminal icon in the dock and select Options → Keep in Dock.

Here is a very brief first taste of using the terminal.

### cd

When you enter the terminal, you are "in" your home directory. Navigating directories will be a critical skill when using the terminal. The "cd" command changes the directory you are "in".

| command | meaning |
| --- | --- |
| `cd` |  cd by itself moves you back to your home directory |
| `cd dir_name` | attempts to change the directory you are "in" to the named directory. |
| `cd ..` | moves you up one directory level |

### pwd

The pwd command "prints the working directory" - i.e. it will print the full path of the directory you are "in" right now.

### ls

The ls command prints a "list" of the current directory OR another file system entity if you specify one.

| command | meaning |
| --- | --- |
| `ls`  | lists the contents of the current directory |
| `ls dir_name`  | lists the contents of the indicated directory |

### ls -l

It is possible to modify the operation of various commands using "command line options". The -l (dash el) option to ls causes it to print its "long" listing - details about the contents such as dates and sizes.

### mkdir

You will need to create new folders / directories. This is done with mkdir.

| command | meaning |
| --- | --- |
| `mkdir new_dir_name`  | attempts to create the indicated directory |

### python

Once Python is installed, you can run a Python program like so:

```python program_name``` or

```python program_name arg1 arg2 ... argn```

## Install brew

### Get / install brew
Copy the following, paste it into the terminal and hit enter.

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

`homebrew` or just `brew` is the Mac's "missing package manager". A package manager is software that makes installing other software easier. Unlike everything you've been sold, sometimes the Mac does NOT make things easier. Kool Aid, a childhood treat best left in childhood.

### Add brew to `path`

Commands that can be run from the terminal can live in many different directories for reasons of organization, for example. To specify where the terminal should look for commands, its maintains a `path`. The path is a list of directories the terminal will examine looking for the program you've asked it to run. The path is a list of directories separated by semicolons. 

The directories to Python must be added to your path.

Upon entering the terminal (recall, you are in your home directory), type the following **EXACTLY**. Any deviation will end in tears.

```vi .profile```

Opens the editor `vi`.

```G```

Goes to the bottom of the file.

```A```

Enters append mode. If you are not at the beginning of a line, hit enter to start a new line.

Copy this next line and paste it into the terminal.

```export PATH="/usr/local/opt/python/libexec/bin:$PATH"```

Enter `ESC` - this is not a word, rather a key on your keyboard typically at the top left. Hitting escape leaves the append mode.

```:wq```

Writes the changes to `.profile` and exits `vi`.

### Install Python

Note that any time `brew` is executed it may choose to update its database. Doing so can take a long time. You'll know it is still working by looking at the title bar of the terminal window. It will change frequently.

```brew install python```

Installing anything can take a long time. Be patient but not too patient. Depending upon your computer, installs can take a long time.

### Verify Python is installed

Enter:

```python3 --version```

A version of Python, if found, will tell you about itself.


