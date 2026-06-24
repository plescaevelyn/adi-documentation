.. _university-courses-electronics-text-chapter-7:

Chapter 7: Diode Application Topics
===============================================================================

After completing this chapter, you should be able to:

* Design peak detector and envelope detector circuits
* Analyze precision rectifier circuits using op-amps
* Understand diode clamping and clipping circuits
* Design logarithmic and exponential amplifiers

7.1 Half-Wave Rectifier with Filter Capacitor or Peak Detector
-------------------------------------------------------------------------------

A peak detector captures and holds the peak value of an input signal.

.. figure:: figures/chptr7-f1.png
   :align: center

   Figure 7.1.1: Simple peak detector circuit

**Operation:**

* When Vin > Vout, the diode conducts and the capacitor charges to the peak
* When Vin < Vout, the diode is reverse-biased and the capacitor holds the peak value
* The capacitor slowly discharges through the load resistance

**Precision Peak Detector:**

.. figure:: figures/chptr7-f2.png
   :align: center

   Figure 7.1.2: Precision half-wave rectifier or peak detector with op-amp

The op-amp reduces the error caused by the diode forward voltage drop.
However, when the op-amp output saturates during the non-conducting phase,
recovery time can be an issue.

7.2 Absolute Value Circuits
-------------------------------------------------------------------------------

Precision rectification circuits convert AC signals to DC with high accuracy,
eliminating errors from diode voltage drops.

7.2.1 Precision Half-Wave Rectifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: figures/chptr7-f3.png
   :align: center

   Figure 7.2.1: Precision half-wave rectifier circuit

.. figure:: figures/chptr7-f4.png
   :align: center

   Figure 7.2.2: Simulation waveforms showing output characteristics

**Operation:**

* For positive inputs: D1 conducts, D2 is off, output follows input (inverted)
* For negative inputs: D2 conducts, D1 is off, output is zero
* The op-amp feedback eliminates diode voltage drop errors

Application Example: Measuring AC Peak Voltage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: figures/chptr7-f5.png
   :align: center

   Figure 7.2.3: Half-wave rectifier with low-pass filter for DC output

By combining a precision rectifier with a low-pass filter, the DC output
represents the average or peak value of the AC input.

7.2.2 Precision Full-Wave Rectifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The precision full-wave rectifier (absolute value circuit) produces an output
that is the absolute value of the input.

.. figure:: figures/chptr7-f6.png
   :align: center

   Figure 7.2.4: Absolute value circuit

.. figure:: figures/chptr7-f7.png
   :align: center

   Figure 7.2.5: Simulation results

**Design Constraints:**

* R2 = R3 for equal gain on positive and negative half-cycles
* R4 = R5 for proper summing

Related Lab Activity:

* :dokuwiki:`Precision Rectifiers, Absolute Value Circuits <university/courses/alm1k/alm-lab-precision-rectifier>`

7.3 Envelope Detector
-------------------------------------------------------------------------------

An envelope detector extracts the modulation envelope from an amplitude
modulated (AM) signal.

.. figure:: figures/chptr7-f8.png
   :align: center

   Figure 7.3.1: Simple envelope detector circuit

.. figure:: figures/chptr7-f9.png
   :align: center

   Figure 7.3.2: Input AM signal and demodulated output

**Design Considerations:**

* The RC time constant must be:

  * Long enough to filter out the carrier frequency
  * Short enough to follow the modulation envelope

* Typical constraint: 1/fc << RC << 1/fm

Where fc is the carrier frequency and fm is the maximum modulation frequency.

**Limitations:**

* Requires band-pass filtering to isolate the desired signal
* Susceptible to noise
* Distortion occurs with overmodulation (modulation index > 100%)

Related Lab Activities:

* :dokuwiki:`ADALM1000 Envelope Detector <university/courses/alm1k/alm-lab-envelope>`
* :dokuwiki:`ADALM2000 AM Demodulation <university/courses/electronics/electronics-lab-am>`

7.4 Diode Clamp
-------------------------------------------------------------------------------

A clamping circuit (DC restorer) shifts the DC level of a signal without
changing its shape or peak-to-peak amplitude.

