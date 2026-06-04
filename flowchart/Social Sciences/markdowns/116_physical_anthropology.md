```mermaid
flowchart TD
    A[<b>Physical Anthropology</b><br>Scientific study of human biological<br>evolution, variation, and adaptation]:::title
    B[<b>GOAL</b><br>Understand human origins<br>and biological diversity]:::goal
    C[<b>CORE SUBFIELDS</b>]:::subfields
    subgraph D[Human Evolution]
        D1[Paleoanthropology, fossil hominins<br>Phylogeny, emergence of Homo sapiens]
    end
    subgraph E[Primatology]
        E1[Behavior, ecology, and genetics<br>of non-human primates]
    end
    subgraph F[Human Variation & Adaptation]
        F1[Population genetics, physiological<br>adaptation, modern human diversity]
    end
    subgraph G[Bioarchaeology & Forensic]
        G1[Skeletal biology, trauma analysis,<br>identification, past health]
    end
    H[<b>THEORIES & METHODS</b>]:::theory
    subgraph I[Theories]
        I1[Evolution by natural selection<br>Population genetics<br>Phylogenetics]
    end
    subgraph J[Methods]
        J1[Comparative anatomy<br>Fossil analysis & dating<br>Genomics (aDNA, GWAS)<br>Morphometrics]
    end
    K[<b>OUTCOMES</b><br>Reconstructing human evolutionary history,<br>forensic identification, informing<br>medicine & public health]:::outcome

    A -->|aims to| B
    B -->|through study of| C
    C -->|includes| D
    C -->|includes| E
    C -->|includes| F
    C -->|includes| G
    D & E & F & G -->|guided by| H
    H -->|includes| I
    H -->|includes| J
    I & J -->|produce| K

    classDef title fill:#f0f7ff,stroke:#4a6fa5,stroke-width:2px,color:#333,stroke-dasharray: 5 5
    classDef goal fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#333
    classDef subfields fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#333
    classDef theory fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:#333
    classDef outcome fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px,color:#333
```
