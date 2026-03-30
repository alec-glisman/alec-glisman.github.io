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

A drug candidate must be potent, selective, safe, metabolically stable, and possible to synthesize. Optimizing all of these properties at once is the central challenge of molecular design. I develop generative models that tackle this multi-parameter optimization through R-group optimization, core-hopping, and knowledge-based molecular design, working directly with medicinal chemistry teams to accelerate design-make-test-analyze cycles. Early SMILES-based RNN approaches generated chemically valid but often practically inaccessible molecules. I transitioned to GFlowNet-based architectures that generate molecules exclusively over validated reaction templates using commercially available building blocks, ensuring every proposed compound carries a reviewable synthetic route. Predictive property models serve as reward functions that teach the generative models which regions of chemical space to explore, and multi-stage curriculum learning guides training from broad chemical validity toward the full multi-parameter objective.

</div>
<figure class="pub-card-figure">
  <svg viewBox="0 0 170 130" xmlns="http://www.w3.org/2000/svg" aria-label="Synthesis-constrained generative design: core scaffold with R-group attachment via reaction templates" role="img">
    <!-- Core scaffold — hexagonal ring -->
    <polygon points="60,35 78,25 96,35 96,55 78,65 60,55" fill="rgba(14,165,201,0.10)" stroke="#0EA5C9" stroke-width="1.5" stroke-linejoin="round"/>
    <!-- Scaffold atom nodes -->
    <circle cx="60" cy="35" r="3.5" fill="rgba(14,165,201,0.18)" stroke="#0EA5C9" stroke-width="1"/>
    <circle cx="78" cy="25" r="3.5" fill="rgba(14,165,201,0.18)" stroke="#0EA5C9" stroke-width="1"/>
    <circle cx="96" cy="35" r="3.5" fill="rgba(14,165,201,0.18)" stroke="#0EA5C9" stroke-width="1"/>
    <circle cx="96" cy="55" r="3.5" fill="rgba(14,165,201,0.18)" stroke="#0EA5C9" stroke-width="1"/>
    <circle cx="78" cy="65" r="3.5" fill="rgba(14,165,201,0.18)" stroke="#0EA5C9" stroke-width="1"/>
    <circle cx="60" cy="55" r="3.5" fill="rgba(14,165,201,0.18)" stroke="#0EA5C9" stroke-width="1"/>
    <!-- Side chain from scaffold -->
    <line x1="60" y1="35" x2="42" y2="25" stroke="#0EA5C9" stroke-width="1.2" opacity="0.5"/>
    <circle cx="42" cy="25" r="3" fill="rgba(14,165,201,0.12)" stroke="#0EA5C9" stroke-width="1"/>
    <line x1="42" y1="25" x2="28" y2="30" stroke="#0EA5C9" stroke-width="1.2" opacity="0.5"/>
    <circle cx="28" cy="30" r="3" fill="rgba(14,165,201,0.12)" stroke="#0EA5C9" stroke-width="1"/>
    <!-- R-group site 1 (right, from scaffold) — dashed circle -->
    <line x1="96" y1="35" x2="116" y2="28" stroke="#0EA5C9" stroke-width="1.2" opacity="0.5"/>
    <circle cx="124" cy="25" r="9" fill="none" stroke="#0EA5C9" stroke-width="1.2" stroke-dasharray="3,2" opacity="0.6"/>
    <text x="124" y="28" text-anchor="middle" font-size="8" font-family="Outfit, sans-serif" fill="#0EA5C9" opacity="0.8">R₁</text>
    <!-- R-group site 2 (bottom, from scaffold) — dashed circle -->
    <line x1="78" y1="65" x2="78" y2="82" stroke="#0EA5C9" stroke-width="1.2" opacity="0.5"/>
    <circle cx="78" cy="92" r="9" fill="none" stroke="#0EA5C9" stroke-width="1.2" stroke-dasharray="3,2" opacity="0.6"/>
    <text x="78" y="95" text-anchor="middle" font-size="8" font-family="Outfit, sans-serif" fill="#0EA5C9" opacity="0.8">R₂</text>
    <!-- Building block 1 — approaching R1 via reaction arrow -->
    <circle cx="152" cy="18" r="4" fill="rgba(27,42,74,0.12)" stroke="#1B2A4A" stroke-width="1"/>
    <line x1="152" y1="18" x2="158" y2="28" stroke="#1B2A4A" stroke-width="1" opacity="0.5"/>
    <circle cx="158" cy="28" r="3.5" fill="rgba(27,42,74,0.10)" stroke="#1B2A4A" stroke-width="1"/>
    <line x1="158" y1="28" x2="152" y2="38" stroke="#1B2A4A" stroke-width="1" opacity="0.5"/>
    <circle cx="152" cy="38" r="3" fill="rgba(27,42,74,0.08)" stroke="#1B2A4A" stroke-width="1"/>
    <!-- Reaction arrow to R1 -->
    <line x1="143" y1="25" x2="135" y2="25" stroke="#1B2A4A" stroke-width="1.2" opacity="0.5"/>
    <path d="M137,22 L133,25 L137,28" fill="none" stroke="#1B2A4A" stroke-width="1.2" opacity="0.5"/>
    <!-- Building block 2 — approaching R2 via reaction arrow -->
    <circle cx="112" cy="105" r="4" fill="rgba(27,42,74,0.12)" stroke="#1B2A4A" stroke-width="1"/>
    <line x1="112" y1="105" x2="120" y2="112" stroke="#1B2A4A" stroke-width="1" opacity="0.5"/>
    <circle cx="120" cy="112" r="3.5" fill="rgba(27,42,74,0.10)" stroke="#1B2A4A" stroke-width="1"/>
    <!-- Reaction arrow to R2 -->
    <line x1="102" y1="98" x2="92" y2="94" stroke="#1B2A4A" stroke-width="1.2" opacity="0.5"/>
    <path d="M95,91 L90,93 L93,97" fill="none" stroke="#1B2A4A" stroke-width="1.2" opacity="0.5"/>
    <!-- "Rxn" label -->
    <text x="148" y="12" font-size="6.5" font-family="Outfit, sans-serif" fill="#1B2A4A" opacity="0.55">rxn</text>
    <text x="122" y="118" font-size="6.5" font-family="Outfit, sans-serif" fill="#1B2A4A" opacity="0.55">rxn</text>
  </svg>
  <figcaption>Synthesis-constrained R-group design</figcaption>
