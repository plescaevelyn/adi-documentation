.. _m1k-alice:

ALICE Desktop User's Guide
===============================================================================

Active Learning Interface (for) Circuits (and) Electronics M1K

Objective
-------------------------------------------------------------------------------

This guide serves as a user's manual for the ALICE Desktop software interface
designed to work with the ADALM1000 active learning kit hardware. Users seeking
information about ALICE for the ADALM2000 (M2K) should consult separate
documentation.

Background
-------------------------------------------------------------------------------

The acronym ALICE derives from "Active Learning Interface (for) Circuits (and)
Electronics," but also references Lewis Carroll's 1865 novel "Alice's Adventures
in Wonderland" and its 1871 sequel "Through the Looking-Glass." The software
enables students to explore circuit theory and electrical engineering concepts
using the ADALM1000 hardware.

.. figure:: images/hookah-smoking_caterpillar.png
   :align: center

   Alice Meets the Caterpillar

Functions
-------------------------------------------------------------------------------

ALICE Desktop provides these capabilities:

* Two-channel oscilloscope for time-domain voltage and current waveform analysis
* Two-channel arbitrary waveform generator (AWG) controls
* X-Y display for voltage/current plotting and waveform histograms
* Phase analyzer with polar plotting of amplitude and phase
* Two-channel spectrum analyzer for frequency-domain analysis
* Bode plotter and network analyzer with integrated sweep generator
* Impedance analyzer for RLC network analysis and vector measurement
* DC ohmmeter for resistance measurement
* Board self-calibration functionality

Required Files
-------------------------------------------------------------------------------

Windows Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ALICE Desktop is Python-based (compatible with Python 2.7 or 3.7). Windows
users can install a standalone executable or the source code. Required
components include:

* Windows executable version 1.3 (latest release)
* Libsmu installer (version 1.0.4) for 64-bit or 32-bit systems
* WinUSB device drivers
* Python packages: tKinter, numpy, matplotlib, libsmu/pysmu

Installation should occur outside the default Program Files directory to avoid
permission issues. The installer creates desktop icons for each tool.

Linux and OSX Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most Linux distributions include Python and may include tKinter and numpy.
Additional setup steps:

1. Install pip3: ``sudo apt-get install python3-pip``
2. Install numpy: ``sudo python3 -m pip install numpy``
3. Install tk: ``sudo apt-get install tk``

Manual Installation: libsmu/pysmu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Non-Windows users must compile libsmu/pysmu by following instructions in the
`Libsmu GitHub Repository <https://github.com/analogdevicesinc/libsmu>`__. The
recommended approach uses Anaconda Python with Conda installation packages.
Test examples are available in the libsmu Python bindings directory.

Once verified, download ALICE Version 1.3 source code from the
`alice GitHub Repository <https://github.com/analogdevicesinc/alice/tree/Version-1.3>`__.

Manual Installation: numpy Python Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linux users may already have numpy installed. Windows users should download
binary installers from SourceForge. Recent versions may require building from
source code for 64-bit compatibility.

Directions
-------------------------------------------------------------------------------

Users should familiarize themselves with ADALM1000 hardware before proceeding.
Reference materials include:

* :ref:`ADALM1000 overview and hardware documentation <m1k>`

**Windows Executable Includes:**

* DC Voltmeter tool
* DC Ohmmeter tool
* DC Meter-Source tool
* DC Power Profiler Tool (Python source available)
* DC Strip Chart Tool (Python source available)
* DC Data-Logger Tool (Python source available)

**Nomenclature Notes:**

* CA-V: Channel A voltage signal
* CA-I: Channel A current signal
* CB-V: Channel B voltage signal
* CB-I: Channel B current signal

Customizing ALICE Desktop
-------------------------------------------------------------------------------

Many aspects can be customized through the alice_init.ini file.

Using the numpy Library
-------------------------------------------------------------------------------

ALICE includes Python's numpy numerical library. Additional functions and
capabilities are documented in the advanced user's guide.

Using Equivalent Time Sampling with the ADALM1000
-------------------------------------------------------------------------------

An advanced feature that increases apparent sampling rates to MSPS for periodic
waveforms.

Oscilloscope / Main Window
-------------------------------------------------------------------------------

The ADALM1000 must be connected via USB before launching the program. The main
window functions as both the oscilloscope tool and control center for opening
additional display windows. It is divided into four sections.

.. figure:: images/main-window-1.png
   :align: center

   ALICE Desktop main window

AWG Controls Window
-------------------------------------------------------------------------------

The AWG controls window provides settings for the arbitrary waveform generators.

The X-Y Plotting Tool
-------------------------------------------------------------------------------

The X-Y Plot Window displays when the corresponding button is clicked in the
Main Window.

