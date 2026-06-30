.. _university-courses-electronics-text-light-sensors-photodiodes:

Photodiodes and Other Light Sensors
===============================================================================

*Author: James Bryant, August 2014*

This document provides an overview of photosensors - devices that convert
light into electronic signals. The coverage focuses primarily on the visible
spectrum (approximately 400-800 nm) and extends into near-infrared and
ultraviolet ranges.

Introduction
-------------------------------------------------------------------------------

Light sensors convert optical signals to electrical signals. This document
covers DC and AC measurement applications, focusing on the interface between
optical and electronic domains.

Vacuum Photocells
-------------------------------------------------------------------------------

The vacuum photocell (phototube or photoelectric cell) was the first practical
photosensor.

.. figure:: figures/cphotodio_f1.jpg
   :align: center

   Figure 1A: Phototube diagram

**Operation:**

* Light strikes a photosensitive cathode
* Electrons are emitted via the photoelectric effect
* Electrons are collected by an anode
* Current is proportional to light intensity

**Photomultipliers:**

.. figure:: figures/cphotodio_f2.jpg
   :align: center

   Figure 1B: Photomultiplier structure

Photomultipliers use multiple dynodes to amplify the initial photoelectron
signal by factors of 10⁶ or more. They remain important for specialized
applications requiring extreme sensitivity:

* Scientific instrumentation
* Medical imaging
* Nuclear and particle physics
* Astronomy

Photoresistors
-------------------------------------------------------------------------------

Photoresistors (also called LDRs - Light Dependent Resistors) change their
resistance based on light intensity.

.. figure:: figures/cphotodio_f3.jpg
   :align: center

   Figure 2: CdS photoresistor

**Materials:**

* Cadmium sulfide (CdS) - visible light
* Cadmium selenide/sulfide - extended red response

**Characteristics:**

* Resistance decreases with increasing light
* Slow response time (tens to hundreds of milliseconds)
* Simple to use - requires only a voltage divider circuit

.. figure:: figures/cphotodio_f4.jpg
   :align: center

   Figure 3: Photoresistor in a gain control application

**Limitations:**

* Environmental concerns (cadmium content)
* Slow response limits AC applications
* Declining use in favor of photodiodes

Photodiodes and Phototransistors
-------------------------------------------------------------------------------

Semiconductor photodiodes are the most common light sensors in modern
electronics.

.. figure:: figures/cphotodio_f5.jpg
   :align: center

   Figure 4: Ideal diode model

**Photodiode Operation:**

.. figure:: figures/cphotodio_f6.jpg
   :align: center

   Figure 5: Ideal semiconductor photodiode

Light absorbed in the depletion region creates electron-hole pairs, generating
a photocurrent proportional to light intensity.

**Operating Modes:**

**Photoconductive Mode (Reverse Biased):**

.. figure:: figures/cphotodio_f7.jpg
   :align: center

   Figure 6: Photoconductive mode operation

* External reverse bias applied
* Faster response (reduced junction capacitance)
* Linear response over wide dynamic range
* Some dark current (noise)

**Photovoltaic Mode (Zero Bias):**

.. figure:: figures/cphotodio_f8.jpg
   :align: center

   Figure 8: Photovoltaic voltage mode circuit

* No external bias required
* Lower noise (no dark current)
* Used in solar cells and precision light measurement

**Phototransistors:**

.. figure:: figures/cphotodio_f9.jpg
   :align: center

   Figure 7: Phototransistor structure

Phototransistors provide current gain (typically 100-1000x) compared to
photodiodes:

* Base-collector junction acts as photodiode
* Transistor action amplifies photocurrent
* Slower than photodiodes due to capacitance
* Higher sensitivity but less linear

Photocell Applications
-------------------------------------------------------------------------------

Light Measurement Circuits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Simple Transistor Detector:**

.. figure:: figures/cphotodio_f10.jpg
   :align: center

   Figure 9: Basic photodetector with transistor amplifier

**Logic Gate Interface:**

.. figure:: figures/cphotodio_f11.jpg
   :align: center

   Figure 10: Photodetector with digital output

**Schmitt Trigger for Threshold Detection:**

.. figure:: figures/cphotodio_f12.jpg
   :align: center

   Figure 11: Schmitt trigger light detector

Adding hysteresis prevents oscillation when light levels are near the threshold.

**Comparator-Based Circuits:**

.. figure:: figures/cphotodio_f13.jpg
   :align: center

   Figure 12: Comparator-based light level detector

.. figure:: figures/cphotodio_f14.jpg
   :align: center

   Figure 13: Comparator with adjustable hysteresis

Voltage Output Circuits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For precision measurement, a transimpedance amplifier converts photocurrent
to voltage:

.. figure:: figures/cphotodio_f15.jpg
   :align: center

   Figure 14: Photodiode with voltage output

.. figure:: figures/cphotodio_f16.jpg
   :align: center

   Figure 15: Photoresistor voltage output circuit

**ADC Interface:**

.. figure:: figures/cphotodio_f17.jpg
   :align: center

   Figure 16: Switched-capacitor ADC input

.. figure:: figures/cphotodio_f18.jpg
   :align: center

   Figure 17: ADC analog input with decoupling

Current-to-Voltage Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: figures/cphotodio_f19.jpg
   :align: center

   Figure 18: Transimpedance amplifier (current-to-voltage converter)

The transimpedance amplifier provides:

* Virtual ground at the photodiode cathode
* Linear conversion: Vout = Iphoto × Rf
* Wide bandwidth with proper compensation

AC Signal Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For detecting modulated light (remote controls, optical communication):

.. figure:: figures/cphotodio_f20.jpg
   :align: center

   Figure 19: AC-coupled photodetector

**Tone Detection with PLL:**

The 567 PLL IC detects a specific frequency, useful for rejecting ambient
light and interference.

Appendix A: Semiconductor Diode Physics
-------------------------------------------------------------------------------

**PN Junction Review:**

The photodiode is fundamentally a PN junction operated in reverse bias or
at zero bias.

Key equations:

**Diode Current:**

.. math::

   I = I_S \left( e^{\frac{qV}{kT}} - 1 \right)

**Photocurrent:**

.. math::

   I_{photo} = \eta \cdot q \cdot \Phi \cdot A

Where:

* η = quantum efficiency
* q = electron charge
* Φ = photon flux (photons/cm²/s)
* A = active area

**Temperature Dependence:**

Dark current approximately doubles for every 10°C temperature increase.

Appendix B: Measuring Photodiodes
-------------------------------------------------------------------------------

**Spectral Characterization:**

Different photodiode materials respond to different wavelength ranges:

* Silicon: 400-1100 nm (peak ~900 nm)
* Germanium: 800-1800 nm
* InGaAs: 900-1700 nm

.. figure:: figures/cphotodio_f22.jpg
   :align: center

   Figure 22: Test setup for photodiode characterization

**LED-Based Testing:**

LEDs can be used to characterize photodiode response at specific wavelengths.
This allows simple verification of photodiode performance without expensive
monochromator equipment.

Related Lab Activities
-------------------------------------------------------------------------------

* :dokuwiki:`LEDs as Light Sensors <university/courses/alm1k/alm-lab-led-sensor>`
* :dokuwiki:`Photodiode Characterization <university/courses/electronics/electronics-lab-photodiode>`

:ref:`Return to Introduction to Electrical Engineering <university-courses-intro_ee>`
