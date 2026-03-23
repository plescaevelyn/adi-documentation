AD-FMCOMMS5-EBZ User Guide
==========================

For many Broadband Wireless Access (BWA) systems, Multi Input – Multi Output (`SIMO / MISO / SU-MIMO / MU-MIMO <https://en.wikipedia.org/wiki/MIMO>`_) operation and RF beamforming are proven techniques for maximizing throughput and efficient spectrum utilization. Modern integrated devices with multi-channel RX and multi-channel TX capability such as the AD9361 make developing MIMO systems with high performance and linearity utilizing integrated receivers, transmitters, and synthesizers a simpler task.

Some systems may require more complex configurations that combine multiple devices. Operating multiple devices while trying to coordinate data for each channel of each device is not practical for devices that operate independently without any mechanism for aligning data timing. Data synchronization into and out of multiple devices is required to implement such configurations. The :adi:`AD-FMComms5-EBZ` is a FMC board for the :adi:`AD9361`, a highly integrated RF Agile Transceiver™, which demonstrates how to design a platform based on multiple devices.

For MIMO systems requiring more than two input or two output channels, multiple
AD9361 devices and a common reference oscillator are required. The AD9361
provides the capability to accept an external reference clock and synchronize
operation with other devices using simple control logic. Each AD9361 includes
its own baseband PLL that generates sampling and data clocks from the reference
clock input, so an additional control mechanism is required to synchronize
multiple devices.

The complete chip level design package can be found on the :adi:`the ADI web site <ad9361_design_files>`. Information on the card, and how to use it, the design package that surrounds it, and the software which can make it work, can be found below in the Table of Contents.

The purpose of the AD-FMCOMMS5-EBZ is to provide a platform to which shows how to connect and synchronize (at the RF side) multiple AD9361s for `SIMO / MISO / SU-MIMO / MU-MIMO <https://en.wikipedia.org/wiki/MIMO>`_ applications. To help with algorithm array processing development, there are a variety of things that can be done, from purchasing complete solutions:

-  `MIMO receiver <https://www.xilinx.com/products/intellectual-property/do-di-mimoenc-lte.html>`_
-  `MIMO transmitter <https://www.xilinx.com/products/intellectual-property/ef-di-mimodec-lte.html>`_

To creating your own with something like `Phased Array System Toolbox <https://www.mathworks.com/products/phased-array/>`_.

If you are just starting a design, or investigating the AD9361 for the first time, it's suggested to get familiar with the single AD9361 based platforms (`ad-fmcomms2-ebz <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz>`_ or `ad-fmcomms3-ebz <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms3-ebz>`_) first.

Note that the AD-FMCOMMS5-EBZ uses a dual FMC connector. This means the base
board requires two adjacent FMC connectors. Suitable base boards for example are
ZC702 and ZC706.

Table of Contents
=================

`ad-fmcomms5-ebz.ashx <http://www.analog.com/-/media/analog/en/evaluation-board-images/images/ad-fmcomms5-ebz.ashx>`_

-  `Introduction <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`_
-  :doc:`FMCOMMS5 Hardware </solutions/reference-designs/fmcomms5/hardware>`: This provides a brief description of the AD-FMCOMMS5-EBZ board by itself, and is a good reference for those who want to understand a little more about the board. If you just want to use the board, you can skip this section, and come back to it when you want to incorporate the AD9361 into your product.

   -  :doc:`Hardware </solutions/reference-designs/fmcomms5/hardware>` (including :doc:`schematics </solutions/reference-designs/fmcomms5/hardware>`)

      -  `Functional Overview & Specifications <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/functional_overview>`_
      -  `Characteristics & Performance <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/card_specification>`_
      -  :doc:`Configuration options </solutions/reference-designs/fmcomms5/hardware/configuration_options>`

   -   `Production Testing Process <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/testing>`_

-  Use the AD-FMCOMMS5-EBZ Board to better understand the AD9361

   -  `What you need to get started <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`_
   -  `Quick Start Guides <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`_

      -  `Linux on ZC702, ZC706, ZED <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`_
      -  `Linux on KC705, VC707 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/microblaze>`_
      -  `Configure a pre-existing SD-Card <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
      -  `Update the old card you received with your hardware <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

   -  Linux Applications

      -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_
      -  `FMCOMMS5 Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms5_plugin>`_
      -  `FMCOMMS2/3/4/5 Advanced Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`_
      -  :doc:`FMComms5 Phase Sync Procedure </solutions/reference-designs/fmcomms5/phase-sync>`
      -  `Command Line/Shell scripts <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`_

   -  Push custom data into/out of the AD-FMCOMMS5-EBZ

      -  `Basic Data files and formats <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>`_
      -  `Create and analyze data files in MATLAB <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`_
      -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`_
      -  `AD9361 libiio streaming example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_

-  Design with the AD9361

   -  `Understanding the AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`_

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  `MATLAB Filter Design Wizard for AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`_

   -  Designing with multiple AD9361s.

      -  :doc:`Multi-Chip Sync(MCS) </solutions/reference-designs/fmcomms5/multi-chip-sync>`, synchronization of multiple devices

   -  Simulation

      -  `MathWorks SimRF Models of the AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`_

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`_
         -  `Beacon Frame Receiver Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`_
         -  `QPSK Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/qpsk_example>`_
         -  `LTE Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/lte_example>`_

      -  `GNU Radio <https://wiki.analog.com/resources/tools-software/linux-software/gnuradio>`_
      -  `FM Radio/Tuner <https://wiki.analog.com/resources/tools-software/fm-radio>`_ (listen to FM signals on the HDMI monitor)
      -  `C example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_

   -  Design a custom AD9361 based platform

      -  `Linux software <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`_

         -  `Linux Device Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`_
         -  `Build the demo on ZC702, ZC706, or ZED from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`_
         -  `Build the demo on KC705 or VC707 for Microblaze from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/microblaze>`_
         -  `Build the 2014_R2 Release Linux kernel from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2014r2>`_
         -  `Customizing the devicetree on the target <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`_

      -  `No-OS Driver <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`_
      -  `HDL Reference Design <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>`_ which you must use in your FPGA.

         -  `Digital Interface Timing Validation <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`_

-  Additional Documentation about SDR Signal Chains

   -  `The math behind the RF <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/math>`_
   -  `IQ rotation, and phase sync <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/iq_rotation>`_

-  `Help and Support <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_

Videos
======

.. note::

   See `ad-fmcomms2-ebz <https://wiki.analog.com/ad-fmcomms2-ebz#videos>`_

Presentations
=============

-  :adi:`Developing Multiple-Input Multiple-Output (MIMO) Systems with the AD9361 <en/education/education-library/webcasts/developing-multiple-input-multiple-output.html>` As Software Defined Radio (SDR) and Multiple-Input Multiple-Output (MIMO) become more prevalent there is a need for more channel diversity. This webcast will detail how to use multiple AD9361 devices to create an NxN MIMO system, as well as explore the available tradeoffs in the design. The AD9361 is a fully integrated 2x2 MIMO transceiver. Its programmability and wideband capability make it ideal for a broad range of transceiver applications.

Warning
-------

.. esd-warning::


.. toctree::
   :hidden:

   hardware
   hardware/configuration_options
   multi-chip-sync
   phase-sync