The Spectrum Analyzer / Bode Plotter
-------------------------------------------------------------------------------

The spectrum analyzer provides frequency-domain analysis, while the Bode plotter
enables network analysis with integrated sweep generation.

DC Ohmmeter Window
-------------------------------------------------------------------------------

This virtual instrument measures unknown resistance.

Digital I/O Controls Windows
-------------------------------------------------------------------------------

The ADALM1000 provides four 3.3V CMOS digital input/output pins on the digital
port connector, accompanied by ground and 3.3V supply connections.

.. figure:: images/m1k-digital-outputs_f1.png
   :align: center

   Digital I/O connector diagram

Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Revision D:** Each GPIO pin connects through 220Ω and 470Ω series resistors

.. figure:: images/m1k-digital-outputs_f2.png
   :align: center

   ALM1000 rev D digital interface

**Revision F:** 220Ω resistors with 4.7kΩ replacements for the higher-value
resistors

.. figure:: images/m1k-f-digital-outputs_f2.png
   :align: center

   ALM1000 rev F digital interface

The 220Ω resistors connect to Port A pins 0-3; the larger-value resistors
connect to Port A pins 4-7.

Digital Control Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The simple digital control interface provides eight rows of selectors—one for
each Port A pin (PA0-PA7). Each pin can be set to:

* Logic low (0)
* High-impedance or floating state (Z) for use as a logic input
* Logic high (1)

.. figure:: images/digital-pio-window.png
   :align: center

   Digital I/O control window

Using Pins for Non-Digital Purposes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The dual resistor configuration can be viewed as a three-position switch
connecting to ground, 3.3V supply, or open circuit. This approach teaches
resistor network concepts including:

* Thevenin and Norton equivalent circuits
* Series/parallel resistor analysis
* Kirchhoff's Voltage Law (KVL) and Current Law (KCL)
* Voltage dividers
* Nodal analysis

.. figure:: images/m1k-digital-outputs_f3.png
   :align: center

   Switch-based analog representation

.. note::

   Nominal values assume ideal conditions; actual values may differ
   significantly. Calculations assume zero MOSFET switch ON-resistance, which
   never occurs in practice.

Eight Equivalent Circuits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nine possible switch combinations yield eight distinct Thevenin equivalent
circuits, plus one open circuit configuration. The first four cases are
straightforward. The next two involve the 220Ω resistor in parallel with the
larger resistor. The final two cases show the 220Ω resistor connected to ground
while the larger resistor connects to 3.3V, and vice versa.

.. figure:: images/m1k-digital-outputs_f4.png
   :align: center

   Eight equivalent circuits diagram

Nine-Level DAC Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A 9-level DAC can be created on each output pin using an external resistor
divider (R1, R2). Two 1kΩ resistors present approximately 500Ω resistance to
1.65V (3.3V/2) on a PIO output. This effective resistance combined with the
eight switchable equivalent circuits produces nine different output voltages.

Using alternative R1 and R2 values generates different voltage ranges.

.. figure:: images/dio-dac-window.png
   :align: center

   Nine-level DAC interface window

Digital State Display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When either digital window is open, the states of PIO 0, PIO 1, PIO 2, and
PIO 3 (left to right) display in the oscilloscope graphics area, updating with
each analog scope refresh.

Steps Performed by ALICE Desktop Self Calibration
-------------------------------------------------------------------------------

ALICE Desktop can perform a self-calibration sequence.

Optional Features and Support for Plug-In Boards
-------------------------------------------------------------------------------

ALICE Desktop interfaces with external plug-in boards that extend functionality:

* External analog multiplexers (increased analog input channels)
* External DDS-based function generators (AD9837-based MiniGen from SparkFun)
* AD5626 serial 12-bit DAC from the ADALP2000 parts kit
* External serial 8-bit DACs (AD7303-based PmodDA1 from Digilent)
* External digital potentiometers (AD840X family, AD5160-based PmodDPOT)
* Generic 3-wire SPI serial output interface

Enable/Disable Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional features are controlled by setting variables in the alice_init.ini
file to either 1 (enabled) or 0 (disabled):

* EnableCommandInterface
* EnableMuxMode
* EnableMinigenMode
* EnablePIODACMode
* EnablePmodDA1Mode
* EnableDigPotMode
* EnableGenericSerialMode
* EnableAD5626SerialMode
* EnableDigitalFilter
* EnableMeasureScreen
* EnableETSScreen

All default to 0. When enabled, a control button appears on the right side of
the main ALICE window.

Multichannel Analog Interface for the ADALM1000
-------------------------------------------------------------------------------

Although the ADALM1000 provides two high-impedance analog input channels with
wide dynamic range, many circuits require monitoring more than two signals
simultaneously. Low-bandwidth sensors (temperature, light) also require
long-duration monitoring.

