.. _university-courses-electronics-text-choosing-transistors:

Choosing Discrete Transistors
===============================================================================

*Author: James Bryant, May 2014*

This document addresses the common challenge of selecting transistors for
circuit designs, particularly when faced with obsolete part numbers. The
focus is on understanding transistor parameters and selecting suitable
replacements rather than searching for specific obsolete devices.

Introduction
-------------------------------------------------------------------------------

A frequent question from hobbyists and students is "Where can I find transistor
XYZ?" Often, the specific device is obsolete or unavailable. A better approach
is to understand the requirements and select from readily available alternatives.

Transistors
-------------------------------------------------------------------------------

Transistors are three-terminal amplifying devices where a small signal at one
terminal controls a larger current between the other two terminals.

**Two Basic Types:**

1. **BJT (Bipolar Junction Transistor):** Current-controlled device
2. **FET (Field-Effect Transistor):** Voltage-controlled device

**Polarities:**

* NPN / N-channel: Current flows from positive supply through device
* PNP / P-channel: Current flows from device to negative supply (or ground)

BJT Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: figures/ctrans_f1.jpg
   :align: center

   Figure 1: Basic function of a transistor

.. figure:: figures/ctrans_f2.jpg
   :align: center

   Figure 2: NPN Bipolar Junction Transistor (BJT)

The BJT consists of three doped semiconductor regions. A small base current
controls a much larger collector current. The ratio IC/IB is the current
gain β (or hfe).

FET Variants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Enhancement Mode MOSFET:**

.. figure:: figures/ctrans_f3.jpg
   :align: center

   Figure 3: N-Channel Enhancement mode MOSFET

* Normally off (no channel at VGS = 0)
* Positive VGS creates conducting channel
* Most common type for switching applications

**Depletion Mode MOSFET:**

.. figure:: figures/ctrans_f4.jpg
   :align: center

   Figure 4: N-Channel Depletion mode MOSFET

* Normally on (channel exists at VGS = 0)
* Negative VGS reduces or eliminates channel
* Used in special applications (current sources, analog switches)

**JFET:**

.. figure:: figures/ctrans_f5.jpg
   :align: center

   Figure 5: N-Channel Depletion mode JFET

* Normally on device
* Negative VGS (for N-channel) reduces drain current
* Simple, low noise, but limited voltage ratings

Choosing Transistors
-------------------------------------------------------------------------------

**General Preferences:**

* Enhancement-mode devices (normally off) are preferred for most applications
* BJTs are often lower cost for simple applications
* MOSFETs have higher input impedance and are easier to drive
* MOSFETs can be more sensitive to ESD damage

Universal Device Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rather than searching for specific part numbers, consider defining your
requirements in terms of universal specifications:

**TUN/TUP (Transistor Universal NPN/PNP):**

General-purpose BJTs meeting minimum specifications:

* VCEO ≥ 20V
* IC ≥ 100mA
* hfe ≥ 100
* ft ≥ 100MHz

**MUN/MUP (MOSFET Universal N/P-channel):**

General-purpose MOSFETs meeting minimum specifications:

* VDS ≥ 20V
* ID ≥ 200mA
* RDS(on) ≤ 1Ω at VGS = 4.5V

Transistor Parameters
-------------------------------------------------------------------------------

Understanding key parameters enables proper device selection:

Electrical Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Breakdown Voltage (BVceo / BVds):**

Maximum voltage the device can withstand. Always select a device rated
above your maximum circuit voltage with appropriate margin.

**Maximum Current (IC(max) / ID(max)):**

Maximum continuous current. Consider peak and pulse currents as well.

**Leakage Current (ICEO / IDSS0):**

Small current flow when the transistor is off. Important for:

* Low-power applications
* High-impedance circuits
* Sample-and-hold circuits

.. figure:: figures/ctrans_f8.jpg
   :align: center

   Figure 8: Low-power inverter demonstrating leakage current effects

