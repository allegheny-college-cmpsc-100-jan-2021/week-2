#!/usr/bin/env python

import markovify

file = open("poems/shakespeare.txt")

model = markovify.NewlineText(file, state_size=2)

# TODO: Use the above model to create a 14-line sonnet which
#       writes to a file called "sonnet.txt"

# HINT: It may be helpful to use a list to collect the lines
#       and then join them using a newline character
