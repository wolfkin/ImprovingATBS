#! python3

import re, pyperclip


#### RegEx for Phone Numbers
phoneRegex = re.compile(r'''
(
(\(?\d{3}\)?)?  #(209)
-
\d{3}           #432
-
\d{4}           #3574
)
''', re.VERBOSE)

# RegEx for Emails
emailRegex = re.compile(r'''
[\w.-]+
@
[\w.-]+
\.
\w{3}
''', re.VERBOSE)

# Get text off clipboard

clipboard = pyperclip.paste()


print('---------------------------')

extractPhones = phoneRegex.findall(clipboard)
processedPhones = []
phoneCount=0
for phone in extractPhones:
	phoneCount +=1
	processedPhones.append(phone[0])

extracteMails = emailRegex.findall(clipboard)
emailCount=0
for phone in extracteMails:
	emailCount +=1
processedeMails = extracteMails


print('From Clipboard')
print(' 1. [%s] Phone Numbers' % (phoneCount))
print(processedPhones)
print(' 2. [%s] eMails' % (emailCount))
print(processedeMails)


# copy extracts to clipboard

results = 'The results for this are:\n' + 'Phone Numbers\n' + '\n'.join(processedPhones) + '\n' + 'Emails\n' + '\n'.join(processedeMails)
print('================')
print(results)
pyperclip.copy(results)
