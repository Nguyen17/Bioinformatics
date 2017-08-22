# @nguyen17.github
# Assignment #2: Trnascribing DNA into RNA

""" 

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

	Given: A DNA string t having length at most 1000 nt.

	Return: The transcribed RNA string of t.

Test case:
input: GATGGAACTTGACTACGTAAATT
output: GAUGGAACUUGACUACGUAAAUU

"""

# MAIN CODE HERE

def dna_to_rna(str):
	str.upper()
	return str.replace('T', 'U')



user_prompt = input("Enter DNA: ")

result = dna_to_rna(user_prompt)
print(result)




# - -
# ====================
# Alternatives
"""
# 1:
@gorysko
	from Bio.Seq import Seq
	from Bio.Alphabet import generic_dna
	
	file = open("rosalind_RNA.txt", "r")
	dna = Seq(file.read(), generic_dna)
	rna = dna.transcribe()
	
	print rna



# 2: (command line)
@prograde
	cat rosalind_rna.txt | tr T U

"""