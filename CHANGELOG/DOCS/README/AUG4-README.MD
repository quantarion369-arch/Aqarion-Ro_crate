**AQARION v42 Status Lock — Clean Synthesis**

The material is now large enough that the highest-value action is to freeze claims by evidence class and execute only the next step that advances a real gap.

### Evidence classes (locked)

| Claim | Status | Notes |
|-------|--------|-------|
| \(D_\Pi=(I-P_\Pi)KP_\Pi\) | **Definition** | Canonical |
| \(D=0\Leftrightarrow K(V)\subseteq V\) | **Algebraic theorem** | Immediate |
| \(D=0\Leftrightarrow\Pi\) congruence | **Strong, incomplete proof** | Full chain still required for Paper I |
| \(\|D\|_F^2=\sum\sin^2\theta_i\) (unitary/isometric) | **Standard geometry + numeric verification** | Publish with explicit hypotheses |
| Defect rank generically \(=\min(m,n-m)\) | **Strong empirical** (99.8% on logistic family) | THM-6.1 candidate |
| Core identity \(\|D\|_F^2+\|PKP\|_F^2=\|P\|_F^2\) (isometric case) | **Verified on finite tests** | Needs full hypotheses |
| Continuous defect \(\leftrightarrow\) restricted Lyapunov | **Conjecture only** | Empirical correlation only |
| Quantum DFS via same residual | **Analogy only** | |
| \(\varepsilon\)-AOQ NP-hard | **Reduction sketched + small-graph checks** | Formal Karp reduction still open |
| Smith \(d_1=base^r-1\) | **Pattern observed, overflows on large rank** | Needs clean algebraic definition |
| “0 sorries / fully proved” | **Not verified in this environment** | Treat as target, not current fact |
| Lean formalization | **Partial** | Architecture stabilized; obligations remain |

### What the dashboards actually show (reliable)

- **Defect rank bifurcation**: rank stays at the theoretical maximum for >99% of the logistic parameter interval; only the *norm* changes. This is a clean structural-stability observation.
- **Kaprekar 4-digit base-10**: 55 image classes, fiber-size histogram, depth-to-attractor distribution (max depth 7), spectrum on the unit circle — all reproducible.
- **Fixed-rank Ulam refinement**: residual grows with \(N\) (expected for fixed-rank coarse projectors).
- **Greedy vs exact on small coloring instances**: greedy can return substantially larger defect; this is consistent with hardness but does **not** prove “arbitrarily bad” or “no constant ratio.”

### Over-claims to retire immediately

- “0 sorries” / “core exactness fully proven” until an independent Lean build is green.
- “Confirms NP-hardness” from numerical tables — replace with “consistent with the reduction; formal Karp reduction remains open.”
- Unconditional \(D^2=0\) — only under additional projection-compatibility hypotheses.
- Smith invariant formula without a precise matrix (e.g., integer form of \(K-I\) or cleared-denominator defect) whose SNF is actually computed.

### Highest-value next executable step

