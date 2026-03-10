.. _ad-fmcomms2-ebz:

AD-FMCOMMS2-EBZ
===============

AD9361 Software Defined Radio Board optimized for 2.4 GHz.

The :adi:`AD-FMCOMMS2-EBZ` is an FMC board for the :adi:`AD9361`, a highly
integrated RF Agile Transceiver. The complete chip level design package can be
found on the ADI website. Information on the card, and how to use it, the
design package that surrounds it, and the software which can make it work, can
be found here.

The purpose of the :adi:`AD-FMCOMMS2-EBZ` is to demonstrate maximum performance
of the :adi:`AD9361` at 2.4 GHz. We use an external Johanson Technology
2450BL15B050E balun rated for 2400-2500 MHz in the design.

This is primarily meant for the RF Engineer to determine exact RF performance
over the 2.4 GHz ISM band before their custom hardware is complete - where the
AD9361 and surrounding circuitry is optimized for the target frequency and
application.

The :adi:`AD-FMCOMMS2-EBZ` board is very similar to the :ref:`AD-FMCOMMS3-EBZ
<ad-fmcomms3-ebz>` board with only one exception: the Rx/Tx RF differential to
single ended transformer. We affectionately call the AD-FMCOMMS2-EBZ the "RF
Engineers" platform, and the :ref:`AD-FMCOMMS3-EBZ <ad-fmcomms3-ebz>`, the
"Software Engineers" platform to denote the difference.

Contents
--------

#. :adi:`Purchase <ad-fmcomms2-ebz#eb-buy>`

#. Introduction

#. FMCOMMS2 Hardware:

   This provides a brief description of the AD-FMCOMMS2-EBZ board by itself,
   and is a good reference for those who want to understand a little more about
   the board.

   #. Hardware (including schematics)
   #. Functional Overview & Specifications
   #. Characteristics & Performance
   #. Configuration options
   #. FCC or CE certification
   #. Tuning the system
   #. Production Testing Process

#. Use the AD-FMCOMMS2-EBZ Board to better understand the AD9361

   #. What you need to get started

   #. Quick Start Guides

      #. Linux on ZC702, ZC706, ZED
      #. Linux on ZCU102
      #. Linux on KC705, VC707
      #. Configure a pre-existing SD-Card
      #. Update the old card you received with your hardware

   #. Linux Applications

      #. :ref:`IIO Oscilloscope <iio-oscilloscope>`
      #. AD936X Control IIO Scope Plugin
      #. AD936X Advanced Control IIO Scope Plugin
      #. Command Line/Shell scripts

   #. Push custom data into/out of the AD-FMCOMMS2-EBZ

      #. Basic Data files and formats
      #. Create and analyze data files in MATLAB
      #. :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`
      #. :ref:`AD9361 libiio streaming example <libiio>`
      #. :ref:`Python Interfaces <pyadi-iio>`

#. Design with the AD9361

   #. Understanding the AD9361

      #. :adi:`AD9361 Product page <AD9361>`
      #. :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      #. :ref:`MATLAB Filter Design Wizard for AD9361 <ad9361 filters>`

   #. Simulation

      #. MathWorks SimRF Models of the AD9361
      #. Installing RF Blockset Models for AD9361
      #. Running the AD9361 Receive Testbench

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. :ref:`Analog Devices Transceiver Toolbox for MATLAB and Simulink <matlab transceiver-toolbox>`
      #. MATLAB/Simulink Examples
      #. :ref:`GNU Radio <gnuradio>`
      #. FM Radio/Tuner
      #. :ref:`C example <libiio>`

   #. Design a custom AD9361 based platform

      #. Linux software

         #. :ref:`Linux Device Driver <ad9361>`
         #. Build the demo on ZC702, ZC706, or ZED from source
         #. Build ZynqMP/MPSoC Linux kernel and devicetrees from source
         #. Build the demo on KC705 or VC707 for Microblaze from source

      #. No-OS Driver
      #. :ref:`HDL Reference Design <fpga hdl>`

#. Additional Documentation about SDR Signal Chains

   #. The math behind the RF

#. Help and Support

Warning
-------

.. esd-warning::

.. toctree::
   :hidden:

   software/filters
