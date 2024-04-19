# Treescriptify-Text
Convert a File containing Tree-like information into TreeScript!

## How To Use
Run the main script with a file name as the first positional argument.

`treescriptify-text <file-name>`

The output is printed to standard out (displayed in the command line output).

#### What you can do with this
1. Pipe the output to a file.
2. Copy the output and paste it where you need to.
3. Look at it to get a clear picture of your directory tree.

## How To Install
You can manually install a release (if you want), or use pip.

`pip install treescriptify-text`

## Types of Valid Input
This will work on commonly encountered tree-like text, such as that produced by the tree command.

It doesn't do anything special to decode the input.
- Infers depth in the tree using the amount of indentation before the file name
- Infers parent directory from depth

### Additional Considerations
If a name in the tree does not contain a file extension, and there is no slash character, it may still be treated as a directory.

### Issues and Contributions
If you encounter a tree-like input that is reasonable and should be handled correctly but isn't, please provide the tree-like input in a new issue.

To improve the speed of resolving your issue, provide one or more test cases that demonstrate the failure. Use the existing test cases as a baseline for how to structure your tests.

### Most Importantly
Enjoy using Treescriptify-Text and feel good every time that it works for you.
