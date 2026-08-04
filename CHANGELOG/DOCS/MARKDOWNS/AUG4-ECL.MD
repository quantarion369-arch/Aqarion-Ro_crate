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
