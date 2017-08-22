# @nguyen17.github
# Assignment # 3 Complementing a strand of DNA
"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string ss is the string scsc formed by reversing the symbols of ss, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

	Given: A DNA string ss of length at most 1000 bp.

	Return: The reverse complement scsc of ss.

Test case:
input: AAAACCCGGT
output: ACCGGGTTTT

"""

# MAIN CODE HERE

import Bio
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

user_prompt = input("Enter Dna: ")
dna_seq = Seq(user_prompt, generic_dna)

complement_dna = dna_seq.complement()
print (complement_dna[::-1])

# ===============
# Alternative
"""
#1:
@gorysko
	from Bio.Seq import Seq

	file = open("rosalind2.txt", "r")
	s = file.read()
	seq = Seq(s)
	seq.reverse_complement()
	print seq.reverse_complement()

#2:
@prograde
	cat rosalind_revc.txt | tr [ACGT] [TGCA] | rev

#3:
@Ben Usman
	st = "AAAACCCGGT"
	st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
	print st
"""