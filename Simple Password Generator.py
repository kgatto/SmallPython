{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\
import string\
string.ascii_letters\
scheme = int(input("Choose a number between 1 and 5 to get a randomly generated password" ))\
masterPassword = 0\
\
if scheme==1:\
    lower_upper_alphabet = string.ascii_letters\
    random_letter = random.choice(lower_upper_alphabet)\
\
    lower_upper_alphabet = string.ascii_letters\
    random_letter2 = random.choice(lower_upper_alphabet)\
\
    lower_upper_alphabet = string.ascii_letters\
    random_letter3 = random.choice(lower_upper_alphabet)\
\
    #making the password \
    pw = random_letter+str(random.randint(1, 1000))+ random_letter3+str(random.randint(1, 1000))+str(random.randint(1, 1000))+random_letter2\
    print(pw)\
    masterPassword=str(pw)\
\
if scheme==2:\
    lower_upper_alphabet = string.ascii_letters\
    random_letter = random.choice(lower_upper_alphabet)\
\
    lower_upper_alphabet = string.ascii_letters\
    random_letter2 = random.choice(lower_upper_alphabet)\
\
    lower_upper_alphabet = string.ascii_letters\
    random_letter3 = random.choice(lower_upper_alphabet)\
\
    #making the password \
    pw = str(random.randint(1, 1000))+random_letter+str(random.randint(1, 1000))+ random_letter3+str(random.randint(1, 1000))+str(random.randint(1, 1000))+random_letter2\
    print(pw)\
    masterPassword=str(pw)\
\
if scheme==3:\
    lower_upper_alphabet = string.ascii_letters\
    random_letter = random.choice(lower_upper_alphabet)\
\
    lower_upper_alphabet = string.ascii_letters\
    random_letter2 = random.choice(lower_upper_alphabet)\
\
    lower_upper_alphabet = string.ascii_letters\
    random_letter3 = random.choice(lower_upper_alphabet)\
    pw = random_letter3+str(random.randint(1, 1000))+ random_letter2+str(random.randint(1, 1000))+str(random.randint(1, 1000))+random_letter2\
    print(pw)\
    masterPassword=str(pw)\
\
if scheme==4:\
    lower_upper_alphabet = string.ascii_letters\
    random_letter = random.choice(lower_upper_alphabet)\
\
    lower_upper_alphabet = string.ascii_letters\
    random_letter2 = random.choice(lower_upper_alphabet)\
\
    lower_upper_alphabet = string.ascii_letters\
    random_letter3 = random.choice(lower_upper_alphabet)\
    pw = random_letter+str(random.randint(1, 1000))+ random_letter2+str(random.randint(1, 1000))+str(random.randint(1, 1000))+random_letter3\
    print(pw)\
    masterPassword=str(pw)\
\
if scheme==5:\
    lower_upper_alphabet = string.ascii_letters\
    random_letter = random.choice(lower_upper_alphabet)\
\
    lower_upper_alphabet = string.ascii_letters\
    random_letter2 = random.choice(lower_upper_alphabet)\
\
    lower_upper_alphabet = string.ascii_letters\
    random_letter3 = random.choice(lower_upper_alphabet)\
    pw = random_letter2+str(random.randint(1, 1000))+ random_letter3+str(random.randint(1, 1000))+str(random.randint(1, 1000))+random_letter2+str(random.randint(1, 1000))\
    print(pw)\
    masterPassword=str(pw)\
\
print("Please enjoy your password! Don't share with anyone else, or you'll need to make a new one.")\
\
#tester to see if master passwords store correctly print(masterPassword)\
\
}