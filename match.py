import os

def find_unaligned_without_aligned(directory):
    unaligned_files = set()
    aligned_files = set()
    
    for file in os.listdir(directory):
        if file.endswith(".fasta"):
            if file.endswith("_mus.fasta"):
                aligned_files.add(file.replace("_mus.fasta", ""))
            else:
                unaligned_files.add(file.replace(".fasta", ""))
    
    missing_aligned = [f + ".fasta" for f in unaligned_files if f not in aligned_files]
    
    return missing_aligned

# Example usage
directory = "path/to/your/directory"
missing_files = find_unaligned_without_aligned(directory)
print("Unaligned files without corresponding aligned files:")
print("\n".join(missing_files))
