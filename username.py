#!/usr/bin/env python

passwords = {'Will':'will123', 'Travis':'456travis', 'Yash':'y789ash'}

users = raw_input("input user name:")
pwd=raw_input("input user password:")

if passwords.has_key(users):
    if pwd == passwords[users]:
        print "access accepted"
    else:
        print "password error"
else:
    print "user does not exist"