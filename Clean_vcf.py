def clean_vcf_sample_names(input_vcf, output_vcf):
    with open(input_vcf, 'r') as infile, open(output_vcf, 'w') as outfile:
        for line in infile:
            if line.startswith('#CHROM'):
                parts = line.strip().split('\t')
                # First 9 fields are standard VCF fields
                cleaned = parts[:9] + [s.removesuffix('paired.fastq.gz') for s in parts[9:]]
                outfile.write('\t'.join(cleaned) + '\n')
            else:
                outfile.write(line)

# Usage
input_vcf = 'eastern.MAFREM.recode.vcf'
output_vcf = 'ecleaned_output2.vcf'
clean_vcf_sample_names(input_vcf, output_vcf)
