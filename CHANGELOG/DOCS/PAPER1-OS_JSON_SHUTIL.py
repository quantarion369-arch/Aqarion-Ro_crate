
import os, json, shutil

base_dir = "/mnt/agents/output/AQARION-PAPER-I"
os.makedirs(f"{base_dir}/spec", exist_ok=True)
os.makedirs(f"{base_dir}/paper-i/theorems", exist_ok=True)
os.makedirs(f"{base_dir}/paper-i/benchmarks", exist_ok=True)
os.makedirs(f"{base_dir}/paper-ii", exist_ok=True)
os.makedirs(f"{base_dir}/paper-iii", exist_ok=True)

# 1. SPEC: Definitions
spec_definitions = """# AQARION Mathematical Specification: Definitions

**Version:** 1.0.0 | **Status:** LOCKED | **Date:** 2026-07-07

---

### D1. Finite Deterministic Dynamical System

A **finite deterministic dynamical system** is a pair $(X, T)$ where $X$ is a finite nonempty set and $T: X \\to X$.

**Notation:** $|X| = n < \\infty$

---

### D2. Function Space

$$F(X) := \\{f: X \\to \\mathbb{R}\\}$$

Dimension $n$. Basis: $\\{\\delta_x\\}_{x \\in X}$ where $\\delta_x(y) = \\delta_{xy}$.

---

### D3. Koopman Operator

$(Kf)(x) := f(T(x))$. Linear, $||K||_\\infty = 1$, matrix $K_{ij} = \\delta_{i, T(j)}$.

---

### D4. Partition

$\\Pi = \\{B_1, \\dots, B_m\\}$ with $B_i \\neq \\emptyset$, disjoint, covering $X$.

---

### D5. Observable Subspace

$$V_\\Pi := \\{f \\in F(X) : f \\text{ constant on each } B_i\\}$$

$\\dim(V_\\Pi) = m$. Basis: $\\{\\mathbf{1}_{B_i}\\}$.

---

### D6. Averaging Projection

$(P_\\Pi f)(x) := \\frac{1}{|B_i|} \\sum_{y \\in B_i} f(y)$ for $x \\in B_i$.

Idempotent, self-adjoint, $\\text{Im}(P_\\Pi) = V_\\Pi$.

---

### D7. Defect Operator

$$D_\\Pi := (I - P_\\Pi) K P_\\Pi$$

Domain: $V_\\Pi \\to V_\\Pi^\\perp$. Measures failure of $K$ to preserve $V_\\Pi$.

---

### D8. Escape Quotient

$$\\mathcal{E}_1(\\Pi, T) := \\dim \\frac{K(V_\\Pi)}{K(V_\\Pi) \\cap V_\\Pi} = \\dim(\\text{Im}(D_\\Pi))$$

---

### D9. Escape Filtration

$$V_\\Pi^{(0)} := V_\\Pi, \\quad V_\\Pi^{(n+1)} := V_\\Pi^{(n)} + K(V_\\Pi^{(n)})$$

$e_n := \\dim(V_\\Pi^{(n+1)} / V_\\Pi^{(n)})$.

---

### D10. Closure Defect

$$\\mathcal{J}_\\Pi := \\sum_{n=0}^\\infty e_n = \\dim(V_\\Pi^\\infty / V_\\Pi)$$

---

## Lock Rule

**No theorem may reference an object not defined in this document.**
"""

with open(f"{base_dir}/spec/definitions.md", "w") as f:
    f.write(spec_definitions)

# 2. SPEC: Axioms
spec_axioms = """# AQARION Mathematical Specification: Axioms

**Version:** 1.0.0 | **Status:** LOCKED | **Date:** 2026-07-07

---

## A1. Finiteness
$X$ finite nonempty. Required by: all theorems.

## A2. Determinism
$T: X \\to X$ total function. Required by: Koopman linearity.

## A3. Real Coefficients
$F(X) = \\{f: X \\to \\mathbb{R}\\}$. Required by: averaging projection.

## A4. Standard Inner Product
$\\langle f, g \\rangle := \\sum_{x \\in X} f(x) g(x)$. Defines $P_\\Pi$ uniquely.

## A5. Nonempty Blocks
$\\forall B_i \\in \\Pi: |B_i| > 0$. Required by: $P_\\Pi$ definition.

## A6. Covers $X$
$\\bigcup B_i = X$. Required by: $V_\\Pi$ subspace property.

---

## Change Protocol
Modify axiom $\\Rightarrow$ re-verify all dependent proofs $\\Rightarrow$ increment version.
"""

with open(f"{base_dir}/spec/axioms.md", "w") as f:
    f.write(spec_axioms)

# 3. SPEC: Proof Obligations
spec_proofs = """# AQARION Mathematical Specification: Proof Obligations

**Version:** 1.0.0 | **Status:** ACTIVE | **Date:** 2026-07-07

---

## Paper I — PROVED

| Theorem | Statement | Status |
|---------|-----------|--------|
| T1 | $P_\\Pi^2 = P_\\Pi$ | PROVED |
| T2 | $D_\\Pi P_\\Pi = D_\\Pi$ | PROVED |
| T3 | $D_\\Pi = 0 \\iff K(V_\\Pi) \\subseteq V_\\Pi$ | PROVED |
| T4 | $D_\\Pi = 0 \\Rightarrow$ exact quotient descent | PROVED |
| T5 | $[P_\\Pi, K] = 0 \\Rightarrow D_\\Pi = 0$ | PROVED |
| T6 | $\\mathcal{E}_1 = \\dim(\\text{Im}(D_\\Pi))$ | PROVED |

## Paper II — CONJECTURE

| Theorem | Statement | Status |
|---------|-----------|--------|
| T7 | $\\dim(V_\\Pi^\\infty / V_\\Pi) = \\sum_n e_n$ | CONJECTURE |
| T8 | $e_n$ non-increasing | CONJECTURE |

## Paper III — OPEN

| Theorem | Statement | Status |
|---------|-----------|--------|
| T10 | $\\mathcal{E}_1$ continuous under partition refinement | CONJECTURE |
| T11 | Same $\\mathcal{E}_1$ profile $\\Rightarrow$ observational equivalence | OPEN |

## Retractions

| Theorem | Date | Reason |
|---------|------|--------|
| T4.2 (converse) | 2026-07-06 | Counterexample exists |
| T6.1v1 | 2026-07-07 | rank=k too strong; needs genericity |
"""

with open(f"{base_dir}/spec/proof_obligations.md", "w") as f:
    f.write(spec_proofs)

# 4. SPEC: Notation
spec_notation = """# AQARION Mathematical Specification: Notation

**Version:** 1.0.0 | **Status:** LOCKED | **Date:** 2026-07-07

| Symbol | Meaning |
|--------|---------|
| $X$ | State space |
| $T$ | Dynamics |
| $K$ | Koopman operator |
| $\\Pi$ | Partition |
| $V_\\Pi$ | Observable subspace |
| $P_\\Pi$ | Averaging projection |
| $D_\\Pi$ | Defect operator |
| $\\mathcal{E}_1$ | Escape quotient |
| $e_n$ | $n$-th escape dimension |
| $\\mathcal{J}_\\Pi$ | Closure defect |
| $V_\\Pi^\\infty$ | Union of escape filtration |
"""

with open(f"{base_dir}/spec/notation.md", "w") as f:
    f.write(spec_notation)

print("SPEC layer: definitions.md, axioms.md, proof_obligations.md, notation.md")SPEC layer: definitions.md, axioms.md, proof_obligations.md, notation.md
