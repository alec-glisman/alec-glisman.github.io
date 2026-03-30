---
layout: single
title: "Research"
permalink: /research/
author_profile: true
excerpt: "Research by Alec Glisman combining physics-based simulation, machine learning, and theoretical mechanics. Generative AI for drug discovery, polyelectrolyte complexation, microhydrodynamics, and lipid membrane mechanics."
---

<div class="hex-bg" style="padding: 0.5em 0; margin-bottom: 0.5em;">

My work sits at the intersection of physics-based simulation, machine learning, and molecular design. I came to drug discovery through soft matter physics, first studying how lipid membranes deform, then how charged polymers and multivalent ions interact in aqueous solution. That grounding in molecular-scale physics shapes how I approach generative AI and property prediction for drug candidates. I care about more than predictive accuracy. I want to understand *why* molecules behave as they do and use that understanding to guide design.

</div>

<div class="section-divider" aria-hidden="true"></div>

<div class="research-card reveal" style="transition-delay: 0s">
<i class="fas fa-brain card-icon"></i>
<div class="pub-card-inner">
<div class="pub-card-body" markdown="1">

### Generative AI & Molecular Design
<span class="research-badge research-badge--ai">AI/ML</span><span class="research-badge research-badge--drug">Drug Discovery</span>

A drug candidate must be potent, selective, safe, metabolically stable, and possible to synthesize. Optimizing all of these properties at once is the central challenge of molecular design. I develop generative models that navigate this landscape through two complementary modes. *De novo generation* explores broad chemical space to discover novel molecular scaffolds. *Series-constrained generation* modifies specific positions on a known active molecule, exploiting accumulated structure-activity relationships during lead optimization. Synthesizability is enforced as a hard constraint: every generated candidate is filtered against known reaction templates and commercially available building blocks, so compounds are synthetically accessible.

</div>
<figure class="pub-card-figure">
  <svg viewBox="0 0 170 130" xmlns="http://www.w3.org/2000/svg" aria-label="Generative molecular design: interconnected molecular graph" role="img">
    <!-- Molecular graph representing de novo generation -->
    <!-- Bonds -->
    <line x1="55" y1="35" x2="85" y2="25" stroke="#0EA5C9" stroke-width="1.5" opacity="0.5"/>
    <line x1="85" y1="25" x2="115" y2="40" stroke="#0EA5C9" stroke-width="1.5" opacity="0.5"/>
    <line x1="115" y1="40" x2="120" y2="72" stroke="#0EA5C9" stroke-width="1.5" opacity="0.5"/>
    <line x1="120" y1="72" x2="95" y2="95" stroke="#0EA5C9" stroke-width="1.5" opacity="0.5"/>
    <line x1="95" y1="95" x2="60" y2="90" stroke="#0EA5C9" stroke-width="1.5" opacity="0.5"/>
    <line x1="60" y1="90" x2="45" y2="62" stroke="#0EA5C9" stroke-width="1.5" opacity="0.5"/>
    <line x1="45" y1="62" x2="55" y2="35" stroke="#0EA5C9" stroke-width="1.5" opacity="0.5"/>
    <!-- Cross bonds -->
    <line x1="55" y1="35" x2="120" y2="72" stroke="#0EA5C9" stroke-width="1" opacity="0.2"/>
    <line x1="85" y1="25" x2="95" y2="95" stroke="#0EA5C9" stroke-width="1" opacity="0.2"/>
    <!-- Atoms (nodes) -->
    <circle cx="55" cy="35" r="8" fill="rgba(14,165,201,0.12)" stroke="#0EA5C9" stroke-width="1.5"/>
    <circle cx="85" cy="25" r="10" fill="rgba(14,165,201,0.15)" stroke="#0EA5C9" stroke-width="1.5"/>
    <circle cx="115" cy="40" r="7" fill="rgba(14,165,201,0.10)" stroke="#0EA5C9" stroke-width="1.5"/>
    <circle cx="120" cy="72" r="9" fill="rgba(14,165,201,0.12)" stroke="#0EA5C9" stroke-width="1.5"/>
    <circle cx="95" cy="95" r="8" fill="rgba(14,165,201,0.12)" stroke="#0EA5C9" stroke-width="1.5"/>
    <circle cx="60" cy="90" r="6" fill="rgba(14,165,201,0.08)" stroke="#0EA5C9" stroke-width="1.5"/>
    <circle cx="45" cy="62" r="7" fill="rgba(14,165,201,0.10)" stroke="#0EA5C9" stroke-width="1.5"/>
    <!-- Generation arrow motif -->
    <path d="M135 60 L148 60" stroke="#0EA5C9" stroke-width="1.5" opacity="0.4"/>
    <path d="M144 55 L150 60 L144 65" fill="none" stroke="#0EA5C9" stroke-width="1.5" opacity="0.4"/>
    <!-- Small generated fragment -->
    <circle cx="158" cy="55" r="4" fill="rgba(14,165,201,0.15)" stroke="#0EA5C9" stroke-width="1"/>
    <circle cx="158" cy="65" r="3.5" fill="rgba(14,165,201,0.10)" stroke="#0EA5C9" stroke-width="1"/>
    <line x1="158" y1="55" x2="158" y2="65" stroke="#0EA5C9" stroke-width="1" opacity="0.4"/>
    <!-- Side chain stub -->
    <line x1="55" y1="35" x2="35" y2="22" stroke="#0EA5C9" stroke-width="1" opacity="0.3"/>
    <circle cx="35" cy="22" r="4" fill="rgba(14,165,201,0.08)" stroke="#0EA5C9" stroke-width="1" opacity="0.5"/>
  </svg>
  <figcaption>Generative molecular design</figcaption>
