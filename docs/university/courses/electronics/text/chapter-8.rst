.. _university-courses-electronics-text-chapter-8:

Chapter 8: Transistors
===============================================================================

After completing this chapter, you should be able to:

* Understand the basic principles of transistor operation
* Identify BJT and MOSFET symbols and terminal names
* Describe the regions of operation for BJTs and MOSFETs
* Apply large-signal and small-signal transistor models
* Calculate transistor parameters for circuit analysis

8.1 Basic Principles
-------------------------------------------------------------------------------

Transistors are active devices that electrically control the flow of current.
They form the basis of all modern electronics, from simple amplifiers to
complex integrated circuits.

**General Three-Terminal Model:**

A transistor can be modeled as a three-terminal device where a small signal
at one terminal controls a larger current between the other two terminals.

**Device Categories:**

* **Current-controlled devices** (BJTs): The output current is controlled
  by an input current
* **Voltage-controlled devices** (FETs): The output current is controlled
  by an input voltage with essentially no input current

**Key Parameters:**

* β (beta) - current gain for BJTs
* α (alpha) - alternative current gain measure
* gm - transconductance (for both BJTs and FETs)

8.1.1 Simple Model Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The transfer characteristic of a transistor shows the relationship between
the control signal and the output current.

.. figure:: figures/chptr8-f1.png
   :align: center

   Figure 8.1.3: Ideal voltage-controlled current source characteristics

.. figure:: figures/chptr8-f2.png
   :align: center

   Figure 8.1.4: Realistic characteristics with physical constraints

8.2 Transistor Symbols
-------------------------------------------------------------------------------

Four basic transistor types correspond to the fundamental device models:

.. figure:: figures/chptr8-f3.png
   :align: center

   Figure 8.2.1: Transistor symbols for BJT and MOSFET types

+----------------+-------------+------------------+
| Type           | Control     | Polarity         |
+================+=============+==================+
| NPN BJT        | Current     | N-type           |
+----------------+-------------+------------------+
| PNP BJT        | Current     | P-type           |
+----------------+-------------+------------------+
| NMOS FET       | Voltage     | N-channel        |
+----------------+-------------+------------------+
| PMOS FET       | Voltage     | P-channel        |
+----------------+-------------+------------------+

**Terminal Names:**

* BJT: Collector (C), Base (B), Emitter (E)
* MOSFET: Drain (D), Gate (G), Source (S)

8.3 Bipolar Junction Transistor Basics
-------------------------------------------------------------------------------

The BJT is a three-terminal semiconductor device used for amplification
and switching. BJTs are minority carrier devices where charge flows via
diffusion across junctions.

**Structure:**

A BJT consists of three doped semiconductor regions:

* **NPN**: N-type emitter, P-type base, N-type collector
* **PNP**: P-type emitter, N-type base, P-type collector

The base region is very thin, allowing carriers to diffuse across it.

8.3.1 Voltage, Current, and Charge Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Three viewpoints describe BJT operation:

1. **Current-control model**: Collector current is controlled by base current
2. **Voltage-control model**: Collector current depends exponentially on VBE
3. **Charge-control model**: Based on stored charge in the base region

The collector current follows an exponential relationship:

.. math::

   I_C = I_S \left( e^{\frac{V_{BE}}{V_T}} - 1 \right)

At typical operating conditions, the -1 term is negligible:

.. math::

   V_{BE} = V_T \ln\left(\frac{I_C}{I_S}\right)

8.3.2 Transistor Alpha and Beta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Beta (β) - Common-Emitter Current Gain:**

.. math::

   \beta = \frac{I_C}{I_B}

Typical values: β = 100 to 300

**Alpha (α) - Common-Base Current Gain:**

.. math::

   \alpha = \frac{I_C}{I_E}

Typical values: α = 0.98 to 0.998

**Relationships:**

.. math::

   \alpha = \frac{\beta}{\beta + 1}

.. math::

   \beta = \frac{\alpha}{1 - \alpha}

8.3.3 NPN Transistor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Structure: P-doped base sandwiched between two N-doped layers.

.. figure:: figures/chptr8-f4.png
   :align: center

   Figure 8.3.9: NPN transistor symbol

**Mnemonic:** "Not Pointing iN" - the arrow points outward from the base.

**Operation:** Forward-biasing the base-emitter junction allows current
amplification at the collector.

8.3.4 PNP Transistor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Structure: N-doped base sandwiched between two P-doped layers.

.. figure:: figures/chptr8-f5.png
   :align: center

   Figure 8.3.10: PNP transistor symbol

**Operation:** The base is pulled low relative to the emitter to turn the
device on. Current flows from emitter to collector.

8.3.5 BJT Regions of Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BJTs have five distinct operational regions defined by junction biasing:

1. **Forward Active (Normal):**

   * Base-emitter: Forward biased
   * Base-collector: Reverse biased
   * IC ≈ β × IB (linear amplification region)

2. **Saturation:**

   * Base-emitter: Forward biased
   * Base-collector: Forward biased
   * Transistor fully "on" (switch closed)

3. **Cut-Off:**

   * Base-emitter: Reverse biased
   * Base-collector: Reverse biased
   * Transistor fully "off" (switch open)

4. **Reverse Active:**

   * Roles of emitter and collector reversed
   * Poor performance, rarely used intentionally

5. **Avalanche Breakdown:**

   * Excessive voltage causes junction breakdown

8.4.1 BJT Large Signal Model
-------------------------------------------------------------------------------

**Cut-Off Region:**

* IB = 0, IC = 0
* The transistor acts as an open circuit

**Active Region:**

* IC = β × IB
* IE = (β + 1) × IB
* IE = IC + IB
* VBE ≈ 0.65V to 0.7V (forward-biased diode)

