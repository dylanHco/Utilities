## Sort samples in alphabetical order

from Bio import SeqIO

def reorder_fasta_alphabetically(input_fasta, output_fasta):
    # Read sequences and sort them by header
    records = sorted(SeqIO.parse(input_fasta, "fasta"), key=lambda r: r.id)
    
    # Write the sorted sequences to a new file
    with open(output_fasta, "w") as out_f:
        SeqIO.write(records, out_f, "fasta")

# Example usage
input_fasta = "input.fasta"  # Replace with your input FASTA file
output_fasta = "sorted_output.fasta"  # Replace with desired output file name
reorder_fasta_alphabetically(input_fasta, output_fasta)

print(f"Reordered FASTA saved as {output_fasta}")
