# Search Methodology & Reproducibility

This document records how the classified bibliography in **[README.md](README.md)** was assembled, so the index can be reproduced or audited. It is the companion methodology for the survey *Agentic Large Language Models: Foundations, Post-Training, Architectures, Security, and Evaluation — A Comprehensive Survey*.

---

This index was assembled through a **semi-systematic literature review** designed
to populate a large, multidisciplinary survey rather than to answer a single
narrow question. The protocol below documents *how* the references were found and
classified so that the result can be reproduced or audited.

## 1. Method in brief

The workflow had six stages:

1. **Scoping.** Fix the survey's spine—post-training-centred agentic LLMs—and
   derive the theme blocks that later became the 12 categories.
2. **Query design.** Translate each theme block into a Boolean query built from
   concept groups (population, intervention, outcome).
3. **Database search.** Run the queries against the sources listed below and
   export the hits (title, authors, abstract, year, venue, identifier).
4. **Title/abstract screening.** Apply inclusion/exclusion criteria; discard
   off-topic, duplicated, or non-LLM hits.
5. **Full-text eligibility and snowballing.** Read the surviving papers and add
   backward (reference-list) and forward (citing-paper) snowballing, starting
   from the anchor surveys.
6. **Classification and indexing.** Assign each accepted work to one of the 12
   categories, attach a stable link, and record it here with a citekey that
   matches `refs.tex`.

## 2. Sources and databases searched

| Source | Coverage / role |
|--------|-----------------|
| arXiv (cs.CL, cs.AI, cs.LG, cs.MA, cs.SE, cs.CR) | Primary source for fast-moving preprints; most links resolve here |
| Google Scholar | Broad recall; forward snowballing via "Cited by" |
| ACM Digital Library | Venue-of-record for KDD, ACL, SOSP, AISec, CSUR |
| IEEE Xplore | ICML/NeurIPS-style and IEEE proceedings, robotics |
| DBLP | Disambiguation of venues and author bibliographies |
| Semantic Scholar | Metadata, abstracts, and citation graph |
| ACL Anthology / OpenReview | NLP and ML conference papers |
| SpringerLink / ScienceDirect | Journals (Frontiers, Nature, Machine Learning) |
| PubMed / JMIR | Clinical and biomedical applications |
| GitHub / vendor reports | Code and technical reports (OpenAI, Anthropic, Meta, Google, DeepSeek, Mistral, Kimi) |

## 3. Search window

