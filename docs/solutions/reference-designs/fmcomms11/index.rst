AD-FMCOMMS11-EBZ User Guide
===========================

The AD-FMComms11-EBZ board is a system platform board for communication infrastructure applications that demonstrates the Direct to RF (DRF) transmitter and observation receiver architecture. Using high sample rate RFDAC(s) and RFADC(s), a number of components in previous generation transmitters can be eliminated, such as mixers, modulators, IF amplifiers and filters. The objective being to bring the ADC or DAC as close to the antenna as possible, leading to possibly more cost effective and efficient communications solution. It is composed of multi-GSps RF ADC :adi:`AD9625` and DAC :adi:`AD9162`, Cheetah and Barium respectively. The transmit path contains a balun, low pass filter, gain block and variable attenuation to produce an output appropriate for a power amplifier module. Along the observation path, the PA output is coupled back into the board through a variable attenuator, a balun and finally the ADC. Clock management is taken care of on board; all the necessary clocks are generated from a reference. Power management is present as well. We will provide typical performance data for the entire range (70 MHz – 6 GHz) which is supported by the platform. This is primarily for system investigation and bring up of various waveforms from a software team before their custom hardware is complete, where they want to see waveforms, but are not concerned about the last 1dB or 1% EVM of performance.

.. image:: images/fmcomms11_image.png
   :align: center
   :width: 600

Table of Contents
-----------------

-  :doc:`Introduction </solutions/reference-designs/fmcomms11/introduction>`
-  :doc:`FMCOMMS11 Hardware </solutions/reference-designs/fmcomms11/hardware>`: This provides a brief description of the AD-FMCOMMS11-EBZ board by itself, and is a good reference for those who want to understand a little more about the board. If you just want to use the board, you can skip this section, and come back to it when you want to incorporate one of the devices into your product.

   -  :doc:`Hardware </solutions/reference-designs/fmcomms11/hardware>` (including :doc:`schematics </solutions/reference-designs/fmcomms11/hardware>`)

      -  :doc:`Functional Overview & Specifications </solutions/reference-designs/fmcomms11/hardware/functional_overview>`
      -  :doc:`Characteristics & Performance </solutions/reference-designs/fmcomms11/hardware/card_specification>`
      -  :doc:`Configuration options </solutions/reference-designs/fmcomms11/hardware/configuration_options>`
      -  :doc:`FCC or CE certification </solutions/reference-designs/fmcomms11/certification>`

   -  :doc:`Production Testing Process </solutions/reference-designs/fmcomms11/testing>`

-  Use the AD-FMCOMMS11-EBZ Board to better understand the :adi:`AD9625` and :adi:`AD9162`

   -  :doc:`What you need to get started </solutions/reference-designs/fmcomms11/prerequisites>`
   -  `Quick-Start Guides <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms11-ebz/quickstart>`_

      -  :doc:`Linux on ZC706 </solutions/reference-designs/fmcomms11/quickstart/zynq>`
      -  `Configure a pre-existing SD-Card <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
      -  `Update the old card you received with your hardware <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

   -  Linux Applications

      -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_

         -  `FMCOMMS11 Control in the IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms11_plugin>`_

   -  :doc:`HDL reference design </solutions/reference-designs/fmcomms11/reference_hdl>`

-  Design with the FMCOMMS11’s AD9625 and AD9162

   -  Understanding the FMCOMMS11

      -  :adi:`AD9162 Product page <AD9162>`
      -  :adi:`AD9625 Product page <AD9625>`

-  `Help and Support <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_

ADI Articles
------------

-   Four Quick Steps to Production: Using Model-Based Design for
    Software-Defined Radio

   -  :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
   -  :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
   -  :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
   -  :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

ADI Videos
----------

-  :adi:`Silent Switcher µModule Regulators Powering GSPS Sampling ADC <en/products/ad9625.html#product-recommendations>`

MathWorks Webinars
------------------

-  `Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <https://www.mathworks.com/videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`_
-  `Getting Started with Software-Defined Radio using MATLAB and Simulink <https://www.mathworks.com/videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`_

Warning
-------

.. esd-warning::


.. toctree::
   :hidden:

   certification
   fmcomms11_plugin
   hardware
   hardware/card_specification
   hardware/configuration_options
   hardware/functional_overview
   introduction
   prerequisites
   quickstart/zynq
   reference_hdl
   testing
