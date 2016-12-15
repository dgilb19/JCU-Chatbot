import re

words = 'dgilb19@gmail.com'
numbers = "numb3rs are cool"

if re.match(r'\w{3,20}@\w{3,20}\W{1}\w{3,5}', words):
    print "good job"
else:
    print "you're bad"
if re.match(r'num\w\d\D{2}\s\w{3}\s\S{1,6}', numbers):
    print "also good job"
else:
    print "also bad job"

print re.split("a", 'swag', re.I)
