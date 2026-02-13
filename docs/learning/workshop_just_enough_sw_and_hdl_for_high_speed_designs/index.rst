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

The source code for the hands-on exercises is provided here:

.. admonition:: Download

   :download:`SDR Lab Source Code <workshop_exercises.zip>`

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

#. Typical customer design flow - Progressive stages from research to production
#. Software in the Design-in Journey - Single cohesive solution meeting customers in their preferred tools
#. Evaluation, test and analysis - Product evaluation to confirm converter performance
#. Algorithmic development, modeling and prototyping - Plug 'n' Play prototyping with 10-15 minute setup
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


Typical customer design flow
----------------------------

Software-defined radio development follows a progressive, stage-based approach that takes designs from initial research through to production deployment. The key advantage of ADI's approach is that the **same HDL, software, and infrastructure components are used throughout the entire flow**, reducing the learning curve and development risk at each stage.

.. figure:: images/customer_design_flow.png
   :alt: Customer Design Flow
   :align: center

   Typical Customer Design Flow

Design Flow Stages
~~~~~~~~~~~~~~~~~~

The typical customer design flow consists of 5 progressive stages, each building upon the previous one while leveraging the same tools, HDL, and software infrastructure throughout.

**1. Research**

In the research phase, engineers validate that the chosen ADI device meets application requirements through simulation and measurement. Key activities include:

* **Behavioral Simulation**: Model the system before building hardware
* **Device Evaluation**: Test actual hardware performance using evaluation boards
* **Measurements**: Characterize critical performance metrics such as SFDR (Spurious-Free Dynamic Range), SNR (Signal-to-Noise Ratio), EVM (Error Vector Magnitude), NF (Noise Figure), and NSD (Noise Spectral Density)

Tools used: Evaluation boards, IIO Oscilloscope, ACE software, bench test equipment.

**2. Algorithm Development**

During algorithm development, engineers implement signal processing algorithms using high-level languages while streaming real data from hardware:

* **MATLAB/Python/GRC Reference Implementation**: Develop algorithms in familiar environments
* **Hardware Streaming**: Stream live data from ADI hardware for validation
* Iterate quickly using interpreted languages and interactive tools
* Validate performance with realistic signal conditions and impairments

Development environments: MATLAB/Simulink with ADI toolboxes, Python with PyADI-IIO, GNU Radio Companion with gr-iio blocks.

**3. Design Elaboration**

The design elaboration phase refines algorithms for embedded deployment through modeling and optimization:

* **Modeling**: Create bit-accurate models of algorithms
* **MATLAB/Python/GRC**: Continue using the same development tools
* **Hardware Streaming**: Validate optimized algorithms with real hardware data
* **Data Type Conversion**: Transition from floating-point to fixed-point arithmetic for efficient hardware implementation

Critical considerations include fixed-point precision, filter coefficient quantization, timing budgets, and FPGA resource utilization.

**4. Prototype**

In the prototype stage, algorithms are deployed to development hardware for integration and optimization:

* **Deployment to Development Board**: Move from simulation to actual hardware (PlutoSDR, Jupiter, or FMC evaluation boards)
* **Design Optimization**: Tune for performance and resource efficiency
* **HDL Integration**: Integrate custom signal processing with ADI reference designs
* **Driver Integration**: Ensure software can control and stream data from the hardware

This stage validates the complete system on development platforms that closely resemble production hardware.

**5. Production**

The final production stage involves deployment to custom hardware with complete system validation:

* **Deployment to Custom Hardware**: Deploy to production platforms (custom boards, System-on-Module, or chip-down designs)
* **Validation with Complete Hardware Solution**: Comprehensive testing with production-representative configurations
* Environmental and reliability testing
* Manufacturing test procedures finalization

Throughout all stages, the same HDL IP cores, Linux kernel drivers, and application software are reused, dramatically reducing development risk and time-to-market.

Platform Progression Path
~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI provides a clear progression of platforms that support the entire design flow, from initial research through production deployment. The key advantage is that **the same HDL, software, and tools work across all platforms**, enabling smooth transitions as your project matures.

