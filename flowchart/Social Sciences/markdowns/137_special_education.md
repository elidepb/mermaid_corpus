```mermaid
flowchart TD
    A[<b>Special Education</b><br>Specially designed instruction<br>for students with disabilities]:::title
    B[<b>GOAL</b><br>Provide FAPE in the LRE<br>and meet individualized needs]:::goal
    C[<b>IDENTIFICATION PROCESS</b>]:::process
    subgraph D[Child Find & Referral]
        D1[Outreach to identify children<br>with potential disabilities<br>Teacher/parent referral]
    end
    subgraph E[Evaluation & Eligibility]
        E1[Multidisciplinary evaluation<br>(cognitive, academic, behavioral)<br>IDEA disability category determination]
    end
    F[<b>IEP DEVELOPMENT</b><br>Team (parents, teachers, specialists)<br>writes IEP: present levels, goals,<br>accommodations, services, placement]:::iep
    G[<b>SERVICE DELIVERY</b><br>Specialized instruction,<br>related services (speech, OT, PT),<br>accommodations & modifications]:::services
    H[<b>MONITORING & REVIEW</b><br>Progress monitoring, annual<br>IEP review, triennial reevaluation]:::monitoring
    I[<b>OUTCOMES</b><br>Meaningful educational benefit,<br>inclusion, independence]:::outcome

    A -->|aims to| B
    B -->|requires| C
    C -->|begins with| D
    D -->|leads to| E
    E -->|if eligible, leads to| F
    F -->|authorizes| G
    G -->|tracked by| H
    H -->|feeds back to| F
    H -->|ensures| I

    classDef title fill:#f0f7ff,stroke:#4a6fa5,stroke-width:2px,color:#333,stroke-dasharray: 5 5
    classDef goal fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#333
    classDef process fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#333
    classDef iep fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:#333
    classDef services fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px,color:#333
    classDef monitoring fill:#fff9c4,stroke:#f9a825,stroke-width:2px,color:#333
    classDef outcome fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#333
```