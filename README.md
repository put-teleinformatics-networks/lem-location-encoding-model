# LEM — Location Encoding Model 1.0

**Location Encoding Model (LEM) 1.0** is a compact, representation-independent information model for describing the physical location of an entity.

The specification defines a common semantic core, value domains, consistency constraints, a deterministic canonical form, and mappings to multiple representations.

## Project status

**Version:** 1.0
**Document type:** Technical specification / research report
**Author:** Piotr Augustyniak, MSc
**Affiliation:** Poznan University of Technology, Faculty of Computing and Telecommunications
**Report number:** RP/01/2026 PL
**Version date:** 2026-09-13
**Build system:** pdfLaTeX + BibTeX

Version 1.0 is the released specification of the LEM model and its associated machine-readable and validation artefacts.

## Key decisions in Model 1.0

* LEM stands exclusively for **Location Encoding Model**.
* Text values contain from 1 to 256 Unicode code points; octet limits belong to the respective representation.
* `Level.value` is a signed `int32` integer.
* Equivalence means exact equality of the decoded partial tuple (`Site?`, `Building?`, `Level?`, `ReferenceSpace?`, `RelativePosition?`).
* The core model does not infer synonyms or identity of natural-language names.
* DNS-safe is a lossy presentation alias, not a reversible LEM representation.
* The TLV profile uses `T = 1` octet, `L = 2` octets, and a 5-octet representation of the numeric Level value (`kind + int32`).

## Repository structure

```text
main.tex
bibliography.bib

chapters/                  Chapters 1–8 and glossary
schemas/                   Core schema and two JSON Schema profiles
yang/lem-location.yang     Informative YANG mapping
tests/                     20 positive and negative test vectors
figures/                   Logos required by the document class
```

## Building the document

```text
latexmk -pdf main.tex
```

The project is prepared for import into Overleaf as a ZIP archive. The main document is `main.tex`, and `latexmkrc` selects pdfLaTeX.

## Artifact validation

```text
python3 -m venv .venv
. .venv/bin/activate

pip install -r tests/requirements.txt

python tests/validate.py
pyang yang/lem-location.yang
```

The repository contains machine-readable schemas, a YANG module, and positive and negative test vectors used to validate the associated artefacts.

## Persistent identifiers and project infrastructure

A permanent W3ID namespace has been **requested** for LEM:

https://w3id.org/lem/

The requested identifiers are:

* **LEM 1.0 specification:** https://w3id.org/lem/1.0/specification
* **Core JSON Schema:** https://w3id.org/lem/1.0/schema/core
* **Emergency profile:** https://w3id.org/lem/1.0/profile/emergency
* **Network infrastructure profile:** https://w3id.org/lem/1.0/profile/network-infrastructure
* **YANG namespace:** https://w3id.org/lem/yang/lem-location

The W3ID namespace request is maintained through the W3ID permanent identifier service. The identifiers become active when the corresponding W3ID configuration is accepted and deployed by the W3ID maintainers.

Project repository:

https://github.com/put-teleinformatics-networks/lem-location-encoding-model

Project infrastructure is maintained within the research environment of the Faculty of Computing and Telecommunications at Poznan University of Technology, including the GitHub organization and persistent-identifier configuration.

The project repository and research infrastructure are institutional project resources. Authorship of the report and copyright ownership are separate matters.

## Scientific status

Version 1.0 is a technical specification supported by syntactic and machine-verifiable validation of the associated artefacts.

The specification does not claim experimental comparison of independent implementations. Such an experiment is recommended as a basis for subsequent scientific research concerning interoperability, implementation behaviour, and practical deployment of LEM.

## Authorship and licenses

The sole author of the report is **Piotr Augustyniak**.

**Piotr Zwierzykowski** is identified as the research group leader and supervisor of the project. He is not a co-author of this version of the LEM report.

The institution and research group identified above maintain the project infrastructure, including the repository and persistent-identifier configuration. This does not, by itself, make them authors of the report or copyright holders of its content.

* The report text, LaTeX sources, and original tables and diagrams are released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. Details and the recommended attribution format are provided in `LICENSE-DOCUMENTATION.md`.
* The JSON Schemas, YANG module, validation code, and test vectors are released under the **Apache License 2.0**. The full license text is provided in `LICENSE-CODE`, with scope and attribution information in `NOTICE`.
* The licenses above do not cover Poznan University of Technology logos, trademarks, the `ppfcmthesis.cls` document class, or third-party materials. These elements remain subject to the rights of their respective owners.

## About

**LEM — Location Encoding Model 1.0** provides:

* a representation-independent location information model,
* defined semantic constraints and equivalence rules,
* JSON Schema profiles,
* an informative YANG mapping,
* test vectors,
* and reproducible validation artefacts.

The project is intended to provide a stable semantic foundation for representing physical location information across different technical representations and application profiles.
