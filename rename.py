import os
import re

# Define the directory containing the FASTA files
fasta_directory = "path_to_your_fasta_files"

# Loop through all files in the directory
for filename in os.listdir(fasta_directory):
    if filename.endswith(".fasta") or filename.endswith(".fa"):  # Adjust extensions if needed
        input_path = os.path.join(fasta_directory, filename)

        # Extract the leading number using regex
        match = re.match(r"^(\d+)", filename)
        if match:
            new_filename = f"{match.group(1)}_gene_alignment.fasta"
            output_path = os.path.join(fasta_directory, new_filename)

            # Rename the file
            os.rename(input_path, output_path)
            print(f"Renamed: {filename} -> {new_filename}")

print("Renaming complete!")
