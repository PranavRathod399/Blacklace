
# Brain-Computer Interface Prototype – Simulated Graphene Amplification

This repository hosts an independent, early-stage research project by **Pranav Rathod**, focused on simulating graphene-inspired signal amplification for brain-computer interface (BCI) applications.

The goal is to explore whether graphene-modeled signal enhancement, paired with adaptive AI decoding, can improve neural signal clarity and enable real-time decoding of cognitive intent. This system is intended to be non-invasive and could support use cases such as assistive communication, neuroprosthetics, and early cognitive diagnostics.

---

## Background

Brain-computer interfaces (BCIs) allow communication between the brain and external devices. However, non-invasive systems often face challenges such as low signal fidelity, electrical noise, and limited decoding accuracy.

Graphene, a one-atom-thick carbon material, exhibits high electrical conductivity, flexibility, and biocompatibility—making it an attractive candidate for amplifying weak EEG signals. While I do not currently have access to graphene materials, this project simulates their theoretical signal-enhancing properties and investigates how such amplification could assist with intent decoding through AI models.

The direction of this work has been inspired by responses and support from **Dr. Jamie Henderson (Stanford)**—who generously shared open datasets, a *Nature* publication, and code—as well as encouragement from **Dr. Bin He (Carnegie Mellon University)**.

---

## Repository Contents

- `/concept_notes/` – System architecture documentation and technical design rationale.
- `/simulations/` – (Coming soon) Signal processing scripts and amplification models.
- `/docs/` – Diagrams and flowcharts (to be added).
- `README.md` – Project summary and development roadmap.

---

## Usage

This repository is under active development. Planned updates include:
- Signal amplification simulation scripts
- Signal filtering and preprocessing modules
- AI-based decoding models for intent recognition

> Requirements (planned):
> - Python 3.9+  
> - NumPy, SciPy, Matplotlib  
> - TensorFlow or PyTorch

---

## Next Steps

- Develop a mapping strategy to associate EEG patterns with cognitive intent (e.g., imagined motion or speech).
- Simulate graphene's amplification effect and test it on open EEG datasets.
- Evaluate changes in signal-to-noise ratio (SNR) and decoding performance.
- Build a baseline neural decoder using RNNs or CNNs.
- Create simple visualizations to track signal clarity, amplification, and classification accuracy.

---

## Project Summary PDF

For a complete overview of the concept and current progress, view the full summary report below:

**[BCI-AI Concept Summary – Pranav Rathod (PDF)](./BCI_AI_Summary_PranavRathod.pdf)**

This document includes:
- System architecture and phase-by-phase strategy  
- Graphene simulation rationale  
- Application use cases  
- AI integration overview

---

## References

- Willett, F. R., et al. (2023). *A high-performance speech neuroprosthesis*. *Nature*. [Read the paper](https://www.nature.com/articles/s41586-023-06502-7)
- Neural dataset (Dryad): [https://doi.org/10.5061/dryad.x69p8czpq](https://doi.org/10.5061/dryad.x69p8czpq)
- Base decoding code: [GitHub – fwillett/speechBCI](https://github.com/fwillett/speechBCI)

---

## License

This project is licensed under the MIT License.  
Feel free to explore, reference, or build upon the work with attribution.

---
## About the Author

I'm a 19-year-old independent learner from India with a strong interest in brain-computer interfaces, neurotechnology, and AI signal decoding. This project is my attempt to build meaningful contributions from first principles—by learning, simulating, and creating with what’s available.

---
## Author

**Pranav Rathod**  
Email: pranavr399@gmail.com  
GitHub: [@PranavRathod399](https://github.com/PranavRathod399)
