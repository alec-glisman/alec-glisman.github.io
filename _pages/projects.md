---
layout: single
title: "Projects"
permalink: /projects/
author_profile: true
excerpt: "Open-source software projects by Alec Glisman in molecular property prediction, diffusion models for polymer design, computational fluid dynamics, and molecular dynamics analysis."
---

Selected software projects. Full list on [GitHub](https://github.com/alec-glisman).

---

<div class="project-card reveal" markdown="1">

<img src="/assets/images/openadmet.png" alt="OpenADMET logo" class="project-card-img project-card-img--logo">

### OpenADMET-ExpansionRx

Stacked ensemble models for predicting drug absorption, distribution, metabolism, and toxicity (ADMET). Combines graph neural networks with molecular fingerprints and physicochemical descriptors. Placed 18th of 400+ submissions in the OpenADMET-ExpansionRx blind challenge across 9 endpoints. Uses curriculum learning, automated hyperparameter tuning, and cross-validation designed for distribution shift.

<div class="project-tags">
  <span class="skill-tag">Python</span>
  <span class="skill-tag">Cheminformatics</span>
  <span class="skill-tag">RDKit</span>
  <span class="skill-tag">Drug Discovery</span>
</div>
<div class="project-links">
  <a href="https://github.com/alec-glisman/OpenADMET-ExpansionRx-Blind-Challenge"><i class="fab fa-github"></i> GitHub</a>
</div>

</div>

<div class="project-card reveal" style="transition-delay: 0.1s" markdown="1">

<img src="https://raw.githubusercontent.com/alec-glisman/DDPM-Enhanced-Sampling/main/images/32PAA_32Ca_32Na_64Cl_NVTeqbm.png" alt="Polyelectrolyte simulation snapshot" class="project-card-img">

### DDPM-Enhanced-Sampling

Generative framework using denoising diffusion probabilistic models (DDPMs) to sample polymer conformations consistent with Boltzmann statistics. Replaces expensive enhanced-sampling simulations with a learned model that generates physically valid conformations orders of magnitude faster.

<div class="project-tags">
  <span class="skill-tag">Python</span>
  <span class="skill-tag">PyTorch</span>
  <span class="skill-tag">Diffusion Models</span>
  <span class="skill-tag">MD Simulation</span>
</div>
<div class="project-links">
  <a href="https://github.com/alec-glisman/DDPM-Enhanced-Sampling"><i class="fab fa-github"></i> GitHub</a>
</div>

</div>

<div class="project-card reveal" style="transition-delay: 0.2s" markdown="1">

<img src="https://raw.githubusercontent.com/alec-glisman/Swimming-in-Potential-Flow/main/docs/images/collinear_swimmer_white_background.png" alt="Collinear swimmer in potential flow" class="project-card-img">

### Swimming-in-Potential-Flow

Companion code for the *Journal of Fluid Mechanics* paper on self-propulsion in potential flow. Implements boundary integral methods and analytical swimming theory in C++/CUDA for studying collective hydrodynamic interactions, demonstrating that viscous dissipation is not required for self-propulsion.

<div class="project-tags">
  <span class="skill-tag">C++</span>
  <span class="skill-tag">CUDA</span>
  <span class="skill-tag">Fluid Dynamics</span>
  <span class="skill-tag">HPC</span>
</div>
<div class="project-links">
  <a href="https://github.com/alec-glisman/Swimming-in-Potential-Flow"><i class="fab fa-github"></i> GitHub</a>
</div>

</div>

<div class="project-card reveal" style="transition-delay: 0.3s" markdown="1">

<img src="https://raw.githubusercontent.com/alec-glisman/Analysis-Polyelectrolyte-Surface-Adsorption/main/images/32PAA_32Ca_32Na_64Cl_NVTeqbm.png" alt="Polyelectrolyte surface adsorption simulation" class="project-card-img">

### Analysis-Polyelectrolyte-Surface-Adsorption

High-performance analysis pipeline for polyelectrolyte molecular dynamics trajectories. Custom multi-threaded MDAnalysis extensions achieve 100x speedup over serial processing for enhanced-sampling simulations. Automates free-energy surface construction from biased trajectory data.

<div class="project-tags">
  <span class="skill-tag">Python</span>
  <span class="skill-tag">MDAnalysis</span>
  <span class="skill-tag">GROMACS</span>
  <span class="skill-tag">HPC</span>
</div>
<div class="project-links">
  <a href="https://github.com/alec-glisman/Analysis-Polyelectrolyte-Surface-Adsorption"><i class="fab fa-github"></i> GitHub</a>
</div>

</div>

<div class="project-card reveal" style="transition-delay: 0.4s" markdown="1">

<img src="/assets/images/gromacs.png" alt="GROMACS logo" class="project-card-img project-card-img--logo">

### Polyelectrolyte-Surface-Adsorption

Production MD simulation workflows for studying polyelectrolyte adsorption to mineral surfaces. Uses GROMACS and metadynamics to compare direct and water-mediated binding modes on CaCO₃, with applications to water treatment and scale inhibition.

<div class="project-tags">
  <span class="skill-tag">Python</span>
  <span class="skill-tag">GROMACS</span>
  <span class="skill-tag">Molecular Dynamics</span>
  <span class="skill-tag">Metadynamics</span>
</div>
<div class="project-links">
  <a href="https://github.com/alec-glisman/Polyelectrolyte-Surface-Adsorption"><i class="fab fa-github"></i> GitHub</a>
</div>

</div>