</figure>
</div>
</div>

<div class="research-card reveal" style="transition-delay: 0.05s" markdown="1">
<i class="fas fa-chart-line card-icon"></i>

### Molecular Property Prediction
<span class="research-badge research-badge--ai">AI/ML</span><span class="research-badge research-badge--drug">Cheminformatics</span>

I developed stacked ensemble models that combine graph neural network representations with molecular fingerprints and physicochemical descriptors to predict absorption, distribution, metabolism, excretion, and toxicity (ADMET) endpoints. Curriculum learning substantially improved generalization. Training first on large public datasets, then fine-tuning on the target distribution, helped the models remain robust across structurally diverse compounds. Cross-validation with both chemical-similarity and temporal splits produced generalization estimates resilient to distribution shift. Evaluated on fully held-out compound libraries in the [OpenADMET-ExpansionRx Blind Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge), this approach placed **18th out of 400+ submissions** across 9 ADMET endpoints.

**Leaderboard:** [OpenADMET-ExpansionRx Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge) · **Code:** [OpenADMET-ExpansionRx-Blind-Challenge](https://github.com/alec-glisman/OpenADMET-ExpansionRx-Blind-Challenge)

</div>

<div class="research-card reveal" style="transition-delay: 0.1s">
<i class="fas fa-atom card-icon"></i>
<div class="pub-card-inner">
<div class="pub-card-body" markdown="1">

### Polyelectrolyte Complexation & Ion Binding
<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Simulation</span>

Charged polymers (polyelectrolytes) in water bind multivalent ions like Ca²⁺, a property exploited in water softening, drug delivery, and scale inhibition. Yet the molecular mechanisms of this binding were not well understood. Using well-tempered metadynamics and Hamiltonian replica exchange, I calculated binding isotherms and free-energy landscapes for Ca²⁺ on poly(acrylic acid), identifying two dominant binding geometries distinguished by carboxylate coordination number. All-atom MD combined with unsupervised deep learning mapped concentration-dependent phase diagrams. Surface adsorption studies showed that water-mediated hydrogen bonds, not direct polymer-surface contacts, govern binding on CaCO₃. This work was conducted in collaboration with Dow Chemical.

**Key papers:** [Langmuir 2025](/publications/2025-langmuir-binding-modes) · [Macromolecules 2024](/publications/2024-macromolecules-polyelectrolyte) · [Langmuir 2024](/publications/2024-langmuir-adsorption-isotherm)

</div>
<figure class="pub-card-figure">
  <img src="/assets/images/2024-langmuir-adsorption-isotherm.jpeg" alt="Ca²⁺ adsorption isotherm and binding free-energy landscape on poly(acrylic acid)">
  <figcaption>Ca²⁺ binding free energy</figcaption>
</figure>
</div>
</div>

<div class="research-card reveal" style="transition-delay: 0.15s">
<i class="fas fa-project-diagram card-icon"></i>
<div class="pub-card-inner">
<div class="pub-card-body" markdown="1">

### AI/ML Methods in Soft Matter
<span class="research-badge research-badge--ai">AI/ML</span><span class="research-badge research-badge--sim">Deep Learning</span>

Polyelectrolyte simulations produce high-dimensional free-energy landscapes where interpretable structure-property relationships are hard to extract directly. I developed workflows coupling enhanced-sampling molecular dynamics with dimensionality reduction and clustering, identifying dominant polymer conformations and their thermodynamic stability from trajectory data. I also trained denoising diffusion probabilistic models (DDPMs) to generate polymer conformational ensembles consistent with Boltzmann statistics. These models offer a fast generative complement to physics-based sampling for polymer design.

**Code:** [DDPM-Enhanced-Sampling](https://github.com/alec-glisman/DDPM-Enhanced-Sampling)

</div>
<figure class="pub-card-figure">
  <img src="/assets/images/2024-macromolecules-polyelectrolyte-association.jpeg" alt="Ca²⁺-mediated polyelectrolyte chain association phase diagram">
  <figcaption>Ion-mediated chain association</figcaption>
</figure>
</div>
</div>

<div class="research-card reveal" style="transition-delay: 0.2s">
<i class="fas fa-water card-icon"></i>
<div class="pub-card-inner">
<div class="pub-card-body" markdown="1">

### Microhydrodynamics & Active Matter
<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Fluid Dynamics</span>

Schools of fish, flocks of birds, and bacterial colonies all display spontaneous collective ordering. I set out to understand how much of this behavior emerges from fluid mechanics alone, without phenomenological interaction rules. I derived an analytical framework for self-propulsion in potential flow showing that a deformable body achieves net displacement by exploiting its configuration-dependent added mass, without performing net work on the fluid. Self-propulsion had previously been thought to require viscous dissipation, which is absent in potential flow. I also developed C++/CUDA boundary integral simulations for many-body Stokes flow, demonstrating that purely hydrodynamic coupling is sufficient to produce collective ordering in active particle suspensions.

**Key paper:** [J. Fluid Mechanics 2022](/publications/2022-potential-flow-2)

</div>
<figure class="pub-card-figure">
  <img src="/assets/images/2022-jfm-swimmer-schematic.svg" alt="Schematic of N connected spherical particles forming a deformable swimmer body">
  <figcaption>Deformable body swimmer model</figcaption>
</figure>
</div>
</div>

<div class="research-card reveal" style="transition-delay: 0.25s">
<i class="fas fa-dna card-icon"></i>
<div class="pub-card-inner">
<div class="pub-card-body" markdown="1">

### Lipid Membrane Mechanics
<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Theory</span>

Lipid membranes are unusual materials. Lipids flow in-plane as a two-dimensional viscous fluid while the membrane bends out-of-plane as an elastic shell. The coupling between these two behaviors had been largely overlooked. Using differential geometry and linear irreversible thermodynamics, I developed a continuum theory for membrane dynamics across planar, spherical, and cylindrical geometries. This work introduced the Scriven-Love number, a dimensionless ratio quantifying when intramembrane viscous stresses matter relative to elastic bending forces. Evaluating this number across physiological processes showed that in-plane viscosity cannot generally be neglected.

**Key paper:** [Physical Review E 2020](/publications/2020-scriven-love-1)

</div>
<figure class="pub-card-figure">
  <img src="/assets/images/2020-pre-scriven-love-figure-1.png" alt="Surface tension and viscous forces on a perturbed lipid membrane">
  <figcaption>Membrane force schematics</figcaption>
</figure>
</div>
</div>
