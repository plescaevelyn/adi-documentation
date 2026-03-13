.. _eval-ad7616-sdz:

EVAL-AD7616-SDZ
===============================================================================

.. image:: images/eval-ad7616-sdz-top.png
   :width: 500

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7616SDZ` is an evaluation board for the :adi:`AD7616`, a
16-bit, data acquisition system (DAS) that supports dual simultaneous sampling
of 16 channels. The AD7616 operates from a single 5V supply and can accommodate
±10V, ±5V, and ±2.5V true bipolar input signals while sampling at throughput
rates up to 1 MSPS per channel pair with 90 dB SNR. Higher SNR performance can
be achieved with the on-chip oversampling mode; 92 dB for an oversampling ratio
of 2.

The input clamp protection circuitry can tolerate voltages up to ±20V. The
AD7616 has 1 MΩ analog input impedance regardless of sampling frequency. The
single supply operation, on-chip filtering, and high input impedance eliminate
the need for driver op-amps and external bipolar supplies.

Each device contains analog input clamp protection, a dual, 16-bit charge
redistribution successive approximation analog-to-digital converter (ADC),
a flexible digital filter, a 2.5V reference and reference buffer, and
high-speed serial and parallel interfaces.

Applications:

- Powerline monitoring
- Protective relays
- Multiphase motor control
- Instrumentation and control systems
- Data acquisition systems (DAS)

Supported Devices
-------------------------------------------------------------------------------

- :adi:`AD7616`

Supported Carriers
-------------------------------------------------------------------------------

- :xilinx:`ZC706` (FMC via SDP-I-FMC)
- :xilinx:`ZedBoard` (FMC via SDP-I-FMC)
- `SDP-K1 <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/SDP-K1.html>`_
  (fly-wire, No-OS)

.. toctree::
   :hidden:

   prerequisites
   user-guide
   no-os
   quickstart/index

Table of contents
-------------------------------------------------------------------------------

#. :ref:`eval-ad7616-sdz prerequisites` — hardware and software you need to
   get started
#. :ref:`eval-ad7616-sdz user-guide` — block diagrams and HDL design
   reference
#. :ref:`eval-ad7616-sdz no-os` — No-OS driver and IIO driver reference
#. :ref:`eval-ad7616-sdz quickstart`:

   #. :ref:`eval-ad7616-sdz quickstart zedboard` — using ZedBoard with
      SDP-I-FMC
   #. :ref:`eval-ad7616-sdz quickstart zc706` — using ZC706
   #. :ref:`eval-ad7616-sdz quickstart sdp-k1` — using SDP-K1 (No-OS,
      bare metal)

.. esd-warning::
