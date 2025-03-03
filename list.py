# List all the Samples found in a fasta file

from Bio import SeqIO

def list_fasta_sample_names(fasta_file):
    sample_names = [record.id for record in SeqIO.parse(fasta_file, "fasta")]
    return sample_names

# Example usage
fasta_file = "your_file.fasta"  # Replace with your FASTA file path
sample_names = list_fasta_sample_names(fasta_file)
print("\n".join(sample_names))
