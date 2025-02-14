from Bio import SeqIO

# Input and output filenames
msa_file = "hyde.fasta"
output_file = "removed.hyde.fasta"
samples_to_remove = {"Carya_illinoinensis","hindsii_373","major_21","major_349","major_381","major_383"}  # Set of samples to exclude

# Read and filter sequences
filtered_records = [record for record in SeqIO.parse(msa_file, "fasta") if record.id not in samples_to_remove]

# Write the filtered sequences to a new file
SeqIO.write(filtered_records, output_file, "fasta")

print(f"Filtered MSA saved as {output_file}")
