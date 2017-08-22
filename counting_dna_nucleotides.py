# @nguyen17.github

# Assignment # 1: Counting DNA Nucleotides

""" Details
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

	An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

 	Given: A DNA string ss of length at most 1000 nt.

	Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.

Test case:

input: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

output: 20 12 17 21 # A, C, G, T format
"""

# Create function to read nucleotides
def read_DNA(nucleotide):
	nucleotide.upper() 						# convert string to uppercase
	
	# Purines Count
	num_Adenine = nucleotide.count('A')		# count the occurence of A
	num_Guanine = nucleotide.count('G')		# count the occurence of G

	# Pyrimidines Count
	num_Thymine = nucleotide.count('T')		# count the occurence of T
	num_Cytosine = nucleotide.count('C')	# count the occurence of C

	# space = " "
	# result = num_Adenine + space + num_Cytosine + space + num_Guanine + space + num_Thymine
	result = [num_Adenine,num_Cytosine, num_Guanine, num_Thymine]

	return result

# Prompt for user input
user_prompt = input("Enter nucleotide string: ")

# Get results
dna_count = read_DNA(user_prompt)

# Output to console
print (dna_count)	

''' =========================================================== 
# Other solutions

Alternative #1:
@Maurício Verardo da Costa
    
    def qt(s):
      return s.count("A"), s.count("G"), s.count("C"), s.count("T")

Alternative #2:
@arekolek

	freq = {'A': 0, 'C': 0, 'G': 0, 'U': 0}
	for i in string:
	    freq[i] = freq[i] + 1

	print freq['A'], freq['C'], freq['G'], freq['U']
	
Alternative #3:
@Yuriy Khamzyaev
	# print(*map(input().count, "ACGT"))

'''