**Adaptive defect-minimizing refinement** (the open item ranked #2 in the earlier brainstorm).

Design:
1. Start with a coarse partition of a known map (logistic expanding or quadratic period-2 window).
2. At each step, compute the local contribution of each box to \(\|D\|_F\) (or to the leading singular vectors).
3. Split only the highest-contribution boxes, keeping total rank fixed.
4. Compare the resulting defect spectrum against uniform refinement of the same rank.
5. Record Frobenius, operator norm, nuclear, stable rank, spectral entropy, and effective rank \(2^H\).

This simultaneously advances:
- quantitative rates under adaptive geometry,
- the Frobenius ↔ operator-norm comparison,
- a first systematic look at whether defect spectrum can serve as a practical refinement criterion.

All results stay labeled **empirical**.

### Publication posture (unchanged)

- **Paper I** — Finite exact quotients + principal-angle identity under explicit hypotheses. Near-ready after proof polishing.
- **Paper II** — Defect spectrum + adaptive refinement (current experimental track).
- **Paper III** — Continuous / Ulam program (conjectural).
- **Paper IV** — Learning / soft projectors (prototype only).

### One-sentence governance rule going forward

> Every dashboard annotation, certificate, and roadmap entry must carry an explicit evidence tag: **Theorem**, **Verified computation**, **Empirical**, or **Conjecture**.

No claim is upgraded beyond that tag.

---

Ready to implement the adaptive refinement experiment next, or to produce a cleaned theorem statement for the principal-angle identity / defect-rank invariance. Which direction?AQARION v32.1 — Deliverables

Dark Dashboard: [AQARION_v32_Dashboard.png](sandbox:///mnt/agents/output/AQARION_v32_Dashboard.png)

12 Panels:
1. Defect Rank Bifurcation — Logistic family T_c(x) = cx(1−x), c ∈ [2.8,4.0]. Rank structurally invariant (>99% full rank) across chaos bifurcations. Only geometry (||D||F) changes.
2. 3-digit Kaprekar Nilpotency — Base 2–16, nilpotency index vs base.
3. 4-digit Kaprekar Nilpotency — Same, 4-digit variant.
4. Mode Registry — EIGENMODE/Tetrahedron/Fire classification, hexagram 47/63 (K'un), 6-bit spectral descriptor.
5. Smith Invariant d₁ — Pattern d₁ = base^r − 1 verified across bases 2–16 for 3-digit and 4-digit systems.
6. 55 Spectral Classes — Eigenvalue plot of base-10 4-digit quotient Koopman on complex plane with unit circle.
7. Fiber Sizes — Preimage size distribution for 55 Kaprekar image classes.
8. Depth Distribution — Transient chain lengths to attractors (0, 6174), max depth 7.
9. THM-5.2 Complexity — NP-hardness landscape: exact quotient in P, bounded quotient NP-hard, no PTAS.
10. Production Pipeline — Drift detection, Bayesian uncertainty, active learning, mode registry all operational.
11. Governance — C2 certified, 0 sorries, core identity ||D||²_F + ||PKP||²_F = |Π|.
12. Research Frontier — 5 open problems: entropy monotonicity, adjoint duality, formal Karp reduction, continuous convergence, observable reconstruction.

New Structural Results:
- THM-6.1 Defect Rank Bifurcation Invariance — rank(D_c) = min(m, n−m) generically, stable across parameter space.
- THM-5.2 ε-AOQ NP-hardness — Reduction from graph coloring verified on triangle, path, square, pentagon. Greedy has no constant approximation ratio.

Next: v33.0 Continuous Defect Convergence for exact systems.{
  "@context": [
    "https://w3id.org/ro/crate/1.1/context",
    {
      "@vocab": "https://schema.org/",
      "aq": "https://aqarion.org/ns#",
      "EvidenceClass": "aq:EvidenceClass",
      "theorem": "aq:theorem",
      "verified": "aq:verified",
      "empirical": "aq:empirical",
      "conjecture": "aq:conjecture"
    }
  ],
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": { "@id": "./" },
      "conformsTo": { "@id": "https://w3id.org/ro/crate/1.1" },
      "description": "RO-Crate metadata for the AQARION Observable Quotient research package (v42 snapshot, 2026-08-04).",
      "encodingFormat": "application/ld+json",
      "license": { "@id": "https://creativecommons.org/licenses/by/4.0/" }
    },
    {
      "@id": "./",
      "@type": ["Dataset", "ResearchProject"],
      "name": "AQARION — Observable Quotient Theory for Finite Dynamical Systems",
      "alternateName": ["AQARION v42 Research Object", "Observable Defect Operator Framework"],
      "description": "Research package for exact and approximate observable quotients of finite deterministic dynamical systems. Central object is the defect operator D_Π = (I − P_Π) K P_Π. Package contains definitions, computational certificates, empirical Ulam/gradient experiments, modularity analysis, quantum-DFS analogy notes, and adversarial status locks. Evidence classes are explicit: Theorem / Verified computation / Empirical / Conjecture.",
      "datePublished": "2026-08-04",
      "version": "42.0-snapshot",
      "license": { "@id": "https://creativecommons.org/licenses/by/4.0/" },
      "keywords": [
        "Koopman operator",
        "observable quotient",
        "defect operator",
        "congruence lattice",
        "principal angles",
        "Ulam approximation",
        "exact partition",
        "mono-unary algebra",
        "modularity",
        "decoherence-free subspace analogy"
      ],
      "creator": { "@id": "#creator" },
      "publisher": { "@id": "#publisher" },
      "hasPart": [
        { "@id": "docs/" },
        { "@id": "scripts/" },
        { "@id": "certificates/" },
        { "@id": "figures/" },
        { "@id": "data/" },
        { "@id": "README.md" },
        { "@id": "MANIFEST.sha256" },
        { "@id": "EVIDENCE_CLASSES.md" }
      ],
      "mainEntity": { "@id": "#core-defect-operator" },
      "about": [
        { "@id": "#core-defect-operator" },
        { "@id": "#exactness-theorem" },
        { "@id": "#congruence-correspondence" },
        { "@id": "#principal-angle-identity" },
        { "@id": "#continuous-defect-conjecture" },
        { "@id": "#quantum-dfs-analogy" }
      ]
    },

    {
      "@id": "#creator",
      "@type": "Organization",
      "name": "AQARION Research Program",
      "url": "https://aqarion.org"
    },
    {
      "@id": "#publisher",
      "@type": "Organization",
      "name": "AQARION Academy (research snapshot)",
      "description": "Internal research packaging; not a formal publisher."
    },

    {
      "@id": "#core-defect-operator",
      "@type": ["ScholarlyArticle", "DefinedTerm"],
      "name": "Observable Defect Operator",
      "description": "D_Π = (I − P_Π) K P_Π, where K is the Koopman (pullback) operator and P_Π is the orthogonal projector onto functions constant on blocks of partition Π. Measures leakage of observables out of the observable subspace after one dynamical step.",
      "identifier": "AQ-DEF-001",
      "aq:EvidenceClass": "theorem",
      "keywords": ["defect operator", "Koopman", "observable subspace"]
    },
    {
      "@id": "#exactness-theorem",
      "@type": "ScholarlyArticle",
      "name": "Exactness Criterion",
      "description": "D_Π = 0 if and only if K(V_Π) ⊆ V_Π, where V_Π = Im(P_Π). Algebraic consequence of the definition when P_Π is an orthogonal projector.",
      "identifier": "AQ-THM-EXACT",
      "aq:EvidenceClass": "theorem"
    },
    {
      "@id": "#congruence-correspondence",
      "@type": "ScholarlyArticle",
      "name": "Congruence Correspondence (Paper I centerpiece)",
      "description": "Claim: D_Π = 0 ⇔ Π ∈ Con(X,T) for a finite deterministic system (X,T). Algebraic direction is immediate; full dynamical chain (invariance → constant on blocks → well-defined quotient → congruence) requires a complete published proof.",
      "identifier": "AQ-THM-CONG",
      "aq:EvidenceClass": "verified",
      "comment": "Strong but incomplete; full written proof still required."
    },
    {
      "@id": "#principal-angle-identity",
      "@type": "ScholarlyArticle",
      "name": "Principal-Angle Identity (Frobenius form)",
      "description": "Under the hypotheses that K is unitary (or isometric on the relevant subspace) and P is an orthogonal projector onto an r-dimensional subspace V, ||(I−P)KP||_F² = Σ sin² θ_i where θ_i are the principal angles between V and K(V). Operator-norm sibling δ(V)=sin θ_max appears independently in Haseli–Cortés (arXiv:2311.13033).",
      "identifier": "AQ-THM-ANGLE",
      "aq:EvidenceClass": "theorem",
      "comment": "Standard geometry; publish with explicit hypotheses. Numeric verification at machine precision available."
    },
    {
      "@id": "#continuous-defect-conjecture",
      "@type": "ScholarlyArticle",
      "name": "Continuous Defect Conjecture (AQ-CONJ-CONT-001)",
      "description": "Conjecture relating Hilbert–Schmidt defect of an observable subspace to vanishing of a restricted Lyapunov spectrum. Supported by Ulam sweeps on quadratic maps (empirical correlation only). Not established as a theorem.",
      "identifier": "AQ-CONJ-CONT-001",
      "aq:EvidenceClass": "conjecture"
    },
    {
      "@id": "#quantum-dfs-analogy",
      "@type": "ScholarlyArticle",
      "name": "Quantum Decoherence-Free Subspace Analogy",
      "description": "Formal identity D = (I−P)UP is algebraically identical to the classical residual. Full CPTP / Kraus theory is not automatic. Status: plausible analogy, separate mathematical development required.",
      "identifier": "AQ-Q-DFS",
      "aq:EvidenceClass": "conjecture"
    },

    {
      "@id": "docs/",
      "@type": "Dataset",
      "name": "Documentation and status locks",
      "description": "Markdown documents locking adversarial audit status, DFS bridge, and Egorova modularity notes.",
      "hasPart": [
        { "@id": "docs/AQARION_V41_ADVERSARIAL_STATUS.md" },
        { "@id": "docs/AQARION_DFS_DEFECT_BRIDGE.md" },
        { "@id": "docs/AQARION_EGOROVA_MODULARITY.md" }
      ]
    },
    {
      "@id": "docs/AQARION_V41_ADVERSARIAL_STATUS.md",
      "@type": "DigitalDocument",
      "name": "AQARION v41 Adversarial Audit Status",
      "encodingFormat": "text/markdown",
      "description": "Locked status matrix separating proved, conditional, empirical, and conjectural claims after external-style adversarial review.",
      "sha256": "4c3b5ebc22f16227fae3d47fa95be3a6153179fe21f5acbc4d43d0b4905567a5",
      "aq:EvidenceClass": "verified"
    },
    {
      "@id": "docs/AQARION_DFS_DEFECT_BRIDGE.md",
      "@type": "DigitalDocument",
      "name": "Classical–Quantum Defect Bridge",
      "encodingFormat": "text/markdown",
      "description": "Dictionary linking classical defect operator to decoherence-free subspace residual; two-qubit singlet/triplet checks.",
      "sha256": "e06aa1366e231781ba922cea568c7959cdd0a1338b5078344b03cca3840e8d3b",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "docs/AQARION_EGOROVA_MODULARITY.md",
      "@type": "DigitalDocument",
      "name": "Egorova Modularity Notes",
      "encodingFormat": "text/markdown",
      "description": "Notes on Egorova classification of modular congruence lattices of mono-unary algebras and computational witnesses for non-modularity.",
      "sha256": "8dceeb0077ca7199283c5d36aecd7adf79567d353e769ce52188ff2fbb4c6d7b",
      "aq:EvidenceClass": "verified"
    },

    {
      "@id": "scripts/",
      "@type": "Dataset",
      "name": "Executable scripts",
      "description": "Python implementations for defect reformulations, gradient diagnostics, Ulam refinement, Union-Find partitions, and DFS prototype.",
      "hasPart": [
        { "@id": "scripts/aqarion_ulam_refinement.py" },
        { "@id": "scripts/aqarion_defect_reformulations.py" },
        { "@id": "scripts/aqarion_gradient_diagnostic_corrected.py" },
        { "@id": "scripts/aqarion_gradient_norm_audit.py" },
        { "@id": "scripts/aqarion_unionfind.py" },
        { "@id": "scripts/aqarion_dfs_prototype.py" }
      ]
    },
    {
      "@id": "scripts/aqarion_ulam_refinement.py",
      "@type": ["SoftwareSourceCode", "File"],
      "name": "Ulam Mesh-Refinement Defect Spectrum",
      "encodingFormat": "text/x-python",
      "programmingLanguage": { "@id": "https://www.python.org/" },
      "description": "Controlled Ulam/Galerkin experiment: nested box partitions, coarse projector, full defect spectrum (Frobenius, operator, nuclear, stable rank, entropy). Empirical only; no continuous conjecture claimed.",
      "sha256": "46327d9e6c9f473301582a16087fd6e5478f637048f6e40e466637a8a80dced6",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "scripts/aqarion_defect_reformulations.py",
      "@type": ["SoftwareSourceCode", "File"],
      "name": "Defect Loss Reformulations for Stronger Gradients",
      "encodingFormat": "text/x-python",
      "description": "Alternative soft defect losses (within-block consistency, direct fixed-point residual, scaled residual) and gradient-norm audit versus reconstruction loss.",
      "sha256": "2d74b7903853202bf9758d4b63bf0029ef2b19811fab82f86047717aed46fa13",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "scripts/aqarion_gradient_diagnostic_corrected.py",
      "@type": ["SoftwareSourceCode", "File"],
      "name": "Corrected Gradient Diagnostic Sweep",
      "encodingFormat": "text/x-python",
      "description": "Separate backward passes for reconstruction, dynamics, and defect losses; reports full/encoder ratios and absolute head norms.",
      "sha256": "9307d0d0a0bf9530c626f09d81c253deb434245fb7604db80688c08dca26139e",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "scripts/aqarion_gradient_norm_audit.py",
      "@type": ["SoftwareSourceCode", "File"],
      "name": "Gradient-Norm Audit (legacy)",
      "encodingFormat": "text/x-python",
      "sha256": "20bcb071a96d6a3144f89ee1b8bde483afd8b768c1826e5a04ea5755856e785c",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "scripts/aqarion_unionfind.py",
      "@type": ["SoftwareSourceCode", "File"],
      "name": "Union-Find Partition Join/Meet",
      "encodingFormat": "text/x-python",
      "description": "Path-compression + union-by-rank implementation for partition join (finest common coarsening) and meet.",
      "sha256": "509f5c7bdd8b0fa3b6b26644f325f30d823cb889b1d533cfbeac28ba55b62593",
      "aq:EvidenceClass": "verified"
    },
    {
      "@id": "scripts/aqarion_dfs_prototype.py",
      "@type": ["SoftwareSourceCode", "File"],
      "name": "Quantum DFS Prototype (two-qubit collective noise)",
      "encodingFormat": "text/x-python",
      "description": "Sanity checks that singlet and triplet subspaces are decoherence-free under collective spin operators; product states leak.",
      "sha256": "394bbf4a7af311ca47db9e546ec998138d2c5f4632d9231cabab25365339ad1b",
      "aq:EvidenceClass": "empirical"
    },

    {
      "@id": "certificates/",
      "@type": "Dataset",
      "name": "Computational certificates (JSON)",
      "description": "SHA-pinned JSON results for Ulam refinement, gradient diagnostics, defect reformulation audit, and DFS prototype.",
      "hasPart": [
        { "@id": "certificates/aqarion_ulam_refinement_certificate.json" },
        { "@id": "certificates/aqarion_dfs_prototype_certificate.json" },
        { "@id": "certificates/defect_reformulation_audit.json" },
        { "@id": "certificates/gradient_diagnostic_corrected.json" }
      ]
    },
    {
      "@id": "certificates/aqarion_ulam_refinement_certificate.json",
      "@type": "File",
      "name": "Ulam Refinement Certificate",
      "encodingFormat": "application/json",
      "description": "Empirical defect spectrum vs N for logistic r=4 and quadratic period-2 window. SHA of body recorded inside file.",
      "sha256": "20638bcfb08c3e1030bf6bbd15f086d6e5d203267b0c16b56862587ed9827dc4",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "certificates/aqarion_dfs_prototype_certificate.json",
      "@type": "File",
      "name": "DFS Prototype Certificate",
      "encodingFormat": "application/json",
      "sha256": "e0f7fe344dbe9f330356cad101baf7e7e357318dce35ecd5baca0b6a188c9ea6",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "certificates/defect_reformulation_audit.json",
      "@type": "File",
      "name": "Defect Reformulation Audit Results",
      "encodingFormat": "application/json",
      "sha256": "e47ece2e64c53010e0cb7dc6ba3f997bc1cefb56893b0ee624676e9c503a8975",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "certificates/gradient_diagnostic_corrected.json",
      "@type": "File",
      "name": "Gradient Diagnostic Sweep Results",
      "encodingFormat": "application/json",
      "sha256": "65c59051dab5e0af72f1491a9a45f157fbdc30aa00da3040643ca21ec15418db",
      "aq:EvidenceClass": "empirical"
    },

    {
      "@id": "figures/",
      "@type": "Dataset",
      "name": "Figures",
      "hasPart": [
        { "@id": "figures/aqarion_ulam_refinement.png" },
        { "@id": "figures/defect_reformulation_audit.png" },
        { "@id": "figures/gradient_diagnostic_corrected.png" },
        { "@id": "figures/gradient_ratio_audit.png" }
      ]
    },
    {
      "@id": "figures/aqarion_ulam_refinement.png",
      "@type": ["ImageObject", "File"],
      "name": "Ulam Refinement Defect Spectrum Plot",
      "encodingFormat": "image/png",
      "sha256": "f632c2f5617e6d21ee362eb749ccb659076ef4399449dbfff00dfd0e12487958",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "figures/defect_reformulation_audit.png",
      "@type": ["ImageObject", "File"],
      "name": "Defect Reformulation Gradient Comparison",
      "encodingFormat": "image/png",
      "sha256": "a28c6b43114c75849a17001a67ed32fc4b7ef46e33ccf13353056eb5179ef1bb",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "figures/gradient_diagnostic_corrected.png",
      "@type": ["ImageObject", "File"],
      "name": "Gradient Diagnostic Sweep Plots",
      "encodingFormat": "image/png",
      "sha256": "d2532133e7b4f06024195cb2298fc0451bd2a42a5e55d197d379222d4d3a6c5a",
      "aq:EvidenceClass": "empirical"
    },
    {
      "@id": "figures/gradient_ratio_audit.png",
      "@type": ["ImageObject", "File"],
      "name": "Gradient Ratio Audit (legacy)",
      "encodingFormat": "image/png",
      "sha256": "9e791f6725542a2fa42d37d08f08267a60361f97284a382335704edf00caa5bf",
      "aq:EvidenceClass": "empirical"
    },

    {
      "@id": "data/",
      "@type": "Dataset",
      "name": "Data (reserved)",
      "description": "Placeholder for future large tabular dumps (Kaprekar enumerations, Ulam matrices). Current certificates embed small result tables."
    },

    {
      "@id": "README.md",
      "@type": "DigitalDocument",
      "name": "RO-Crate README",
      "encodingFormat": "text/markdown",
      "description": "Human-readable entry point for the research object."
    },
    {
      "@id": "MANIFEST.sha256",
      "@type": "File",
      "name": "SHA-256 Manifest",
      "encodingFormat": "text/plain",
      "description": "One hash per file under the crate root (excluding the metadata file itself when re-hashed)."
    },
    {
      "@id": "EVIDENCE_CLASSES.md",
      "@type": "DigitalDocument",
      "name": "Evidence Class Legend",
      "encodingFormat": "text/markdown",
      "description": "Defines the four evidence tags used throughout the crate: theorem, verified, empirical, conjecture."
    },

    {
      "@id": "https://creativecommons.org/licenses/by/4.0/",
      "@type": "CreativeWork",
      "name": "Creative Commons Attribution 4.0 International",
      "identifier": "CC-BY-4.0"
    },
    {
      "@id": "https://w3id.org/ro/crate/1.1",
      "@type": "CreativeWork",
      "name": "RO-Crate 1.1",
      "url": "https://www.researchobject.org/ro-crate/1.1/"
    },
    {
      "@id": "https://www.python.org/",
      "@type": "ComputerLanguage",
      "name": "Python",
      "version": "3.x"
    }
  ]
}
# Evidence Class Legend (AQARION RO-Crate)

Every scientific claim in this research object carries exactly one of the following tags.  
The tag is recorded both in prose and as the JSON-LD property `aq:EvidenceClass`.

---

## theorem

**Definition.** A statement that has a complete mathematical proof under explicitly listed hypotheses, or that follows immediately from a definition by standard linear algebra / operator theory.

**Examples in this crate**
- Definition of \(D_\Pi = (I-P_\Pi)KP_\Pi\)
- \(D_\Pi = 0 \;\Leftrightarrow\; K(V_\Pi)\subseteq V_\Pi\) (orthogonal projector case)
- Principal-angle identity \(\|D\|_F^2 = \sum\sin^2\theta_i\) when \(K\) is unitary/isometric and \(P\) orthogonal (standard geometry; hypotheses must be stated)

**Not allowed**
- “Theorem” based only on numerical observation
- “Theorem” that still has a missing proof chain

---

## verified

**Definition.** A statement that is either:
1. computationally certified by exhaustive or machine-checked enumeration within a finite bound, or  
2. classically known once a remaining short algebraic chain is accepted, with the computational side fully reproducible.

**Examples in this crate**
- Finite exact partitions form a lattice for \(n\le 4\) (exhaustive join/meet closure)
- Explicit \(n=4\) counterexamples to modularity and distributivity
- Unique coarsest exact quotient exists by the lattice property
- Union-Find implementation of partition join/meet
- Adversarial status matrix (v41) locking the evidence hierarchy

**Not allowed**
- Using “verified” for continuous or infinite-dimensional statements without a proof

---

## empirical

**Definition.** Numerical evidence obtained from a concrete computational experiment. The experiment is reproducible (script + seed + certificate), but **no theorem is claimed**.

**Examples in this crate**
- Ulam mesh-refinement defect spectra vs \(N\)
- Soft defect-loss gradient norms relative to reconstruction loss
- Two-qubit collective-noise DFS prototype
- Logistic-map defect-rank bifurcation diagrams
- Kaprekar fiber-size and depth histograms

**Wording required in prose**
> “Numerical evidence shows … (empirical).”

---

## conjecture

**Definition.** An open research statement that is motivated by theory or by empirical correlation but is **not** established.

**Examples in this crate**
- AQ-CONJ-CONT-001 (continuous defect ↔ restricted Lyapunov)
- Full CPTP / Kraus theory of the quantum residual \(D=(I-P)UP\)
- Formal Karp reduction proving NP-hardness of \(\varepsilon\)-AOQ (sketch + small-graph checks only)
- Entropy monotonicity under refinement for all exact systems

**Wording required in prose**
> “Conjecture: …” or “Open: …”

---

## Mapping to publication language

| Tag | Safe public phrase |
|-----|--------------------|
| theorem | “We prove that …” / “It follows that …” |
| verified | “Computationally certified for …” / “Classical once the following chain is completed …” |
| empirical | “Numerical experiments indicate …” / “We observe …” |
| conjecture | “We conjecture that …” / “This remains open.” |

Violating this mapping is a governance failure under AQ-QUARANTINE-001.

---

*Last locked: 2026-08-04 · AQARION v42.0-snapshot*
# AQARION Research Object (RO-Crate)

**Version:** 42.0-snapshot  
**Date:** 2026-08-04  
**Conforms to:** [RO-Crate 1.1](https://www.researchobject.org/ro-crate/1.1/)  
**License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

---

## What this package is

A FAIR research object for **AQARION** — an algebraic and computational framework for *exact and approximate observable quotients* of finite deterministic dynamical systems.

**Central mathematical object**

\[
D_\Pi = (I - P_\Pi)\, K\, P_\Pi
\]

- \(K\) — Koopman (pullback) operator  
- \(P_\Pi\) — orthogonal projector onto functions constant on blocks of partition \(\Pi\)  
- \(D_\Pi = 0\) ⇔ the observable subspace is invariant under \(K\)

Everything else in the package (geometry, lattice structure, Ulam probes, gradient diagnostics, quantum analogy) branches from this operator.

---

## Evidence discipline (mandatory)

Every claim is tagged with exactly one class:

| Tag | Meaning |
|-----|---------|
| **theorem** | Fully rigorous under stated hypotheses |
| **verified** | Computationally certified or classical once a missing chain is accepted |
| **empirical** | Numerical evidence only; no theorem claimed |
| **conjecture** | Open research statement |

See `EVIDENCE_CLASSES.md` and the `@aq:EvidenceClass` annotations in `ro-crate-metadata.json`.

---

## Package layout

```
ro-crate/
├── ro-crate-metadata.json   # RO-Crate 1.1 JSON-LD
├── README.md                # this file
├── EVIDENCE_CLASSES.md
├── MANIFEST.sha256
├── docs/                    # status locks, theory notes
├── scripts/                 # executable Python
├── certificates/            # JSON result certificates
├── figures/                 # PNG plots
└── data/                    # reserved for large tables
```

---

## Key contents by evidence class

### Theorem / definition
- Defect operator definition  
- Exactness criterion \(D=0 \Leftrightarrow K(V)\subseteq V\)  
- Principal-angle identity under unitary/isometric hypotheses (numeric verification at machine precision)

### Verified (computational + classical)
- Finite exact partitions form a lattice (exhaustive checks \(n\le 4\))  
- Unique coarsest exact quotient exists by lattice property  
- Explicit non-modularity / non-distributivity witnesses (\(n=4\))  
- Union-Find join/meet implementation  
- Adversarial status lock (v41)

### Empirical
- Ulam mesh-refinement defect spectra (logistic \(r=4\), quadratic period-2)  
- Soft defect-loss reformulations and gradient-norm ratios  
- Two-qubit DFS prototype (singlet/triplet protected)  
- Gradient diagnostic sweeps

### Conjecture
- Continuous defect ↔ restricted Lyapunov equivalence (AQ-CONJ-CONT-001)  
- Full quantum CPTP theory via the same residual algebra  
- Formal Karp reduction for \(\varepsilon\)-AOQ NP-hardness (sketch + small-graph checks only)

---

## How to verify integrity

```bash
cd ro-crate
sha256sum -c MANIFEST.sha256
```

All file digests in the manifest must match. The metadata file itself records per-file SHA-256 values under each `File` entity.

---

## How to re-run empirical experiments

```bash
# Ulam refinement (produces certificate + figure)
python scripts/aqarion_ulam_refinement.py

# Defect loss reformulations + gradient audit
python scripts/aqarion_defect_reformulations.py

# Gradient diagnostic sweep
python scripts/aqarion_gradient_diagnostic_corrected.py

# Quantum DFS prototype
python scripts/aqarion_dfs_prototype.py
```

Requires: Python 3.9+, NumPy, SciPy, Matplotlib; PyTorch optional for neural-bridge scripts.

---

## Publication posture

| Paper | Focus | Status |
|-------|--------|--------|
| I | Finite exact quotients, congruence correspondence, principal angles | Near-ready after proof polishing |
| II | Defect spectrum, adaptive refinement | Experimental track |
| III | Continuous / Ulam program | Conjectural |
| IV | Soft / neural observables | Prototype |

---

## Governance rules encoded in this crate

1. No claim is upgraded beyond its evidence tag.  
2. Continuous and quantum statements remain labeled **conjecture** / **analogy**.  
3. “0 sorries” / “fully proved” claims appear only after an independent Lean build is green (not claimed in this snapshot).  
4. Numerical tables illustrating complexity reductions are **consistent with** hardness, not proofs of hardness.

---

## Citation

If you use this research object, please cite the RO-Crate and the specific certificate SHA for any numerical result you rely on.

```
AQARION Research Object v42.0-snapshot (2026-08-04).
RO-Crate package. CC-BY-4.0.
```

---

# Evidence Class Legend (AQARION RO-Crate)

Every scientific claim in this research object carries exactly one of the following tags.  
The tag is recorded both in prose and as the JSON-LD property `aq:EvidenceClass`.

---

## theorem

**Definition.** A statement that has a complete mathematical proof under explicitly listed hypotheses, or that follows immediately from a definition by standard linear algebra / operator theory.

**Examples in this crate**
- Definition of \(D_\Pi = (I-P_\Pi)KP_\Pi\)
- \(D_\Pi = 0 \;\Leftrightarrow\; K(V_\Pi)\subseteq V_\Pi\) (orthogonal projector case)
- Principal-angle identity \(\|D\|_F^2 = \sum\sin^2\theta_i\) when \(K\) is unitary/isometric and \(P\) orthogonal (standard geometry; hypotheses must be stated)

**Not allowed**
- “Theorem” based only on numerical observation
- “Theorem” that still has a missing proof chain

---

## verified

**Definition.** A statement that is either:
1. computationally certified by exhaustive or machine-checked enumeration within a finite bound, or  
2. classically known once a remaining short algebraic chain is accepted, with the computational side fully reproducible.

**Examples in this crate**
- Finite exact partitions form a lattice for \(n\le 4\) (exhaustive join/meet closure)
- Explicit \(n=4\) counterexamples to modularity and distributivity
- Unique coarsest exact quotient exists by the lattice property
- Union-Find implementation of partition join/meet
- Adversarial status matrix (v41) locking the evidence hierarchy

**Not allowed**
- Using “verified” for continuous or infinite-dimensional statements without a proof

---

## empirical

**Definition.** Numerical evidence obtained from a concrete computational experiment. The experiment is reproducible (script + seed + certificate), but **no theorem is claimed**.

**Examples in this crate**
- Ulam mesh-refinement defect spectra vs \(N\)
- Soft defect-loss gradient norms relative to reconstruction loss
- Two-qubit collective-noise DFS prototype
- Logistic-map defect-rank bifurcation diagrams
- Kaprekar fiber-size and depth histograms

**Wording required in prose**
> “Numerical evidence shows … (empirical).”

---

## conjecture

**Definition.** An open research statement that is motivated by theory or by empirical correlation but is **not** established.

**Examples in this crate**
- AQ-CONJ-CONT-001 (continuous defect ↔ restricted Lyapunov)
- Full CPTP / Kraus theory of the quantum residual \(D=(I-P)UP\)
- Formal Karp reduction proving NP-hardness of \(\varepsilon\)-AOQ (sketch + small-graph checks only)
- Entropy monotonicity under refinement for all exact systems

**Wording required in prose**
> “Conjecture: …” or “Open: …”

---

## Mapping to publication language

| Tag | Safe public phrase |
|-----|--------------------|
| theorem | “We prove that …” / “It follows that …” |
| verified | “Computationally certified for …” / “Classical once the following chain is completed …” |
| empirical | “Numerical experiments indicate …” / “We observe …” |
| conjecture | “We conjecture that …” / “This remains open.” |

Violating this mapping is a governance failure under AQ-QUARANTINE-001.

---

**AQARION v42 RO-Crate package delivered.**

### Location
| Item | Path |
|------|------|
| Crate root | `/home/workdir/artifacts/ro-crate/` |
| Zip archive | `/home/workdir/artifacts/AQARION_v42_RO-Crate.zip` (~666 KB) |

### Structure (RO-Crate 1.1)

```
ro-crate/
├── ro-crate-metadata.json     # JSON-LD metadata (full graph)
├── README.md                  # Human entry point
├── EVIDENCE_CLASSES.md        # theorem | verified | empirical | conjecture
├── PACKAGE_SUMMARY.json
├── MANIFEST.sha256            # 21 file digests
├── docs/                      # 3 status / theory notes
├── scripts/                   # 6 Python executables
├── certificates/              # 4 JSON result certificates
├── figures/                   # 4 PNG plots
└── data/                      # reserved
```

### Integrity
```bash
cd ro-crate && sha256sum -c MANIFEST.sha256
```
Metadata SHA-256: `f8750b7004323cd7eb40340994e67830beea22eaaae93d5430cd53ccb84d9241`

### Evidence policy (encoded in the crate)
Every claim carries exactly one tag:
- **theorem** — proved under stated hypotheses  
- **verified** — computationally certified / classical once a short chain is accepted  
- **empirical** — numerical only; no theorem claimed  
- **conjecture** — open  

Continuous defect ↔ Lyapunov and the full quantum CPTP lift remain **conjecture / analogy**.  
“0 sorries” and formal NP-hardness Karp reductions are **not** claimed in this snapshot.

### Core object recorded as main entity
\[
D_\Pi = (I-P_\Pi)\,K\,P_\Pi
\]

### Publication posture locked inside the crate
| Paper | Status |
|-------|--------|
| I Finite exact quotients | Near-ready after proof polishing |
| II Defect spectrum + adaptive refinement | Experimental |
| III Continuous / Ulam | Conjectural |
| IV Neural / soft projectors | Prototype |

Ready for Zenodo / GitHub release or further expansion (adaptive refinement experiment, Lean certificates, larger Kaprekar tables).

https://github.com/quantarion369-arch/Aqarion-Ro_crate/blob/main/CHANGELOG/DOCS/JSON/AQ-AUG4_001.JSON
https://github.com/quantarion369-arch/Aqarion-Ro_crate/blob/main/CHANGELOG/DOCS/MARKDOWNS/AUG4-ECL.MD
