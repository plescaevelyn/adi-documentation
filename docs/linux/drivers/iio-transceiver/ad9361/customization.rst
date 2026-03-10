:orphan:

.. _ad9361 customization:

AD9361 Device Driver Customization
==================================

This page documents configuration options for the AD9361 transceiver device
driver, covering both Linux and No-OS implementations.

The configuration options map Linux Device Tree attributes to No-OS
``AD9361_ParamInit`` structure members.

Base Configuration
------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Parameter
     - Description
   * - 2Rx2Tx mode enable
     - Default is 1Rx1Tx mode
   * - 1Rx1Tx mode channel selection
     - Select which channel to use in 1R1T mode
   * - FDD/TDD mode selection
     - Frequency or Time Division Duplex
   * - Dual synth mode in TDD
     - Enable dual synthesizer in TDD mode
   * - VCO calibration skip option
     - Skip VCO calibration at startup

ENSM Control
------------

- Pulse vs. level mode for control pins
- Pin-based vs. SPI control selection
- Independent FDD mode for individual RX/TX control

LO Control
----------

- RX/TX synthesizer frequencies
- Fastlock delay and pin control settings
- External LO enable options
- Target frequency reference override

Rate & Bandwidth Control
------------------------

- RX/TX path clock frequencies (array of 6 values)
- RF bandwidth settings (RX and TX)

RF Port Control
---------------

- RX/TX port input/output selection
- Phase inversion between RX channels

TX Attenuation
--------------

- Power-up attenuation in millidB
- Alert state gain update control

Reference Clock Control
-----------------------

- XO disable and external reference clock selection
- DCXO coarse/fine tuning values

RX DC/QEC Tracking
------------------

- Offset tracking update event masks
- Attenuation ranges for high/low frequency bands
- Sample count settings affecting loop gain
- Slow mode for QEC tracking near DC

Gain Control Configuration
--------------------------

Manual/AGC Modes
~~~~~~~~~~~~~~~~

- Split vs. full gain table modes
- Per-channel gain control operation (manual/fast AGC/slow AGC/hybrid)
- ADC overload thresholds (large and small)
- LMT overload thresholds
- Low power threshold for AGC

MGC (Manual Gain Control)
~~~~~~~~~~~~~~~~~~~~~~~~~

- Gain step increments/decrements
- Control input pin enable per channel
- Split table control mode selection

AGC (Automatic Gain Control)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Overload exceed counters
- Gain step increments
- Digital saturation handling
- Inner/outer threshold settings with step sizes
- Attack delay configuration

Fast AGC
~~~~~~~~

- Power measurement duration
- State transition timing
- Low power threshold management
- Lock level gain increase settings
- Peak detector final settling steps
- Gain unlocking behavior post-RX exit
- Energy loss and signal strength thresholds

RSSI Configuration
------------------

RSSI Restart Modes
~~~~~~~~~~~~~~~~~~

- **Mode 0**: Triggers when fast attack AGC locks
- **Mode 1**: Triggers on EN_AGC pin high
- **Mode 2**: Triggers on RX mode entry
- **Mode 3**: Triggers on gain change (FDD)
- **Mode 4**: Triggers on SPI write (FDD)
- **Mode 5**: Triggers on gain change OR EN_AGC (FDD)

RSSI Parameters
~~~~~~~~~~~~~~~

- Restart mode selection (6 modes: 0-5)
- Duration, delay, and wait timing
- Unit selection (RX samples vs. microseconds)
- Gain step error table calibration values

Auxiliary ADC/DAC/Sensor Control
--------------------------------

Aux ADC
~~~~~~~

- Decimation settings
- Clock frequency configuration

Temperature Sensor
~~~~~~~~~~~~~~~~~~

- Decimation values
- Measurement interval in milliseconds
- Offset in signed degrees Celsius
- Periodic measurement enable

Aux DAC (Dual channels)
~~~~~~~~~~~~~~~~~~~~~~~

- Manual mode vs. ENSM slaving
- Default voltage per DAC
- Active state selection (RX/TX/ALERT)
- Delay timing (RX/TX modes)

GPIO Configuration
------------------

GPO (General Purpose Output) - 4 Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each GPO (0-3) supports:

- Inactive state logic level selection
- RX/TX mode state triggering
- Delay timing from ENSM state changes (0-255 microseconds)

Control Output Setup
~~~~~~~~~~~~~~~~~~~~

32 indexed output modes available including:

- VCO calibration status
- Quadrature calibration states
- Gain lock/change indicators
- Energy loss and signal strength detection
- Overflow conditions
- ENSM state encoding

Clock Output Configuration
--------------------------

CLKOUT Modes:

- **Mode 0**: Disabled
- **Mode 1**: Buffered XTALN/DCXO
- **Modes 2-8**: ADC_CLK divided by 2, 3, 4, 8, 16, 32, 64 respectively

RF Port Selection
-----------------

RX Port Input Select (0-8)
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Values 0-2: Balanced pair configurations (A/B/C)
- Values 3-8: Unbalanced single-ended options

TX Port Output Select
~~~~~~~~~~~~~~~~~~~~~

- Value 0: TX1A, TX2A
- Value 1: TX1B, TX2B

External LNA Control
--------------------

- Settling delay in nanoseconds
- Gain in millidB (0-31500 in 500mdB steps)
- Bypass loss specification
- GPO pin routing for gain control
- Gain table index enable

TX Monitor Control
------------------

Settings for transmit path monitoring:

- Low/high gain thresholds
- DC tracking enable
- One-shot vs. continuous mode
- Measurement delay and duration
- Front-end gain per channel
- LO common mode settings

Digital Interface Configuration
-------------------------------

Physical Interface Options
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Parallel port I/Q swap
- Channel swap capability
- Frame pulse mode (continuous vs. 50% duty cycle)
- 2R2T timing selection
- Data bus inversion
- Data clock inversion
- FDD alternate word order

Data Port Modes
~~~~~~~~~~~~~~~

- Single vs. dual data rate
- LVDS vs. CMOS selection
- Full/half duplex mode
- Single/dual port mode
- Full port data path control
- Port swapping

Signal Timing/Delay
~~~~~~~~~~~~~~~~~~~

- RX data delay relative to frame
- RX/TX clock delays (0.3 ns/LSB typical)
- LVDS bias voltage control (75-450 mV)
- On-chip termination for LVDS
- LVDS pair phase inversion control

Related Documentation
---------------------

- :ref:`AD9361 Linux Device Driver <ad9361>`
- :ref:`AD936x FIR Filter Wizard <ad9361 filters>`
