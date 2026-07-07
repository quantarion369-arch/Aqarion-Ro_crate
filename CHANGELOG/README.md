AQARION RO-Crate explores a research object model where scientific claims, supporting evidence, verification procedures, and cryptographic certificates are represented as explicit machine-readable entities.

---

# CHANGELOG

All notable changes to this project will be documented in this file.

This project follows a research-object development model where
semantic changes, schema decisions, and verification milestones
are recorded explicitly.

---

## [0.1.0] - Initial Experimental Profile

### Added

- Initial AQARION Research Object Profile concept.
- Extension model built on top of RO-Crate.
- Separation between:
  - RO-Crate artifact description layer.
  - AQARION claim verification layer.
- Initial directory structure proposal:

                 Human Researcher
                       |
                       v
                AQARION Objects
                       |
        +--------------+--------------+
        |                             |
        v                             v
    RO-Crate                    Verification Engine
    Packaging                   Proof / Computation
        |                             |
        +--------------+--------------+
                       |
                       v
              Certified Research Object
                       |
                       v
                 AI Research Assistant

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

#AQARION RO-Crate

An experimental extension profile for RO-Crate research objects.

---

#Overview

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

#Why AQARION RO-Crate?

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
· statement – Human‑readable description
· depends_on – List of other claims or definitions it relies on
· evidence – Links to proofs, scripts, or datasets
· status – PROPOSED, PROVED, CERTIFIED, or RETRACTED
· certificate – SHA‑256 hash of the verification output

Evidence

Evidence is the supporting material for a claim. It can be:

· Formal proof – Lean, Coq, or Isabelle source
· Computational verification – Python script with exact arithmetic
· Counterexample – A counterexample that falsifies a previous claim
· Dataset – Input data used in the verification

Certificates

A certificate is a machine‑readable attestation that a claim has been verified. It includes:

· Claim ID and version
· Verification timestamp
· SHA‑256 of the verification output
· Reference to the verification workflow

Revisions

AQARION RO-Crate tracks the entire history of a claim's lifecycle. All changes are immutable and preserved in the revisions/ directory.

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
  "id": "CLAIM-001",
  "type": "Theorem",
  "statement": "The gap observable partition defines an exact deterministic quotient for the 4‑digit Kaprekar map.",
  "depends_on": [
    "DEF-gap-partition",
    "LEMMA-kaprekar-deterministic"
  ],
  "evidence": [
    {
      "type": "formal-proof",
      "artifact": "evidence/theorem/Quotient.lean"
    },
    {
      "type": "exhaustive-verification",
      "artifact": "evidence/computation/verify.py",
      "result": "PASS",
      "certificate": {
        "algorithm": "SHA-256",
        "value": "be7ff691d39499d6cf3ef2b157a764c980b787d6c6a1c86ad6ac5a1e065b4329"
      }
    }
  ],
  "status": "CERTIFIED",
  "certificate": {
    "algorithm": "SHA-256",
    "value": "be7ff691d39499d6cf3ef2b157a764c980b787d6c6a1c86ad6ac5a1e065b4329"
  }
}
```

---

Status: Experimental

AQARION RO-Crate is currently an experimental extension profile. It is being developed as part of the broader AQARION research framework and is open to community feedback.

· ✅ Claim structure defined
· ✅ Evidence provenance specified
· ✅ Certificate format documented
· 🔄 Validator tooling in progress
· 🔄 RO-Crate compliance validation

---

Relationship to Core RO-Crate

AQARION RO-Crate is a fork of the RO-Crate repository, used to prototype the extension profile. The goal is to eventually merge the AQARION profile back into the RO-Crate ecosystem as an official profile extension.

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
