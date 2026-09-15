# LEM — Location Encoding Model 1.0

RC2 candidate for a **technical specification / research report** preprint.

* Author identified in the manuscript: **Piotr Augustyniak, MSc**
* Affiliation: Poznan University of Technology, Faculty of Computing and Telecommunications
* Report number: RP/01/2026 PL
* Version date: 2026-09-13
* Build system: pdfLaTeX + BibTeX

## Key decisions in Model 1.0

* LEM stands exclusively for **Location Encoding Model**.
* Text values contain from 1 to 256 Unicode code points; octet limits belong to the respective representation.
* `Level.value` is a signed `int32` integer.
* Equivalence means exact equality of the decoded partial tuple `(Site?, Building?, Level?, ReferenceSpace?, RelativePosition?)`.
* The core model does not infer synonyms or identity of natural-language names.
* DNS-safe is a lossy presentation alias, not a reversible LEM representation.
* The TLV profile uses T = 1 octet, L = 2 octets, and a 5-octet representation of the numeric `Level` value (`kind` + `int32`).

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

```bash
latexmk -pdf main.tex
```

The project is prepared for import into Overleaf as a ZIP archive. The main document is `main.tex`, and `latexmkrc` selects pdfLaTeX.

## Artifact validation

```bash
python3 -m venv .venv
. .venv/bin/activate

pip install -r tests/requirements.txt

python tests/validate.py
pyang yang/lem-location.yang
```

## Persistent identifiers and project infrastructure

The RC2 version uses the persistent namespace:

`https://w3id.org/lem/`

The intended identifiers are:

* LEM 1.0 specification: `https://w3id.org/lem/1.0/specification`
* Core JSON Schema: `https://w3id.org/lem/1.0/schema/core`
* Emergency profile: `https://w3id.org/lem/1.0/profile/emergency`
* Network infrastructure profile: `https://w3id.org/lem/1.0/profile/network-infrastructure`
* YANG namespace: `https://w3id.org/lem/yang/lem-location`

The project repository, W3ID redirect configuration, and archived releases are maintained within **Poznan University of Technology, Faculty of Computing and Telecommunications, research group led by Piotr Zwierzykowski**. The project infrastructure is not owned by the author's or group leader's private account. The technical GitHub organization identifier and target redirect addresses are to be specified when configuring the repository and registering the W3ID namespace. Authorship of the report and copyright ownership are separate matters.

## Scientific status

Version 1.0 is a technical specification supported by syntactic validation of the associated artifacts. It does not yet include an experimental comparison of independent implementations. Such an experiment is recommended as a basis for a subsequent scientific research paper.

## Authorship and licenses

The sole author of the report is **Piotr Augustyniak**. Piotr Zwierzykowski is identified as the research group leader and is **not a co-author of this version**.

The institution and research group identified above maintain the project infrastructure, including the repository and persistent-identifier configuration. This does not, by itself, make them authors of the report or copyright holders of its content.

* The report text, LaTeX sources, and original tables and diagrams are released under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license. Details and the recommended attribution format are provided in `LICENSE-DOCUMENTATION.md`.

* The JSON Schemas, YANG module, validation code, and test vectors are released under the Apache License 2.0. The full license text is provided in `LICENSE-CODE`, with scope and attribution information in `NOTICE`.

* The licenses above do not cover Poznan University of Technology logos, trademarks, the `ppfcmthesis.cls` document class, or third-party materials. These elements remain subject to the rights of their respective owners.
