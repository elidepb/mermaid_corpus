```mermaid
flowchart TD
    MedicalInformatics[Medical Informatics] --> EHR[Electronic Health Records]
    MedicalInformatics --> Decision[Clinical Decision Support]
    MedicalInformatics --> Standards[Health Information Standards]
    EHR --> Implementation[EHR Implementation]
    EHR --> Interoperability[Interoperability]
    Decision --> CDS[CDS Systems]
    Decision --> Alerts[Clinical Alerts]
    Standards --> HL7[HL7 Standards]
    Standards --> DICOM[DICOM]
```