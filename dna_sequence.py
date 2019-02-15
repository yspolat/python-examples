# DNA Sequence
#
# Assume that you will write a program to align two input DNA strings. But first, you have to check whether the input strings are 
# indeed correctly defined DNA sequences or not, meaning that they consist only of the letters “A”, “C”, “G”, and “T”, either 
# lowercase or uppercase (i.e. case-insensitive).
#
# ACTGCGT --> Valid DNA
# ACTYRA --> Invalid DNA

validChars = "ACGT"
flag = True

DNA = input("Enter the DNA sequence: ")
for ch in DNA:
  if ch not in validChars:
    flag = False
    break
    
if flag:
  print("It is a valid DNA")
else:
  print("It is an invalid DNA")
