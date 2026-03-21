---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
excerpt: "Research by Alec Glisman combining physics-based simulation, machine learning, and theoretical mechanics — generative AI for drug discovery, polyelectrolyte complexation, microhydrodynamics, and lipid membrane mechanics."
---

Research combining physics-based simulation, machine learning, and theoretical mechanics to understand soft matter systems at molecular and mesoscopic scales, and applying AI/ML to accelerate drug discovery.

---

<div class="research-card reveal" markdown="1">

### Generative AI & Molecular Design

Application of generative AI techniques to inverse design of novel small molecules with targeted properties for drug discovery. Transformer and recurrent neural network (RNN) architectures with reinforcement learning (RL) guide the design of synthesizable molecules for structure-based and ligand-based drug design (SBDD/LBDD). Complemented by graph neural network (GNN) and conformer ensemble-based ADMET models with uncertainty quantification to accelerate design-make-test-analyze (DMTA) cycles.

</div>

<div class="research-card reveal" style="transition-delay: 0.05s" markdown="1">

### QSAR Modeling & ADMET Property Prediction

Application of deep learning to predict molecular properties across a broad range of ADMET (absorption, distribution, metabolism, excretion, and toxicity) endpoints. Developed ensemble machine learning models for the OpenADMET blind challenge, using cheminformatics features and graph-based representations to predict drug candidate properties. This work bridges physics-based understanding of molecular structure with data-driven predictive modeling for drug discovery.

</div>

<div class="research-card reveal" style="transition-delay: 0.1s" markdown="1">

### Polyelectrolyte Complexation & Ion Binding

Calculated adsorption isotherms and free-energy landscapes for Ca²⁺ binding on poly(acrylic acid) using well-tempered metadynamics and Hamiltonian replica exchange, identifying two dominant binding modes distinguished by carboxylate coordination number. Mapped concentration-dependent phase diagrams using all-atom molecular dynamics and unsupervised deep learning, revealing how Ca²⁺–PAA–Ca²⁺ bridges drive like-charge polyelectrolyte chain association and precipitation. Characterized polyelectrolyte adsorption to mineral (CaCO₃) surfaces, finding that water-mediated hydrogen bond interactions dominate over direct polymer–surface contacts. Applied generative diffusion probabilistic models (DDPMs) to generate polymer conformational ensembles consistent with their Boltzmann distributions, enabling sequence design with enhanced calcium tolerance. Collaborated with Dow Chemical on water treatment applications.

**Key papers:** [Langmuir 2025](/publications/2025-langmuir-binding-modes) · [Macromolecules 2024](/publications/2024-macromolecules-polyelectrolyte) · [Langmuir 2024](/publications/2024-langmuir-adsorption-isotherm)

</div>

<div class="research-card reveal" style="transition-delay: 0.15s" markdown="1">

### AI/ML Methods in Soft Matter

Applied deep learning and unsupervised learning methods to determine structure-property relationships in aqueous polyelectrolyte systems. Developed workflows combining enhanced sampling molecular dynamics with unsupervised clustering and dimensionality reduction to identify dominant polymer conformations and their thermodynamic stability. Used denoising diffusion probabilistic models (DDPMs) to generate polymer conformational ensembles consistent with Boltzmann distributions, providing a generative complement to physics-based simulation for polymer design.

</div>

<div class="research-card reveal" style="transition-delay: 0.2s" markdown="1">

### Microhydrodynamics & Active Matter

Derived an analytical framework for self-propulsion in potential flow, demonstrating that at high Reynolds number a deformable body can achieve net displacement over a deformation cycle by exploiting the dependence of added mass on instantaneous body configuration — without doing net work on the fluid. Developed C++/CUDA multi-threaded boundary integral simulations for many-particle hydrodynamic interactions in Stokes flow. Demonstrated how purely mechanical coupling drives collective emergent structures in active particle systems.

**Key paper:** [J. Fluid Mechanics 2022](/publications/2022-potential-flow-2)

</div>

<div class="research-card reveal" style="transition-delay: 0.25s" markdown="1">

### Lipid Membrane Mechanics

Introduced the Scriven-Love number — a dimensionless ratio quantifying when intramembrane viscous stresses significantly affect membrane relaxation dynamics relative to elastic bending forces. Developed continuum theory coupling in-plane viscous flow to out-of-plane elastic bending using differential geometry and linear irreversible thermodynamics. Demonstrated that the Scriven-Love number takes non-negligible values across physiologically relevant biological processes, showing that in-plane viscous forces cannot generally be neglected in lipid membrane analysis.

**Key paper:** [Physical Review E 2020](/publications/2020-scriven-love-1)

</div>
