---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
excerpt: "Research by Alec Glisman combining physics-based simulation, machine learning, and theoretical mechanics: generative AI for drug discovery, polyelectrolyte complexation, microhydrodynamics, and lipid membrane mechanics."
---

Research applying generative AI and machine learning to drug discovery, spanning molecular design, multi-parameter optimization, and ADMET property prediction. This work is grounded in physics-based simulation, enhanced sampling methods, and theoretical mechanics for soft matter systems at molecular and mesoscopic scales.

---

<div class="research-card reveal" markdown="1">

### Generative AI & Molecular Design

Identifying drug candidates requires jointly satisfying competing objectives across potency, selectivity, ADMET properties, PK/PD profiles, and synthetic feasibility. Generative models are trained to navigate this multi-parameter optimization (MPO) landscape through two modes suited to different campaign stages: de novo generation samples broad chemical space to identify novel scaffolds, and chemical series-constrained generation performs scaffold-anchored R-group expansion within established medicinal chemistry series to build on accumulated SAR knowledge during lead optimization. Synthesizability is enforced as a hard constraint through reaction template filtering and compatibility screening against commercially available building block catalogs, ensuring generated candidates are tractable to synthesize and shortening design-make-test-analyze (DMTA) cycle times.

</div>

<div class="research-card reveal" style="transition-delay: 0.05s" markdown="1">

### QSAR Modeling & ADMET Property Prediction

Stacked ensemble models combining graph-based molecular representations with cheminformatics feature sets (extended-connectivity fingerprints, physicochemical descriptors) were developed to predict ADMET endpoints. Curriculum learning was used to incorporate external public datasets, progressively transferring representation quality to the target distribution. Hyperparameter optimization via Optuna and repeated cross-validation with both chemical similarity and temporal splits were applied to produce estimates of generalization performance that are robust to distribution shift. Evaluated in the [OpenADMET-ExpansionRx Blind Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge), the approach was assessed on fully held-out compound libraries spanning structurally diverse chemical space, achieving 18th place out of over 400 submissions across 9 ADMET endpoints.

**Leaderboard:** [OpenADMET-ExpansionRx Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge) · **Code:** [OpenADMET-ExpansionRx-Blind-Challenge](https://github.com/alec-glisman/OpenADMET-ExpansionRx-Blind-Challenge)

</div>

<div class="research-card reveal" style="transition-delay: 0.1s" markdown="1">

### Polyelectrolyte Complexation & Ion Binding

Calculated adsorption isotherms and free-energy landscapes for Ca²⁺ binding on poly(acrylic acid) using well-tempered metadynamics and Hamiltonian replica exchange, identifying two dominant binding modes distinguished by carboxylate coordination number. Mapped concentration-dependent phase diagrams using all-atom molecular dynamics and unsupervised deep learning, revealing how Ca²⁺–PAA–Ca²⁺ bridges drive like-charge polyelectrolyte chain association and precipitation. Characterized polyelectrolyte adsorption to mineral (CaCO₃) surfaces, finding that water-mediated hydrogen bond interactions dominate over direct polymer–surface contacts. Applied generative diffusion probabilistic models (DDPMs) to generate polymer conformational ensembles consistent with their Boltzmann distributions, enabling sequence design with enhanced calcium tolerance. Collaborated with Dow Chemical on water treatment applications.

**Key papers:** [Langmuir 2025](/publications/2025-langmuir-binding-modes) · [Macromolecules 2024](/publications/2024-macromolecules-polyelectrolyte) · [Langmuir 2024](/publications/2024-langmuir-adsorption-isotherm)

</div>

<div class="research-card reveal" style="transition-delay: 0.15s" markdown="1">

### AI/ML Methods in Soft Matter

Applied deep learning and unsupervised learning methods to determine structure-property relationships in aqueous polyelectrolyte systems. Developed workflows combining enhanced sampling molecular dynamics with unsupervised clustering and dimensionality reduction to identify dominant polymer conformations and their thermodynamic stability. Used denoising diffusion probabilistic models (DDPMs) to generate polymer conformational ensembles consistent with Boltzmann distributions, providing a generative complement to physics-based simulation for polymer design.

**Code:** [DDPM-Enhanced-Sampling](https://github.com/alec-glisman/DDPM-Enhanced-Sampling)

</div>

<div class="research-card reveal" style="transition-delay: 0.2s" markdown="1">

### Microhydrodynamics & Active Matter

Derived an analytical framework for self-propulsion in potential flow, showing that at high Reynolds number a deformable body achieves net displacement over a deformation cycle by exploiting the body-configuration dependence of added mass, without requiring net work on the fluid. Developed C++/CUDA multi-threaded boundary integral simulations for many-particle hydrodynamic interactions in Stokes flow. Showed that purely mechanical hydrodynamic coupling produces collective ordering in active particle suspensions.

**Key paper:** [J. Fluid Mechanics 2022](/publications/2022-potential-flow-2)

</div>

<div class="research-card reveal" style="transition-delay: 0.25s" markdown="1">

### Lipid Membrane Mechanics

Introduced the Scriven-Love number, a dimensionless ratio quantifying when intramembrane viscous stresses affect membrane relaxation dynamics relative to elastic bending forces. Developed continuum theory coupling in-plane viscous flow to out-of-plane elastic bending using differential geometry and linear irreversible thermodynamics. Established that the Scriven-Love number takes non-negligible values across physiologically relevant biological processes, indicating that in-plane viscous forces are a necessary consideration in lipid membrane analysis.

**Key paper:** [Physical Review E 2020](/publications/2020-scriven-love-1)

</div>
