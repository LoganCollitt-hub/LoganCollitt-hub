def find_mutation_positions(dna_sequence, target_nucleotide='C'):
    for i, base in enumerate(dna_sequence):
        if base != target_nucleotide: mutation_positions.append(i)
    return mutation_positions

target = "T"
i = 0  #index
current_sequence = ""
longest_sequence = ""
mutation_positions = []

# Creates variables for input values that can be used in a loop.

while True:
    try:
        dna_sequence = input("Enter your sequence here: ").upper().replace(" ", "")
        if not dna_sequence:
            raise ValueError("You must enter a sequence!")
        if not set(dna_sequence) <= {"A", "T", "C", "G"}:
            print("Invalid Sequence!")
            continue
# A loop that continuously executes a block of code until the user enters a valid dna sequence. 

        while i < len(dna_sequence):
            nucleotide = dna_sequence[i]
            if nucleotide == target:
                current_sequence += nucleotide
            else:
                current_sequence = ""
# While the index is less than the length of the dna sequence,
# Check whether the nucleotide is equal to 'T' and build the longest run.

            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            i += 1  #Increase the index by 1.
        print("Longest run:", longest_sequence)
        # Prints the longest run and terminates the sequence.
        mutation_positions = find_mutation_positions(dna_sequence,'C')
        print("Possible mutation positions for 'C':", mutation_positions)
        break
# Calls the find mutation function 
    except ValueError as e:
        print(e)
        continue
# Executes error script.
    