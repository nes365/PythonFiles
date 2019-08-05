#!/usr/bin/python3.1
while True:
    s = input('Enter a string of at least 4 characters, or q to quit: ')
    if s == 'q':
              break
    if len(s) < 4:
              print("Value is too small.")
              continue
    print("The string was of sufficient length")
    raise SystemExit
