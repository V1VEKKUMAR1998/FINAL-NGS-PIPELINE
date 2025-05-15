# .gitpod.Dockerfile
FROM gitpod/workspace-full:latest

# Install common bioinformatics tools
USER root
RUN apt-get update && apt-get install -y \
    fastqc \
    bwa \
    samtools \
    freebayes \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER gitpod
