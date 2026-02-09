Just Enough Software and HDL for High-Speed Designs
===================================================

This workshop goes through the software tools typically used 
when working with the ADALM Pluto board, demonstrating its versatility 
and showing hands-on exercises to get you up and running quickly.

This workshop was presented at the 2023 FTC.

Slide Deck and Booklet
----------------------

Since this tutorial is also designed to be presented as a live, hands-on
workshop, a slide deck is provided here:

.. admonition:: Download

   :download:`SDR Lab Slide Deck <Train_Just enough Software and HDL for High Speed designs.pdf>`

A complete booklet of the hands-on activity is also provided, as a companion to
following the tutorial yourself:

.. admonition:: Download

   :download:`SDR Lab Booklet <instructions_sdr_lab.pdf>`

.. The source code for the hands-on exercises is provided here:
..
.. .. admonition:: Download
..
..    :download:`SDR Lab Source Code <sdr_lab_source_code.zip>`
..
.. The SD Card image for the hands-on exercises is provided here:
..
.. .. admonition:: Download
..
..    :download:`SDR Lab Image <SDR_Lab_Image.zip>`

.. contents:: Workshop Contents
   :local:
   :depth: 3


Prerequisites
~~~~~~~~~~~~~

**Hardware Requirements**:

* ADALM-PLUTO SDR board (provided in workshop kit)
* USB cable (provided)
* SMA cables for loopback connections (provided)
* Two antennas for wireless experiments (provided)
* PC/Laptop with USB port

**Software Requirements**:

The workshop SD card image provides all necessary software pre-installed. If setting up your own environment, you will need:

* Python 3.7 or newer
* PyADI-IIO library
* GNU Radio 3.8 or newer with gr-iio blocks
* IIO Oscilloscope (optional, for visualization)
* libiio library

**Recommended Background Knowledge**:

* **Basic DSP Concepts**: 
  
  * Understanding of sampling, frequency, and time domain
  * Familiarity with I/Q (In-phase/Quadrature) signals
  * Basic knowledge of filtering

* **Programming**:
  
  * Basic Python programming skills
  * Familiarity with NumPy and Matplotlib is helpful

* **Communications Fundamentals**:
  
  * Understanding of modulation concepts
  * Basic radio frequency (RF) concepts

**Prior experience with GNU Radio or MATLAB is helpful but not required.** The workshop provides step-by-step instructions for all exercises.


Learning Objectives
~~~~~~~~~~~~~~~~~~~

By the end of this workshop, you will have a solid understanding of:

#. Typical customer design flow
#. Software in the Design-in Journey
#. Evaluation, test and analysis
#. Algorithmic development, modeling and prototyping
#. Building blocks for development and new revenue streams
#. Common architecture patterns used for easy transition between platforms

Analysis, control and evaluation tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. (ACE) Software
#. IIO Oscilloscope
#. Scopy
#. qIQ Receiver
#. MATLAB Simulink

Hands-on exercises
~~~~~~~~~~~~~~~~~~

By the end of this workshop, you will:

#. Understand why traditional MCU SPI controllers limit converter performance
#. Learn the SPI Engine Framework architecture and components
#. Build a complete AD7984 precision converter system
#. Compare regular SPI vs. SPI Engine performance metrics
#. Achieve near-datasheet performance with proper FPGA integration


Introduction
------------

Software Defined Radio (SDR)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Defined Radio represents a fundamental shift from traditional radio architectures. Unlike conventional radios that are optimized for specific applications using fixed hardware (Super Heterodyne architecture), SDR systems are reconfigurable and multipurpose, leveraging software to define radio functionality.

**What Makes a Radio "Software Defined"?**

A true SDR system features:

* **Zero-IF architecture**: Direct conversion receiver/transmitter architecture
* **Software-based signal processing**: Most signal processing tasks are performed in software rather than dedicated hardware
* **Reconfigurability**: The same hardware can be reprogrammed for different applications and protocols

**Why Use SDR?**

Modern SDR designs address multiple challenges in radio system development:

#. **Complexity Management**: Radio development requires expertise across multiple domains:
   
   * RF hardware design
   * Digital hardware (FPGA/ASIC)
   * DSP algorithms
   * Software engineering
   * System-on-Chip (SoC) assembly
   * Communications theory

#. **Reduced Development Time**: By moving functionality to software, SDR enables:
   
   * Faster prototyping and iteration
   * Algorithm development in familiar tools (MATLAB, Python, GNU Radio)
   * Testing and verification with real hardware in the loop

#. **System Flexibility**: The same SDR hardware can support multiple applications:
   
   * Communications systems (GSM, Wi-Fi, LTE)
   * Radar systems (Doppler, FMCW)
   * Spectrum analysis
   * Signal intelligence (SIGINT)

#. **Reduced System Complexity and Cost**: 
   
   * Hardware reuse across different applications
   * Software updates instead of hardware redesigns
   * Lower prototyping costs

The Industrial I/O (IIO) Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This workshop leverages Analog Devices' IIO framework, which provides:

* **Hardware Abstraction**: Unified interface across different ADI converter and transceiver products
* **Cross-Platform Support**: Works on Linux, Windows, and macOS
* **Network Transparency**: Control hardware locally or remotely over TCP/IP, USB, or Serial
* **Language Bindings**: Program in C, C++, Python, MATLAB, or C#
* **Efficient Data Transport**: High-speed DMA-based buffering for continuous data streaming

Common Architecture for Platform Portability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the key advantages demonstrated in this workshop is the ability to reuse the same software, HDL (Hardware Description Language), and tools across different platforms:

**Platform Progression**:

#. **ADALM-PLUTO** (Entry Level)
   
   * AD9363 transceiver
   * Zynq-7010 FPGA
   * USB connectivity
   * Ideal for learning and algorithm development

#. **Jupiter SDR** (Mid-Range)
   
   * ADRV9002 dual transceiver
   * ZynqMP-ZU3EG
   * Higher bandwidth and performance
   * Ethernet and USB3 connectivity

#. **Production Platforms** (High-End)
   
   * ADRV9009, AD9081/AD9082 (MxFE)
   * Larger FPGAs (ZU11EG, VCU118, etc.)
   * Multi-channel systems
   * Full production capabilities

All platforms share:

* Common HDL IP cores from https://github.com/analogdevicesinc/hdl
* Common Linux kernel and drivers from https://github.com/analogdevicesinc/linux  
* Same software libraries (libIIO, PyADI-IIO)
* Compatible with MATLAB, Simulink, GNU Radio

This common architecture enables you to:

* Develop and validate algorithms on low-cost hardware (ADALM-PLUTO)
* Transition smoothly to higher-performance platforms
* Reuse code from prototype to production
* Minimize learning curve between platforms
