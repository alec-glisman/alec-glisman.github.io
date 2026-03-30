---
permalink: /
title: "Alec Glisman"
excerpt: "Senior AI/ML Scientist at Merck applying generative AI and physics-based simulation to drug discovery. PhD Chemical Engineering, Caltech 2024."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div class="reveal hero-wrapper hex-bg">
  <!-- Decorative background accent icons -->
  <svg class="hero-bg-icon" style="top: 10px; right: 20px;" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="1.2" aria-hidden="true">
    <circle cx="12" cy="5" r="3"/><circle cx="5" cy="18" r="3"/><circle cx="19" cy="18" r="3"/>
    <line x1="12" y1="8" x2="5" y2="15"/><line x1="12" y1="8" x2="19" y2="15"/>
  </svg>
  <svg class="hero-bg-icon" style="bottom: 15px; right: 55px;" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#7C3AED" stroke-width="1.2" aria-hidden="true">
    <path d="M3 17 C7 13, 11 19, 15 14 S21 11, 21 11"/>
    <path d="M3 13 C7 9, 11 15, 15 10 S21 7, 21 7" opacity="0.5"/>
  </svg>
  <svg class="hero-bg-icon" style="bottom: 20px; left: 85px;" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="1.2" aria-hidden="true">
    <circle cx="8" cy="12" r="3"/><circle cx="16" cy="8" r="3"/><circle cx="16" cy="16" r="3"/>
    <line x1="11" y1="12" x2="13" y2="9"/><line x1="11" y1="12" x2="13" y2="15"/>
  </svg>

  <div class="hero-icon-column">
    <div class="hero-icon-item">
      {% include domain-icons.html icon="ai" size="26" label="AI and Machine Learning" %}
      <span class="hero-icon-label">AI/ML</span>
    </div>
    <div class="hero-icon-divider"></div>
    <div class="hero-icon-item">
      {% include domain-icons.html icon="physics" size="26" label="Physics" %}
      <span class="hero-icon-label">Physics</span>
    </div>
    <div class="hero-icon-divider"></div>
    <div class="hero-icon-item">
      {% include domain-icons.html icon="drug" size="26" label="Drug Design" %}
      <span class="hero-icon-label">Drug Design</span>
    </div>
    <div class="hero-icon-divider"></div>
    <div class="hero-icon-item">
      {% include domain-icons.html icon="fluids" size="26" label="Fluid Dynamics" %}
      <span class="hero-icon-label">Fluids</span>
    </div>
  </div>

  <div class="hero-intro" markdown="1">

I am a **Senior AI/ML Scientist at Merck & Co.**, where I apply predictive deep learning and generative AI to accelerate drug discovery. I bridge physics-based simulation and cheminformatics with machine learning to design, predict, and optimize small molecule therapeutics.

My background spans fluid mechanics, polymer physics, and generative chemistry. I completed my PhD in Chemical Engineering at Caltech in 2024 under [Prof. Zhen-Gang Wang](http://zgwlab.che.caltech.edu/). My thesis used molecular simulations of charged polymers and multivalent ions to explain mechanisms of mineralization, adsorption, and polymer-surface interactions. Earlier, I worked with [Prof. John F. Brady](https://cheme.caltech.edu/groups/jfb/index.html) on self-propulsion in active matter and with [Prof. Kranthi K. Mandadapu](https://mandadapu-group.github.io/) at UC Berkeley on the mechanics of lipid membranes.

I welcome collaborations in AI for science, molecular modeling, and generative chemistry.

  </div>
</div>

<div class="section-divider" aria-hidden="true"></div>

## Research Background

My work spans generative AI for drug discovery and the physics of soft matter.

<div class="research-card reveal" style="transition-delay: 0.05s" markdown="1">
<i class="fas fa-brain card-icon"></i>

### Generative AI, Molecular Design & Property Prediction

<span class="research-badge research-badge--ai">AI/ML</span><span class="research-badge research-badge--drug">Drug Discovery</span>

Drug design requires simultaneous optimization of potency, selectivity, pharmacokinetic and safety properties, and synthesizability. I build generative models that jointly optimize these competing objectives while enforcing synthesizability as a hard constraint, so every proposed molecule can actually be made. I also develop ensemble property-prediction models combining graph neural networks with molecular fingerprints, placing 18th out of 400+ submissions in the [OpenADMET-ExpansionRx Blind Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge).

</div>

<div class="research-card reveal" style="transition-delay: 0.1s" markdown="1">
<i class="fas fa-atom card-icon"></i>

### Polyelectrolyte Simulations & Ion Binding

<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--ai">AI/ML</span>

Charged polymers (polyelectrolytes) in water bind multivalent ions like calcium, a property exploited in water softening and scale inhibition. Yet the molecular mechanisms of this binding were not well understood. Using all-atom molecular dynamics and enhanced sampling, I showed that calcium bridges between carboxylate groups on neighboring polymer chains drive chain association and precipitation. I combined these simulations with unsupervised deep learning to map concentration-dependent phase diagrams and structure-property relationships in collaboration with Dow Chemical.

</div>

<!-- Hidden to shorten main page:
<div class="research-card reveal" style="transition-delay: 0.15s" markdown="1">
<i class="fas fa-water card-icon"></i>

### Microhydrodynamics & Active Matter

<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Fluid Dynamics</span>

Active matter systems, including fish schools, bacterial colonies, and swimming microorganisms, display striking collective behaviors. I set out to understand how much of this emerges from fluid mechanics alone, without phenomenological interaction rules. I derived a framework for self-propulsion in potential flow and found that a deformable body can achieve net displacement without performing net work on the fluid. Viscous dissipation had previously been considered necessary for propulsion. I also developed C++/CUDA simulations showing that purely hydrodynamic coupling can produce emergent collective ordering.

</div>

<div class="research-card reveal" style="transition-delay: 0.2s" markdown="1">
<i class="fas fa-dna card-icon"></i>

### Lipid Membrane Mechanics

<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Theory</span>

Lipid membranes are not simply static barriers. They flow in-plane as viscous fluids while bending out-of-plane as elastic shells, making them unusual materials whose dynamics are difficult to analyze. I developed a continuum theory coupling in-plane viscous flow to out-of-plane elastic bending, introducing the [Scriven-Love number](/publications/2020-scriven-love-1), a dimensionless ratio that quantifies when intramembrane viscous stresses matter relative to elastic bending forces. Computing this number across physiologically relevant processes showed that in-plane viscosity cannot generally be ignored in membrane dynamics.

</div>
-->

<div class="section-divider" aria-hidden="true"></div>

<div class="reveal" style="transition-delay: 0.25s" markdown="1">

## Education

| | |
|---|---|
| **PhD, Chemical Engineering** | California Institute of Technology, 2024 |
| **MS, Chemical Engineering** | California Institute of Technology, 2022 |
| **BS, Chemical Engineering** | University of California, Berkeley, 2019 |

</div>

<div class="reveal" style="transition-delay: 0.35s" markdown="1">

<a href="/publications/" class="btn--primary-cta">Publications</a>
<a href="/experience/" class="btn--outline-cta">Experience</a>
<a href="/projects/" class="btn--outline-cta">Projects</a>
<a href="https://www.linkedin.com/in/alec-glisman" class="btn--outline-cta">Contact</a>

</div>
