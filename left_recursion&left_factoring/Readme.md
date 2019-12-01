# eliminate left recursion and left factoring of CFG.
 
 ##### Assume that grammars given have no cycles & no epsilon productions.
 
 ### input file format:
 #####   non terminal colon set of production rules (tokens are space separated) 
 ex:
 E : T + E | T
 T : int | int * T | ( E )
##### How to run:-

   from command line:
   python "script_name"  --file "input file name"