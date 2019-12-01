# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 22:58:32 2019

@author: Lenovo
"""
import argparse
import copy 
      
def left_recursion_elimination(rules,non_terminals):
    for i in range(0,len(non_terminals)):
        for j in range(0,i):
                rules2 = copy.deepcopy(rules)
                for key,rule in rules2.items():
                   if any(r[0]==non_terminals[j] and key==non_terminals[i] for r in rule):
                             indirect=rules2[non_terminals[j]] 
                             new_rule=[]
                             for prod in rule: 
                                 if prod[0]==non_terminals[j]:
                                     remain=prod[1:]
                                     sub_prod= list(map(lambda orig_string: orig_string + remain, indirect))
                                     new_rule.extend(sub_prod)
                                 else:
                                     new_rule.append(prod)
                             rules[key]=new_rule
        direct_recursion=direct_elimination(rules[non_terminals[i]],non_terminals[i])
        if direct_recursion!={}:
            rules.update(direct_recursion)                     

    return   rules
    
def direct_elimination(rule,non_terminal):
    """
    rule is list of lists of strings
    """
    new_rules={}  
    new_non_terminal=non_terminal+"'"
    if any(r[0] == non_terminal for r in rule):
        new_rules[non_terminal]=[]
        new_rules[new_non_terminal]=[]
        for i in rule:
            if i[0]!=non_terminal:
                        i.append(new_non_terminal)
                        new_rules[non_terminal].append(i)
            else:
                        li=i[1:]
                        li.append(new_non_terminal)
                        new_rules[new_non_terminal].append(li )
        new_rules[new_non_terminal].append(["epsilon"])  
    return new_rules    


def write_file(rules,non_terminals):    
  recursion_elimination=left_recursion_elimination(rules,non_terminals)
  output_file=open("recursion_result.txt","w+")   
  for key,val in recursion_elimination.items():
       output_file.write(key+" "+":"+" ")
       for v in range(0,len(val)):  
         q=""  
         if val[v] =="epsilon":
             output_file.write("epsilon")
         else: 
             li=val[v]
             q= " ".join(li)
             if v==len(val)-1:
                 output_file.write(q)
             else:
                 output_file.write(q+" "+"|"+" ")
       output_file.write("\n")
  output_file.close()            
                

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')
    
    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                            metavar="file")
    
    args = parser.parse_args()

    rules={}
    with open(args.file, mode='r', encoding='utf-8-sig') as file:
        for line in file:
            x=line.split(':')
            y=x[1:]
            z=y[0].split('|')
            l=[]
            for i in z:
                p=i.strip('\n')
                j=[p]
                l.append(j)
            kk=x[0].strip(' ')  
            rules[kk]=l
    for k, v in rules.items():
                li=[]
                for o in v:
                    l=[]
                    if o[0] !=" epsilon":
                        j=o[0].split(' ')
                        for jj in j:
                            if jj!='':
                                l.append(jj)
                        li.append(l)
                    else: 
                       str1= o[0].strip(' ')
                       li.append([str1])
                rules[k]=li

    terminals=[]
    non_terminals=[]
    for k,v in rules.items():
      if k not in non_terminals:
          non_terminals.append(k)
      for i in v:  
         if i=='epsilon':
            if i not in terminals:
               terminals.append(i)
         else:    
            for ii in i:
                if ii not in terminals and ii not in rules.keys():
                    terminals.append(ii) 
    #print(rules,terminals,non_terminals)                
    write_file(rules,non_terminals)
    
    