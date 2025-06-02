# Autonomous, Low-Power AI System for Plant Health Monitoring in Space and Resilient Agriculture

This repository documents a senior capstone project submitted to the NASA EPSCoR ISS Flight Opportunity. The system monitors plant health aboard the International Space Station using a fault-tolerant, low-power AI framework that integrates sensor fusion, Verilog-based logic, and explainable AI. It also supports dual-use applications in climate-resilient, off-grid agriculture in Hawai‘i.

## Project Goals

- Monitor plant stress in microgravity using thermal, moisture, CO₂, humidity, and RGB data.
- Execute AI inference and sensor fusion with onboard, low-power components.
- Provide logic-based fallback, override, and safety mechanisms (e.g., watchdog, TMR).
- Operate within ISS constraints: low crew time, low power (<3W), 3U volume.
- Transition to radiation-hardened FPGA systems post-prototype (e.g., Xilinx XQRKU060).

## System Architecture Overview

![System Block Diagram](system-diagram.png)

This block diagram shows the full autonomous pipeline for the plant health monitoring system, including sensor inputs, onboard AI logic, safety controls, and responsive outputs.

