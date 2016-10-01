#!/usr/bin/env python
#coding: utf-8

#Encoding is in utf-8 since I want to print out Korean characters
#And since the default python encoding is in ASCII, I had to change it to UTF-8 to make sure that it prints out these characters
#Note that I used the cgi server code from the cgi tutorial website suggested in the class piazza page
#the following code is also based on that cgi tutorial; however, I've made the appropriate modifications to make sure
#that the code runs as specified in the question
import cgi
import sys
import os
form = cgi.FieldStorage()
 

#default HTML header and the accept language header
#to tell the web application that it should only accept engilsh, finnish and korean browser languages
#form is the comment box that user enters the input
print "Content-type: text/html; charset=utf-8"
print "Accept-Language: fi, en, ko"
print
print "The form input is below...<br/>"
print"""<form>
  String Input: <form method="post" action="test_form.py"><textarea name="comments" id="comments" cols="25" rows="3"></textarea>
  <input type="submit" value="submit" />
</form>"""
val1 = form.getvalue("comments")
print val1




#this section checks whether the user input contains only English letters and/or digits without any spcade
#if yes, the web app outputs the length of the string in bytes and characters
#and prints out a welcome message in english, korean and finnish
if all(x.isalpha() or x.isdigit() for x in u):
    print ("Input string only consists of letters and digits.\n")
    print ("Length of string in characters: ")
    print("\n")
    j = len(u)
    print j
    print("Length of string in bytes: ")
    unicode_string=bytes.decode("utf-8")
    print len(unicode_string)
    print("Welcome")
    print("환영")
    print("Tervetuloa")
else:
    print("is not in unicode");






#print val1