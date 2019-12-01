import argparse
from collections import defaultdict
          
def find_longest_prefix(x):
    x_max = len(max(x, key=len))
    for i in range(0, x_max)[::-1]:
        trim = [j[:i] for j in x]
        trimmed= [tuple(i) for i in trim]
        result = defaultdict(list)
        for j in set(trimmed):
            result[trimmed.count(j)].append(j)
        highest_count = max(result)
        words=[]
        if highest_count >= 2:
            prefix = result[highest_count]
            prefixx= [list(i) for i in prefix]
            if prefixx==[[]]:
                words=[]
            else:    
               #words=[j for k in prefixx for j in x if j[:len(k)]==k]
               for k in prefixx:
                   w=[]
                   for j in x:
                       if j[:len(k)]==k:
                           w.append(j)
                   words.append(w)        
            return prefixx, words

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif
      
def diff(a, b):
    lenght=len(b)
    diff = a[lenght:]
    if diff!=[]:
      return diff
    else:
        return ["epsilon"]
def left_factoring(rules):  
    new_rules={}
    for key,rule in rules.items():
        stop=True
        count=0
        while(stop):
            if len(rule)>1:
                prefix,productions=find_longest_prefix(rule)
                if (prefix==[[]]):
                    stop=False
                    break
                for indx,_ in enumerate(prefix):
                    rule=Diff(rule, productions[indx])
                    remain_prod=[diff(i,prefix[indx]) for i in productions[indx]]
                    count=count+1
                    new_rules[key+("'"*count)]=remain_prod
                    prefix[indx].append(key+("'"*count))
                    rule.append(prefix[indx])
                    rules[key]=rule
           

            else:
                stop=False
    rules.update(new_rules)
    return rules        
def write_file(rules):
  factoring=left_factoring(rules)
  output_file=open("factoring_result.txt","w+")   
  for key,val in factoring.items():
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
    write_file(rules)  

