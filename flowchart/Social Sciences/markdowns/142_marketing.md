```mermaid
flowchart TD
    A[<b>Marketing</b><br>Organizational function for creating,<br>communicating, and delivering value]:::title
    B[<b>GOAL</b><br>Build profitable customer relationships<br>and sustainable brand equity]:::goal
    C[<b>CORE COMPONENTS</b>]:::core
    subgraph D[Market Understanding]
        D1[Market research & consumer insights<br>Environmental scanning<br>Competitive analysis]
    end
    subgraph E[Strategy (STP)]
        E1[Segmentation<br>Targeting<br>Positioning & differentiation]
    end
    subgraph F[Marketing Mix]
        F1[Product (features, quality, branding)<br>Price (value, discounts, models)<br>Place (channels, logistics, coverage)<br>Promotion (ads, PR, sales, digital)<br>Services: People, Process, Physical evidence]
    end
    G[<b>THEORETICAL FOUNDATIONS</b><br>Consumer behavior & buyer decision<br>Maslow's hierarchy of needs<br>AIDA model, Porter's five forces<br>Brand equity & loyalty]:::theory
    H[<b>MARKETING CYCLE</b><br>Research → Strategy → Implementation<br>→ Evaluation → Feedback]:::process
    I[<b>OUTCOMES</b><br>Customer loyalty, market share,<br>brand advocacy, profitability]:::outcome

    A -->|aims to| B
    B -->|requires| C
    C -->|begins with| D
    D -->|feeds into| E
    E -->|shapes| F
    D & E & F -->|guided by| G
    G -->|drives| H
    H -->|yields| I

    classDef title fill:#f0f7ff,stroke:#4a6fa5,stroke-width:2px,color:#333,stroke-dasharray: 5 5
    classDef goal fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#333
    classDef core fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#333
    classDef theory fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:#333
    classDef process fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px,color:#333
    classDef outcome fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#333
```