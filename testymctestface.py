import re

words = 'dgilb19@gmail.com'

if re.match(r'\w{3,20}@\w{3,20}\W{1}\w{3,5}', words):
    print "good job"
else:
    print "you're bad"
