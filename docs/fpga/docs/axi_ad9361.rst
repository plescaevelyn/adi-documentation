:orphan:

.. _fpga axi_ad9361:

AXI_AD9361 IP Core
==================

The AXI_AD9361 is an FPGA IP core that interfaces with the AD9361 transceiver
device. This documentation covers the IP core and requires familiarity with the
device for complete understanding.

.. note::

   This documentation is being migrated to GitHub. The updated version is
   available at the
   `HDL library documentation <https://analogdevicesinc.github.io/hdl/library/axi_ad9361/index.html>`_.

Features
--------

- AXI Lite control/status interface
- PRBS monitoring capability
- Hardware and software DC filtering
- IQ correction functionality
- Internal Direct Digital Synthesis (DDS)
- Programmable line delays
- Receive and transmit loopback modes
- Support for both Altera and Xilinx FPGA devices

Architecture
------------

The core comprises several functional modules:

Interface Module
~~~~~~~~~~~~~~~~

Supports CMOS Dual Port Full Duplex or LVDS modes, with platform-specific
implementations for Intel and Xilinx devices.

Receive Path
~~~~~~~~~~~~

Contains ADC channel processing with:

- DC filtering
- IQ correction
- Data format control
- PN monitoring for signal validation

Transmit Path
~~~~~~~~~~~~~

Features DAC channel processing with:

- DDS (Direct Digital Synthesis)
- IQ correction
- Multiple data source selection (DDS, pattern, PRBS, loopback)

TDD Control
~~~~~~~~~~~

Manages Time Division Duplex operation for simultaneous transmit/receive
scenarios.

Internal Interface Signals
--------------------------

ENABLE
~~~~~~

Software-controlled signal activating specific channels, used by PACK/UNPACK
cores for routing.

VALID
~~~~~

Indicates valid sample availability on the DATA port; reflects the sampling
rate relative to interface clock frequency.

DATA
~~~~

16-bit analog samples following strict conventions:

- Most significant sample represents newest data
- Sign extension for sub-16-bit ADCs
- MSB truncation for DACs

Parameters
----------

Core configuration includes:

- ``MODE_1R1T`` - Selection between 1RX1TX vs 2RX2TX
- TDD disable option
- CMOS/LVDS interface selection
- Individual datapath disable flags for ADC/DAC processing blocks like DC
  filtering and DDS

Register Map
------------

Base Registers (0x0000-0x0007)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Version, ID, scratch, and configuration information.

ADC Common (0x0010-0x0031)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Interface control, clock configuration, synchronization status.

ADC Channel (0x0100-0x01FF)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Per-channel control including:

- DC filter coefficients
- IQ correction parameters
- PN monitor selection

DAC Common (0x1000-0x102F)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Transmit interface configuration and synchronization.

DAC Channel (0x1100-0x11FF)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- DDS tone generation
- IQ correction
- Data source selection

TDD Control (0x2000-0x203B)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Frame timing, VCO control, data path activation windows.

Software Support
----------------

Implementation software is available through:

- `No-OS projects <https://github.com/analogdevicesinc/no-OS>`_ for embedded
  systems
- `ADI Linux drivers <https://github.com/analogdevicesinc/linux>`_ for
  Linux-based systems

Related Documentation
---------------------

- `AD9361 Reference Manual (UG-570) <https://www.analog.com/media/en/technical-documentation/user-guides/AD9361_Reference_Manual_UG-570.pdf>`_
- FMCOMMS2/3/4/5 reference designs
- Xilinx 7-Series documentation (IO, clocking, libraries)