.. figure:: figures/chptr8-f6.png
   :align: center

   Figure 8.4.1: NPN and PNP active region large-signal models

**Saturation Region:**

* Both junctions forward biased
* VCE(sat) ≈ 0.1V to 0.3V
* β is significantly reduced

8.4.2 Early Effect (Base Width Modulation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Discovered by James Early at Bell Labs, this effect describes how collector
voltage affects collector current in the active region.

.. figure:: figures/chptr8-f7.png
   :align: center

   Figure 8.4.2: Early voltage demonstration with characteristic curves

As collector voltage increases:

* The collector-base depletion region widens
* The effective base width narrows
* The current gain increases slightly

**Early Voltage (VA):**

The Early voltage is found by extrapolating the IC-VCE curves backward to
their intersection point on the voltage axis. Typical values: 50V to 200V.

8.5 MOSFET Basics
-------------------------------------------------------------------------------

8.5.1 Basic Structure and Principle of Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) is a
voltage-controlled device with extremely high input impedance.

.. figure:: figures/chptr8-f8.png
   :align: center

   Figure 8.5.1: NMOS cross-section and circuit symbol

**Structure:**

* Source and drain: Heavily doped N-type regions (for NMOS)
* Substrate (body): P-type material
* Gate: Polysilicon separated from channel by thin oxide insulator

.. figure:: figures/chptr8-f9.png
   :align: center

   Figure 8.5.2: Top view showing gate dimensions (L, W)

**Key Dimensions:**

* L = gate length (source-to-drain distance)
* W = gate width

**Operation:**

A positive gate voltage (for NMOS) attracts electrons to the surface,
forming an inversion layer that creates a conducting channel between
source and drain.

8.6 MOSFET Large Signal Model
-------------------------------------------------------------------------------

8.6.1 Modes of Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**1. Cut-Off / Subthreshold (VGS < Vth):**

Theoretically no conduction, but weak-inversion leakage current exists:

.. math::

   I_D \approx I_{D0} \cdot e^{\frac{V_{GS} - V_{th}}{nV_T}}

Where n is the slope factor (typically 1.3 to 1.5).

**2. Triode / Linear Region (VGS > Vth AND VDS < VGS - Vth):**

The transistor acts as a voltage-controlled resistor:

.. math::

   I_D = \mu_n C_{ox} \frac{W}{L} \left[ (V_{GS} - V_{th})V_{DS} - \frac{V_{DS}^2}{2} \right]

For small VDS (deep triode):

.. math::

   I_D \approx \mu_n C_{ox} \frac{W}{L} (V_{GS} - V_{th}) V_{DS}

**3. Saturation / Active Mode (VGS > Vth AND VDS > VGS - Vth):**

The channel "pinches off" near the drain:

.. math::

   I_D = \frac{\mu_n C_{ox}}{2} \frac{W}{L} (V_{GS} - V_{th})^2 (1 + \lambda V_{DS})

**Key Parameters:**

* **Transconductance:**

.. math::

   g_m = \mu_n C_{ox} \frac{W}{L} (V_{GS} - V_{th}) = \frac{2I_D}{V_{GS} - V_{th}}

* **Overdrive voltage:** Vov = VGS - Vth

* **Output resistance:**

.. math::

   r_o = \frac{1}{\lambda I_D}

* **Channel-length modulation:** λ (similar to Early effect in BJTs)

8.7 Small Signal Hybrid-π Models
-------------------------------------------------------------------------------

The hybrid-π model is a popular small-signal model for low-frequency analysis.

8.7.1 BJT Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: figures/chptr8-f10.png
   :align: center

   Figure 8.7.1: BJT Hybrid-π model

**Parameters:**

1. **Transconductance:**

.. math::

   g_m = \frac{I_C}{V_T}

2. **Input resistance:**

.. math::

   r_\pi = \frac{\beta}{g_m} = \frac{\beta V_T}{I_C}

3. **Output resistance:**

.. math::

   r_o = \frac{V_A}{I_C}

4. **Intrinsic emitter resistance:**

.. math::

   r_e = \frac{1}{g_m} = \frac{V_T}{I_C}

8.7.2 MOSFET Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: figures/chptr8-f11.png
   :align: center

   Figure 8.7.2: MOSFET Hybrid-π model

**Parameters:**

1. **Transconductance:**

.. math::

   g_m = \sqrt{2 \mu_n C_{ox} \frac{W}{L} I_D} = \frac{2I_D}{V_{ov}}

2. **Output resistance:**

.. math::

   r_o = \frac{1}{\lambda I_D}

3. **Input resistance:** Essentially infinite (gate is insulated)

8.8 The T Model
-------------------------------------------------------------------------------

The T model is an alternative small-signal representation, useful in certain
circuit configurations.

.. figure:: figures/chptr8-f12.png
   :align: center

   Figure 8.8.1: MOSFET and BJT T models

Both PNP/PMOS versions are identical to NPN/NMOS counterparts with appropriate
polarity changes.

Related Lab Activities
-------------------------------------------------------------------------------

* :dokuwiki:`ADALM1000 Lab Activity 3: BJT as a Diode <university/courses/alm1k/alm-lab-bjt-diode>`
* :dokuwiki:`ADALM1000 Lab Activity 4: BJT I/V Curves <university/courses/alm1k/alm-lab-bjt-iv>`
* :dokuwiki:`ADALM1000 Lab Activity 3M: MOS as a Diode <university/courses/alm1k/alm-lab-mos-diode>`
* :dokuwiki:`ADALM1000 Lab Activity 4M: MOS I/V Curves <university/courses/alm1k/alm-lab-mos-iv>`

:ref:`Return to Introduction to Electrical Engineering <university-courses-intro_ee>`
