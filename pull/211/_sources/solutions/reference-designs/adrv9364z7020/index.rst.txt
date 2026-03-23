ADRV9364-Z7020 System on Module (SOM) SDR
=========================================

.. image:: images/aes-z7pz-sdr1-g-front.jpg
   :align: right
   :width: 400

The :adi:`ADRV9364 <en/products/rf-microwave/integrated-transceivers-transmitters-receivers/wideband-transceivers-ic/adrv9364.html#product-samplebuy>` is built on a portfolio of highly integrated System-On-Module (SOMs) based on the Xilinx Zynq®-7000 All Programmable (AP)SoC. Built on the AD9364, it is schematically & HDL similar to the `ad-fmcomms4-ebz <https://wiki.analog.com/ad-fmcomms4-ebz>`_.

The purpose of the SDR is to provide an RF platform to software developers, system architects, product developers, etc, who want a single platform which operates over a wide tuning range (70 MHz – 6 GHz) that is capable of being used for prototyping, evaluation, and as a reference design to help with production volume.

Table of Contents
-----------------

-  :adi:`Purchase <en/products/rf-microwave/integrated-transceivers-transmitters-receivers/wideband-transceivers-ic/ADRV9364.html>`
-  `Introduction <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`_
-  `RF SOM Hardware <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/hardware>`_
-  `Tuning the system <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tuning>`_
-  Use the PicoZed SDR Hardware to better understand the AD9364

   -  `What you need to get started <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`_
   -  `Quick Start Guides <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`_

      -  `Linux on PicoZed SDR <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`_
      -  `Configure a pre-existing SD-Card <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
      -  `Update the old card you received with your hardware <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

   -  Linux Applications

      -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_
      -  `PicoZed SDR Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_plugin>`_
      -  `PicoZed SDR Advanced Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`_
      -  `Command Line/Shell scripts <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`_

   -  Push custom data into/out of the PicoZed SDR.

      -  `Basic Data files and formats <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>`_
      -  `Create and analyze data files in MATLAB <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`_
      -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`_
      -  `AD9361 libiio streaming example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_
      -  `Python Support with AD9364 Interface Class <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_

-  Design with the AD9364

   -  `Understanding the AD9364 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`_

      -  :adi:`AD9364 Product page <AD9364>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  `MATLAB Filter Design Wizard for AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`_

   -  Simulation

      -  `MathWorks SimRF Models of the AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`_

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`_
         -  `Beacon Frame Receiver Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`_
         -  `QPSK Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/qpsk_example>`_
         -  `LTE Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/lte_example>`_
         -  `ADS-B Airplane Tracking Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/adsb_example>`_

      -  `GNU Radio <https://wiki.analog.com/resources/tools-software/linux-software/gnuradio>`_
      -  `FM Radio/Tuner <https://wiki.analog.com/resources/tools-software/fm-radio>`_ (listen to FM signals on the HDMI monitor)
      -  `C example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_

   -  Targeting

      -  `Analog Devices BSP for MathWorks HDL Workflow Advisor <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`_

   -  Complete Workflow

      -  `ADS-B Airplane Tracking Tutorial <https://wiki.analog.com/resources/eval/user-guides/picozed_sdr/tutorials/adsb>`_

   -  Design a custom AD9364 based platform

      -  `Linux software <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`_

         -  `Linux Device Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`_
         -  `Build the demo on ZC702, ZC706, or ZED from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`_
         -  `Build the demo on KC705 or VC707 for Microblaze from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/microblaze>`_
         -  `Build the 2014_R2 Release Linux kernel from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2014r2>`_
         -  `Customizing the devicetree on the target <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`_

      -  `No-OS Driver <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`_
      -  `HDL Reference Design <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>`_ which you must use in your FPGA.

         -  `Digital Interface Timing Validation <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`_

-  `Additional Documentation about SDR Signal Chains <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/additional_docs>`_

   -  `The math behind the RF <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/math>`_

-  `Help and Support <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_

Warning
-------

.. esd-warning::
