#!/usr/bin/env python


matt={'name':'matt','job':'financial consultant','phone number': '9192222222','hobbie':'music,basketball','address':{'city':'Washingtion D.C.','zipcode':'34776'}}
russell={'name':'russell','job':'student','phone number': '9193333333','hobbie':'music,jogging','address':{'state':'NC','city':'Chapel Hill','zipcode':'27713'}}
friends = {'Russell':russell,'Matt':matt}



introduction="My name is " + friends['Russell']['name']+", I am a " + friends['Russell']['job']+", my phone number is " + friends['Russell']['phone number'] + ", " + friends['Russell']['hobbie'] + ", I live in " + friends['Russell']['address']['city'] + ", and my area code is " + friends['Russell']['address']['zipcode'] + "."

print introduction