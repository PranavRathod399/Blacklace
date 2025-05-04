# Blacklace: Graphene Amplifier Evolution Log

This document outlines the rationale, experiments, challenges, and eventual reformation of the graphene-based signal amplifier used in Blacklace.

---

## 1. Why Graphene?

Graphene was selected as the base material for its exceptional electrical, thermal, and mechanical properties:

- **High electrical conductivity**  
- **Atomic-scale thickness** enabling compact design  
- **Temperature stability** across typical BCI operating conditions  
- **Biocompatibility** with skin-contact interfaces  
- **Signal sensitivity** superior to traditional metals like gold or silver chloride

Compared to dry electrodes, graphene offered an increase in signal resolution, faster charge transfer rates, and stability over long periods without the need for gels or re-wetting.

---

## 2. Experimental Results with Pure Graphene

**Thickness Tested:**  
- Monolayer (1 atom thick)  
- Few-layer (2–5 layers)  
- Multilayer (>10 layers)

**Best Performing Configuration:**  
- Few-layer graphene (~3–4 layers) offered optimal balance between conductivity and manufacturability.

**Observations:**  
- **Signal amplification** was excellent, with minimal baseline drift.  
- **Thermal noise** was negligible due to material stability.  
- **Impedance** was low and consistent across test frequencies.

---

## 3. The Problem

Despite the performance benefits, pure graphene introduced **a critical issue**:

- **Power consumption was ~50x higher** than standard dry electrode systems.
- Continuous operation led to **heating** at localized junctions.
- Environmental noise coupling was amplified along with the neural signal.

This made pure graphene **impractical for wearable, low-power BCI applications.**

---

## 4. Signal Noise Amplification

While graphene captured weak neural signals, it also amplified:
- **Powerline interference (50/60Hz)**
- **Muscle artifact cross-talk**
- **Ambient EMI**

Attempts to shield the system resulted in increased complexity and further power use.

---

## 5. Solutions and the Reformation

### **A. Composite Graphene Integration**
- Switched to **graphene-PDMS** and **graphene-PEDOT:PSS** composites
- Achieved ~30–40% reduction in power draw
- Impedance slightly increased but signal fidelity remained acceptable

### **B. Analog Signal Conditioning**
- Introduced **notch filters** at 50Hz to reduce powerline interference  
- Added **bandpass filters** to isolate neural frequency bands (1–100 Hz)

---

## 6. Outcome

Blacklace v0.2 now uses a **graphene composite amplifier** with:
- Lower power consumption  
- Retained high SNR  
- Compatibility with skin-contact dry electrode setups  
- Embedded analog filters for real-time noise rejection

---

## 7. Future Work

- Explore **carbon nanotube** composites for further optimization  
- Conduct **long-term impedance stability** tests  
- Benchmark composite electrodes in mobile environments  
- Integrate directly with IRS decoding stack

---

*Logged by Pranav Rathod  
May 2025*
