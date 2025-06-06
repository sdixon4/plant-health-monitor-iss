# HELEN Fusion 360 Script Library

This folder contains modular Fusion 360 Python scripts used to generate the physical enclosure for **HELEN** — *Hybrid Embedded Logic for Ecological Neuroinference* — a plant health monitoring payload designed for ISS deployment through the NASA EPSCoR Flight Opportunity.

Each script is independently executable and builds a single parametric feature (e.g., base, lid, vent, mounting post). Together, they form a complete 1U CubeSat-compatible housing with mechanical and sensor integration.

---

## 🧩 Component Scripts

| Script Name | Description |
|-------------|-------------|
| `HELEN_Base_Builder.py`        | Creates the main 85 mm × 85 mm × 20 mm enclosure base with 2 mm shell walls |
| `HELEN_Lid_Generator.py`       | Adds a 2 mm removable lid that caps the enclosure cleanly |
| `HELEN_Vents_Thermal.py`       | Cuts a 4 mm thermal vent on the Y+ wall for an MLX90640 IR sensor |
| `HELEN_Vents_CO2.py`           | Cuts a 5 mm circular vent on the X+ wall for a CO₂/gas sensor |
| `HELEN_Standoffs_Generator.py` | Adds four internal standoffs (3 mm dia × 10 mm height) for mounting a sensor board |
| `HELEN_ScrewHoles_Generator.py`| Drills centered M2.5 mounting holes into each standoff (2.6 mm diameter) |
| `HELEN_Camera_Window.py`       | Cuts a 10 mm × 6 mm rectangular window on the Y+ wall for an imaging module (e.g., Arducam) |

---

## 🛠️ How to Use

These scripts are intended to be run from within **Fusion 360**:

1. Open Fusion 360
2. Go to **Utilities > Scripts and Add-Ins**
3. Load each `.py` file from this folder one by one
4. Scripts will incrementally build HELEN's enclosure in the same workspace

All features are designed to be layered cleanly and exported together as `.f3d`, `.step`, or `.stl` for fabrication, proposal rendering, or integration.

---

## 📐 Design Philosophy

- Parametric, scriptable design using Fusion 360 API (Python)
- Modular script files = easy testing, adaptation, and future-proofing
- Compliant with 1U CubeSat interior volume standards (≤ 100 mm × 100 mm × 113.5 mm)
- Designed for **functionality + proposal aesthetics** (EPSCoR reviewer friendly)

---

## 🛰️ Attribution

Developed by [Shelby Dixon](https://github.com/sdixon4) as part of the **HELEN ISS Payload Capstone Project** for submission to NASA EPSCoR 2025.

For questions, reproduction, or extension — feel free to fork this repo or contact via [GitHub](https://github.com/sdixon4).

---