The primary window is **2017–2026**, chosen because the transformer architecture
(2017) marks the start of the modern LLM era. Pre-2017 material—classical AI,
reinforcement learning, and neuroscience-inspired memory work—was retrieved
exclusively through **backward snowballing** from the accepted papers, and is
collected in [Category 12](#12-infrastructure-efficiency–classical-foundations).

## 4. Search keys and fields

Queries were run over **title**, **abstract**, and **author keywords** where the
source supports field-restricted search; otherwise the default full-text index
was used. The following conventions were applied:

- **Exact phrases** in double quotes (e.g. `"prompt injection"`) to reduce noise.
- **Truncation** with `*` (e.g. `agent*` matches *agent*, *agents*, *agentic*).
- **Boolean** `AND` / `OR` to combine concept groups; `NOT` to remove
  off-domain noise (e.g. `NOT drug` in healthcare queries).
- **Field operators** where available: `allintitle:` and `abs:` (Google
  Scholar), `arxiv:cat` (arXiv category filter), venue filters on ACM/IEEE.

## 5. Concept groups

| Block | Terms |
|-------|-------|
| P (population) | `"large language model"` OR `LLM` OR `"foundation model"` OR `"language model"` |
| I1 (agentic) | `agent` OR `agentic` OR `"autonomous agent"` OR `"LLM agent"` OR `"tool-augmented"` |
| I2 (adaptation) | `"post-training"` OR `"instruction tuning"` OR `SFT` OR `RLHF` OR `DPO` OR `"reward model"` |
| I3 (reasoning) | `"chain-of-thought"` OR `"tree of thoughts"` OR `"self-consistency"` OR `"test-time scaling"` OR `"process reward model"` |
| I4 (tools) | `"tool use"` OR `"function calling"` OR `"retrieval-augmented generation"` OR `RAG` OR `API` |
| I5 (systems) | `"multi-agent"` OR `multiagent` OR `"agent architecture"` OR `memory` OR `"hierarchical memory"` |
| O (outcome) | `reasoning` OR `planning` OR `robustness` OR `safety` OR `alignment` OR `evaluation` OR `benchmark` |

## 6. Example search queries

| Theme (→ category) | Example Boolean query | Primary sources |
|--------------------|-----------------------|-----------------|
| Core agentic LLMs (1) | `("large language model" OR LLM OR "foundation model") AND (agent OR agentic OR "autonomous agent") AND (reasoning OR planning OR "tool use")` | arXiv, Google Scholar |
| Post-training (2, 3) | `("large language model" OR LLM) AND ("post-training" OR "instruction tuning" OR SFT OR RLHF OR "direct preference optimization" OR "reward model")` | arXiv, ACL Anthology |
| Reasoning & test-time scaling (4) | `("large language model" OR LLM) AND ("chain-of-thought" OR "tree of thoughts" OR "self-consistency" OR "test-time scaling" OR "process reward model")` | arXiv, NeurIPS |
| Models & reports (5) | `("GPT-4" OR "Llama" OR "Gemini" OR "Claude" OR "Qwen" OR "DeepSeek" OR "Mistral" OR "Kimi") AND ("technical report" OR "system card")` | arXiv, vendor sites |
| Tool use & retrieval (6) | `("large language model" OR LLM) AND ("tool use" OR "function calling" OR "retrieval-augmented generation" OR RAG OR "API")` | arXiv, ICLR |
| Architectures, planning & memory (7) | `("large language model" OR LLM) AND (agent* ) AND ("architecture" OR "memory" OR "planning" OR "long-horizon")` | arXiv, CoRL |
| Multi-agent (8) | `("large language model" OR LLM) AND ("multi-agent" OR multiagent OR "agent collaboration" OR "multi-agent debate")` | arXiv, ACL |
| Safety & security (9) | `("large language model" OR LLM OR agent) AND ("prompt injection" OR jailbreak OR alignment OR "agent safety" OR guardrail)` | arXiv, ACM AISec |
| Evaluation & benchmarks (10) | `("large language model" OR LLM OR agent) AND (benchmark OR evaluation OR reproducibility OR "red-teaming")` | arXiv, ACL, NeurIPS D&B |
| Applications (11) | `(agent OR "large language model") AND ("software engineering" OR healthcare OR "scientific discovery" OR robotics OR finance)` | PubMed, arXiv, IEEE |
| Infrastructure & classics (12) | `("large language model" OR LLM) AND (vLLM OR quantization OR "efficient inference" OR "distributed training")` | arXiv, ACM SOSP, IEEE |

## 7. Inclusion and exclusion criteria

**Include** a work if it: (i) is about LLMs or LLM-based agents (including
post-training, reasoning, tool use, multi-agent, safety, evaluation, or a direct
application); (ii) proposes a method, model, benchmark, dataset, framework, or
survey; (iii) is peer-reviewed **or** a well-cited preprint from a recognised
group or vendor; and (iv) is written in English.

**Exclude** a work if it: (i) concerns agents or reinforcement learning without
a language-model component; (ii) is a duplicate or an extended abstract of an
already-included paper; (iii) is a marketing or opinion piece with no method or
evidence; (iv) cannot be retrieved in full text; or (v) is superseded by a later
version already included.

## 8. Screening and classification

Screening proceeded in two passes: a fast **title/abstract pass** followed by a
**full-text pass** for borderline cases. Accepted works were then assigned to the
single best-fitting category from the 12-theme scheme by matching their title and
abstract against the concept groups above; genuinely cross-cutting works (for
example, benchmarks that are also multi-agent systems) were placed by their
*primary contribution*. Anchors for snowballing were the four most relevant prior
surveys—Wang et al. (2024), Xi et al. (2023), Plaat et al. (2025), and Kumar et
al. (2025).

## 9. How to reproduce this index

The tables here are a deterministic transform of the survey's bibliography, so
they can be regenerated as follows:

1. **Extract.** Parse `refs.tex` and collect each `\bibitem{key}` together with
   its authors, title, venue, and year.
2. **Normalise.** Derive a clean `Title`, `Venue / Year`, and `Type` for each
   entry; strip LaTeX macros (`\textit`, `\emph`, accents).
3. **Resolve links.** If an arXiv identifier is present, emit
   `https://arxiv.org/abs/<id>`; else if a DOI is present, emit
   `https://doi.org/<doi>`; else use the publisher or GitHub URL. Entries with no
   stable identifier are marked `—`.
4. **Classify.** Map each entry to one of the 12 categories using the concept
   groups in §5 (keyword match plus manual review for cross-cutting works).
5. **Emit.** Render the category tables and write this `README.md`.
6. **Commit.** The mapping is stable, so re-running the pipeline reproduces the
   same output modulo link additions.

A minimal extraction step, for reference:

```python
import re
bib = open("refs.tex", encoding="utf-8").read()
entries = re.findall(r"\\bibitem\{(?P<key>[^}]+)\}(?P<body>.*?)(?=\\bibitem|\\end\{thebibliography\})",
                     bib, flags=re.S)
for e in entries:
    body = " ".join(e["body"].split())
    arxiv = re.search(r"arXiv:(\d{4}\.\d{4,5})", body)
    doi   = re.search(r"doi:\s*(10\.[^\s,;]+)", body)
    print(e["key"], "->",
          f"https://arxiv.org/abs/{arxiv.group(1)}" if arxiv
          else (f"https://doi.org/{doi.group(1)}" if doi else "—"))
```

## 10. Reporting Standards

The review protocol follows established guidance for systematic and structured
literature reviews. These works are cited in the survey's methodology section and
recorded here for completeness.

| Title | Venue / Year | Type | Link |
|-------|--------------|------|------|
| Preferred Reporting Items for Systematic Reviews and Meta-Analyses: The PRISMA Statement | PLoS Medicine, 2009 | Methodology | [DOI](https://doi.org/10.1371/journal.pmed.1000097) |
| The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews | BMJ, 2021 | Methodology | [DOI](https://doi.org/10.1136/bmj.n71) |
| Literature Review as a Research Methodology: An Overview and Guidelines | Journal of Business Research, 2019 | Methodology | [DOI](https://doi.org/10.1016/j.jbusres.2019.07.039) |

## 11. Limitations

The index inherits the usual limitations of a fast-moving, arXiv-heavy field:
some entries are preprints that have not completed peer review; venue metadata
can change between preprint and camera-ready versions; publisher-hosted links may
require subscriptions while the arXiv mirror remains open; and links can rot over
time. Coverage is English-only and reflects the search window and criteria above;
it is a curated snapshot of the works cited in the survey, not an exhaustive map
of the field.

—
