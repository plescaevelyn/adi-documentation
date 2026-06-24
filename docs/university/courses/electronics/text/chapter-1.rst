.. _university-courses-electronics-text-chapter-1:

Chapter 1: Introduction and Chapter Objectives
===============================================================================

After completing this chapter, you should be able to:

* Define active versus passive devices
* Apply Kirchhoff's current and voltage laws
* Create equivalent circuits using Thévenin and Norton approaches
* Convert between equivalent circuit types
* Use superposition for multi-source analysis

1.1 Active Versus Passive Devices
-------------------------------------------------------------------------------

Electronic components can be divided into two main categories: active and passive
devices. Passive devices, such as resistors, capacitors, and inductors, cannot
control the flow of electrical current - they can only consume, store, or release
electrical energy. Active devices, such as transistors and operational amplifiers,
can control the flow of electrical current and can amplify signals.

Active devices can be further subdivided into:

* **Voltage-controlled devices** - where the output current is controlled by an
  input voltage (e.g., MOSFETs)
* **Current-controlled devices** - where the output current is controlled by an
  input current (e.g., BJTs)

1.2 Notation and Conventional Terminology
-------------------------------------------------------------------------------

Throughout this text, the following notation conventions are used:

* **Uppercase letters** (V, I) - DC or RMS values
* **Lowercase letters** (v, i) - instantaneous or small-signal values
* **Lowercase with uppercase subscripts** (vBE, iC) - total instantaneous values

1.3 Basic Quantities
-------------------------------------------------------------------------------

Before proceeding, you should be familiar with the following foundational concepts:

* Ohm's law: V = IR
* Resistance, capacitance, and inductance
* Basic circuit analysis methods
* Simulation software (SPICE-based tools)

1.4 Kirchhoff's Circuit Laws
-------------------------------------------------------------------------------

1.4.1 Kirchhoff's Current Law (KCL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current entering any junction in a circuit network is equal to the current
leaving that junction. Mathematically:

.. math::

   \sum I_{in} = \sum I_{out}

Or equivalently, the algebraic sum of all currents at a node equals zero:

.. math::

   \sum I = 0

.. figure:: figures/chptr1-f1.png
   :align: center

   Figure 1.4.1: Current flow at a circuit node

1.4.2 Kirchhoff's Voltage Law (KVL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sum of all the voltages around a loop of circuit elements is equal to zero.
Mathematically:

.. math::

   \sum V = 0

.. figure:: figures/chptr1-f2.png
   :align: center

   Figure 1.4.2: Voltage relationships in a circuit loop

1.5 Thévenin's Theorem
-------------------------------------------------------------------------------

Thévenin's theorem states that any linear network with two terminals can be
replaced by an equivalent circuit consisting of a single voltage source VTH
in series with a single resistor RTH.

.. figure:: figures/chptr1-f3.png
   :align: center

   Figure 1.5.1: Thévenin equivalent circuit

To find the Thévenin equivalent:

1. Calculate the open-circuit voltage across the terminals (VTH)
2. Calculate the equivalent resistance seen from the terminals with all
   independent sources turned off (RTH)

Related Lab Activities:

* :dokuwiki:`ADALM1000 Lab: Thévenin Equivalent <university/courses/alm1k/circuits1/alm-cir-thevenin-lab>`
* :dokuwiki:`ADALM2000 Lab: Thévenin Equivalent <university/courses/electronics/electronics-lab-1>`

1.6 Norton's Theorem
-------------------------------------------------------------------------------

Norton's theorem is the dual of Thévenin's theorem. It states that any linear
network with two terminals can be replaced by an equivalent circuit consisting
of an ideal current source IN in parallel with a single resistor RN.

.. figure:: figures/chptr1-f4.png
   :align: center

   Figure 1.6.1: Norton equivalent circuit

The Norton current IN equals the short-circuit current between the terminals,
and RN equals RTH.

The relationship between Thévenin and Norton equivalents:

.. math::

   I_N = \frac{V_{TH}}{R_{TH}}

.. math::

   R_N = R_{TH}

1.7 Superposition Theorem
-------------------------------------------------------------------------------

The superposition theorem states that in a linear circuit with multiple
independent sources, the response (voltage or current) at any point can be
calculated by summing the individual responses caused by each source acting alone,
with all other independent sources turned off (voltage sources replaced by
short circuits, current sources replaced by open circuits).

.. figure:: figures/chptr1-f5.png
   :align: center

   Figure 1.7.1: Circuit with two voltage sources

**Example:**

Consider a circuit with two voltage sources V1 and V2, and three resistors
R1, R2, and R3. To find the voltage across R2:

1. Turn off V2 (replace with short circuit), calculate the contribution from V1
2. Turn off V1 (replace with short circuit), calculate the contribution from V2
3. Add the two contributions algebraically

.. figure:: figures/chptr1-f6.png
   :align: center

   Figure 1.7.2: Analysis with V2 = 0

.. figure:: figures/chptr1-f7.png
   :align: center

   Figure 1.7.3: Analysis with V1 = 0

**Important Limitation:**

The Superposition Theorem works only for circuits that are reducible to
series/parallel combinations and requires linear relationships between voltage
and current. It cannot be applied to circuits containing nonlinear components
such as diodes or transistors operating in their nonlinear regions.

Section Summary
-------------------------------------------------------------------------------

In this chapter, we covered:

* The distinction between active and passive devices
* Notation conventions used in electronics
* Kirchhoff's Current Law (KCL) and Voltage Law (KVL)
* Thévenin's and Norton's theorems for circuit simplification
* The Superposition theorem for analyzing circuits with multiple sources

:ref:`Return to Introduction to Electrical Engineering <university-courses-intro_ee>`
