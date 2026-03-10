:orphan:

.. _ad9361 filters:

AD936x FIR Filter Design Wizard
===============================

The AD9361 Filter Design Wizard is a MATLAB application enabling users to
design transmitter and receiver FIR filters. The tool accounts for magnitude
and phase response across analog and digital filter stages in the signal chain.

Features
--------

- Selection of appropriate digital filters for receive and transmit paths
- Programmable FIR filter design with coefficient generation
- Filter coefficient export to ``.ftr`` format for hardware loading
- Independent and composite filter response analysis

Prerequisites
-------------

Required MATLAB components:

- MATLAB (R2015b or newer)
- Signal Processing Toolbox
- DSP System Toolbox
- Fixed-Point Designer (for HDL generation)

Download and Installation
-------------------------

The wizard is available from the
`Analog Devices GitHub repository <https://github.com/analogdevicesinc/ad936x-filter-wizard>`_
at different release versions in MATLAB App installer (``.mlappinstall``) or
archive formats (zip/tarball).

Launch methods:

- Right-click ``AD9361_Filter_Wizard.fig`` and select "Open in GUIDE," then
  press Ctrl+T
- Execute ``AD9361_Filter_Wizard`` from MATLAB command line

Basic Usage
-----------

The application provides a dropdown list with default parameter profiles for
common LTE applications. Users can select profiles like "LTE10 (Rx & Tx)" which
auto-populate parameters.

LTE Bandwidth Reference
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 25 30 30

   * - LTE Spec
     - Bandwidth (MHz)
     - RF Bandwidth (MHz)
     - Sample Rate (MSPS)
   * - 1.4
     - 1.08
     - 1.92
     - 1.92
   * - 3
     - 2.7
     - 3.84
     - 3.84
   * - 5
     - 4.5
     - 7.68
     - 7.68
   * - 10
     - 9
     - 15.36
     - 15.36
   * - 15
     - 13.5
     - 23.04
     - 23.04
   * - 20
     - 18
     - 30.72
     - 30.72

Input Parameters
~~~~~~~~~~~~~~~~

- Magnitude specifications (Apass, Astop)
- Frequency specifications (Fpass, Fstop)
- AD936x clock settings

Filter Results
~~~~~~~~~~~~~~

After design execution, the GUI displays:

- Magnitude response plot (0 to half data rate on x-axis)
- Filter Results panel showing actual Apass, Astop, FIR tap count, passband
  group delay variance

Filter Visualization Tool (FVTool)
----------------------------------

Two FVTool button options provide detailed analysis:

Passband Focus
~~~~~~~~~~~~~~

- Half-band and composite HB + FIR magnitude response
- FIR-only magnitude response with toolbar navigation to phase, group delay,
  impulse response, poles/zeros
- Overall passband group delay with calculated variance

Full Bandwidth Focus
~~~~~~~~~~~~~~~~~~~~

- Complete magnitude response with zoom in/out capabilities

Output Options
--------------

Save to Workspace
~~~~~~~~~~~~~~~~~

Exports filter objects named ``AD9361_Tx_Filter_object`` or
``AD9361_Rx_Filter_object`` as ``mfilt.cascade`` objects. Also generates
``FMCOMMS2_TX_Model_init`` or ``FMCOMMS2_RX_Model_init`` data structures for
SimRF model initialization.

Coefficients to .ftr File
~~~~~~~~~~~~~~~~~~~~~~~~~

Requires both Transmit and Receive filter designs. User specifies filename and
location through dialog window. Compatible with IIO Oscilloscope application.

Zynq Board Integration
~~~~~~~~~~~~~~~~~~~~~~

Three target-specific functions:

- Connect to target via IP address input
- Read clock settings from detected target
- Save FIR coefficients directly to target hardware

Advanced Options
----------------

Enable additional options through "Advanced" toggle:

Phase Equalization
~~~~~~~~~~~~~~~~~~

Reduces passband group delay variance across the filter chain by finding
optimal target delay. Process may require several minutes depending on system
performance.

Additional Parameters
~~~~~~~~~~~~~~~~~~~~~

- **Astop (FIR)**: Specifies FIR attenuation independent of composite response
- **Fcutoff (Analog)**: Sets Butterworth analog filter cutoff frequency;
  auto-calculated by default
- **Use Internal FIR**: Toggle AD9361 internal FIR implementation; disabling
  removes tap constraints enabling minimum-order design
- **Generate HDL**: Invokes ``fdhdltool`` for FPGA implementation with
  configurable generation options

MATLAB Function Interface
-------------------------

Alternative command-line usage:

.. code:: matlab

   output = design_filter(input)

Input Structure Fields
~~~~~~~~~~~~~~~~~~~~~~

1. ``Rdata``: Input/output sample data rate (Hz)
2. ``FIR``: FIR interpolation/decimation factor
3. ``PLL_mult``: PLL multiplication value
4. ``Fpass``: Passband frequency (Hz)
5. ``Fstop``: Stopband frequency (Hz)
6. ``Apass``: Maximum passband ripple (dB)
7. ``Astop``: Minimum stopband attenuation (dB)
8. ``FIRdBmin``: Minimum FIR rejection requirement (dB)
9. ``phEQ``: Phase equalization flag (enabled: non-(-1), disabled: -1)
10. ``int_FIR``: AD9361 FIR usage (enabled: 1, disabled: 0)
11. ``wnom``: Analog cutoff frequency (Hz)

Output Structure Fields
~~~~~~~~~~~~~~~~~~~~~~~

1. ``firtaps``: 16-bit fixed-point FIR coefficients
2. ``filter``: System object for visualization (excludes analog filters)
3. ``delay``: Actual delay value used in phase equalization

Filter Architecture
-------------------

Transmit Path
~~~~~~~~~~~~~

Signal flow from source through:

- PROG TX FIR (programmable poly-phase filter with 1×, 2×, or 4× interpolation
  or bypass)
- HB1, HB2, HB3: Selectable half-band digital filters
- INT3: Fixed digital filter
- DAC (represented by sinc function in analysis)
- Two-stage analog low-pass filtering

Receive Path
~~~~~~~~~~~~

Signal flow from antenna through:

- Two-stage analog low-pass filtering
- ADC (represented by sinc³ function in analysis)
- HB3/DEC3, HB2, HB1: Fixed decimation filters
- PROG RX FIR (programmable poly-phase filter with 1×, 2×, or 4× decimation or
  bypass)

FIR Tap Constraints
~~~~~~~~~~~~~~~~~~~

- Minimum: 16 taps
- Maximum: 64 taps (1× interpolation) or 128 taps (2× and 4× interpolation)
- Quantized in 16-tap groups

C/C++ Implementation
--------------------

Two deployment paths are available:

GPL-Licensed C Version
~~~~~~~~~~~~~~~~~~~~~~

Provided in the
`libiio library <https://github.com/analogdevicesinc/libiio>`_ with complete
filter coefficient generation source.

MATLAB Codegen Support
~~~~~~~~~~~~~~~~~~~~~~

Alternative in ad936x-filter-wizard codegen-support branch with
``alternative_internal_filter_designer_cg`` function providing coefficient-only
output.

Code Generation Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Required MathWorks components:

- MATLAB
- Signal Processing Toolbox
- Fixed-Point Designer
- MATLAB Coder

Support
-------

Technical assistance is available through the
:ez:`EngineerZone Help & Support <sw-interface-tools>` community forums.