.. figure:: figures/chptr7-f10.png
   :align: center

   Figure 7.4.1: Input and output waveforms showing clamping effect

.. figure:: figures/chptr7-f11.png
   :align: center

   Figure 7.4.2: DC restoring circuit schematic

**Operation:**

* The capacitor charges to a voltage that shifts the entire waveform
* The diode determines the reference point (positive or negative peak)
* The RC time constant must be much larger than the signal period

**Precision Op-Amp Clamp:**

.. figure:: figures/chptr7-f12.png
   :align: center

   Figure 7.4.3: Precision op-amp clamp with reference voltage

The op-amp version allows clamping to an arbitrary reference voltage and
eliminates the diode forward voltage error.

7.5 Diode Clippers/Limiters
-------------------------------------------------------------------------------

Clipping circuits limit the voltage excursion of a signal, preventing it
from exceeding specified levels.

.. figure:: figures/chptr7-f13.png
   :align: center

   Figure 7.5.1: Ideal clipping transfer function

.. figure:: figures/chptr7-f14.png
   :align: center

   Figure 7.5.2: Input and clipped output waveforms

**Parallel (Shunt) Clipper:**

.. figure:: figures/chptr7-f15.png
   :align: center

   Figure 7.5.3: Parallel/shunt clipper circuit

**Series Clipper:**

.. figure:: figures/chptr7-f16.png
   :align: center

   Figure 7.5.4: Series clipper circuit

**Limitations:**

* Diode capacitance causes signal attenuation at high frequencies
* Leakage current affects low-level signals
* The transition between clipping and linear regions is not perfectly sharp

7.6 Voltage-Controlled Variable Attenuator
-------------------------------------------------------------------------------

A diode's small-signal resistance varies with bias current, allowing it to
function as a voltage-controlled attenuator.

.. figure:: figures/chptr7-f17.png
   :align: center

   Figure 7.6.1: Variable attenuator circuit

**Small-Signal Resistance:**

.. math::

   r_d = \frac{nV_T}{I_D}

Where:

* n = ideality factor
* VT = thermal voltage (≈ 26 mV at room temperature)
* ID = DC bias current

The attenuation is controlled by varying the DC bias current, which changes
the diode's AC resistance in a voltage divider configuration.

7.7 Logarithmic Output Amplifiers
-------------------------------------------------------------------------------

Logarithmic amplifiers produce an output proportional to the logarithm of
the input signal.

.. figure:: figures/chptr7-f18.png
   :align: center

   Figure 7.7.1: Log amplifier with diode in feedback

.. figure:: figures/chptr7-f19.png
   :align: center

   Figure 7.7.2: Logarithmic transfer characteristic

**Transfer Function:**

Using the diode equation in the op-amp feedback:

.. math::

   V_{out} = -nV_T \ln\left(\frac{V_{in}}{I_S R}\right)

**Applications:**

* Compressing wide dynamic range signals
* Analog computation (multiplication via log addition)
* Audio companders

**Note:** This basic circuit does not compensate for temperature drift.
Practical log amplifiers use matched transistors and temperature compensation.

7.8 Exponential (Antilog) Output Amplifiers
-------------------------------------------------------------------------------

Antilogarithmic amplifiers produce an output proportional to the exponential
of the input signal.

.. figure:: figures/chptr7-f20.png
   :align: center

   Figure 7.8.1: Antilogarithmic amplifier schematic

.. figure:: figures/chptr7-f21.png
   :align: center

   Figure 7.8.2: Exponential transfer characteristic

**Transfer Function:**

.. math::

   V_{out} = -I_S R \cdot e^{\frac{V_{in}}{nV_T}}

**Applications:**

* Expanding compressed signals
* Analog computation (division via log subtraction)
* Function generation

Related Lab Activities
-------------------------------------------------------------------------------

* :dokuwiki:`ADALM1000 Lab: Log/Antilog Amplifiers <university/courses/alm1k/alm-lab-log-amp>`
* :dokuwiki:`ADALM2000 Lab: Diode Clippers and Clampers <university/courses/electronics/electronics-lab-clipper>`

:ref:`Return to Introduction to Electrical Engineering <university-courses-intro_ee>`
