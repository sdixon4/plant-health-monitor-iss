# NASA EPSCoR ISS Proposal — Draft Outline  
**Project Title:** Autonomous, Low-Power AI System for Plant Health Monitoring in Space and Resilient Agriculture

---

## 1. Abstract
- Summary of mission, objectives, methodology, and dual-use value
- <4000 characters (limit for NASA submission)
- Already drafted in `abstract.md`

---

## 2. Introduction and Background
- The challenge of sustainable plant growth in space
- What has already been attempted on the ISS (Veggie, etc.)
- Why early detection of plant stress matters for long-duration missions
- Novelty: fusion of AI + embedded sensing + Verilog logic
- Dual relevance to Earth (Hawai‘i climate resilience, off-grid ag)

---

## 3. Objectives and Microgravity-Specific Significance
- What scientific questions require microgravity to answer?
- What plant-environment anomalies does this system detect that can’t be replicated on Earth?
- Risk response matrix:
  | Space Anomaly | Sensor Challenge | System Response |
  |---------------|------------------|------------------|
  | CO₂ pooling   | Confused gas readings | Multi-point polling + logic override |
  | No convection | Uneven temp zones | Thermal mapping + misting lockout |

---

## 4. System Architecture and Design
- Sensor Suite:
  - IR thermal, CO₂, humidity, RGB, soil moisture
- Embedded Logic:
  - Verilog for TMR, watchdog, fallback, override
- AI Inference:
  - Quantized CNNs (trained via Brevitas/FINN)
  - Python inference engine
- XAI:
  - Transparent status codes (“Why was misting halted?”)
  - Crew-facing status lights or alert tiers
- Ethical/Fail-Safe Design:
  - Watchdog > XAI > Override chain hierarchy
- Planned figures:
  - `docs/system-diagram.png`
  - `docs/safety-logic-flow.png`

---

## 5. ISS Constraints and Flight Integration
- Power: <3W average draw, with pulsed sensing
- Volume: <3U CubeSat (100mm x 100mm x 340.5mm)
- Mass: Estimate and reserve margin
- Crew Time: Only during install/removal
- Compatibility: Express Rack or equivalent enclosure mockup
- Environment: Radiation, thermal, launch vibration
- Hardware readiness: PYNQ-Z2 prototype → Xilinx XQRKU060 target

---

## 6. Safety, Redundancy, and Fault Tolerance
- TMR logic voter (Verilog)
- Fallback states and misting lockout
- Watchdog state machine
- Safe-state escalation plan (Red/Yellow/Green)
- Radiation mitigation: logic-level protection, XQRKU060 path
- Planned simulations:
  - Logic.ly (`simulations/`) voter test
  - LTSpice failover timing test

---

## 7. Timeline and Milestones
| Phase | Date Range | Deliverable |
|-------|------------|-------------|
| Prototype architecture | June–July 2025 | PYNQ-Z2 + Logic.ly verified |
| Local farm testing | Aug–Sept 2025 | CO₂ + IR log validation |
| Verilog optimization | Fall 2025 | Integrated watchdog TMR |
| Migration study | Spring 2026 | RH-FPGA selection + schematic |
| Final testing | May 2026 | ISS deployment simulation |

- Visual timeline: `docs/timeline-gantt.png`

---

## 8. Budget Justification
- Component list + costs (PYNQ-Z2, sensors, enclosure)
- Radiation-ready upgrade path (XQRKU060)
- Power budget table: by sensor and logic block
- Development vs deployment phases
- Alignment with EPSCoR PoP (3-year use)

---

## 9. Broader Impacts and Dual-Use Potential
- Use in off-grid climate-resilient farming (e.g., post-fire, Hawai‘i)
- Local collaboration: HFUU, CTAHR
- Food security, sovereignty, and STEM pipeline support
- Planned pilot test site (O‘ahu or Kaua‘i)
- Outreach plan: high school demo, GitHub publication

---

## 10. Letters of Collaboration
- Hawai‘i Farmers Union United (HFUU) → Use case, testing data
- Texas A&M Controlled Env. Systems → Testbed support
- NASA Veggie or CTAHR → Data, review, or advisory support

---

## 11. Appendices
- Abstract
- Visuals and schematics
- Budget table
- Risk disclosures (2 CFR 200.206)
- References to prior art and systems