Hardware Solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ALICE interfaces with external multichannel analog multiplexers:

* SparkFun 74HC4067 16:1 MUX breakout board
* SparkFun 74HC4051 8:1 MUX breakout board
* Custom M1k-compatible multiplexer designs

.. figure:: images/analog-mux-curcuit.png
   :align: center

   Generic analog multiplexer

.. figure:: images/cd4052-analog-mux.png
   :align: center

   CD4052 analog mux schematic example

.. figure:: images/adg609-analog-mux.png
   :align: center

   ADG609 analog mux schematic example

Enabling Multiplexer Controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure this line in alice_init.ini:

.. code-block:: python

   global EnableMuxMode; EnableMuxMode = 1

.. figure:: images/analog-mux-controls.png
   :align: center

   Analog Mux Control window

The analog Mux control window displays four sets of voltage controls. When
open, Channel B voltage and current controls on the main scope window are
replaced. Check boxes select which multiplexer input channels display. The
Mux-Enb checkbox sets PIO-2 low (unchecked) or high (checked) for multiplexers
with enable-low or enable-high inputs respectively.

.. figure:: images/analog-mux-window.png
   :align: center

   Four-channel Mux display

Alternating Sweep Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This technique, common in analog CRT oscilloscopes with single electron beams,
switches multiple input channels to beam deflection circuits on alternating
sweeps. Requires periodic signals with triggering/syncing from the same input
(Channel A).

Channel A serves as the trigger signal—either the AWG generator output or
external signal in Hi-Z mode. Because a multiplexer connects to Channel B,
that channel's AWG output function is set to Hi-Z mode, and current waveform
display is disabled.

Chopping Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A second multiplexer interface mode rapidly switches input signals to beam
deflection circuits. The M1k's 100 KSPS sampling rate allows a square wave
from AWG Channel A to drive multiplexer controls at 1/4 the sample rate
(25 KSPS). Each multiplexer input receives two samples; software ignores the
first (for settling) and uses the second. The 25 KSPS data is up-sampled to
100 KSPS using 4X digital interpolation filtering.

The software automatically configures Channel A AWG settings. Once set, these
should not be manually changed during Chop Sweep mode operation.

Synchronization Pulse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A sync/sweep start pulse outputs on PIO 3 just before each analog sweep. The
pulse direction (high-going or low-going) is selectable. This "reset" pulse
is necessary when using alternating sweep for circuits containing state, such
as digital counters or state machines.

External DDS-Based Function Generators
-------------------------------------------------------------------------------

The ADALM1000's four general-purpose digital I/O pins function as a serial
port (SPI) for interfacing with direct digital synthesis (DDS) waveform
generators like the AD9837 and AD9833, capable of producing sine, triangular,
and square wave outputs.

Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SparkFun offers the MiniGen breakout board ($29.95) based on the AD9837.
Connection to the ADALM1000 digital connector is straightforward:

* Install a 6-pin right-angle male header
* Connect FSYNC, SDATA, SCLK to PIO 0, PIO 1, PIO 3 respectively
* Wire the VIN pin to 3.3V and GND to GND with jumper wires
* Solder the on-board LDO bypass jumper to power directly from 3.3V
* Install a two-pin female right-angle connector to analog output points

.. figure:: images/mini-gen-connections.png
   :align: center

   AD9837 MiniGen connection diagram

MiniGen Control Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The control interface allows:

* Selection of four possible waveform shapes
* Master clock frequency setting (board includes 16MHz crystal oscillator)
* Output frequency adjustment

.. figure:: images/alice-ets-guide-f21.png
   :align: center

   AD983X DDS function generator controls

The MiniGen produces a fixed 1V peak-to-peak amplitude signal centered on
supply/2 (approximately 1.65V).

AD9833 Compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD9833 is functionally similar to the AD9837. Its serial interface
waveforms and control/frequency/phase register configurations match the
AD9837, allowing ALICE Desktop compatibility by connecting I/O pins
appropriately to FSYNC, SDATA, and SCLK.

MiniGen with Bode Plotter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As of ALICE 1.1 Desktop (version 6-19-2017), the MiniGen can serve as the
sweep signal source for the Bode Plotter. Opening the MiniGen controls before
the Bode Plot window reveals a third Sweep Generator option. While the
MiniGen's fixed 1V peak-to-peak amplitude centered on half the 3.3V supply
provides less flexibility than internal AWG sources, it generates much higher
frequencies, enabling sweeps approaching the 50kHz limit of the 100 KSPS
sampling rate.

External Serial 8-Bit DAC Pmods
-------------------------------------------------------------------------------

