# NGS-PIPELINE

**Project Overview**

- Objective: To process raw sequencing reads and identify genetic variants.

- Data: Paired-end sequencing files (ERR5743893_1.fastq.gz, ERR5743893_2.fastq.gz) aligned to the reference genome (MN908947.fasta).

- Output: A variant call file (ERR5743893_trimmed.vcf) and visualizations created via Python.

## **Repository Structure**

- .gitignore → Excludes large files from version control.

- .gitpod.Dockerfile, .gitpod.yml → Gitpod environment setup.

- ERR5743893_1.fastq.gz, ERR5743893_2.fastq.gz → Raw NGS paired-end FASTQ files.

- MN908947.fasta → Reference genome used for alignment.

- ERR5743893_trimmed.vcf → Variant call file generated after processing.

- visualizationngs1.py → Python script for visualizing NGS/variant data.

- README.md → Project documentation (this file).

## **Workflow**

- Quality Control & Preprocessing

- Input: Paired-end FASTQ files.

- Trimming and filtering steps applied (not shown in repo but assumed).

- Alignment & Variant Calling

- Reference genome: MN908947.fasta.

- Generated variant calls stored in ERR5743893_trimmed.vcf.

## **Visualization**

- visualizationngs1.py provides visual insights into read/variant distribution.

## **Tools & Technologies**

- Languages: Python (for visualization)

- NGS Tools (assumed used): FastQC, BWA, Samtools, BCFtools

- Data formats: FASTQ, FASTA, VCF

## **Future Improvements**

- Automate the pipeline with a shell script.

- Add quality control reports (FastQC).

- Expand visualization with more genomic plots.
