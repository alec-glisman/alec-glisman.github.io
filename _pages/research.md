---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
excerpt: "Research by Alec Glisman combining physics-based simulation, machine learning, and theoretical mechanics: generative AI for drug discovery, polyelectrolyte complexation, microhydrodynamics, and lipid membrane mechanics."
---

My work sits at the intersection of physics-based simulation, machine learning, and molecular design. I came to drug discovery through a background in soft matter physics: first studying how lipid membranes deform, then how polyelectrolytes and multi-valent ions interact in aqueous solution. That grounding in molecular-scale physics shapes how I approach generative AI and ADMET modeling: I am interested not just in predictive accuracy, but in understanding *why* molecules behave as they do and using that understanding to guide design.

---

<div class="research-card reveal" markdown="1">

### Generative AI & Molecular Design
<span class="research-badge research-badge--ai">AI/ML</span><span class="research-badge research-badge--drug">Drug Discovery</span>

Identifying drug candidates requires jointly satisfying competing objectives across potency, selectivity, ADMET properties, PK/PD profiles, and synthetic feasibility, and no single objective can be compromised without practical consequences. I work on generative models that navigate this multi-parameter optimization (MPO) landscape through two modes suited to different campaign stages: de novo generation, which samples broad chemical space to identify novel scaffolds, and chemical series-constrained generation, which performs scaffold-anchored R-group expansion within established medicinal chemistry series to build on accumulated SAR knowledge during lead optimization. I enforce synthesizability as a hard constraint through reaction template filtering and compatibility screening against commercially available building block catalogs, ensuring generated candidates are tractable to synthesize and shortening design-make-test-analyze (DMTA) cycle times.

</div>

<div class="research-card reveal" style="transition-delay: 0.05s" markdown="1">

### QSAR Modeling & ADMET Property Prediction
<span class="research-badge research-badge--ai">AI/ML</span><span class="research-badge research-badge--drug">Cheminformatics</span>

I developed stacked ensemble models combining graph-based molecular representations with cheminformatics feature sets (extended-connectivity fingerprints, physicochemical descriptors) to predict ADMET endpoints. I used curriculum learning to incorporate external public datasets, progressively transferring representation quality to the target distribution, a strategy that proved important for generalizing to structurally diverse chemical space. Hyperparameter optimization via Optuna and repeated cross-validation with both chemical similarity and temporal splits produced estimates of generalization performance robust to distribution shift. I entered the [OpenADMET-ExpansionRx Blind Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge), where the approach was assessed on fully held-out compound libraries, achieving 18th place out of over 400 submissions across 9 ADMET endpoints.

**Leaderboard:** [OpenADMET-ExpansionRx Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge) · **Code:** [OpenADMET-ExpansionRx-Blind-Challenge](https://github.com/alec-glisman/OpenADMET-ExpansionRx-Blind-Challenge)

</div>

<div class="research-card reveal" style="transition-delay: 0.1s" markdown="1">

### Polyelectrolyte Complexation & Ion Binding
<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Simulation</span>

Aqueous polyelectrolytes are widely used to chelate multi-valent cations like Ca²⁺, serving essential roles in water softening, drug delivery, and mineralization control, but the molecular mechanisms driving their complexation remained poorly understood. I calculated adsorption isotherms and free-energy landscapes for Ca²⁺ binding on poly(acrylic acid) using well-tempered metadynamics and Hamiltonian replica exchange, identifying two dominant binding modes distinguished by carboxylate coordination number. Interestingly, I found that increasing Ca²⁺ concentration did drive chain–chain association, but the binding energy was not simply proportional to the number of ion bridges; instead, correlations between chelated ions governed the interaction. I mapped concentration-dependent phase diagrams using all-atom molecular dynamics and unsupervised deep learning, and characterized polyelectrolyte adsorption to mineral (CaCO₃) surfaces, finding that water-mediated hydrogen bonds dominate over direct polymer–surface contacts. I also applied generative diffusion probabilistic models (DDPMs) to generate polymer conformational ensembles consistent with Boltzmann distributions, enabling sequence design with enhanced calcium tolerance. This work was done in collaboration with Dow Chemical on water treatment applications.

**Key papers:** [Langmuir 2025](/publications/2025-langmuir-binding-modes) · [Macromolecules 2024](/publications/2024-macromolecules-polyelectrolyte) · [Langmuir 2024](/publications/2024-langmuir-adsorption-isotherm)

</div>

<div class="research-card reveal" style="transition-delay: 0.15s" markdown="1">

### AI/ML Methods in Soft Matter
<span class="research-badge research-badge--ai">AI/ML</span><span class="research-badge research-badge--sim">Deep Learning</span>

The free energy landscapes of polyelectrolyte systems are high-dimensional and complex, making it difficult to extract interpretable structure-property relationships from simulation data alone. I applied deep learning and unsupervised learning to bridge this gap, developing workflows that combine enhanced sampling molecular dynamics with dimensionality reduction and clustering to identify dominant polymer conformations and their thermodynamic stability. I also developed workflows using denoising diffusion probabilistic models (DDPMs) to generate polymer conformational ensembles consistent with Boltzmann distributions, providing a generative complement to physics-based simulation for polymer design.

**Code:** [DDPM-Enhanced-Sampling](https://github.com/alec-glisman/DDPM-Enhanced-Sampling)

</div>

<div class="research-card reveal" style="transition-delay: 0.2s" markdown="1">

### Microhydrodynamics & Active Matter
<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Fluid Dynamics</span>

Active systems such as schools of fish, flocks of birds, and growing bacterial colonies display spontaneous collective ordering, and I aimed to understand how much of this behavior emerges from fluid mechanics alone, without phenomenological interaction rules. I derived an analytical framework for self-propulsion in potential flow and found that at high Reynolds number, a deformable body achieves net displacement over a deformation cycle by exploiting its configuration-dependent added mass, without requiring net work on the fluid. This result was surprising: self-propulsion had previously been thought to require viscous dissipation, which is absent in potential flow. I also developed C++/CUDA multi-threaded boundary integral simulations for many-particle Stokes flow interactions, showing that purely hydrodynamic coupling is sufficient to produce collective ordering in active particle suspensions.

**Key paper:** [J. Fluid Mechanics 2022](/publications/2022-potential-flow-2)

</div>

<div class="research-card reveal" style="transition-delay: 0.25s" markdown="1">

### Lipid Membrane Mechanics
<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Theory</span>

Lipid membranes are unusual materials: lipids flow in-plane as a two-dimensional viscous fluid, yet the membrane bends out-of-plane as an elastic shell. This dual character makes membrane dynamics difficult to analyze, and the coupling between in-plane viscosity and out-of-plane bending had been largely overlooked. I developed a continuum theory using differential geometry and linear irreversible thermodynamics to describe membrane dynamics across various geometries, and in doing so introduced the Scriven-Love number, a dimensionless ratio that quantifies when intramembrane viscous stresses affect membrane relaxation relative to elastic bending forces. Calculating non-negligible Scriven-Love numbers across physiologically relevant biological processes showed that in-plane viscous flows cannot generally be ignored when analyzing lipid membrane behavior.

**Key paper:** [Physical Review E 2020](/publications/2020-scriven-love-1)

</div>
