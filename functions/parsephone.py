"""Parse U.S. phone numbers """


import re

class InvalidPhoneNumber(Exception): pass

phonePattern = re.compile(r"""
    ^            # match beginning of string
    \D*          # swallow anything that isn't numeric
    1?           # swallow leading 1, if present
    \D*          # swallow anything that isn't numeric
    (\d{3})      # capture 3-digit area code
    \D*          # swallow anything that isn't numeric
    (\d{3})      # capture 3-digit trunk
    \D*          # swallow anything that isn't numeric
    (\d{4})      # capture 4-digit number
    \D*          # swallow anything that isn't numeric
    (\d*)        # capture extension, if present
    """, re.VERBOSE)

def parsePhoneNumber(phoneNumber):
    match = phonePattern.search(phoneNumber)
    if match:
        return match.groups()
    else:
        raise InvalidPhoneNumber, phoneNumber
