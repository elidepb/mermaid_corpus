```mermaid
flowchart TD
    A[<b>Cognitive Psychology</b><br>Scientific study of mental<br>processes and the mind]:::title
    B[<b>GOAL</b><br>Understand how the mind<br>processes information and<br>guides behavior]:::goal
    C[<b>CORE MENTAL DOMAINS</b>]:::domains
    subgraph D[Perception & Attention]
        D1[Visual & auditory perception<br>Selective, divided &<br>sustained attention]
    end
    subgraph E[Memory Systems]
        E1[Sensory, short-term/<br>working, long-term memory<br>Encoding, storage, retrieval]
    end
    subgraph F[Higher Cognition]
        F1[Language & comprehension<br>Reasoning & decision making<br>Problem solving & creativity]
    end
    G[<b>METHODS & PARADIGMS</b><br>Behavioral experiments<br>Cognitive neuroscience (fMRI, EEG)<br>Computational modeling]:::methods
    H[<b>THEORETICAL PERSPECTIVES</b><br>Information processing<br>Connectionism / PDP<br>Embodied cognition]:::theory
    I[<b>APPLICATIONS</b><br>Education, AI, clinical psychology,<br>human‑computer interaction]:::outcome

    A -->|aims to| B
    B -->|by investigating| C
    C -->|includes| D
    C -->|includes| E
    C -->|includes| F
    D & E & F -->|studied via| G
    G -->|guided by| H
    H -->|produces insights for| I

    classDef title fill:#f0f7ff,stroke:#4a6fa5,stroke-width:2px,color:#333,stroke-dasharray: 5 5
    classDef goal fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#333
    classDef domains fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#333
    classDef methods fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:#333
    classDef theory fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px,color:#333
    classDef outcome fill:#fff9c4,stroke:#f9a825,stroke-width:2px,color:#333
```
