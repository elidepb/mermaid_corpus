```mermaid
flowchart TD
    A[<b>Water Pollution</b><br>Contamination of water bodies<br>by harmful substances]:::title
    B[<b>PRIMARY CONCERN</b><br>Understand sources & impacts<br>to develop control strategies]:::concern
    C[<b>CORE ASPECTS</b>]:::aspects
    
    subgraph D[Pollution Sources]
        D1[Point sources<br>Industrial & wastewater<br>Non-point: runoff]
    end
    
    subgraph E[Pollutant Types]
        E1[Nutrients & heavy metals<br>Organic chemicals<br>Pathogens & microplastics]
    end
    
    subgraph F[Transport & Fate]
        F1[Surface runoff<br>Groundwater infiltration<br>Bioaccumulation]
    end
    
    subgraph G[Environmental Impacts]
        G1[Ecosystem degradation<br>Aquatic toxicity<br>Biodiversity loss]
    end
    
    subgraph H[Control Measures]
        H1[Wastewater treatment<br>Best management practices<br>Regulatory frameworks]
    end
    
    I[<b>ASSESSMENT PROCESS</b><br>Monitoring, Identification<br>Impact assessment, Control]:::process
    
    J[<b>ADDRESSES</b><br>Contamination through treatment,<br>management & policy]:::outcome
    
    A -->|raises| B
    B -->|through understanding| C
    C -->|includes| D
    C -->|includes| E
    C -->|includes| F
    C -->|includes| G
    C -->|includes| H
    D & E & F & G & H -->|unified by| I
    I -->|enables| J
    
    classDef title fill:#f0f7ff,stroke:#4a6fa5,stroke-width:2px,color:#333,stroke-dasharray: 5 5
    classDef concern fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#333
    classDef aspects fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#333
    classDef process fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#333
    classDef outcome fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#333
```
