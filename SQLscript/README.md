# SQL script

Created by Lev Zavodskov

Automated SQL comparator used to find discrepancies between two similar or supposedly identical tables, dbs.

In production this code was compiled as an executable to avoid any enviromental requiremts to run it.

Steps to run it:

Pre-step: Establish background SSH tunnel or SSH based corporate vpn
1) Respecify credentials, version, logs save directory and "date related criteria" in config.ini according to your needs
2) Specify codes for testing universes in universes.txt
3) Specify column names in columnnames.txt
4) Run main.exe

Output:
- Once started the executable cmd propmt will open user will be able to monitor scripts progress: Current universe, current column within that unverse, ammount of discrepancies logged(if any), whether or not an error was encountered or column was not present in tables structure.
- Once it's done running through all specified tables the prompt will stop and wait for any input before closing.

Note that this piece of code was edited to hide any confidential info AFTER I stopped working on the project this tool was made for. Therefore I have no means to test it and might have developed bugs that were not present in initial version of this tool. Anyway this representation should give you enough information about my skills. Ready to discuss your questions at any time.