**Current Gain (β / hfe):**

For BJTs, the ratio of collector current to base current. Varies with:

* Operating current
* Temperature
* Device-to-device variation

**Transconductance (gfs):**

For FETs, the ratio of drain current change to gate voltage change.
Higher gfs means better voltage-to-current conversion.

**Threshold Voltage (Vgs(th)):**

For MOSFETs, the gate voltage at which the device begins to conduct.
Important for logic-level compatibility.

**Saturation Voltage (VCE(sat)):**

For BJTs, the collector-emitter voltage when fully on. Lower is better
for switching efficiency.

**On-Resistance (RDS(on)):**

For MOSFETs, the drain-source resistance when fully on. Lower is better
for power efficiency.

Frequency/Speed Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Transition Frequency (ft):**

The frequency at which BJT current gain drops to unity. Higher ft means
better high-frequency performance.

**Switching Times (ton / toff):**

Time required to turn the device on or off. Important for:

* PWM applications
* High-frequency switching
* Digital logic interfaces

**Capacitances (Cin, Cout, Cfb):**

Parasitic capacitances affect high-frequency performance and switching speed.

.. figure:: figures/ctrans_f11.jpg
   :align: center

   Figure 11: Parasitic capacitances of transistors

**Noise Figure (NF):**

Important for low-noise amplifier design. Measured in dB.

Physical Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Package Styles:**

.. figure:: figures/ctrans_f6.jpg
   :align: center

   Figure 6: Common transistor packages

* Through-hole: TO-92, TO-220, TO-3
* Surface mount: SOT-23, SOT-223, DPAK, D2PAK

**Pinout Variations:**

.. figure:: figures/ctrans_f7.jpg
   :align: center

   Figure 7: Six possible pinouts for a TO-92 package

Always verify pinout before installation - there is no universal standard.

**Thermal Considerations:**

Power dissipation creates heat. Thermal resistance (θJA, θJC) determines
how hot the device gets for a given power dissipation.

Circuit Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Emitter/Source Follower:**

.. figure:: figures/ictrans_f9.jpg
   :align: center

   Figure 9: BJT and MOSFET emitter/source follower comparison

**Current Output Stage:**

.. figure:: figures/ctrans_f10.jpg
   :align: center

   Figure 10: MOSFET advantage for current output (zero gate current)

Choosing a Transistor: Practical Approach
-------------------------------------------------------------------------------

**Step-by-Step Selection:**

1. **Determine polarity:** NPN/N-channel or PNP/P-channel?
2. **Choose type:** BJT or MOSFET based on drive requirements
3. **Specify voltage:** Maximum voltage with margin
4. **Specify current:** Maximum current with margin
5. **Select package:** Through-hole or surface mount, thermal requirements
6. **Consider power:** Calculate dissipation, select appropriate package

**Using Parametric Search:**

Major distributors provide parametric search tools:

* Digi-Key
* Mouser
* Arrow
* Avnet
* Farnell/Newark
* RS Components

Enter your requirements and compare available options.

**Verification:**

1. Review complete datasheet for selected device
2. Simulate circuit with SPICE model if available
3. Build and test prototype
4. Verify performance over temperature range if required

**Documentation Best Practice:**

When publishing designs, specify generic requirements rather than specific
part numbers. This allows readers to select available devices and prevents
designs from becoming obsolete when specific parts are discontinued.

References
-------------------------------------------------------------------------------

* Lilienfeld, J.E., "Method and apparatus for controlling electric currents,"
  US Patent 1,745,175, 1930
* Shockley, W., "Circuit element utilizing semiconductive material,"
  US Patent 2,569,347, 1951
* Bardeen, J. and Brattain, W.H., "Three-electrode circuit element utilizing
  semiconductive materials," US Patent 2,524,035, 1950

:ref:`Return to Introduction to Electrical Engineering <university-courses-intro_ee>`
