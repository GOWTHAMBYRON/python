# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 10:42:26 2025

@author: admin
"""

Deepak = {'Python' , 'Java' , 'C','C++'}
uma = {'PHP','SQL','ASP.NET','C'}

print(f'Deepak : {Deepak} \nUma :{uma}')

inte = Deepak.intersection(uma)
print("The commom between Deepak and Uma :",inte)
print("Languages known by both of them :",Deepak.union(uma))
print("Languages known by Deepak not by Uma",Deepak.difference(uma))
print("Languages known by Uma not by Deepak",uma.difference(Deepak))
Deepak.add('Go')
print(f"After update Deepak is {Deepak}")
uma.remove('SQL')
print(f"After removing a language in Uma is {uma}")