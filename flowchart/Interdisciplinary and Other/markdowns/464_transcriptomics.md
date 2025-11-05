```mermaid
flowchart TD
    Transcriptomics[Transcriptomics] --> Sequencing[RNA Sequencing]
    Transcriptomics --> Analysis[Expression Analysis]
    Transcriptomics --> Applications[Applications]
    Sequencing --> RNAseq[RNA-seq]
    Sequencing --> Microarray[Microarray]
    Analysis --> Differential[Differential Expression]
    Analysis --> Clustering[Expression Clustering]
    Applications --> Disease[Disease Studies]
    Applications --> Development[Development Studies]
```