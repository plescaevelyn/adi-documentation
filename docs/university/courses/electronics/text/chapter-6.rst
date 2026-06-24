.. _university-courses-electronics-text-chapter-6:

Chapter 6: Diode Applications
===============================================================================

Power Supplies, Voltage Regulators & Limiters

After completing this chapter, you should be able to:

* Design half-wave and full-wave rectifier circuits
* Calculate ripple voltage and select filter capacitors
* Understand voltage doubler circuits
* Design Zener diode voltage regulators
* Analyze diode clipper and clamper circuits

6.1 Rectifier
-------------------------------------------------------------------------------

A rectifier is a circuit that converts alternating current (AC) to direct
current (DC). This process is called rectification and is fundamental to
power supply design.

6.1.1 Half-Wave Rectification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The simplest rectifier uses a single diode to block one half-cycle of the
AC input while passing the other half-cycle.

.. figure:: figures/chptr6-f1.png
   :align: center

   Figure 6.1: Half-wave rectifier circuit

For an input voltage Vin = Vp sin(ωt):

* During positive half-cycles: Vout ≈ Vin - VD (diode conducts)
* During negative half-cycles: Vout = 0 (diode blocks)

The DC component of the output is:

.. math::

   V_{DC} = \frac{V_p - V_D}{\pi} \approx \frac{V_p}{\pi}

**Efficiency:** Only 50% of the input power is utilized, making half-wave
rectification inefficient for most applications.

6.1.2 Full-Wave Rectification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full-wave rectifiers convert both half-cycles of the AC input to DC output,
doubling the efficiency.

**Bridge Rectifier (4 diodes):**

.. figure:: figures/chptr6-f3.png
   :align: center

   Figure 6.2: Bridge rectifier circuit

The bridge rectifier is the most common configuration. It uses four diodes
but does not require a center-tapped transformer.

Output DC voltage:

.. math::

   V_{DC} = \frac{2(V_p - 2V_D)}{\pi} \approx \frac{2V_p}{\pi}

Note: Two diode drops (2VD ≈ 1.4V) are lost in this configuration.

**Center-Tapped Transformer (2 diodes):**

.. figure:: figures/chptr6-f5.png
   :align: center

   Figure 6.3: Center-tapped transformer with 2 diodes

This configuration requires only two diodes but needs a center-tapped
transformer, which may be more expensive.

**Dual Polarity Output:**

.. figure:: figures/chptr6-f8.png
   :align: center

   Figure 6.4: Dual polarity configuration with 4 diodes and center tap

6.1.3 Rectifier Output Smoothing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The pulsating DC output from a rectifier must be filtered to reduce ripple
and produce a steady DC voltage.

**RC Filter:**

.. figure:: figures/chptr6-f10.png
   :align: center

   Figure 6.5(a): Half-wave RC-Filter

.. figure:: figures/chptr6-f12.png
   :align: center

   Figure 6.5(b): Full-wave RC-Filter

The ripple voltage for a capacitor filter is approximately:

.. math::

   V_{ripple} \approx \frac{I_{load}}{fC}

Where:

* Iload = DC load current
* f = ripple frequency (line frequency for half-wave, 2× line frequency for full-wave)
* C = filter capacitance

**LC π-Filter:**

.. figure:: figures/chptr6-f13.png
   :align: center

   Figure 6.6: LC π-filter

For superior ripple reduction, an LC filter or voltage regulator (section 6.3)
can be used.

6.2 Voltage-Doubling Rectifiers
-------------------------------------------------------------------------------

Voltage doublers combine rectification with voltage multiplication to produce
a DC output approximately twice the peak AC input voltage.

.. figure:: figures/chptr6-f14.png
   :align: center

   Figure 6.7: Voltage doubler circuit

**Operation:**

* During negative half-cycles, C1 charges through D1 to Vp
* During positive half-cycles, C1's voltage adds to the input, and C2 charges
  through D2 to approximately 2Vp

**Applications:**

* Low-current, high-voltage supplies
* CRT displays
* Situations where transformer weight/cost must be minimized

Section Review
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Key concepts covered:

* Half-wave rectification is simple but inefficient (50%)
* Full-wave rectification provides better efficiency and lower ripple
* Filter capacitors smooth the pulsating DC output
* Ripple voltage is inversely proportional to capacitance and frequency

6.3 Zener Diode as Voltage Regulator
-------------------------------------------------------------------------------

A Zener diode operating in reverse breakdown provides a stable reference
voltage, making it useful for simple voltage regulators.

.. figure:: figures/chptr6-f8.png
   :align: center

   Figure 6.8: Zener Diode Voltage Reference circuit

**Design Considerations:**

1. The series resistor RS must limit the current to safe levels
2. The Zener must conduct enough current to remain in breakdown
3. The power dissipation must not exceed the Zener's rating

**Design Equations:**

The series resistor value:

.. math::

   R_S = \frac{V_{in} - V_Z}{I_Z + I_L}

Where:

* Vin = input voltage
* VZ = Zener voltage
* IZ = Zener current
* IL = load current

Power dissipation in the Zener:

.. math::

   P_Z = V_Z \times I_Z

Regulator Design Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Design a 5V regulator to supply up to 60mA from a 12V input.

**Solution:**

1. Select a Zener diode: 4.7V Zener (closest standard value below 5V)
2. Minimum Zener current for regulation: IZ(min) ≈ 5mA
3. At no load: IZ(max) = IZ(min) + IL(max) = 5mA + 60mA = 65mA

Calculate series resistor:

.. math::

   R_S = \frac{12V - 4.7V}{65mA} = \frac{7.3V}{65mA} \approx 112\Omega

Use standard value: RS = 100Ω or 120Ω

Power ratings:

* Resistor power: P = I²R = (65mA)² × 112Ω ≈ 0.47W → Use 1W resistor
* Zener power: P = VZ × IZ(max) = 4.7V × 65mA ≈ 0.31W → Use 500mW or 1W Zener

Exercise 6.3.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test your understanding of Zener regulators:

1. What happens to IZ when the load current increases?
2. What happens to VZ if the Zener operates below its minimum current?
3. Why must RS be chosen carefully for varying load conditions?
4. What is the maximum power dissipation in the Zener at no load?
5. How does input voltage variation affect regulation?
6. What are the limitations of this simple regulator compared to IC regulators?

Related Lab Activities
-------------------------------------------------------------------------------

* :dokuwiki:`ADALM1000 Lab: Rectifiers <university/courses/alm1k/alm-lab-rectifiers>`
* :dokuwiki:`ADALM2000 Lab: Zener Diode Regulator <university/courses/electronics/electronics-lab-zener>`

:ref:`Return to Introduction to Electrical Engineering <university-courses-intro_ee>`
