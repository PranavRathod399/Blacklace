# 🧠 AI-Driven Brain-Computer Interface (BCI) with Graphene-Based Signal Amplification

Welcome to the official repository for my independent research project focused on building a non-invasive Brain-Computer Interface (BCI) system. This project explores how simulated **graphene-based neural signal amplification** and **adaptive deep learning models** can translate human thought into real-time digital actions.

**Author**: Pranav Rathod (19, India)  
**Status**: Active Research | Early Prototype  
**Affiliations**: Community-supported | Collaborating with insights from Stanford & CMU open research

---
## Table of Contents
1. [Overview](#project-overview)
2. [Motivation](#scientific-motivation)
3. [Architecture](#system-architecture)
4. [Installation](#installation––running)
5. [Demo](#demo-output)
6. [Roadmap](#roadmap)
7. [Contributing](#contributions–feedback)
---

## 🚀 Project Overview

This project simulates a next-gen BCI system by integrating:
- Graphene-inspired signal amplification
- Real EEG data from public datasets
- AI models for decoding mental intent into executable commands

The system is designed to aid individuals with **paralysis, speech disorders**, and **mobility impairments** by enabling direct communication from brain to machine—without surgical implants.

---

## 🧪 Scientific Motivation

Inspired by research in **graphene electronics** and breakthroughs in **speech neuroprosthetics**, this project investigates:
- How graphene-like amplification might improve EEG signal fidelity
- How deep learning can decode inner speech or intent from neural signals
- Whether these can be combined into a fully non-invasive BCI pipeline

Reference support includes:
- [Stanford’s Speech BCI Dataset (Dryad)](https://doi.org/10.5061/dryad.x69p8czpq)
- [Nature 2023: High-Performance Speech Neuroprosthesis](https://www.nature.com/articles/s41586-023-06202-0)
- [Willett et al. RNN Decoder GitHub](https://github.com/fwillett/speechBCI)

---
## ⚙️ System Architecture

```
- [x] [EEG Data Input (real/simulated)]
                |
                v
- [x] [Graphene Amplifier Simulation] 
                |
                v
- [o] [Preprocessing & Noise Reduction]
                |
                v
- [] [Deep Learning Model (CNN/RNN)]
                |
                v
- [] [Thought Prediction / Intent Output]
                |
                v
- [] [Applications: Cursor / Text / Prosthetics]
```

---
## 📂 Repository Structure

```
├── Graphene_Amplifier1.ipynb         # Jupyter notebook for graphene amplifier simulation
├── BCI_AI_Summary_PranavRathod.pdf   # Visual and written proposal
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⬇️ Installation & Running

### Option 1: Run on Google Colab

> Upload your EEG `.mat` or `.csv` file  
> Open `Graphene_Amplifier1.ipynb`  
> Visualize raw vs. amplified EEG signals

### Option 2: Local Setup

```bash
git clone https://github.com/PranavRathod399/BCI_graphene_prototype.git
cd BCI_graphene_prototype
# Install necessary packages as per the notebook requirements
```

---

## 🧠 Demo Output (to be updated)

---

## 📅 Roadmap

- [x] Graphene-inspired amplifier (simulated)  
- [x] Dryad EEG dataset integration  
- [ ] CNN/RNN for intent decoding  
- [ ] Signal classification benchmarking  
- [ ] Graphene hardware exploration (future)  
- [ ] Full BCI prototype UI  
---
## Phase 1 Complete: Graphene Amplifier Simulation Results

**Objective:**  
To simulate the behavior of a theoretical graphene-based amplifier for EEG signal enhancement, using Python tools and synthetic neural waveforms as a foundation.

**Tools Used:**  
- Python (Google Colab)  
- NumPy, Matplotlib, SciPy  
- Simulated EEG-style signals

**Key Results:**  
- Modeled basic signal amplification using graphene-inspired properties.  
- Observed improved amplitude and waveform clarity across signal variations.  
- Compared input vs. amplified waveforms in both time and frequency domains.  
- Established a flexible signal pipeline for future integration with neural decoding systems.

**Key Visuals & Outputs:**

### Original EEG Signal (Simulated)
![Original Signal]()

### Amplified EEG Signal
![Amplified Signal]()

### Raw vs Amplified Comparison
![Comparison]()

### SNR Calculation Visualization
![SNR]()

Full code and simulation in [Graphene_Amplifier1.ipynb](https://github.com/PranavRathod399/BCI_graphene_prototype/blob/main/Graphene_Amplifier1.ipynb)

**Reflection:**  
This phase validated the feasibility of modeling signal amplification through simulated graphene behavior. The signal pipeline and logic now set the stage for **Phase 2: Filtering, Interference Handling, and AI Integration**.

**Note:**  
Phase 2 will also incorporate **real EEG datasets** to evaluate how the amplifier behaves on authentic neural signals, enabling more realistic signal-to-noise analysis and preparing the ground for machine learning integration.

---

## Phase 2: Real-World Optimization Begins — Interference, Noise & AI Filtering

This marks the beginning of **Phase 2** of the BCI Graphene Prototype — moving beyond basic signal simulation into real-world constraints and optimization.

### Tackling Interference & Signal Noise

Graphene’s extreme sensitivity is a double-edged sword. While it can amplify weak brain signals, it’s also vulnerable to environmental EM noise (WiFi, radio, Bluetooth, etc.).

### Why It Matters
In practical BCI systems, **noise resilience** is critical. This phase explores strategies to ensure the amplifier doesn't get overwhelmed in real-world settings.

### Strategies Explored

- **Signal Isolation & Shielding**  
  Simulated physical protections like **Faraday cages** to block external signals.

- **Frequency Filtering**  
  Implementing **band-pass filters** to isolate neural frequencies (0.5–100 Hz).

- **Graphene-based Adaptive Filtering**  
  Investigating how graphene’s tunable conductivity could support *smart*, dynamic filtering.

- **AI-Powered Noise Cancellation**  
  Early-stage conceptual models for training AI to:
  - Distinguish between real brain signals and interference.
  - Adapt filtering over time as environments change.

- **Signal Averaging Techniques**  
  Using multiple time-frame readings to reduce transient noise while preserving meaningful patterns.

### Looking Ahead
This phase forms the bridge between my materials-level amplifier model and the eventual **AI-powered neural decoding** engine.

Stay tuned for Phase 3 — integrating learning models with the filtered signal stream.

---


## 🤝 Contributions & Feedback

This is an independent, learning-driven project. I'm always open to:

- Feedback on architecture or models  
- Help with decoding models and preprocessing  
- Mentorship or collaboration  

> Email: pranavr399@gmail.com  
> GitHub: [github.com/PranavRathod399](https://github.com/PranavRathod399)

---

## ⚖️ License

This project is licensed under the MIT License—open to use, modification, and sharing for non-commercial and educational purposes.

---

**Developed independently by Pranav Rathod — driven by a passion to build real-world solutions using thought-powered technology.**
