.. _university-courses-electronics-text-chapter-5:

Chapter 5: Solid-State Diodes and Diode Characteristics
===============================================================================

After completing this chapter, you should be able to:

* Understand the physics of PN junctions
* Describe diode behavior under forward and reverse bias conditions
* Apply the diode equation to calculate current and voltage
* Use linear and small-signal models for diode analysis
* Understand temperature effects on diode characteristics

5.1 The PN Junction
-------------------------------------------------------------------------------

The PN junction is formed by joining p-type and n-type semiconductor materials.
It is the elementary building block of almost all semiconductor electronic
devices including diodes, transistors, solar cells, LEDs, and integrated circuits.

5.1.1 Properties of a PN Junction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When p-type and n-type materials are joined:

* Electrons from the n-region diffuse into the p-region
* Holes from the p-region diffuse into the n-region
* This creates a **depletion region** at the junction
* The depletion region is devoid of mobile charge carriers
* A built-in electric field opposes further diffusion

.. figure:: figures/chptr5-f1.png
   :align: center

   Figure 5.1: PN junction at equilibrium

5.1.2 Equilibrium (Zero Bias)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At equilibrium (no external voltage applied):

* The diffusion of carriers is balanced by the electric field
* A **built-in potential** (V₀) exists across the junction
* For silicon: V₀ ≈ 0.7V
* For germanium: V₀ ≈ 0.3V

.. figure:: figures/chptr5-f2.png
   :align: center

   Figure 5.2: Charge density in the depletion region

5.1.3 Forward Bias
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a positive voltage is applied to the p-side relative to the n-side
(forward bias):

* The external voltage opposes the built-in potential
* The depletion region narrows
* The barrier to current flow is reduced
* Current flows easily through the junction

5.1.4 Reverse Bias
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a negative voltage is applied to the p-side relative to the n-side
(reverse bias):

* The external voltage adds to the built-in potential
* The depletion region widens
* The barrier to current flow increases
* Only a very small leakage current flows

.. figure:: figures/chptr5-f5.png
   :align: center

   Figure 5.4: PN junction voltage gap diagram

Section Summary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PN junction forms the basis for all semiconductor devices. The depletion
region and built-in potential create a barrier that can be controlled by
external voltage, enabling the rectifying behavior of diodes.

5.2 Actual Diodes
-------------------------------------------------------------------------------

.. figure:: figures/chptr5-f3.png
   :align: center

   Figure 5.3a: Diode schematic symbol

.. figure:: figures/chptr5-f4.jpg
   :align: center

   Figure 5.3b: Small signal diode photograph

The current-voltage relationship of a real diode is described by the
**Shockley diode equation**:

.. math::

   I_D = I_S \left( e^{\frac{V_D}{nV_T}} - 1 \right)

Where:

* ID = diode current
* IS = reverse saturation current (typically 10⁻¹² to 10⁻¹⁵ A)
* VD = voltage across the diode
* n = ideality factor (1 to 2)
* VT = thermal voltage = kT/q ≈ 26 mV at room temperature

.. figure:: figures/chptr5-f5.png
   :align: center

   Figure 5.5: Diode V-I characteristic curve

For forward bias where VD >> VT:

.. math::

   I_D \approx I_S \cdot e^{\frac{V_D}{nV_T}}

Solving for voltage:

.. math::

   V_D = nV_T \ln\left(\frac{I_D}{I_S}\right)

**Zener Diodes:**

Zener diodes are designed to operate in the reverse breakdown region,
providing a stable reference voltage.

.. figure:: figures/chptr5-f6.png
   :align: center

   Figure 5.6: 6.2V Zener diode behavior

5.3 Temperature Behavior of Diodes
-------------------------------------------------------------------------------

Diode characteristics are temperature-dependent:

* The forward voltage decreases by approximately **-2 mV/°C**
* The reverse saturation current doubles for every 10°C increase
* The thermal voltage VT is proportional to absolute temperature

.. figure:: figures/chptr5-f7.png
   :align: center

   Figure 5.7: Temperature dependence at multiple currents

At a constant current, the temperature coefficient of forward voltage is:

.. math::

   \frac{dV_D}{dT} \approx -2 \text{ mV/°C}

5.4 Linear Model
-------------------------------------------------------------------------------

For many applications, a simplified linear model is sufficient:

**Ideal Diode Model:**

* Forward bias: VD = 0 (short circuit)
* Reverse bias: ID = 0 (open circuit)

**Constant Voltage Drop Model:**

* Forward bias: VD = 0.7V (for silicon)
* Reverse bias: ID = 0 (open circuit)

**Piecewise Linear Model:**

* Forward bias: VD = V₀ + ID × rD
* Where V₀ ≈ 0.6-0.7V and rD is the dynamic resistance

5.5 Small-Signal Model
-------------------------------------------------------------------------------

For small AC signals superimposed on a DC operating point, the diode can be
modeled as a small-signal resistance:

.. figure:: figures/chptr5-f8.png
   :align: center

   Figure 5.8: I-V characteristics with tangent line

The small-signal (dynamic) resistance is found by differentiating the diode
equation:

.. math::

   \frac{dI_D}{dV_D} = \frac{I_D}{nV_T}

Therefore, the small-signal resistance is:

.. math::

   r_d = \frac{nV_T}{I_D}

At room temperature with n = 1:

.. math::

   r_d = \frac{26 \text{ mV}}{I_D}

**Example:** At ID = 1 mA, rd = 26 Ω

Section Summary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The small-signal model allows analysis of circuits where both DC bias and
small AC signals are present. The dynamic resistance is inversely proportional
to the DC operating current.

Physical Constants
-------------------------------------------------------------------------------

* Boltzmann constant: k = 1.38 × 10⁻²³ J/K
* Electron charge: q = 1.6 × 10⁻¹⁹ C
* Thermal voltage at room temperature (300K): VT = kT/q ≈ 26 mV

Related Lab Activities
-------------------------------------------------------------------------------

* :dokuwiki:`ADALM1000 Lab Activity 2: Diode I vs. V curves <university/courses/alm1k/alm-lab-2>`
* :dokuwiki:`ADALM2000 Lab Activity 2: Diode characteristics <university/courses/electronics/electronics-lab-diode>`
* :dokuwiki:`PN Junction Capacitance Measurement <university/courses/alm1k/alm-lab-pn-capacitance>`

:ref:`Return to Introduction to Electrical Engineering <university-courses-intro_ee>`
