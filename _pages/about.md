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

I am a **Senior AI/ML Scientist at Merck & Co.**, focusing on the application of generative AI techniques to design small molecules with desired properties that are easily synthesizable, accelerating structure-based and ligand-based drug design. I completed my PhD in Chemical Engineering at Caltech in 2024 under [Prof. Zhen-Gang Wang](http://zgwlab.che.caltech.edu/), and previously worked in [Prof. John F. Brady's](https://cheme.caltech.edu/groups/jfb/index.html) group. I received my B.S. in Chemical Engineering from UC Berkeley in 2019, where I worked with [Prof. Kranthi K. Mandadapu](https://mandadapu-group.github.io/) on the dimensional analysis of lipid bilayers.

</div>

## Research Background

My doctoral work spanned three interconnected themes in soft matter physics and computational chemistry, applying both AI/ML techniques and physics-based methods to study these systems:

<div class="research-card reveal" style="transition-delay: 0.05s" markdown="1">

### Polyelectrolyte Simulations & Ion Binding

Molecular dynamics and enhanced sampling simulation of polyelectrolyte complexation, Ca²⁺ adsorption isotherms, and precipitation mechanisms in aqueous solution. Applied unsupervised deep learning to elucidate phase diagrams and discover key structure-property relationships. Industry collaboration with Dow Chemical on water treatment polymer additives.

</div>

<div class="research-card reveal" style="transition-delay: 0.1s" markdown="1">

### Microhydrodynamics & Active Matter

Theoretical and computational study of self-propulsion in potential flow, boundary integral methods for many-body Stokes flow, and emergent collective behaviors in active particle systems.

</div>

<div class="research-card reveal" style="transition-delay: 0.15s" markdown="1">

### Lipid Membrane Mechanics

Continuum mechanics of curved lipid bilayers using differential geometry and balance-law formulations. Introduced the [Scriven-Love number](/publications/2020-scriven-love-1), a dimensionless ratio comparing in-plane viscous forces to elastic bending forces in membrane dynamics.

</div>

<div class="research-card reveal" style="transition-delay: 0.2s" markdown="1">

### Generative AI, Molecular Design & QSAR Modeling

**Generative molecular design.** Drug design is formulated as a multi-parameter optimization (MPO) problem over a joint chemical-property space, simultaneously targeting PK/PD profiles, ADMET endpoints, potency, and aqueous solubility. Two generation modes cover distinct campaign stages: de novo generation samples broad chemical space to identify novel scaffolds, and chemical series-constrained generation performs scaffold-anchored R-group elaboration and analog enumeration within established medicinal chemistry series, retaining prior SAR knowledge and supporting lead optimization. SMILES-based recurrent neural network (RNN) and Transformer generative models are iteratively fine-tuned via reinforcement learning (RL) against an ensemble of in silico QSAR scoring functions to produce candidates with high predicted probability of success across all optimization criteria. Graph neural network (GNN) architectures operating on molecular graphs complement SMILES-based generators by capturing non-local structural features that improve sample diversity and property coverage. Synthetic accessibility is enforced through reaction template filtering and compatibility constraints against commercially available building block catalogs, reducing the time between in silico design and practical synthesis within design-make-test-analyze (DMTA) cycles.

**QSAR modeling and property prediction.** In the [OpenADMET-ExpansionRx Blind Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge), stacked ensemble models combining graph-based molecular representations with cheminformatics feature sets (extended-connectivity fingerprints, physicochemical descriptors) were developed to predict ADMET endpoints on fully held-out compound libraries. The approach achieved **[rank X] on the public leaderboard** [*please fill in rank/score*], demonstrating generalization across structurally diverse chemical space.

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
