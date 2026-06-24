.. _university-courses-electronics-text-chapter-2:

Chapter 2: Operational Amplifier Basics
===============================================================================

After completing this chapter, you should be able to:

* List the properties of an ideal operational amplifier
* Draw inverting and non-inverting op-amp configurations
* Derive gain equations for basic op-amp circuits
* Understand summing, differential, and instrumentation amplifier circuits
* Analyze integrator and differentiator circuits

2.1 The Ideal Voltage Feedback Op Amp
-------------------------------------------------------------------------------

The operational amplifier (op-amp) is one of the most versatile and widely used
analog integrated circuits. Originally developed for analog computers to perform
mathematical operations (hence the name "operational"), op-amps are now used in
countless applications from signal conditioning to active filters.

.. figure:: figures/chptr2-f1.png
   :align: center

   Figure 2.1: Standard Op Amp Symbol

2.2 Ideal Voltage Feedback (VFB) Model
-------------------------------------------------------------------------------

An ideal voltage feedback operational amplifier has the following characteristics:

* **Infinite open-loop gain** (AOL = ∞)
* **Infinite input impedance** (Zin = ∞)
* **Zero output impedance** (Zout = 0)
* **Infinite bandwidth**
* **Zero input offset voltage**
* **Zero input bias current**
* **Zero noise**

.. figure:: figures/chptr2-f2.png
   :align: center

   Figure 2.2: The Attributes of an Ideal Voltage Feedback Op Amp

In practice, these ideal assumptions lead to two important rules for analyzing
op-amp circuits with negative feedback:

1. **No current flows into the input terminals** (due to infinite input impedance)
2. **The voltage difference between the inputs is zero** (due to infinite gain
   with negative feedback)

2.3 Basic Operation
-------------------------------------------------------------------------------

The op-amp amplifies the difference between its two inputs:

.. math::

   V_{out} = A_{OL} \times (V_+ - V_-)

Where:

* Vout is the output voltage
* AOL is the open-loop gain
* V+ is the non-inverting input voltage
* V- is the inverting input voltage

2.4 Inverting and Non-inverting Configurations
-------------------------------------------------------------------------------

The two fundamental op-amp configurations are:

**Inverting Configuration:**

.. figure:: figures/chptr2-f3.png
   :align: center

   Figure 2.3: Inverting Mode Op Amp Stage

**Non-Inverting Configuration:**

.. figure:: figures/chptr2-f4.png
   :align: center

   Figure 2.4: Non-Inverting Mode Op Amp Stage

2.5 Inverting Op Amp Gain Derivation
-------------------------------------------------------------------------------

For the inverting amplifier configuration:

.. figure:: figures/chptr2-f5.png
   :align: center

   Figure 2.5: Inverting Amplifier Gain

The closed-loop gain is:

.. math::

   A_v = \frac{V_{out}}{V_{in}} = -\frac{R_f}{R_{in}}

The negative sign indicates that the output is inverted (180° phase shift)
relative to the input.

**Input impedance:** Zin = Rin

2.6 Non-inverting Op Amp Gain Derivation
-------------------------------------------------------------------------------

For the non-inverting amplifier configuration:

.. figure:: figures/chptr2-f6.png
   :align: center

   Figure 2.6: Non-Inverting Amplifier Gain

The closed-loop gain is:

.. math::

   A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_f}{R_{in}}

Note that the minimum gain for this configuration is 1 (unity gain buffer when
Rf = 0 or Rin = ∞).

**Input impedance:** Zin ≈ ∞ (very high)

2.7 Inverting Summing Op Amp Stage
-------------------------------------------------------------------------------

The summing amplifier adds multiple input signals:

.. figure:: figures/chptr2-f7.png
   :align: center

   Figure 2.7: Summing Amplifier

.. math::

   V_{out} = -R_f \left( \frac{V_1}{R_1} + \frac{V_2}{R_2} + \frac{V_3}{R_3} \right)

If all input resistors are equal (R1 = R2 = R3 = R):

.. math::

   V_{out} = -\frac{R_f}{R} (V_1 + V_2 + V_3)

2.8 The Differential Op Amp Stage
-------------------------------------------------------------------------------

The differential amplifier (also called a subtractor) amplifies the difference
between two input signals:

.. figure:: figures/chptr2-f8.png
   :align: center

   Figure 2.8: The Differential Amplifier Stage (Subtractor)

When R1 = R3 and R2 = R4:

.. math::

   V_{out} = \frac{R_2}{R_1} (V_2 - V_1)

.. figure:: figures/chptr2-f9.png
   :align: center

   Figure 2.8.1: Buffered Differential Amplifier Stage

2.9 The Instrumentation Amplifier
-------------------------------------------------------------------------------

The instrumentation amplifier provides high input impedance, adjustable gain,
and excellent common-mode rejection. It is commonly used for precision
measurement applications.

**Three Op-Amp Configuration:**

.. figure:: figures/chptr2-f9.png
   :align: center

   Figure 2.9: High Input Impedance Instrumentation Amplifier

.. math::

   V_{out} = \left( 1 + \frac{2R_1}{R_G} \right) \frac{R_3}{R_2} (V_2 - V_1)

**Two Op-Amp Configuration:**

.. figure:: figures/chptr2-f10.png
   :align: center

   Figure 2.10: Instrumentation Amplifier Using Two Op Amps

Section Summary
-------------------------------------------------------------------------------

At this point, you should be able to:

* List the properties of an ideal op-amp
* Draw and analyze inverting and non-inverting configurations
* Calculate gain for basic op-amp circuits
* Design summing and differential amplifier circuits
* Understand instrumentation amplifier topologies

2.10 Integration and Differentiation
-------------------------------------------------------------------------------

2.10.1 The Ideal Inverting Integrator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The integrator produces an output proportional to the integral of the input signal:

.. figure:: figures/chptr2-f11.png
   :align: center

   Figure 2.11: Inverting Integrator

.. math::

   V_{out}(t) = -\frac{1}{RC} \int V_{in}(t) \, dt

In the frequency domain:

.. math::

   \frac{V_{out}}{V_{in}} = -\frac{1}{j\omega RC}

.. figure:: figures/chptr2-f12.png
   :align: center

   Figure 2.12: Ideal Integrator Simulation

2.10.2 The Ideal Differentiator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The differentiator produces an output proportional to the derivative of the
input signal:

.. figure:: figures/chptr2-f13.png
   :align: center

   Figure 2.13: Inverting Differentiator

.. math::

   V_{out}(t) = -RC \frac{dV_{in}(t)}{dt}

In the frequency domain:

.. math::

   \frac{V_{out}}{V_{in}} = -j\omega RC

.. figure:: figures/chptr2-f14.png
   :align: center

   Figure 2.14: Ideal Differentiator Simulation

Related Lab Activities
-------------------------------------------------------------------------------

* :dokuwiki:`ADALM1000 Lab: Op Amp as Comparator <university/courses/alm1k/alm-lab-opamp-comparator>`
* :dokuwiki:`ADALM2000 Lab: Op Amp Open Loop Gain <university/courses/electronics/electronics-lab-2>`

:ref:`Return to Introduction to Electrical Engineering <university-courses-intro_ee>`
