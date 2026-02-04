def reverse_complement(dna_sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    complement_list = [complement_dict[base] for base in dna_sequence]
    reverse_complement_list = complement_list[::-1]
    reverse_complement = ''.join(reverse_complement_list)
    print("The reverse complement is:", reverse_complement)
    return reverse_complement

dna_sequence = input("Enter your sequence here: ").upper().replace(' ',"") # Accepts user input, converts to uppercase and removes gaps in the sequence.
if set(dna_sequence) <= {"A","T","C","G"}:
  nucleotide_counts = {n: dna_sequence.count(n) for n in "ATCG"} #Accepts a users input and calculates the number of nucleotides
  print(nucleotide_counts)
  reverse_complement = reverse_complement(dna_sequence)
  print(reverse_complement)
  sequence_list = list(dna_sequence)
  start_index = dna_sequence.index('GAT') #Checks the sequence and returns the first entry of 'GAT'
  print("Starting index of 'GAT':", start_index)
else:
    print("Invalid Sequence!")