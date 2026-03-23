.. _adrv9361z7035:

ADRV9361-Z7035
==============

.. image:: http://picozed.org/sites/default/files/styles/product_slider/public/product/hand.png
   :alt: http://picozed.org/sites/default/files/styles/product_slider/public/product/hand.png
   :align: right

The :adi:`ADRV9361-Z7035` is built on a portfolio of highly integrated
System-On-Module (SOMs) based on the Xilinx Zynq®-7000 All Programmable (AP)SoC.
Starting with the AD9361, it is schematically & HDL similar to the
:external+hdl:ref:`AD-FMCOMMS3-EBZ <fmcomms2>`.

The purpose of the :adi:`ADRV9361-Z7035` RF SOM is to provide an RF platform to
software developers, system architects, product developers, etc, who want a
single platform operating over a wide tuning range (70 MHz - 6 GHz) that is
capable of being used for prototype, evaluation and reference design to help
with production volume.

.. toctree::
   :hidden:

   introduction
   prerequisites
   mechanical
   electrical-specifications
   performance
   quickstart
   revision-history

Table of Contents
-----------------

- :dokuwiki:`Introduction to the AD9361. <resources/eval/user-guides/ad9361>`
- :dokuwiki:`Introduction <resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`
- :dokuwiki:`Tuning the system <resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tuning>`
- ADRV9361-Z7035 Hardware

   -  :ref:`Introduction <adrv9361z7035 introduction>`
   -  :ref:`Prerequisites <adrv9361z7035 prerequisites>`
   -  :ref:`Quick Start <adrv9361z7035 quickstart>`
   -  :ref:`Mechanical Design <adrv9361z7035 mechanical>`
   -  :ref:`Electrical Specifications <adrv9361z7035 electrical_specifications>`
   -  :ref:`Performance <adrv9361z7035 performance>`

      -  :dokuwiki:`Power and Sequencing <resources/eval/user-guides/pzsdr/power-and-sequencing>`

   -  :ref:`Revision History <adrv9361z7035 revision_history>`

      -  including schematics and BOM

   -  Carriers

      -  :dokuwiki:`FMC Carrier (PZSDRCC-FMC) <resources/eval/user-guides/pzsdr/carriers/fmc>`
      -  :dokuwiki:`Breakout Carrier (PZSDRCC-BRK) <resources/eval/user-guides/pzsdr/carriers/brk>`
      -  :dokuwiki:`PCIe Carrier (PZSDRCC-PCIE) <resources/eval/user-guides/pzsdr/carriers/pcie>`
      -  :dokuwiki:`PackRF Carrier (PZSDRCC-PackRF) <resources/eval/user-guides/pzsdr/carriers/packrf>`

- Use the RF SOM Hardware to better understand the AD9361

   -  :dokuwiki:`What you need to get started <resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`
   -  :dokuwiki:`Quick Start Guides <resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`

      -  :dokuwiki:`Linux on RF SOM <resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`
      -  :dokuwiki:`Configure a pre-existing SD-Card <resources/tools-software/linux-software/kuiper-linux>`
      -  :dokuwiki:`Update the old card you received with your hardware <resources/tools-software/linux-software/kuiper-linux>`

   -  Basic Applications

      -  :dokuwiki:`IIO Scope <resources/tools-software/linux-software/iio_oscilloscope>`
      -  :dokuwiki:`AD9361 Control IIO Scope Plugin <resources/tools-software/linux-software/fmcomms2_plugin>`
      -  :dokuwiki:`AD9361 Advanced Control IIO Scope Plugin <resources/tools-software/linux-software/fmcomms2_advanced_plugin>`
      -  :dokuwiki:`Command Line/Shell scripts <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`

   -  Push custom data into/out of the RF SOM SDR.

      -  :dokuwiki:`Basic Data files and formats <resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>`
      -  :dokuwiki:`Create and analyze data files in MATLAB <resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`
      -  :dokuwiki:`Stream data into/out of MATLAB <resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
      -  :dokuwiki:`AD9361 libiio streaming example <resources/tools-software/linux-software/libiio>`

- Design with the AD9361

   -  :dokuwiki:`Understanding the AD9361 <resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  :dokuwiki:`MATLAB Filter Design Wizard for AD9361 <resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`

   -  Simulation

      -  :dokuwiki:`MathWorks RF Blockset Models of the AD9361 <resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  :dokuwiki:`Stream data into/out of MATLAB <resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         -  :dokuwiki:`Beacon Frame Receiver Example <resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`
         -  :dokuwiki:`QPSK Transmit and Receive Example <resources/tools-software/linux-software/libiio/clients/qpsk_example>`
         -  :dokuwiki:`LTE Transmit and Receive Example <resources/tools-software/linux-software/libiio/clients/lte_example>`
         -  :dokuwiki:`ADS-B Airplane Tracking Example <resources/tools-software/linux-software/libiio/clients/adsb_example>`

      -  :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
      -  :dokuwiki:`FM Radio/Tuner <resources/tools-software/fm-radio>` (listen to FM signals on the HDMI monitor)
      -  :dokuwiki:`C example <resources/tools-software/linux-software/libiio>`

   -  Targeting

      -  :dokuwiki:`Analog Devices BSP for MathWorks HDL Workflow Advisor <resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`

   -  Complete Workflow

      -  :dokuwiki:`ADS-B Airplane Tracking Tutorial <resources/eval/user-guides/picozed_sdr/tutorials/adsb>`
      -  :dokuwiki:`QPSK Modem Design Workflow <resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp_modem>`

   -  Design a custom AD9361 based platform

      -  :dokuwiki:`Linux software <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`

         -  Linux resources:

            - :external+linux:ref:`Linux AD9361 Device Driver <ad9361>`
            - :external+linux:ref:`Linux AD9361 Device Driver Customization <ad9361-customization>`

         -  :ref:`Building Zynq Linux kernel and devicetree <linux-kernel zynq>`
         -  :dokuwiki:`Customizing the devicetree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

      -  :dokuwiki:`No-OS Driver <resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`
      -  :external+hdl:ref:`HDL Reference Design <adrv9361z7035>` which you must
         use in your FPGA.

         -  :dokuwiki:`Digital Interface Timing Validation <resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`

- Additional Documentation about SDR Signal Chains

   -  :dokuwiki:`The math behind the RF <resources/eval/user-guides/ad-fmcomms1-ebz/math>`

- :dokuwiki:`Help and Support <resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`
- Videos and Webinars

   -  `Radio Deployment on SoC Platforms <https://www.mathworks.com/videos/radio-deployment-on-soc-platforms-1513346830203.html>`_

Warning
-------

.. esd-warning::
