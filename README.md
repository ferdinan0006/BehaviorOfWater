# BehaviorOfWater
This repository describes and analyses the behavior of a water drop in dependence of the fall height.

# Fluid Dynamics of Water Droplet Impact

This repository contains the data, analysis scripts, and results for a physics project investigating the fluid dynamics and splash behavior of water droplets impacting a liquid surface. The project examines the conditions under which splashes occur and analyzes their characteristics (number, height, diameter, and shape) based on the initial impact conditions.

## Repository Structure

The repository is organized into the following sections:

### 1. Code
*   **Surface Tension:** Scripts used for calculating the surface tension of water using the Du-Noüy ring method data.
*   **Splash Behavior:** Scripts for analyzing the slow-motion video data (240 FPS) to extract droplet and pillar characteristics, calculate Weber numbers, and perform statistical analyses (e.g., linear regression and binned median trends).

### 2. Data
*   **Surface Tension:** Raw measurements from the precision scale used to determine the tear-off force for rings of 625 µm and 1000 µm diameter.
*   **Splash Behavior:** Data extracted from manual video analysis, including the number of detached droplets, maximum height, diameter of the highest droplet, and qualitative categorization ("Säule" or "Tropfen") for drop heights ranging from 5 cm to 60 cm.

### 3. Figures
*   **Surface Tension:** Plots illustrating the surface tension measurements and tear-off forces.
*   **Splash Behavior:**
    *   Setup diagram.
    *   Histograms showing the frequency of pillars ("Säulen") vs. droplets ("Tropfen") as a function of drop height.
    *   Scatter plot with linear fit showing splash diameter versus Weber number.
    *   Scatter plot with binned median trend showing splash height versus Weber number.

### 4. Results
The analysis yielded the following key findings:
*   **Surface Tension:** The surface tension of the tap water was determined to be $\sigma = 48.67 \pm 0.33 \text{ mN/m}$, though this deviated significantly from standard literature values due to systematic errors.
*   **Splash Formation:** Droplet formation primarily occurs at moderate drop heights (10-50 cm, Weber numbers 100-750), while extreme heights (<10 cm and >50 cm) predominantly result in pillar formation without detachment.
*   **Diameter:** The diameter of the resulting splash exhibits a linear relationship with the Weber number ($D = (0.127 \cdot We \pm 1.05) \text{ mm}$, $R^2 = 0.874$).
*   **Height:** The splash height exhibits a highly non-linear relationship with the Weber number, peaking steeply at $We \approx 280$ before gradually declining toward a saturation value at higher Weber numbers. Pillars reach a maximum height of approximately 2.2 cm.
*   **Conclusion:** The simple conservation of energy principle and the static Weber number are insufficient to fully describe the structural development of the splash; dissipative effects, such as surface waves, must be considered.

## Dependencies

You can install the necessary Python packages using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
