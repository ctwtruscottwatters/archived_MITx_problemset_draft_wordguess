# -*- coding: utf-8 -*-
import random
import sys
" Charles Truscott is happily sitting a unit at MIT through edX :-) "
" Woohooo!! Lifelong dream come TRUE of sitting a unit from MIT "
"""" 
runfile('C:/Users/user/.spyder-py3/ifnotin.py', wdir='C:/Users/user/.spyder-py3')
C:\Users\user\.spyder-py3\ifnotin.py:59: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if len(not_chosen) is 0:

Pick a letter: a
Correct! a is in the word.
Correct answers:	 ['a', 'a', 'a']


Pick a letter: p
Incorrect, p is not in the word
Correct answers:	 ['a', 'a', 'a']


Pick a letter: b
Correct! b is in the word.
Correct answers:	 ['b', 'a', 'a', 'a']


Pick a letter: c
Incorrect, c is not in the word
Correct answers:	 ['b', 'a', 'a', 'a']


Pick a letter: n
Correct! n is in the word.
Correct answers:	 ['b', 'a', 'n', 'a', 'n', 'a']

The answer was:	 banana
End of Game
I love MIT. Charles Truscott
"""""
def main():
    words = ["apple", "pear", "banana", "peach"]
    
    
    y = words[random.randint(1, len(words))]
    p, q, r, s = 0, 0, 0, 0
    d = {}
    
    for n in y:
            d.get(s)
            d[p] = n
            p += 1
            
    copy_dict = d
    
    
    fin = False
    choices = []
    not_chosen = []
    correct_answers = []
    wrong_answers = []
    not_found_letters = []
    z = y
    z_copy = z
    not_found = True
    for n in y:
        not_chosen.append(n)
    while(not fin):
        found = False
        choice = input('Pick a letter: ')
        for n in y:
                if choice == n:
                    correct_answers.append(choice)
                    for x in not_chosen:
                        if x == choice:
                            not_chosen.remove(choice)
                            found = True
    
        if found == True:
            print("Correct! {} is in the word.".format(choice))
        elif found == False:
            print("Incorrect, {} is not in the word".format(choice))
        found = False
    
        temp = []
        for q in z:
            for r in correct_answers:
                if q == r:
                    temp.append(r)
                    break
        print('Correct answers:\t', temp, end='\n\n')
        
        if len(not_chosen) is 0:
            print('The answer was:\t', y)
            print("End of Game")
            print('I love MIT. Charles Truscott')
            sys.exit()
        # print(not_chosen)
        
if __name__ == "__main__": main()
    
                    
             
        
                
    
                    
                
