# Foil Strain Gauge Calculation Toolkit

A Python-based toolkit for calculating strain gauge parameters, including a core calculation module and a user-friendly web interface.

[简体中文](README/README_zh.md) | [English](README.md)

## Overview

This toolkit provides functionality to compute key parameters for foil strain gauges, such as strain coefficient, microstrain, and gauge factor (GF). It includes:
- A core calculation module (`basic_calculation.py`) with essential strain gauge formulas
- A web interface for interactive parameter input and real-time calculations

## Features

- **Core Calculations**: Compute strain-related parameters using fundamental mechanical and electrical properties of strain gauges
- **Web Interface**: Easy-to-use browser-based interface with input validation and unit conversion (Ω, kΩ, MΩ)
- **Interactive Results**: Instant calculation of:
  - Strain coefficient (epsilon)
  - Microstrain (μ_epsilon)
  - Gauge factor (GF)

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/foil-strain-gauge-calculation-toolkit.git
   cd foil-strain-gauge-calculation-toolkit
   ```

2. Install required dependencies (create a `requirements.txt` with necessary packages like Flask if not present):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Using the Core Calculation Module
Import the `basic_calculation` module in your Python scripts to use the calculation functions directly:
```python
from code.basic_calculation import epsilon_calculate
from code.basic_calculation import gf_sensitivity_calculate

# Example usage
params = {
    "y": 0.5,    # Free end deflection (mm)
    "x": 20,     # Distance from strain gauge to load point (mm)
    "h": 3,      # Beam thickness (mm)
    "l": 100,    # Cantilever beam length (mm)
    "R_0": 120,   # Zero-strain resistance (Ω)
    "R_1": 120.1  # Current resistance (Ω)
}

epsilon_calculate = epsilon_calculate(**params)
gf_sensitivity_calculate = gf_sensitivity_calculate(**params)

print(f"epsilon: {epsilon_calculate['epsilon']}")
print(f"mu_epsilon: {epsilon_calculate['mu_epsilon']}")
print(f"Gauge factor: {gf_sensitivity_calculate['gf']}")
```

### 2. Using the Web Interface
1. Start the web application:
   ```bash
   python web/basic_calculation/app.py
   ```

2. Open your browser and navigate to `http://localhost:5000` (or the port specified in the output)

3. Enter the required parameters:
   - Free end deflection (y)
   - Distance from strain gauge to load point (x)
   - Beam thickness (h)
   - Cantilever beam length (l)
   - Zero-strain resistance (R₀) with unit selection
   - Current resistance (R₁) with unit selection

4. Click "开始计算" (Start Calculation) to view results

## Project Structure
```
foil-strain-gauge-calculation-toolkit/
├── code/
│   └── basic_calculation.py   # Core calculation logic
└── web/
    └── basic_calculation/
        ├── app.py             # Web server (Flask application)
        └── templates/
            └── index.html     # Web interface template
```

## License
[MIT](LICENSE)