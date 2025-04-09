def clean_vcf_sample_names(input_vcf, output_vcf):
    with open(input_vcf, 'r') as infile, open(output_vcf, 'w') as outfile:
        for line in infile:
            if line.startswith('#CHROM'):
                parts = line.strip().split('\t')
                # The first 9 columns are VCF metadata; samples start from column 10
                cleaned = parts[:9] + [s.replace('.paired.fastq.gz', '') for s in parts[9:]]
                outfile.write('\t'.join(cleaned) + '\n')
            else:
                outfile.write(line)

# Usage example
input_vcf = 'input.vcf'
output_vcf = 'cleaned_output.vcf'
clean_vcf_sample_names(input_vcf, output_vcf)
