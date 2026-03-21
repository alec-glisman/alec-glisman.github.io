---
permalink: /
title: "Alec Glisman"
excerpt: "Senior AI/ML Scientist"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div class="reveal hero-intro" markdown="1">

I am a **Senior AI/ML Scientist at Merck & Co.**, where I develop generative AI tools to help design small molecules that are both therapeutically effective and practically synthesizable, shortening the gap between computational design and the lab bench. I completed my PhD in Chemical Engineering at Caltech in 2024 under [Prof. Zhen-Gang Wang](http://zgwlab.che.caltech.edu/), where my research centered on the molecular physics of polyelectrolyte complexation and its applications to water remediation d. Earlier, I worked in [Prof. John F. Brady's](https://cheme.caltech.edu/groups/jfb/index.html) group studying self-propulsion in active matter systems. I received my B.S. in Chemical Engineering from UC Berkeley in 2019, where I worked with [Prof. Kranthi K. Mandadapu](https://mandadapu-group.github.io/) on the mechanics of lipid membranes.

</div>

## Research Background

My doctoral work spanned three interconnected themes in soft matter physics and computational chemistry, applying both AI/ML techniques and physics-based methods to study these systems:

<div class="research-card reveal" style="transition-delay: 0.05s" markdown="1">

### Generative AI, Molecular Design & QSAR Modeling

<span class="research-badge research-badge--ai">AI/ML</span><span class="research-badge research-badge--drug">Drug Discovery</span>

Designing a drug candidate requires jointly satisfying competing objectives (potency, selectivity, ADMET properties, and synthesizability), none of which can be ignored. I develop generative models that navigate this multi-parameter optimization landscape, enforcing synthesizability as a hard constraint through reaction template filtering and compatibility screening against commercially available building blocks. I also built ensemble QSAR models combining graph-based representations with cheminformatics fingerprints, which placed 18th out of 400+ submissions in the [OpenADMET-ExpansionRx Blind Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge).

</div>

<div class="research-card reveal" style="transition-delay: 0.1s" markdown="1">

### Polyelectrolyte Simulations & Ion Binding

<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--ai">AI/ML</span>

Polyelectrolytes are widely used to chelate multi-valent ions for water softening, but the molecular mechanisms driving their complexation (including the counterintuitive "like-charge attraction") remain poorly understood. I used all-atom molecular dynamics and enhanced sampling to probe these mechanisms, and found that ion correlations, rather than direct ion bridges, are the primary driver of chain–chain association. I applied unsupervised deep learning to elucidate phase diagrams and structure-property relationships, and collaborated with Dow Chemical on water treatment applications.

</div>

<div class="research-card reveal" style="transition-delay: 0.15s" markdown="1">

### Microhydrodynamics & Active Matter

<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Fluid Dynamics</span>

Active matter systems, including fish schools, bacterial colonies, and swimming microorganisms, display striking collective behaviors, and I set out to understand how much of this emerges from fluid mechanics alone, without any phenomenological interaction rules. I derived a framework for self-propulsion in potential flow and found that a deformable body can achieve net displacement without performing net work on the fluid, a result that was surprising since viscous dissipation had previously been considered necessary for propulsion. I also developed C++/CUDA simulations showing that purely hydrodynamic coupling can produce emergent collective ordering.

</div>

<div class="research-card reveal" style="transition-delay: 0.2s" markdown="1">

### Lipid Membrane Mechanics

<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Theory</span>

Lipid membranes are not simply static barriers; they flow in-plane as viscous fluids while bending out-of-plane as elastic shells, making them unusual materials whose dynamics are difficult to analyze. I developed a continuum theory coupling in-plane viscous flow to out-of-plane elastic bending, and in doing so introduced the [Scriven-Love number](/publications/2020-scriven-love-1), a dimensionless ratio that quantifies when intramembrane viscous stresses matter relative to elastic bending forces. Calculating non-negligible Scriven-Love numbers across physiologically relevant processes showed that in-plane viscosity cannot generally be ignored in membrane dynamics.

</div>

<div class="reveal" style="transition-delay: 0.25s" markdown="1">

## Education

| | |
|---|---|
| **PhD, Chemical Engineering** | California Institute of Technology, 2024 |
| **BS, Chemical Engineering** | University of California, Berkeley, 2019 |

</div>

<div class="reveal" style="transition-delay: 0.35s" markdown="1">

<a href="/publications/" class="btn--primary-cta">Publications</a>
<a href="/experience/" class="btn--outline-cta">Experience</a>
<a href="/projects/" class="btn--outline-cta">Projects</a>
<a href="https://www.linkedin.com/in/alec-glisman" class="btn--outline-cta">Contact</a>

</div>
