#!/usr/bin/python3
# Task Number 2-print_alphabet.py

"""This script print the alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
	print("{}".format(chr(letter)), end="")
