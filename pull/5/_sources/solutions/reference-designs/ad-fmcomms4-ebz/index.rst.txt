.. _ad-fmcomms4-ebz:

AD-FMCOMMS4-EBZ
===============

AD9364 Wideband Software Defined Radio Board.

The :adi:`AD-FMCOMMS4-EBZ` is an FMC board for the :adi:`AD9364`, a highly
integrated RF Agile Transceiver. The complete chip level design package can be
found on the ADI website. Information on the card, and how to use it, the
design package that surrounds it, and the software which can make it work, can
be found here.

The purpose of the :adi:`AD-FMCOMMS4-EBZ` is to provide an RF platform to
software developers, system architects, etc, who want a single Rx / single Tx
platform which operates over a wide tuning range (70 MHz - 6 GHz).

The :adi:`AD-FMCOMMS4-EBZ` board is very similar to the :ref:`AD-FMCOMMS2-EBZ
<ad-fmcomms2-ebz>` and :ref:`AD-FMCOMMS3-EBZ <ad-fmcomms3-ebz>` boards with one
primary difference: instead of incorporating the :adi:`AD9361` (2 Rx, 2 Tx
configuration), it utilizes the :adi:`AD9364`, which offers a more economical
1 Rx, 1 Tx architecture. The board includes dual external balun options - one
for broader tuning applications (Mini-Circuits TCM1-63AX+) and optimized
variants for 2.4 GHz operations.

Contents
--------

#. :adi:`Purchase <ad-fmcomms4-ebz#eb-buy>`

#. Introduction

#. FMCOMMS4 Hardware

   #. Functional Overview & Specifications
   #. Characteristics & Performance
   #. Configuration options
   #. FCC/CE certification information
   #. System tuning guidance
   #. Production Testing Process

#. Use the AD-FMCOMMS4-EBZ Board

   #. What you need to get started

   #. Quick Start Guides

      #. Linux on ZC702, ZC706, ZED
      #. Linux on ZCU102
      #. Linux on KC705, VC707
      #. SD-Card configuration
      #. Hardware update procedures

   #. Linux Applications

      #. :ref:`IIO Oscilloscope <iio-oscilloscope>`
      #. AD936X Control IIO Scope Plugin
      #. Shell scripts

   #. Data file handling

      #. Basic IQ datafiles and formats
      #. MATLAB integration
      #. :ref:`Python Interfaces <pyadi-iio>`

#. AD9364 Design Integration

   #. Understanding the AD9364

      #. :adi:`AD9364 Product page <AD9364>`
      #. :ref:`MATLAB Filter Design Wizard <ad9361 filters>`

   #. Simulation tools (MathWorks SimRF)
   #. Hardware-in-loop development

      #. :ref:`Analog Devices Transceiver Toolbox <matlab transceiver-toolbox>`
      #. :ref:`GNU Radio <gnuradio>`
      #. FM radio applications
      #. :ref:`C examples <libiio>`

   #. Custom platform development

      #. Linux software

         #. :ref:`Linux Device Driver <ad9361>`
         #. Build instructions for Zynq platforms
         #. Build ZynqMP/MPSoC kernel and devicetrees

      #. No-OS Driver
      #. :ref:`HDL reference designs <fpga hdl>`
      #. Digital interface timing validation

#. Additional Resources

   #. RF mathematical foundations
   #. SDR For Engineers educational material
   #. Help and support

Warning
-------

.. esd-warning::
