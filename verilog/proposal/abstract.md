# Abstract

This project proposes the development of a low-power, fault-tolerant AI system to monitor plant health aboard the International Space Station (ISS). The system integrates thermal infrared, CO₂, humidity, moisture, and RGB sensors to detect early signs of plant stress in a microgravity environment.

The proposed system addresses challenges unique to space, such as CO₂ pooling, non-convective heat buildup, and unpredictable fluid behavior. These conditions are not present in Earth-based agriculture and require a custom sensing and analysis pipeline. The system performs onboard AI inference using quantized neural networks, supported by logic-level watchdog and override functionality to ensure operational safety.

The control logic is written in Verilog and includes triple modular redundancy (TMR) to mitigate faults due to radiation exposure. Inference and sensor fusion are handled through a Python layer running on the PYNQ-Z2 platform. The design supports zero-crew-time operation, fits within a 3U volume constraint, and consumes less than 3W of power. It is intended to migrate to radiation-hardened FPGA platforms such as the Xilinx XQRKU060.

This system also has dual-use relevance for climate-resilient agriculture in off-grid or disaster-affected areas of Hawai‘i. By validating its functionality under spaceflight conditions, the project contributes both to sustainable life support systems in orbit and to local food security and infrastructure resilience on Earth.