The digital I/O pins interface with the PmodDA1 4-channel DAC module from
Digilent and other distributors such as Mouser.

PmodDA1 Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The module contains two AD7303 8-bit dual voltage output DACs. Its 6-pin male
connector plugs directly into the ADALM1000 digital port.

.. figure:: images/pmodda1-obl-400.png
   :align: center

   PmodDA1 module

.. figure:: images/pmodda1-block-336.png
   :align: center

   PmodDA1 block diagram

.. warning::

   Because the ADALM1000's component side faces downward, the PmodDA1 must also
   be installed component-side down. Carefully verify pin labels on both boards
   before connection.

**Pin Configuration:**

* PIO 0: SYNC input for both DACs
* PIO 1: Data input for first AD7303
* PIO 2: Data input for second AD7303
* PIO 3: SCLK serial clock input for both DACs

**Reference Configuration:**

The DACs are generally configured to use VDD/2 as reference. Since VDD is the
3.3V supply from the digital port connector, all four output channels produce
0 to 3.3V output ranges.

**Alternative Component Form:**

AD7303 DACs are available in 8-pin PDIP packages for solderless breadboard
integration with other circuit components.

PmodDA1 Control Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The interface provides controls for all four DAC channels. Users enter desired
DC voltages (0 to 3.3V, less one LSB) and click Update to send new values to
the DACs.

.. figure:: images/pmod-da1-controls.png
   :align: center

   PmodDA1 control window

External Digital Potentiometers
-------------------------------------------------------------------------------

The AD8402 dual 10kΩ and AD8403 quad 10kΩ digital potentiometers feature 8-bit
resolution in PDIP packages suitable for solderless breadboards.

PmodDPOT Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD5160-based PmodDPOT features a single 8-bit 10kΩ digital potentiometer
with a 6-pin male connector for direct ADALM1000 digital port connection.

.. figure:: images/pmod_dpot_top.png
   :align: center

   PmodDPOT

.. warning::

   The PmodDPOT must be installed component-side down, matching the ADALM1000
   orientation. Verify pin labels on both boards carefully before connection.

AD8402 Connection Details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connections for the AD8400 single and AD8403 quad variants are similar.

.. figure:: images/ad8402-connections.png
   :align: center

   AD8402 connections diagram

Digital Pot Control Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The interface features:

* Check boxes to select which potentiometers (up to four on the AD8403)
  receive data
* Individual sliders for each potentiometer, controlling values from 0 to 255
* Radio button selection between AD840X family (10-bit data: 8-bit value +
  2-bit address) and AD5160 single potentiometer (8-bit data)

.. figure:: images/dig-pot-controls.png
   :align: center

   Digital Pot control window

Generic 3-Wire SPI Output
-------------------------------------------------------------------------------

The digital I/O pins output serial data to generic 3-wire SPI serial input
devices. The interface allows configuring any of the four PIO digital pins
(0-3) as:

* SCLK (serial clock)
* SData (serial data)
* Latch (sometimes called CS or SYNC) outputs

Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Number of bits per digital write
* Data word format (decimal/integer or hexadecimal with 0x00 prefix)
* Latch output resting level (Latch Phase selector)
* Bit transmission order (LSB-first or MSB-first)

Some serial devices operate on the rising or falling edge of the Latch signal;
edge selection is available.

.. figure:: images/serial-out-controls.png
   :align: center

   Generic Serial Interface screen

**Operation:**

The current data value is sent/written each time the Send button is clicked.

Command Line Interface
-------------------------------------------------------------------------------

ALICE Desktop provides a command line interface for advanced users requiring
full data access and inner program workings, particularly the numpy array math
function library.

Enabling the Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the activation button does not appear in the main ALICE window.
Enable it by adding to alice_init.ini:

.. code-block:: python

   global EnableCommandInterface; EnableCommandInterface = 1

.. figure:: images/command-line-window.png
   :align: center

   ALICE Command Interface

Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The interface requires basic Python syntax familiarity and understanding of
ALICE variable structure. Multiple functions per line are separated using
semicolons. Command execution occurs via <enter>/<return> key or Execute
button click.

The last successfully executed line displays below "Last command." Command
sequences can be entered in plain text files and run as scripts using the
Run Script button.

**Example numpy Function:**

To save the VBuffA (Channel A voltage waveform buffer) to a .csv file:

.. code-block:: python

   numpy.savetxt("my_data.csv", VBuffA, delimiter=",", fmt='%2.4f')

Where:

* ``"my_data.csv"`` is the destination filename
* ``VBuffA`` is the data array
* ``delimiter=","`` uses commas for column separation
* ``fmt='%2.4f'`` formats output to 4 decimal places

Advanced information on ALICE's inner workings, variable and array names, and
numpy function library capabilities can be found in the alice source code and
documentation.
