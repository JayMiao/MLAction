import re
mySent = 'This book is the best book on Python or M.L. I have ever laid eyes upon.'
regEx = re.compile('\\W*')
listOfTokens = regEx.split(mySent)

print listOfTokens