.. list-table:: ADI Platform Comparison
   :header-rows: 1
   :widths: 20 15 15 15 15 20

   * - Platform
     - Device
     - FPGA
     - Connectivity
     - RF Bandwidth
     - Design Flow Stages
   * - ADALM-PLUTO
     - AD9363
     - Zynq-7010
     - USB 2.0
     - Up to 20 MHz
     - Research, Algorithm Development
   * - Jupiter SDR
     - ADRV9002 (2×)
     - ZynqMP-ZU3EG
     - USB3, Ethernet
     - Up to 40 MHz
     - Algorithm Development, Design Elaboration
   * - MxFE Boards
     - AD9081/AD9082
     - ZCU102, VCU118, etc.
     - PCIe, Ethernet
     - 200+ MHz
     - Design Elaboration, Prototype
   * - ADRV9009-ZU11EG
     - ADRV9009 (2×)
     - ZynqMP-ZU11EG
     - Ethernet, Custom
     - Up to 200 MHz
     - Prototype, Production
   * - Custom Designs
     - Any ADI device
     - Customer choice
     - Application-specific
     - Varies
     - Production

All platforms share the same HDL IP cores (https://github.com/analogdevicesinc/hdl), Linux kernel drivers (https://github.com/analogdevicesinc/linux), and software libraries (PyADI-IIO, MATLAB toolboxes), enabling seamless code reuse across the development progression.


Software in the Design-in Journey
----------------------------------

ADI's software ecosystem provides a cohesive solution across the entire design-in journey, supporting multiple development environments while maintaining a common underlying infrastructure. The ecosystem enables engineers to work in their preferred tools—whether GUI-based applications, scripting environments, or modeling platforms—all leveraging the same drivers, libraries, and hardware abstraction layers.

**Common Software Infrastructure:**

* **libiio**: Cross-platform library providing unified hardware access
* **IIO Kernel Drivers**: Linux drivers for ADI converters and transceivers
* **iiod Server**: Network-transparent access to hardware
* **Language Bindings**: Support for C, C++, Python, MATLAB, and more

**Development Tools and Environments:**

* **IIO Oscilloscope**: GUI application for quick visualization and device control
* **MATLAB/Simulink**: ADI toolboxes for algorithm development and modeling
* **Python/Jupyter**: PyADI-IIO library with NumPy/SciPy integration
* **GNU Radio**: gr-iio blocks for flowgraph-based development
* **ACE Software**: Analysis, Control, and Evaluation tools
* **Scopy**: Advanced measurement and analysis platform

This single cohesive software solution meets customers in their ecosystem or at their tools of choice, ensuring the same underlying infrastructure supports rapid prototyping, algorithm development, and production deployment.


Evaluation, Test and Analysis
-----------------------------

**Product Evaluation** focuses on using hardware and software components to confirm that the converter meets application needs.

.. figure:: images/sw_solution.png
   :alt: Software Solution Architecture
   :align: center

   Single cohesive software solution supporting multiple user personas and tools

* Using evaluation boards and software tools to verify device performance
* Characterizing key metrics (SFDR, SNR, EVM, NF, NSD)
* Time investment is (very roughly) proportional to complexity and how application specific it needs to be

**Tools:** IIO Oscilloscope, ACE software, Scopy, bench test equipment


Algorithmic Development, Modeling and Prototyping
-------------------------------------------------

**Product Prototyping** provides Plug 'n' Play hardware and software to see the key features and performance of the part.

* Configure, capture signals, or generate waveforms in 10-15 minutes
* Stream real data from hardware into development environments (MATLAB, Python, GNU Radio)
* Develop and validate algorithms with hardware-in-the-loop

**Development Environments:** MATLAB/Simulink, Python/PyADI-IIO, GNU Radio Companion


Common Architecture for Easy Platform Transition
-------------------------------------------------

The common architecture across ADI's platforms makes it easy to transition between hardware as your project evolves from prototype to production.

.. figure:: images/commonarchmakesiteasytotransformbetweenplatforms.png
   :alt: Common Architecture Makes It Easy to Transition Between Platforms
   :align: center

   Common architecture enables seamless transitions between platforms

**Shared Software and HDL Stack:**

* **Same libraries**: libiio, PyADI-IIO, and hardware drivers work across all platforms
* **Common Linux image**: ADI Kuiper Linux brings up the same software stack whether on a laptop or embedded board
* **Unified HDL**: Common FPGA designs across all SDR platforms
* **Consistent drivers**: Same drivers whether accessing hardware locally or via USB

**Platform Progression:**

* **Start with ADALM-PLUTO**: Provides quick verification, rapid algorithm development, and SIGINT applications at very low cost
* **Scale to production**: Same software and HDL seamlessly transfer to higher-performance platforms
* **Use modules for clean design**: Leverage ADI's reference designs and IP cores

**Open Source Repositories:**

* Common Linux kernel and drivers: https://github.com/analogdevicesinc/linux
* Common HDL IP cores: https://github.com/analogdevicesinc/hdl

This architecture ensures that code developed on entry-level hardware like ADALM-PLUTO can be reused on production platforms with minimal changes, dramatically reducing development risk and time-to-market.


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
