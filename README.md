# Keyboard-Macro-Clone-Hero
macro to make using the keyboard in clone hero easier

how does it work?
basically to your input of the previously selected keys touch one more key, in this case the n key.
inside this repository you will find 2 files 1 is executable to get and use without the need to understand any code. the only requirement is that inside your game you must set the n key to strump up or strump down so every time you press one of your keys it will play them automatically without you manually using the strump.

the executable comes with 4 options 
-start macro
-stop the macro
-set the keys
-show current keys

the executable comes with the default keys of the clone hero. if you would use another key combination you should set them. and don't worry the program generates a file called set-up_keys.ini where it will save your configuration. this file generates itself if it is missing, so if you delete it, don't worry, you just have to put your keys back in again.

inside the Clon Hero game you must add in the strump up or down as you prefer the n key must be in one of the 2 for the program to work since the executable is not prepared to change the strump key (for now probably later it will be updated).

The second file called keyboard_macro_example.py has the base code to make the macro start and stop work. 
the code is completely free to use and modifiable. if you want to make your own executable I advise you to make your code in python and then use the pyinstaller library to convert the python file into the executable.to run the .py file without creating your own executable it is preferable to rename the extension to .pyw so that the pyhton file will run as an executable with the thinker library.

extra considerations.
if you prefer to use the executable directly it is possible that windows detects it as malicious software but it is not, it detects it by the fact that it reads the inputs.
to let windows run the program you must enter windows defender or antivurus and add a rule to let keyboard_macro.exe run.

I will not release the original source code of the executable until I add the last function I have in mind for the program.

Link to pyinstaller: https://pyinstaller.org/en/stable/index.html
