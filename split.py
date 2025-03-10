from Bio import SeqIO
import os

def split_fasta_by_species(input_fasta, output_dir):
    """Splits a FASTA file into separate files for each species.

    Args:
        input_fasta (str): Path to the input multi-sequence FASTA file.
        output_dir (str): Directory to store the split FASTA files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    species_dict = {}

    # Read the input FASTA file
    with open(input_fasta, "r") as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            species_name = record.id.split(" ")[0]  # Extract species name (before first space)

            # Store sequences in a dictionary
            if species_name not in species_dict:
                species_dict[species_name] = []
            species_dict[species_name].append(record)

    # Write each species' sequences to a separate FASTA file
    for species, records in species_dict.items():
        output_file = os.path.join(output_dir, f"{species}.fasta")
        with open(output_file, "w") as out_fasta:
            SeqIO.write(records, out_fasta, "fasta")
        print(f"Saved {len(records)} sequences to {output_file}")

# Example usage
input_fasta = "input.fasta"  # Replace with your actual input file
output_dir = "split_fasta_output"  # Directory to store split files
split_fasta_by_species(input_fasta, output_dir)
