#AQARION RO-Crate

An experimental extension profile for RO-Crate research objects.

---

Overview

AQARION RO-Crate extends the RO-Crate standard to support semantic claim structures, fine-grained evidence provenance, machine-verifiable certificates, and reproducible validation workflows.

This profile enables research objects to contain not just files and metadata, but also the justification for every scientific assertion they contain.

```
┌─────────────────────────────────────────────────────────────┐
│                     RO-Crate Core                           │
│  (files, metadata, provenance, workflows, relationships)    │
├─────────────────────────────────────────────────────────────┤
│                     AQARION Profile                         │
│  (claims, evidence, dependencies, certificates)             │
└─────────────────────────────────────────────────────────────┘
```

---

Why AQARION RO-Crate?

Problem Solution
Research artifacts contain claims, but the justification is often implicit or scattered. Claims are first‑class entities with explicit status and evidence links.
Evidence is hard to trace back to specific assertions. Each claim links directly to its supporting proof, computation, or dataset.
Reproducibility requires manual verification. Certificates provide machine‑verifiable SHA‑256 anchors.
Results change, but history is opaque. Immutable revision history tracks claim evolution and retractions.

---

Core Concepts

Claims

A claim is a scientific assertion — a theorem, lemma, computational result, or benchmark observation. Each claim is a JSON object with:

· id – Unique identifier (e.g., CLAIM-001)
· type – e.g., Theorem, Lemma, Benchmark
· statement – Human‑readable description
· profile and profile_version – AQARION profile metadata
· schema_version – Version of the claim schema
· provenance – Creation metadata (creator, timestamp, pipeline)
· dependencies – Typed list of other claims or definitions it relies on
· evidence – Links to proofs, scripts, or datasets, each with its own integrity certificate
· status – PROPOSED, PROVED, CERTIFIED, or RETRACTED
· certificate – SHA‑256 hash of the claim‑validation output

Evidence

Evidence is the supporting material for a claim. It can be:

· Formal proof – Lean, Coq, or Isabelle source
· Computational verification – Python script with exact arithmetic
· Counterexample – A counterexample that falsifies a previous claim
· Dataset – Input data used in the verification

Each evidence item carries an integrity certificate (SHA‑256 of the file or output).

Certificates

A certificate is a machine‑readable attestation that a claim has been verified. It is typed:

· claim-validation – certifies the claim’s verification status.
· evidence-integrity – certifies the integrity of an evidence file or result.

Every certificate includes the algorithm (SHA‑256) and the hash value.

Revisions

AQARION RO-Crate tracks the entire history of a claim's lifecycle. All changes are immutable and preserved in the revisions/ directory, including a killed claims archive for claims that were retracted or falsified.

---

Repository Structure

```
aqarion-ro-crate/
│
├── ro-crate-metadata.json          # Standard RO-Crate metadata
│
├── aqarion/
│   ├── claims/
│   │   ├── CLAIM-001.json          # Primary theorem
│   │   └── CLAIM-002.json          # Benchmark result
│   │
│   ├── definitions/
│   │   └── DEF-001.json            # Core definitions
│   │
│   ├── evidence/
│   │   ├── theorem/
│   │   │   └── Quotient.lean       # Lean formal proof
│   │   ├── computation/
│   │   │   └── verify.py           # Executable verification
│   │   └── datasets/
│   │       └── kaprekar.json       # Benchmark data
│   │
│   ├── verification/
│   │   ├── certificate.json        # Canonical certificate
│   │   └── provenance.json         # W3C PROV provenance
│   │
│   └── revisions/
│       ├── history.json            # Immutable event log
│       └── killed/                 # Killed claims archive
│           └── KC-001.json         # Falsified claim (preserved)
│
├── LICENSE
└── README.md
```

---

Claim Example

aqarion/claims/CLAIM-001.json

```json
{
  "profile": "AQARION-RO-Crate",
  "profile_version": "0.1.0",
  "schema_version": "1.0",

  "id": "CLAIM-001",
  "type": "Theorem",
  "statement": "The gap observable partition defines an exact deterministic quotient for the 4‑digit Kaprekar map.",

  "provenance": {
    "created": "2026-07-06T12:00:00Z",
    "creator": "AQARION Research Node #10878",
    "generated_by": "AQARION verification pipeline v19.0"
  },

  "dependencies": [
    { "id": "DEF-gap-partition", "type": "definition" },
    { "id": "LEMMA-kaprekar-deterministic", "type": "lemma" }
  ],

  "evidence": [
    {
      "type": "formal-proof",
      "artifact": "evidence/theorem/Quotient.lean",
      "certificate": {
        "type": "evidence-integrity",
        "algorithm": "SHA-256",
        "value": "a1b2c3d4e5f6..."
      }
    },
    {
      "type": "exhaustive-verification",
      "artifact": "evidence/computation/verify.py",
      "result": "PASS",
      "certificate": {
        "type": "evidence-integrity",
        "algorithm": "SHA-256",
        "value": "f6e5d4c3b2a1..."
      }
    }
  ],

  "status": "CERTIFIED",
  "certificate": {
    "type": "claim-validation",
    "algorithm": "SHA-256",
    "value": "be7ff691d39499d6cf3ef2b157a764c980b787d6c6a1c86ad6ac5a1e065b4329"
  }
}
```

