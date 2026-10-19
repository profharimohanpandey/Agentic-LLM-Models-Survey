# Figures

Figures used in the survey paper, with descriptions for readers. Figure numbers
follow the paper *Agentic Large Language Models: Foundations, Post-Training,
Architectures, Security, and Evaluation* (Information Sciences, V9).

| File | Figure | Topic |
|------|--------|-------|
| [AgenticLLM_Review_Pipeline.png](AgenticLLM_Review_Pipeline.png) | Figure 1 | Review pipeline and paper organisation |
| [Review_Three_Axes.pdf](Review_Three_Axes.pdf) | Figure 2 | Three-axis review-design framework |
| [Review_screening.png](Review_screening.png) | Figure 3 | PRISMA-style screening and selection flow |
| [Figure_02.pdf](Figure_02.pdf) | Figure 4 | Classification into four macro-themes and twelve categories |
| [Figure_03.pdf](Figure_03.pdf) | Figure 5 | Distribution of the 212 reference entries across categories |

---

## Figure 1 — Review pipeline (`AgenticLLM_Review_Pipeline.png`)

**Review pipeline for the agentic LLM survey, with 16 sections grouped into
eight stages.** The sequence moves from review design and foundations through
training, reasoning, and system architectures to safety, applications,
evaluation, and research priorities. Arrows indicate the reading order, while
branches identify the main topics and their corresponding sections.

*What to look for:* the figure doubles as a map of the paper. Sections 2–4
establish the review protocol, background, and formal models; Sections 5–7
cover post-training, reasoning, and comparisons across AI approaches;
Sections 8–11 cover architectures, tools, coordination, and security; the
remaining sections address applications, evaluation, open problems, and future
research.

## Figure 2 — Three-axis framework (`Review_Three_Axes.pdf`)

**Three-axis framework for the review design (Section 2.1).** The *capability*
axis describes what agentic systems do (reasoning, acting, interacting); the
*lifecycle* axis locates model adaptation and inference-time control
(pretraining, post-training, inference-time control); and the *assurance* axis
organises evaluation, safety and security, and governance. Each source is
examined jointly across these conceptual dimensions.

*What to look for:* the three axes are the analytical grid used throughout the
review. Considering them together helps distinguish an architectural change
from changes in model adaptation or compute. The framework is paired with the
eight review questions (RQ1–RQ8) in Table 5 of the paper.

## Figure 3 — Screening and selection flow (`Review_screening.png`)

**Review screening and selection flow.** Identification n = 1,183 records
retrieved from databases and preprint servers; deduplication n = 792 unique
records after merging versions; title/abstract screening (IC1–IC5 and
EC1–EC5) n = 361; full-text eligibility with backward and forward citation
searches (snowballing) n = 250. Separate duplicate-removal, exclusion, and
snowball-addition counts are not reported. The final original reference set
contains n = 212 entries: 209 survey references and 3 review-methodology
references, distributed across 12 categories (the classification is shown in
Figure 4).

*What to look for:* a PRISMA-style account of how the bibliography was
constructed, including which counts are unavailable (reported as "not
reported" rather than estimated). The protocol follows PRISMA reporting
guidance and Snyder's semi-systematic approach (Section 2).

## Figure 4 — Classification of the reference set (`Figure_02.pdf`)

**Classification of the original 212-entry reference set (209 survey
references and 3 review-methodology sources) into four macro-themes and twelve
thematic categories.** The four macro-themes and their totals are:

- **Foundations & adaptation** — 62 references
- **Reasoning, planning & memory** — 35 references
- **Grounding & interaction** — 27 references
- **Assurance & deployment** — 88 references

The twelve categories are: (1) Surveys & foundations, (2) Post-training &
PEFT, (3) RL, reward & alignment, (4) Test-time scaling & reasoning,
(5) Foundation & reasoning models, (6) Tool use & retrieval, (7)
Architectures, planning & memory, (8) Multi-agent systems, (9) Safety &
security, (10) Evaluation & benchmarks, (11) Applications, and (12)
Infrastructure & classics. Category numbers correspond to the classified
bibliography in the companion repository. Cross-listed works are counted once
by primary contribution.

*What to look for:* Evaluation & benchmarks is the largest category (40
entries), followed by Infrastructure & classics (26) and the tied pair of
Foundation & reasoning models and Architectures, planning & memory (21 each).

## Figure 5 — Distribution across categories (`Figure_03.pdf`)

**Distribution of the original 212 reference entries across the twelve
thematic categories, including the 3 review-methodology references.** The
counts describe the full reference set; each entry is assigned to exactly one
category by its primary contribution. Counts per category: Surveys &
foundations 14; Post-training & PEFT 8; RL, reward & alignment 19; Test-time
scaling & reasoning 14; Foundation & reasoning models 21; Tool use & retrieval
10; Architectures, planning & memory 21; Multi-agent systems 17; Safety &
security 11; Evaluation & benchmarks 40; Applications 11; Infrastructure &
classics 26.

*What to look for:* the bar chart makes the imbalance between categories
immediately visible — evidence synthesis and evaluation dominate the field,
while post-training-specific work (8 entries) is comparatively sparse.

---

*File-name note:* `Figure_02.pdf` and `Figure_03.pdf` are legacy file names;
they correspond to **Figures 4 and 5** of the current paper version.
