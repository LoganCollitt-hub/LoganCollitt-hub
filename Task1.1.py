while True: # Creates a continuous loop that executes a set of statements as long as conditions are met.
    try: # Used for error handling.
        dna_sequence = input("Enter your sequence here: ").upper().replace(' ',"") # Accepts user input, converts to uppercase and removes gaps in the sequence.
        if not dna_sequence:
            raise ValueError("You must enter a sequence!") #Raises a Value Error.

        if set(dna_sequence) <= {"A","T","C","G"}: #Creates a set and compares bases to conditions.
                print("Valid Sequence!")

                nucleotide_counts = {n: dna_sequence.count(n) for n in "ATCG"}  # Dictionary function.
                print(nucleotide_counts)

                gc_count = nucleotide_counts["G"] + nucleotide_counts["C"]
                gc_content = (gc_count / len(dna_sequence)) * 100
                print(f"GC content is: {gc_content:.2f}%")
                break  # Ends the script
        else:
            print("Invalid Sequence!")
    except ValueError as e: #Executes the code to raise a Value Error.
        print(e)
        break