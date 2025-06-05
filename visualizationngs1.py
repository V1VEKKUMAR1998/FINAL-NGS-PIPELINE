import pysam
import pandas as pd
import matplotlib.pyplot as plt

# Read VCF file
vcf_file = "ERR5743893_trimmed.vcf"
variants = []

with pysam.VariantFile(vcf_file) as vcf:
    for record in vcf:
        variants.append({
            'Position': record.pos,
            'Reference': record.ref,
            'Alternate': ','.join(record.alts),
            'Quality': record.qual
        })

# Create DataFrame
df = pd.DataFrame(variants)

# Plot variant positions and quality
plt.figure(figsize=(10, 6))
plt.scatter(df['Position'], df['Quality'], alpha=0.5)
plt.xlabel('Genomic Position')
plt.ylabel('Variant Quality')
plt.title('Variant Quality vs. Genomic Position')
plt.grid(True)
plt.savefig('variant_quality_plot.png')
plt.show()