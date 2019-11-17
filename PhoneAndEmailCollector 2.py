#! python3

import re, pyperclip

# Regex for Vietnam mobile phone numbers
phoneRegex = re.compile(r'''
# 0983888888, 0983 888 888, 098 888 8888

0\d\d\s?\d\s?\d\d\s?\d\s?\d\d\d

''', re.VERBOSE)

# Regex for email addresses
emailRegex = re.compile(r'''
# some.+_-thing@some.+_-.com.vn or .co.uk

(^[a-zA-Z0-9_.+-]+   # the name
@                    # the @ symbol
[a-zA-Z0-9-]+        # the domain before dot
\.[a-zA-Z0-9-.]+$)   # the domain after dot

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the phone and email from that text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)

# Copy the extracted phone and email to the clipboard
result = "\n".join(extractedPhone) + "\n" + "\n".join(extractedEmail)
pyperclip.copy(result)
