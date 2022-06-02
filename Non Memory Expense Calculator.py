{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 print("Welcome to sim-u-account! An interactive budgeting game. Lets learn finance and have fun!")\
print("We will begin with some introductions. I am Callie Y. or Callout and Line item Likeley Items Eating Your Funds.")\
print("But you can just call me Callie")\
name = input ("what is your name?")\
print("Hello " +name.title()+ ". Lets begin by getting some basic information about your budget!")\
\
balanceTotal= input ("How much do you make in a month?")\
if int(balanceTotal) >10000:\
    print("You didnt have to lie, I still would have liked you.")\
    balanceTotal= input ("How much do you REALLY make in a month?")\
else:\
    print("Thank You")\
print("We will start with $" + str(balanceTotal))\
\
\
print("Lets begin by talking about your expenses for the month! We will go over them one at at time, when you have entered them all, press 0 to end")\
exp=-1\
total = 0\
maxexp = 0 \
minexp = 0\
\
while exp!=0:\
    exp = int(input("What is the expense? or type 0 to end."))\
    total = total+exp\
    if exp>maxexp:\
        maxexp=exp\
    if exp<minexp:\
        minexp=exp\
print ("Your total fixed expenses are " +str(total))  \
print("Your largest single expense is "+str(maxexp))\
print("Your smallest single expense is "+str(minexp))\
\
\
totalFixed=int(total)\
PFBalance = int(balanceTotal) - int(totalFixed)\
\
print("Your total balance after fixed expenses is: "+ str(PFBalance))\
\
if int(totalFixed)>int(balanceTotal):\
    print("You already spend more than you make. Thats not good news.")\
\
print("Let's move onto your variable expenses.")\
nonFixedExp=input("Add a single estimate of your non-fixed expenses (gas, food,takeout, treats, medical expenses...ect)")\
print("Your non-fixed expenses are "+str(nonFixedExp))\
allExpenses=int(nonFixedExp)+int(totalFixed)\
print("Your total fixed and non-fixed expenses are " +str(allExpenses))}