---

Status: Experimental

AQARION RO-Crate is currently an experimental extension profile. It is being developed as part of the broader AQARION research framework and is open to community feedback.

Component Status
Claim schema ✅ Stable
Evidence model ✅ Stable
Certificate model ✅ Stable
Provenance model ✅ Stable
RO-Crate metadata compatibility 🟡 In progress
Validator tooling 🟡 In progress
Integration with AQARION verification engine 🔵 Planned

---

Relationship to Core RO-Crate

AQARION RO-Crate is an experimental extension profile implemented as a forked prototype of the RO-Crate ecosystem. The purpose of the fork is to test claim, evidence, certificate, and validation structures before proposing compatibility improvements or formal profile adoption upstream.

```
RO-Crate Core
     │
     ▼
AQARION RO-Crate (this repository)
     │
     ▼
AQARION Framework (verification, certification, event sourcing)
```

---

Getting Started

```bash
git clone https://github.com/quantarion369-arch/Aqarion-Ro_crate.git
cd Aqarion-Ro_crate
```

Browse the aqarion/ directory to explore claims, evidence, and certificates.

Validation

Validate against RO-Crate tooling:

```bash
ro-crate-validator ./ro-crate-metadata.json
```

Validate AQARION‑specific structure:

```bash
python -m aqarion.validator ./aqarion/
```

---

Contributing

AQARION RO-Crate is an open research prototype. Contributions are welcome in the following areas:

1. Profile definition – Refining the JSON schema for claims, evidence, and certificates
2. Validator tooling – Python and TypeScript validators
3. Examples – More research object examples
4. Tooling integration – RO‑Crate Python library extensions
5. Documentation – User guides and tutorials

---

Related Projects

Project Description
RO-Crate Core research object packaging standard
AQARION‑ARITHMETIC Mathematical framework for exact quotient certification
AQARION‑RO‑Crate‑Py Python library for working with AQARION RO-Crates

---

License

· Code: MIT
· Documentation: CC‑BY‑4.0
· RO‑Crate core: Apache 2.0 (inherited from upstream)

---

Citation

If you use AQARION RO-Crate in your research, please cite:

```
AQARION Research Node #10878. AQARION RO-Crate: Experimental Extension Profile
for RO-Crate Research Objects. GitHub repository.
https://github.com/quantarion369-arch/Aqarion-Ro_crate
```

---

Contact

· Maintainer: AQARION Research Node #10878
· Repository: github.com/quantarion369-arch/Aqarion-Ro_crate
· Framework: AQARION‑ARITHMETIC

---

Part of the AQARION research framework for verifiable computational mathematics.

---

This is the GitHub repository for contributing to the [Research Object Crate](https://researchobject.github.io/ro-crate/) specification.

The [docs/](docs/) folder has the [MarkDown](https://guides.github.com/features/mastering-markdown) content that is rendered to <https://researchobject.github.io/ro-crate/> by [GitHub pages](https://pages.github.com/). Alias <http://researchobject.org/ro-crate/> (note, no https) redirects.

Feel free to use other folders for non-web content, e.g. examples, JSON-LD contexts, test scripts.

## Contribute

This repository is coordinated by the [RO-Crate team](https://researchobject.github.io/ro-crate/#contribute).

To suggest changes, improvements or issues, use the GitHub repository
<https://github.com/ResearchObject/ro-crate> - if you are new to GitHub or Open
Source you may appreciate the [GitHub guides](https://guides.github.com/) like
[Hello World](https://guides.github.com/activities/hello-world/),
[MarkDown](https://guides.github.com/features/mastering-markdown/) and [How to
contribute to open source](https://opensource.guide/how-to-contribute/)

You are welcome to [join us](https://github.com/ResearchObject/ro-crate/issues/1)! 

Contributors are expected to comply with our [Code of Conduct](CODE_OF_CONDUCT.md)
to ensure an open and inclusive environment.

## License

* © 2019-2025 Research Object Crate contributors <https://github.com/ResearchObject/ro-crate/graphs/contributors>
* © 2018-2020 University of Technology Sydney, Australia
* © 2018-2025 The University of Manchester, UK

The specification and documentation maintained in this repository is Open Source and licensed as [Apache License, version 2.0](LICENSE), see <https://www.apache.org/licenses/LICENSE-2.0> for details.

Any contributions received are assumed to be [covered by the Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0#contributions).

The RO-Crate JSON-LD contexts `context.json` and JSON-LD examples within this specification are distributed under [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/). 
