'''
Created on Jan 9, 2019

@author: Nik
'''
#make a python program that will ask the user for their name, age, and country (use a list of any 10 countries)
#given that information, if the user wants to drive, you gotta respond accordingly to their age
#if they want to drink, same thing
#if  they want to gamble, do that too
#do all this using a class, and methods
def exitscreen():
    userend=str(input("enter y to restart the program or enter n to quit the program: "))
    if userend == 'y':
        title()
    if userend =='n':
        exit()
    if userend != 'y' or 'n': 
        exitscreen()

provinces = ['ON', 'BC', 'QB', 'AB', 'NS', 'MB', 'SK', 'NB', 'PEI', 'NL']

def title():
    print("welcome to the legal age program")

    age=(input("enter your age: "))
    try:
        val = int(age)
        pass
    except ValueError:
        print("that was an invalid age")
        title()
        exitscreen()

    print("the list of provinces are: ON, BC, QB, AB, NS, MB, SK, NB, PEI, NL")
    province=str(input("enter your province: "))
    if province not in provinces:
        print("that was an invalid entry") 
        title()
    def ontario():

        if age < '19':
            print("you are not old enough to drink")
            print("you are not old enough to gamble")
        if age >= '19':
            print("you are old enough to drink")
            print("you are old enough to gamble")
        if age < '16':
            print("you are not old enough to drive")
        if age >= '16':
            print("you are old enough to drive")

        
    def britishcolumbia():
        if age < '19':
            print("you are not old enough to drink")
            print("you are not old enough to gamble")
        if age >= '19':
            print("you are old enough to drink")
            print("you are old enough to gamble")
        if age < '16':
            print("you are not old enough to drive")
        if age >= '16':
            print("you are old enough to drive")
    
    def quebec():
 
        if age < '18':
            print("you are not old enough to drink")
        if age >= '18':
            print("you are old enough to drink")
        if age < '16':
            print("you are not old enough to drive")
        if age >= '16':
            print("you are old enough to drive")
        if age < '19':
            print("you are not old enough to gamble")
        if age >= '19':
            print("you are old enough to gamble")
    def alberta():
        if age < '18':
            print("you are not old enough to drink")
            print("you are not old enough to gamble")
        if age >= '18':
            print("you are old enough to drink")
            print("you are old enough to gamble")
        if age < '16':
            print("you are not old enough to drive")
        if age >= '16':
            print("you are old enough to drive")

    def novascotia():
        if age < '19':
            print("you are not old enough to drink")
            print("you are not old enough to gamble")
        if age >= '19':
            print("you are old enough to drink")
            print("you are old enough to gamble")
        if age < '16':
            print("you are not old enough to drive")
        if age >= '16':
            print("you are old enough to drive")
    
    def manitoba():
        if age < '18':
            print("you are not old enough to drink")
            print("you are not old enough to gamble")
        if age >= '18':
            print("you are old enough to drink")
            print("you are old enough to gamble")
        if age < '16':
            print("you are not old enough to drive")
        if age >= '16':
            print("you are old enough to drive")
    def saskat():
        if age < '19':
            print("you are not old enough to drink")
            print("you are not old enough to gamble")
        if age >= '19':
            print("you are old enough to drink")
            print("you are old enough to gamble")
        if age < '16':
            print("you are not old enough to drive")
        if age >= '16':
            print("you are old enough to drive")
    def new():
        if age < '19':
            print("you are not old enough to drink")
            print("you are not old enough to gamble")
        if age >= '19':
            print("you are old enough to drink")
            print("you are old enough to gamble")
        if age < '16':
            print("you are not old enough to drive")
        if age >= '16':
            print("you are old enough to drive")
    def prince():
        if age < '19':
            print("you are not old enough to drink")
            print("you are not old enough to gamble")
        if age >= '19':
            print("you are old enough to drink")
            print("you are old enough to gamble")
        if age < '16':
            print("you are not old enough to drive")
        if age >= '16':
            print("you are old enough to drive")
    def newfound():
        if age < '19':
            print("you are not old enough to drink")
            print("you are not old enough to gamble")
        if age >= '19':
            print("you are old enough to drink")
            print("you are old enough to gamble")
        if age < '16':
            print("you are not old enough to drive")
        if age >= '16':
            print("you are old enough to drive")    
    
    if province == provinces[0]:
        ontario()

    if province == provinces[1]:
        britishcolumbia()

    if province == provinces[2]:
        quebec()

    if province == provinces[3]:
        alberta()

    if province == provinces[4]:
        novascotia()
    
    if province == provinces[5]:
        manitoba()
    
    if province == provinces[6]:
        saskat()
    
    if province == provinces[7]:
        new()
    
    if province == provinces[8]:
        prince()
    
    if province == provinces[9]:
        newfound()
title()
exitscreen()

#provinces = ['ON', 'BC', 'QB', 'AB', 'NS', 'MB', 'SK', 'NB', 'PEI', 'NL']
#provinces[0]=Age(19,16,19)
#provinces[1]=Age(19,16,19)
#provinces[2]=Age(18,16,19)
#provinces[3]=Age(18,16,18)
#provinces[4]=Age(19,16,19)
#provinces[5]=Age(18,16,18)
#provinces[6]=Age(19,16,19)
#provinces[7]=Age(19,16,19)
#provinces[8]=Age(19,16,19)
#provinces[9]=Age(19,16,19)




    

    

    
    
    