</figure>
</div>
</div>

<div class="research-card reveal" style="transition-delay: 0.05s">
<i class="fas fa-chart-line card-icon"></i>
<div class="pub-card-inner">
<div class="pub-card-body" markdown="1">

### Molecular Property Prediction
<span class="research-badge research-badge--ai">AI/ML</span><span class="research-badge research-badge--drug">Cheminformatics</span>

I built an automated benchmarking and deployment pipeline for predicting absorption, distribution, metabolism, excretion, and toxicity (ADMET) endpoints across multiple therapeutic programs. The pipeline spans gradient-boosted trees, message-passing neural networks, and foundation models. In my experience, careful data curation and splitting drive model quality more than architecture selection. I use clustering-based scaffold splits and temporal splits to approximate the out-of-distribution challenges of real drug discovery, and statistical hypothesis testing to provide grounded architecture selection for each endpoint. These models are deployed directly to medicinal chemists for real-time property predictions and serve as reward functions for generative molecular design. As independent external validation, I applied similar pipelines to the [OpenADMET-ExpansionRx Blind Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge) and ranked **25th among 100 finalists** across 9 ADMET endpoints.

**Leaderboard:** [OpenADMET-ExpansionRx Challenge](https://huggingface.co/spaces/openadmet/OpenADMET-ExpansionRx-Challenge) · **Code:** [OpenADMET-ExpansionRx-Blind-Challenge](https://github.com/alec-glisman/OpenADMET-ExpansionRx-Blind-Challenge)

</div>
<figure class="pub-card-figure">
  <svg viewBox="0 0 170 130" xmlns="http://www.w3.org/2000/svg" aria-label="Multi-architecture benchmarking: molecule input to parallel models producing property predictions" role="img">
    <!-- Input molecule (small graph) -->
    <circle cx="22" cy="52" r="5" fill="rgba(14,165,201,0.15)" stroke="#0EA5C9" stroke-width="1.2"/>
    <circle cx="14" cy="64" r="4" fill="rgba(14,165,201,0.12)" stroke="#0EA5C9" stroke-width="1.2"/>
    <circle cx="30" cy="64" r="4" fill="rgba(14,165,201,0.12)" stroke="#0EA5C9" stroke-width="1.2"/>
    <circle cx="22" cy="74" r="3.5" fill="rgba(14,165,201,0.10)" stroke="#0EA5C9" stroke-width="1"/>
    <line x1="22" y1="52" x2="14" y2="64" stroke="#0EA5C9" stroke-width="1" opacity="0.5"/>
    <line x1="22" y1="52" x2="30" y2="64" stroke="#0EA5C9" stroke-width="1" opacity="0.5"/>
    <line x1="14" y1="64" x2="22" y2="74" stroke="#0EA5C9" stroke-width="1" opacity="0.5"/>
    <line x1="30" y1="64" x2="22" y2="74" stroke="#0EA5C9" stroke-width="1" opacity="0.5"/>
    <!-- Diverging arrows from molecule to models -->
    <line x1="36" y1="55" x2="52" y2="35" stroke="#0EA5C9" stroke-width="1" opacity="0.35"/>
    <line x1="36" y1="63" x2="52" y2="63" stroke="#0EA5C9" stroke-width="1" opacity="0.35"/>
    <line x1="36" y1="71" x2="52" y2="91" stroke="#0EA5C9" stroke-width="1" opacity="0.35"/>
    <!-- Model A box (top) -->
    <rect x="54" y="24" width="52" height="20" rx="3" fill="rgba(14,165,201,0.08)" stroke="#0EA5C9" stroke-width="1.2"/>
    <text x="80" y="37" text-anchor="middle" font-size="7" font-family="Outfit, sans-serif" fill="#1B2A4A" opacity="0.7">Trees</text>
    <!-- Model B box (middle) -->
    <rect x="54" y="52" width="52" height="20" rx="3" fill="rgba(14,165,201,0.12)" stroke="#0EA5C9" stroke-width="1.2"/>
    <text x="80" y="65" text-anchor="middle" font-size="7" font-family="Outfit, sans-serif" fill="#1B2A4A" opacity="0.7">MPNN</text>
    <!-- Model C box (bottom) -->
    <rect x="54" y="80" width="52" height="20" rx="3" fill="rgba(14,165,201,0.08)" stroke="#0EA5C9" stroke-width="1.2"/>
    <text x="80" y="93" text-anchor="middle" font-size="7" font-family="Outfit, sans-serif" fill="#1B2A4A" opacity="0.7">Foundation</text>
    <!-- Converging arrows from models to prediction -->
    <line x1="108" y1="35" x2="124" y2="55" stroke="#0EA5C9" stroke-width="1" opacity="0.35"/>
    <line x1="108" y1="63" x2="124" y2="63" stroke="#0EA5C9" stroke-width="1" opacity="0.35"/>
    <line x1="108" y1="91" x2="124" y2="71" stroke="#0EA5C9" stroke-width="1" opacity="0.35"/>
    <!-- Prediction output — bar chart motif -->
    <rect x="128" y="68" width="7" height="22" rx="1" fill="rgba(14,165,201,0.25)" stroke="#0EA5C9" stroke-width="0.8"/>
    <rect x="138" y="50" width="7" height="40" rx="1" fill="rgba(14,165,201,0.35)" stroke="#0EA5C9" stroke-width="0.8"/>
    <rect x="148" y="58" width="7" height="32" rx="1" fill="rgba(14,165,201,0.20)" stroke="#0EA5C9" stroke-width="0.8"/>
    <!-- Labels -->
    <text x="22" y="18" text-anchor="middle" font-size="6.5" font-family="Outfit, sans-serif" fill="#1B2A4A" opacity="0.5">molecule</text>
    <text x="80" y="16" text-anchor="middle" font-size="6.5" font-family="Outfit, sans-serif" fill="#1B2A4A" opacity="0.5">models</text>
    <text x="142" y="42" text-anchor="middle" font-size="6.5" font-family="Outfit, sans-serif" fill="#1B2A4A" opacity="0.5">ADMET</text>
  </svg>
  <figcaption>Multi-architecture benchmarking</figcaption>
</figure>
</div>
</div>

<div class="research-card reveal" style="transition-delay: 0.1s">
<i class="fas fa-atom card-icon"></i>
<div class="pub-card-inner">
<div class="pub-card-body" markdown="1">

### Polyelectrolyte Complexation & Ion Binding
<span class="research-badge research-badge--physics">Physics</span><span class="research-badge research-badge--sim">Simulation</span>

Charged polymers (polyelectrolytes) in water bind multivalent ions like Ca²⁺, a property exploited in water softening, drug delivery, and scale inhibition. Yet the molecular mechanisms underlying ion-mediated chain-chain attraction remained elusive. Using well-tempered metadynamics and Hamiltonian replica exchange, I calculated binding isotherms and free-energy landscapes for Ca²⁺ on poly(acrylic acid). Increasing Ca²⁺ concentrations induced attraction between chains, but the binding energy was not contingent on the number of ion bridges formed; instead, correlations between chelated ions were the primary driver. At high ionic strengths, electrostatic screening significantly reduced ion bridging. Surface adsorption studies showed that water-mediated hydrogen bonds and ion bridges through interfacial water, not direct polymer-surface contacts, govern binding on CaCO₃. This toolkit was extended to copolymers of acrylic acid with vinyl acetate and vinyl alcohol, and to polypeptides of aspartate and glutamate. This work was conducted in collaboration with Dow Chemical.

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

Polyelectrolyte simulations produce high-dimensional free-energy landscapes where interpretable structure-property relationships are hard to extract directly. I trained an autoencoder neural network to analyze ion-polyelectrolyte complex structures; the learned latent space effectively differentiated dominant polymer conformations and distinguished ions bridging across chains from those adsorbed on single chains, revealing distinct contributions of each binding mode. I also developed denoising diffusion probabilistic models (DDPMs) to generate polymer conformational ensembles consistent with Boltzmann statistics, accelerating conformational exploration that would otherwise require substantially more simulation time.

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

Schools of fish, flocks of birds, and bacterial colonies all display spontaneous collective ordering. I set out to understand how much of this behavior emerges from fluid mechanics alone, without phenomenological interaction rules. Using a multipole expansion technique, I derived an analytical framework for self-propulsion in potential flow showing that a deformable body achieves net displacement by exploiting its configuration-dependent added mass, without performing net work on the fluid. Self-propulsion had previously been thought to require viscous dissipation, which is absent in potential flow. I then developed C++/CUDA many-body simulations parallelized via OpenMP, demonstrating that purely hydrodynamic interactions are sufficient to produce emergent collective structures. The fluid medium establishes a natural length scale, dependent on body configuration and velocity, that governs the system dynamics.

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

Lipid membranes are unusual materials. Lipids flow in-plane as a two-dimensional viscous fluid while the membrane bends out-of-plane as an elastic shell. The coupling between these two behaviors had been largely overlooked. Using differential geometry and linear irreversible thermodynamics, I developed a continuum theory for membrane dynamics across planar, spherical, and cylindrical geometries. A scaling analysis identified two governing dimensionless numbers: the Föppl-von Kármán number, comparing tension to bending forces, and the Scriven-Love number, a novel ratio comparing out-of-plane forces from intramembrane viscous stresses to elastic bending forces. Evaluating these numbers across physiological processes and *in vitro* experiments showed that in-plane viscosity cannot generally be neglected.

**Key paper:** [Physical Review E 2020](/publications/2020-scriven-love-1)

</div>
<figure class="pub-card-figure">
  <img src="/assets/images/2020-pre-scriven-love-figure-1.png" alt="Surface tension and viscous forces on a perturbed lipid membrane">
  <figcaption>Membrane force schematics</figcaption>
</figure>
</div>
</div>
