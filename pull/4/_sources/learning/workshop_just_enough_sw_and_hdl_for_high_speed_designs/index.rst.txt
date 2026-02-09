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


Typical Customer Design Flow
-----------------------------

Software-defined radio development follows a progressive, stage-based approach that takes designs from initial research through to production deployment. The key advantage of ADI's approach is that the **same HDL, software, and infrastructure components are used throughout the entire flow**, reducing the learning curve and development risk at each stage.

Design Flow Stages
~~~~~~~~~~~~~~~~~~

1. Research Phase
^^^^^^^^^^^^^^^^^

In the initial research phase, engineers focus on understanding device capabilities and validating that the chosen converter or transceiver meets application requirements.

**Key Activities:**

* **Behavioral Simulation**: Model the system before building hardware
* **Device Evaluation**: Test actual hardware performance
* **Measurements**: Characterize key metrics

  * SFDR (Spurious-Free Dynamic Range)
  * SNR (Signal-to-Noise Ratio)
  * EVM (Error Vector Magnitude)
  * NF (Noise Figure)
  * NSD (Noise Spectral Density)

**Tools:** Evaluation boards, IIO Oscilloscope, ACE software, bench test equipment

2. Algorithm Development
^^^^^^^^^^^^^^^^^^^^^^^^

Once the hardware is validated, development shifts to implementing the signal processing algorithms that define your application's functionality.

**Key Activities:**

* Develop reference implementations in high-level languages
* Stream real data from hardware for algorithm validation
* Test algorithms with realistic signal conditions
* Iterate quickly using familiar development environments

**Tools and Languages:**

* **MATLAB/Simulink**: For engineers familiar with MathWorks ecosystem
* **Python**: Using PyADI-IIO for streamlined hardware access
* **GNU Radio Companion (GRC)**: For visual flowgraph-based development

**Hardware Streaming:** All platforms support continuous data streaming to development workstations, enabling hardware-in-the-loop algorithm validation.

3. Design Elaboration
^^^^^^^^^^^^^^^^^^^^^

With proven algorithms, this phase focuses on refining the implementation for target hardware deployment.

**Key Activities:**

* **Modeling**: Create bit-accurate models of algorithms
* **Data Type Conversion**: Move from floating-point to fixed-point arithmetic
* **Performance Optimization**: Optimize for latency, throughput, and resource usage
* **Hardware Streaming**: Continue testing with real hardware data

**Critical Considerations:**

* Fixed-point precision requirements
* Filter coefficient quantization effects
* Timing and latency budgets
* FPGA resource utilization

4. Prototype
^^^^^^^^^^^^

The prototype phase involves deploying your design to development hardware that closely resembles the production system.

**Key Activities:**

* **Deployment to Development Board**: Move from simulation to hardware
* **Design Optimization**: Tune for performance and resource efficiency
* **HDL Integration**: Integrate custom processing with ADI reference designs
* **Driver Integration**: Ensure software can control and stream data from hardware

**Platform Options:**

* **PlutoSDR/Jupiter**: For initial prototyping and validation
* **FMC Evaluation Board + FPGA Carrier**: For more complex systems
* **Custom Development Board**: For production-representative hardware

**HDL Integration Points:**

ADI's reference designs provide clear integration points where you can insert custom signal processing blocks between the ADC/DAC interface and the DMA subsystem.

5. Production
^^^^^^^^^^^^^

The final stage involves deploying to production hardware with full system validation.

**Key Activities:**

* Deploy to custom hardware platform
* Complete system validation with production-representative configurations
* Validate environmental and reliability requirements
* Finalize manufacturing test procedures

**Platform Options:**

* **System-on-Module (SOM)**: Integrated solutions like ADRV9009-ZU11EG
* **Custom Chip-Down Design**: Full custom hardware using same IP cores and drivers

Platform Progression Path
~~~~~~~~~~~~~~~~~~~~~~~~~~

The beauty of this design flow is that you can start small and scale up while reusing your work:

.. code-block:: text

   PlutoSDR/JupiterSDR → Evaluation Board + FMC → Full Custom Design
   (Algorithm Dev)        (Prototyping)            (Production)

**All stages use:**

* Same HDL IP cores from https://github.com/analogdevicesinc/hdl
* Same Linux kernel drivers from https://github.com/analogdevicesinc/linux
* Same application software (MATLAB/Python/GNU Radio code)
* Same development tools (Vivado, IIO ecosystem)

This consistency dramatically reduces development risk and enables rapid iteration.


Software in the Design-in Journey
----------------------------------

ADI's software strategy recognizes that different engineers have different needs at different stages of the design journey. The ecosystem provides a **single cohesive software solution** that meets customers in their preferred development environment while maintaining consistency across the entire workflow.

User Personas and Their Needs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The software ecosystem addresses four distinct user personas, each with increasing technical depth and time investment requirements:

1. Analog Engineer (Evaluation & Research)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Primary Need:** "Configure, capture, and analyze data as quickly and simply as possible"

**Typical Use Case:** Initial device evaluation to confirm the converter or transceiver meets application requirements.

**Time Investment:** Minutes to hours

**Tools:**

* **Hardware:** Evaluation board with pre-configured firmware
* **Software:**

  * IIO Oscilloscope for quick data visualization
  * ACE (Analysis | Control | Evaluation) software
  * Scopy for advanced measurements

**Key Feature:** Zero setup time - connect board via USB and start capturing data immediately.

2. Modeling/Domain Expert (Algorithm Development)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Primary Need:** "Model and process data using familiar tools"

**Typical Use Case:** Develop and validate signal processing algorithms using captured data from real hardware.

**Time Investment:** Days to weeks

**Tools:**

* **MATLAB/Simulink:**

  * ADI-TRX Toolbox (Transceiver Toolbox)
  * ADI-HSX Toolbox (High-Speed Converter Toolbox)
  * ADI-SENSOR Toolbox (IMU/sensor interfaces)
  * ADI-TOF Toolbox (Time-of-Flight applications)

* **Python:**

  * PyADI-IIO library for hardware abstraction
  * NumPy, SciPy, Matplotlib for DSP and visualization

* **GNU Radio:**

  * gr-iio plugin for ADI hardware
  * Visual flowgraph development with GRC

**Key Feature:** Stream data directly from hardware into familiar development environments - no need to learn new tools.

3. Embedded Software Engineer (Prototyping)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Primary Need:** "Target more representative hardware and software configurations"

**Typical Use Case:** Deploy algorithms to embedded processors, optimize for resource constraints, integrate with application firmware.

**Time Investment:** Weeks to months

**Tools and Components:**

* **Firmware Applications:**

  * Reference applications showing driver usage
  * Example configurations for common use cases

* **Linux Support:**

  * ADI Kuiper Linux distribution
  * Pre-configured kernel with IIO drivers
  * Device tree examples

* **Embedded Frameworks:**

  * tinyIIO for microcontroller integration
  * ARM mbed support
  * STM32 integration examples

**Key Feature:** Transition from desktop development to embedded targets while maintaining same IIO abstraction layer.

4. Embedded Software & Digital HDL Engineers (Production)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Primary Need:** "Implement the software and/or digital interface with host MCU/FPGA"

**Typical Use Case:** Production-ready implementation with custom hardware, optimized drivers, and FPGA integration.

**Time Investment:** Months

**Tools and Components:**

* **No-OS Drivers:**

  * Bare-metal device drivers
  * Minimal footprint for resource-constrained MCUs
  * Example applications

* **Linux Kernel Drivers:**

  * Mainline kernel IIO subsystem
  * ADI-specific device drivers
  * Source code access for customization

* **HDL (Hardware Description Language):**

  * Reference designs for all ADI parts
  * Modular IP cores (JESD204, DMA, ADC/DAC interfaces)
  * Vivado/Quartus projects
  * Integration guides

**Key Feature:** Full access to source code at all levels - kernel drivers, HDL, and bare-metal firmware.

Software Architecture Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All these personas are served by a common software architecture based on the **Industrial I/O (IIO) framework**:

**Architecture Layers:**

.. code-block:: text

   ┌─────────────────────────────────────────────────────┐
   │  Application Layer                                   │
   │  (MATLAB, Python, GNU Radio, Custom Apps)           │
   └──────────────────────┬──────────────────────────────┘
                          │
   ┌──────────────────────▼──────────────────────────────┐
   │  libiio (Abstraction Library)                       │
   │  - C/C++/C#/Python/MATLAB bindings                  │
   └──────────────────────┬──────────────────────────────┘
                          │
   ┌──────────────────────▼──────────────────────────────┐
   │  Backend (Local/Network/USB/Serial)                 │
   └──────────────────────┬──────────────────────────────┘
                          │
   ┌──────────────────────▼──────────────────────────────┐
   │  iiod Server (Optional - for remote access)         │
   └──────────────────────┬──────────────────────────────┘
                          │
   ┌──────────────────────▼──────────────────────────────┐
   │  Linux Kernel IIO Subsystem                         │
   │  - Device drivers                                   │
   │  - Sysfs attributes (configuration)                 │
   │  - Character device (high-speed data)               │
   └──────────────────────┬──────────────────────────────┘
                          │
   ┌──────────────────────▼──────────────────────────────┐
   │  Hardware (ADC/DAC/Transceiver)                     │
   └─────────────────────────────────────────────────────┘

**Key Components:**

* **libiio**: Cross-platform library providing unified API
* **iiod**: TCP/IP server enabling remote hardware access
* **IIO Kernel Drivers**: Device-specific drivers in Linux kernel
* **Language Bindings**: Native support for C, C++, C#, Python, MATLAB

**Key Benefits:**

#. **Remote Access**: Control hardware over network (TCP/IP), USB, or serial
#. **Cross-Platform**: Same code works on Windows, Linux, macOS
#. **Language Choice**: Use your preferred programming language
#. **Consistent Interface**: Same attribute model across all devices

Third-Party Tool Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Beyond ADI's tools, the IIO framework enables integration with third-party applications:

* **PyADI-IIO**: Python abstraction layer making hardware easier to use
* **GNU Radio**: Open-source SDR framework with gr-iio plugin
* **MATLAB/Simulink**: MathWorks ecosystem via IIO System Objects
* **qIQ Receiver**: Signal quality evaluation tool for transceivers
* **SDRangel**: Third-party SDR application with IIO support

This open ecosystem approach ensures you're not locked into specific tools.


Evaluation, Test and Analysis
------------------------------

The evaluation phase is where engineers confirm that an ADI converter or transceiver meets their application requirements. This phase's duration is proportional to the complexity and specificity of your application - from minutes for simple validation to weeks for comprehensive system characterization.

System Architecture for Evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI's evaluation architecture uses a **hardware/software stack** that provides immediate access to device functionality:

Hardware Stack
^^^^^^^^^^^^^^

.. code-block:: text

   ┌───────────────────────────────────────┐
   │  Host Computer (Windows/Linux/Mac)    │
   └──────────────────┬────────────────────┘
                      │ USB or Ethernet
   ┌──────────────────▼────────────────────┐
   │  Evaluation Board                     │
   │  ┌─────────────────────────────────┐  │
   │  │ ARM SoC (Processing System)     │  │
   │  │  - Linux OS                     │  │
   │  │  - Kernel IIO Drivers           │  │
   │  │  - libiio (local)               │  │
   │  │  - iiod (TCP/IP server)         │  │
   │  └───────────┬─────────────────────┘  │
   │              │ AXI Interface           │
   │  ┌───────────▼─────────────────────┐  │
   │  │ FPGA (Programmable Logic)       │  │
   │  │  - Transceiver/ADC/DAC HDL      │  │
   │  │  - AXI DMA                      │  │
   │  │  - JESD204 Interface            │  │
   │  └───────────┬─────────────────────┘  │
   │              │ Serial/Parallel         │
   │  ┌───────────▼─────────────────────┐  │
   │  │ ADI Device (ADC/DAC/Transceiver)│  │
   │  └─────────────────────────────────┘  │
   └───────────────────────────────────────┘

**Communication Paths:**

* **Control Path**: SPI/GPIO for device configuration (sample rate, gain, filters, etc.)
* **Data Path**: High-speed DMA for continuous sample streaming
* **Network Path**: USB or Ethernet for remote access from host

Software Stack
^^^^^^^^^^^^^^

The software stack provides multiple access methods for different use cases:

* **GUI Applications**: For visual interaction and quick measurements
* **Command-Line Tools**: For scripting and automation
* **Programming Libraries**: For custom applications
* **Third-Party Tools**: For specialized analysis

Evaluation Tools
~~~~~~~~~~~~~~~~

1. IIO Oscilloscope
^^^^^^^^^^^^^^^^^^^

The **IIO Oscilloscope** is ADI's primary GUI tool for device evaluation and data visualization.

**Key Features:**

* **Multi-Domain Visualization:**

  * Time domain plots with trigger support
  * Frequency domain (FFT) analysis
  * Constellation diagrams for QAM/PSK signals
  * Eye diagrams

* **Measurement Capabilities:**

  * Markers for precise measurements
  * Math operations (add, subtract, multiply signals)
  * Statistical measurements (mean, RMS, peak-to-peak)

* **Device Configuration:**

  * GUI controls for all device attributes
  * Sample rate, gain, frequency, filter configuration
  * Save/load configuration profiles

* **Plugin Architecture:**

  * Device-specific plugins for specialized controls
  * Custom GUIs for complex configuration scenarios
  * Community-contributed plugins

* **Cross-Platform:**

  * Runs on Windows, Linux, and macOS
  * Same interface across all platforms

**Typical Workflow:**

#. Connect evaluation board via USB
#. Launch IIO Oscilloscope
#. Select device from detected IIO contexts
#. Configure device parameters (sample rate, frequency, gain)
#. Capture and visualize data
#. Export data for offline analysis

2. ACE (Analysis | Control | Evaluation) Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**ACE** provides advanced analysis capabilities with device-specific optimizations.

**Features:**

* ADGenericIIO Board Plugin for IIO device support
* Advanced configuration wizards
* Comprehensive device characterization
* Automated test sequences

3. Scopy
^^^^^^^^

**Scopy** is ADI's next-generation instrument software that will eventually replace IIO Oscilloscope.

**Features:**

* Modern, responsive UI
* Advanced visualization options
* Multiple instrument modes (oscilloscope, spectrum analyzer, network analyzer, signal generator)
* Plugin support for device-specific functionality
* Improved performance for high sample rate devices

4. qIQ Receiver
^^^^^^^^^^^^^^^

**qIQ Receiver** is a third-party Windows application specialized for signal quality evaluation.

**Best For:**

* Evaluating transceiver performance with external signal sources
* EVM (Error Vector Magnitude) measurements
* Constellation quality analysis
* Signal demodulation and decoding

**Supported Devices:**

* ADI transceivers (AD9361, AD9363, ADRV9002, ADRV9009)
* Direct-sampling receivers

**Typical Use Case:** Connect a signal generator to the receiver, capture the signal with qIQ, and immediately see EVM, constellation, and other quality metrics.

Command-Line Tools (libiio)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For automation and scripting, libiio provides a comprehensive set of command-line utilities:

iio_info
^^^^^^^^

**Purpose:** Display information about IIO devices and contexts

**Usage Examples:**

.. code-block:: bash

   # List all IIO contexts (local and network)
   iio_info -s

   # Show detailed device information
   iio_info -u ip:192.168.2.1

   # Display context attributes
   iio_info -a

**Output:** Device names, channels, attributes, sample rates, buffer capabilities

iio_attr
^^^^^^^^

**Purpose:** Read and write IIO device attributes

**Usage Examples:**

.. code-block:: bash

   # Read RX LO frequency
   iio_attr -u ip:192.168.2.1 -c ad9361-phy voltage0 frequency

   # Set TX attenuation
   iio_attr -u ip:192.168.2.1 -c ad9361-phy voltage0 hardwaregain -5.0

   # List all attributes for a device
   iio_attr -u ip:192.168.2.1 -c ad9361-phy

**Key Feature:** Scriptable configuration for automated test sequences

iio_readdev
^^^^^^^^^^^

**Purpose:** Capture samples from IIO device to file or stdout

**Usage Examples:**

.. code-block:: bash

   # Capture 1 million samples to file
   iio_readdev -u ip:192.168.2.1 -s 1000000 cf-ad9361-lpc > capture.bin

   # Continuous capture with pipe to processing
   iio_readdev -u ip:192.168.2.1 cf-ad9361-lpc | python process.py

**Output Format:** Binary I/Q sample data

iio_writedev
^^^^^^^^^^^^

**Purpose:** Transmit samples from file to IIO device

**Usage Examples:**

.. code-block:: bash

   # Transmit waveform file
   iio_writedev -u ip:192.168.2.1 cf-ad9361-dds-core-lpc < waveform.bin

   # Continuous transmission with cyclic buffer
   iio_writedev -u ip:192.168.2.1 -c 1000000 cf-ad9361-dds-core-lpc < signal.bin

iio_reg
^^^^^^^

**Purpose:** Direct register access for debugging (SPI, I2C, MMIO)

**Usage Examples:**

.. code-block:: bash

   # Read register 0x037
   iio_reg -u ip:192.168.2.1 ad9361-phy 0x037

   # Write register
   iio_reg -u ip:192.168.2.1 ad9361-phy 0x037 0x1A

**Warning:** Direct register access bypasses driver protection. Use only for debugging.

Evaluation Best Practices
~~~~~~~~~~~~~~~~~~~~~~~~~~

**1. Start Simple**

Begin with IIO Oscilloscope to verify basic functionality before moving to advanced tools or custom code.

**2. Use Reference Signals**

For accurate characterization, use high-quality signal generators and reference sources.

**3. Document Configuration**

Save device configurations and test parameters for reproducibility.

**4. Remote Access**

Leverage network support for remote testing and automation:

.. code-block:: python

   # Python example - remote access
   import adi

   # Access device over network
   sdr = adi.Pluto("ip:192.168.2.1")
   sdr.sample_rate = 2e6
   data = sdr.rx()

**5. Automated Testing**

Use command-line tools and Python scripts for repeatable test sequences.


Algorithmic Development, Modeling and Prototyping
--------------------------------------------------

Once hardware evaluation confirms device suitability, the next phase focuses on **algorithm development** - implementing the signal processing that defines your application. ADI's ecosystem enables **model-based design** approaches that let you develop algorithms in familiar, high-level environments while maintaining hardware-in-the-loop validation.

Philosophy: Plug 'n' Play Prototyping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The goal of this phase is to:

* **See key features/performance** of the ADI part in your application
* **Configure, capture, and generate** signals quickly (10-15 minutes to first data)
* **Develop algorithms** in your preferred environment (MATLAB, Python, GNU Radio)
* **Validate with real hardware** throughout the development process

Model-Based Design Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The algorithmic development workflow progresses through four key stages:

1. Hardware Evaluation
^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Understand hardware capabilities and limitations

**Activities:**

* Stream data from real RF hardware into development environment
* Characterize noise floors, dynamic range, filter responses
* Validate hardware-in-the-loop setups

**Tools:** Any platform from ADALM-PLUTO to production boards

2. System Simulation
^^^^^^^^^^^^^^^^^^^^

**Objective:** Model the complete RF signal chain

**Activities:**

* Create behavioral models of RF components
* Simulate end-to-end system performance
* Identify bottlenecks and optimization opportunities
* Trade-off analysis (sample rates, filter orders, precision)

**MATLAB Example:** Simulink models combining Communications Toolbox, DSP System Toolbox, and ADI IIO System Objects

3. Algorithm Development
^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Develop, model, and simulate communications/signal processing algorithms

**Activities:**

* Implement modulation/demodulation schemes
* Design and optimize filters
* Develop synchronization and timing recovery
* Implement error correction coding
* Test with real-world data from hardware

**Requirements Verification:**

* Validate algorithms meet system requirements (BER, EVM, latency)
* Test corner cases and impairments
* Stress-test with realistic signal conditions

4. Code Generation and Targeting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Transition from simulation to deployable implementation

**Activities:**

* **HDL Code Generation**: Convert MATLAB/Simulink models to synthesizable HDL
* **C/C++ Code Generation**: Target embedded processors
* **Production Deployment**: Integrate with FPGA and embedded systems
* **Hardware Testing**: Validate generated code on target platform

**Tools:**

* MATLAB HDL Coder
* MATLAB Embedded Coder
* Vivado for FPGA synthesis
* GNU Radio for C++ deployment

Development Environments and Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MATLAB and Simulink
^^^^^^^^^^^^^^^^^^^

ADI provides comprehensive MATLAB toolbox support for rapid prototyping:

**ADI-TRX Toolbox (Transceiver Toolbox for MATLAB & Simulink)**

* **Supported Devices:**

  * AD9361, AD9363, AD9364 (Pluto)
  * ADRV9002 (Jupiter)
  * ADRV9009 (various platforms)
  * AD9081, AD9082 (MxFE platforms)

* **Features:**

  * IIO System Objects for streaming
  * Hardware-in-the-loop Simulink blocks
  * Transmit and receive continuous data
  * Device configuration from MATLAB
  * Examples for common use cases

**ADI-HSX Toolbox (High-Speed Converter Toolbox)**

* **Focus:** High-speed ADCs and DACs
* **Applications:** Wideband receivers, arbitrary waveform generation

**ADI-SENSOR Toolbox (Accelerometer & Gyroscope)**

* **Devices:** ADXL, ADIS IMU products
* **Applications:** Motion sensing, navigation, inertial measurement

**ADI-TOF Toolbox (Time-of-Flight)**

* **Devices:** AD-FXTOF1 and similar
* **Applications:** 3D imaging, depth sensing, LIDAR

**Example Workflow (MATLAB):**

.. code-block:: matlab

   % Configure ADALM-PLUTO
   rx = sdrrx('Pluto');
   rx.RadioID = 'usb:0';
   rx.CenterFrequency = 915e6;
   rx.BasebandSampleRate = 2e6;
   rx.OutputDataType = 'double';
   rx.SamplesPerFrame = 4096;

   % Receive samples
   [data, validData] = rx();

   % Process with Communications Toolbox
   spectrum = abs(fft(data));
   plot(spectrum);

PyADI-IIO (Python)
^^^^^^^^^^^^^^^^^^

**PyADI-IIO** is a Python abstraction module that makes ADI hardware incredibly easy to use from Python.

**Design Philosophy:**

* **Pythonic interfaces** for ADI hardware
* **Hide complexity** of IIO attribute structure
* **Custom classes** for specific parts (e.g., `adi.Pluto()`, `adi.ad9081()`)
* **Simple to get started** - just a few lines of code

**Features:**

* Object-oriented device interfaces
* NumPy array integration
* Works with SciPy, Matplotlib, scikit-learn, TensorFlow
* Same code structure across all ADI devices

**Example (ADALM-PLUTO Loopback):**

.. code-block:: python

   import adi
   import numpy as np
   import matplotlib.pyplot as plt

   # Create device object
   sdr = adi.Pluto("ip:192.168.2.1")

   # Configure
   sdr.sample_rate = int(2e6)
   sdr.rx_lo = int(915e6)
   sdr.tx_lo = int(915e6)
   sdr.tx_hardwaregain_chan0 = -30  # dB

   # Create complex waveform
   fc = 100000  # 100 kHz tone
   N = 2048
   ts = 1 / sdr.sample_rate
   t = np.arange(0, N * ts, ts)
   i = np.cos(2 * np.pi * t * fc) * 2**14
   q = np.sin(2 * np.pi * t * fc) * 2**14
   iq = i + 1j * q

   # Transmit
   sdr.tx(iq)

   # Receive
   samples = sdr.rx()

   # Plot spectrum
   plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate / 1e6)
   plt.xlabel("Frequency (MHz)")
   plt.show()

**Portability:** The same code works on Pluto, Jupiter, Talise, MxFE - just change the device class:

.. code-block:: python

   # sdr = adi.Pluto("ip:192.168.2.1")
   # sdr = adi.adrv9002("ip:analog.local")
   sdr = adi.ad9081("ip:10.48.65.123")

GNU Radio
^^^^^^^^^

**GNU Radio** is a free, open-source software development toolkit for building signal processing applications.

**Key Features:**

* **Modular architecture** with reusable signal processing blocks
* **Visual programming** with GNU Radio Companion (GRC)
* **C++ and Python** implementations
* **Extensive block library** for communications and DSP

**gr-iio Plugin for ADI Hardware:**

* IIO source and sink blocks
* Device configuration from flowgraph
* Streaming integration with GNU Radio scheduler
* Examples for all ADI platforms

**Example Application Flow:**

#. Create flowgraph in GRC with IIO source block
#. Add signal processing blocks (filters, demodulators, etc.)
#. Add visualization sinks (FFT, scope, constellation)
#. Generate Python code and run
#. Modify parameters in real-time

**Typical Use Cases:**

* Digital modem implementation (PSK, QAM, FSK)
* Spectrum analysis applications
* Protocol decoders and encoders
* Radar signal processing

System Architecture for Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All development tools interact with ADI hardware through a common architecture:

.. code-block:: text

   ┌─────────────────────────────────────────────────┐
   │ Application Layer                               │
   │ (MATLAB/Simulink, Python, GNU Radio)            │
   └───────────────────┬─────────────────────────────┘
                       │
   ┌───────────────────▼─────────────────────────────┐
   │ libiio / tinyiiod                               │
   │ (Cross-platform abstraction layer)              │
   └───────────────────┬─────────────────────────────┘
                       │
   ┌───────────────────▼─────────────────────────────┐
   │ Hardware Platform (Pluto/Jupiter/Talise/MxFE)   │
   │                                                  │
   │  ┌────────────────────────────────────────────┐ │
   │  │ ARM CPU (Processing System)                │ │
   │  │  - Linux OS                                │ │
   │  │  - IIO Kernel Drivers                      │ │
   │  │  - iiod Server                             │ │
   │  └──────────────┬─────────────────────────────┘ │
   │                 │ AXI Bus                        │
   │  ┌──────────────▼─────────────────────────────┐ │
   │  │ FPGA Fabric (Programmable Logic)           │ │
   │  │                                             │ │
   │  │  ┌─────────────────────────────────┐       │ │
   │  │  │ User Logic                       │       │ │
   │  │  │ (Custom signal processing)       │       │ │
   │  │  └─────────────┬───────────────────┘       │ │
   │  │                │                             │ │
   │  │  ┌─────────────▼───────────────────┐       │ │
   │  │  │ AXI DMA                          │       │ │
   │  │  └─────────────┬───────────────────┘       │ │
   │  │                │                             │ │
   │  │  ┌─────────────▼───────────────────┐       │ │
   │  │  │ Transmitter/Receiver HDL         │       │ │
   │  │  │ (ADI Reference Design)           │       │ │
   │  │  └─────────────┬───────────────────┘       │ │
   │  │                │                             │ │
   │  └────────────────┼─────────────────────────────┘ │
   │                   │ JESD204/Parallel             │
   │  ┌────────────────▼─────────────────────────────┐ │
   │  │ ADI Device (ADC/DAC/Transceiver)             │ │
   │  └──────────────────────────────────────────────┘ │
   └───────────────────────────────────────────────────┘

**Integration Points:**

* **AXI-Stream Interface**: Insert custom processing blocks between DMA and transceiver HDL
* **Register Maps**: Configure custom IP via AXI-Lite
* **Partial Reconfiguration**: Swap processing chains dynamically (Xilinx only)

Hardware Platforms for Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All these tools work across ADI's platform portfolio:

**Entry Level: ADALM-PLUTO**

* AD9363 transceiver
* Zynq-7010 FPGA
* Up to 20 MHz RF bandwidth
* 325 MHz - 3.8 GHz tuning range
* USB 2.0 connectivity
* <$150 USD
* **Ideal for:** Learning, algorithm development, classroom use

**Mid-Range: Jupiter**

* ADRV9002 dual transceiver
* ZynqMP-ZU3EG FPGA
* Wider bandwidth and more channels
* Ethernet and USB3
* **Ideal for:** More complex algorithms requiring higher bandwidth

**High-Performance: MxFE Platforms**

* AD9081/AD9082 Mixed-Signal Front End
* Multiple carrier options: ZCU102, ZC706, VCK190, VCU118, VCU128
* Highest sampling rates (up to 12 GSPS DAC, 4 GSPS ADC)
* Multi-channel with JESD204C
* **Ideal for:** Wideband, multi-channel applications

**Production: QUAD-MxFE, ADRV9009-ZU11EG**

* Multi-chip solutions
* Production-ready SOM modules
* **Ideal for:** Transition to production hardware

**Key Point:** The same MATLAB, Python, or GNU Radio code works across all platforms with minimal or no changes.

Common Development Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Streaming Data Acquisition
^^^^^^^^^^^^^^^^^^^^^^^^^^^

All tools support continuous data streaming for long-duration captures:

.. code-block:: python

   # Python example - continuous streaming
   import adi

   sdr = adi.Pluto()
   sdr.rx_buffer_size = 2**16  # 64K samples per call

   while True:
       samples = sdr.rx()  # Get next buffer
       # Process samples...

Transmit and Receive (Loopback Testing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use TX and RX simultaneously to test modems and processing:

.. code-block:: python

   # Transmit known signal, receive and validate
   sdr.tx_cyclic_buffer = True  # Repeat TX automatically
   sdr.tx(tx_waveform)

   rx_samples = sdr.rx()
   # Correlate, demodulate, check BER...

Hardware-in-the-Loop (HIL) Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Keep hardware connected throughout development:

.. code-block:: matlab

   % MATLAB - continuous HIL
   while ~isDone
       rxData = rx();  % Receive from hardware

       % Algorithm processing
       processed = myAlgorithm(rxData);

       % Metrics
       evm = calculateEVM(processed);
       updatePlots(evm);
   end

Example: Complete SDR Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Scenario:** Develop a QPSK modem for a custom communications link

**Stage 1: Pure Simulation (MATLAB)**

.. code-block:: matlab

   % Simulate ideal QPSK system
   data = randi([0 3], 1000, 1);
   modData = pskmod(data, 4);
   rxData = awgn(modData, 20, 'measured');
   demodData = pskdemod(rxData, 4);
   [numErrors, ber] = biterr(data, demodData);

**Stage 2: Hardware-in-the-Loop (MATLAB + Pluto)**

.. code-block:: matlab

   % Transmit QPSK through real hardware
   tx = sdrtx('Pluto');
   rx = sdrrx('Pluto');

   % Configure
   tx.CenterFrequency = 915e6;
   rx.CenterFrequency = 915e6;

   % Transmit modulated data
   tx(modData);

   % Receive and demodulate
   rxData = rx();
   demodData = pskdemod(rxData, 4);
   [numErrors, ber] = biterr(data, demodData);

**Stage 3: Embedded Deployment (Python on Pluto)**

Deploy algorithm to run on Pluto's ARM processor:

.. code-block:: python

   #!/usr/bin/env python3
   # Runs on Pluto embedded Linux
   import adi
   import numpy as np

   sdr = adi.ad9361()  # Local access, no network
   sdr.sample_rate = 2e6

   while True:
       samples = sdr.rx()
       demod_data = qpsk_demod(samples)  # Your algorithm
       process_data(demod_data)

**Stage 4: FPGA Integration**

Move performance-critical processing to FPGA fabric using HDL Coder or hand-coded HDL.

Key Takeaway
~~~~~~~~~~~~

The algorithmic development phase bridges the gap between hardware evaluation and production deployment. By maintaining **hardware connectivity throughout development**, you validate algorithms with real-world signals, impairments, and noise - catching issues early before costly hardware redesigns.


Building Blocks for Development and New Revenue Streams
--------------------------------------------------------

ADI's ecosystem provides **modular hardware and software building blocks** that enable rapid prototyping and clear paths from evaluation to production. This modular approach reduces development risk, accelerates time-to-market, and opens new revenue opportunities by reusing proven components.

Hardware Building Blocks
~~~~~~~~~~~~~~~~~~~~~~~~

Development Platform Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ADI's hardware strategy uses a **modular, FMC-based architecture** that separates concerns:

.. code-block:: text

   ┌─────────────────────────────────────────────────────┐
   │ Open Market Carrier Boards (FPGA + SoC)             │
   │ - Xilinx: ZCU102, ZC706, VCU118, VCU128, etc.       │
   │ - Intel: Arria 10, Stratix 10, Agilex               │
   │ - AMD Versal: VCK190, VMK180                        │
   └──────────────────────┬──────────────────────────────┘
                          │ FMC Connector(s)
   ┌──────────────────────▼──────────────────────────────┐
   │ ADI Evaluation Boards (Daughter Boards)             │
   │ - MxFE: AD9081, AD9082                              │
   │ - Transceivers: ADRV9009, ADRV9002, AD9361          │
   │ - Converters: AD9208, AD9172, etc.                  │
   │ - Interface: LVDS/CMOS, JESD204B, JESD204C          │
   └─────────────────────────────────────────────────────┘

**Key Advantage:** Mix and match carrier boards (FPGA resources, connectivity) with ADI daughter boards (RF performance, bandwidth) to match application requirements.

RF Application Options by Bandwidth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ADI offers evaluation boards optimized for different bandwidth requirements:

**40 MHz Channel Bandwidth**

* **Interface:** LVDS/CMOS parallel
* **Sample Rate:** Up to 61.44 MSPS
* **Channels:** Typically 2-channel systems
* **Example Devices:** AD9361, AD9363, ADRV9002 (narrowband mode)
* **Applications:** Narrowband communications, IoT, sub-6GHz cellular

**70 MHz Channel Bandwidth**

* **Interface:** JESD204B serial
* **Sample Rate:** Up to 491 MSPS
* **Channels:** 2-channel systems
* **Example Devices:** ADRV9009, AD9371
* **Applications:** Wideband communications, radar, SIGINT

**200 MHz Channel Bandwidth**

* **Interface:** JESD204B/C high-speed serial
* **Sample Rate:** Up to 12 GSPS (DAC), 4 GSPS (ADC)
* **Channels:** 4+ channel systems
* **Example Devices:** AD9081, AD9082 (MxFE family)
* **Applications:** Ultra-wideband systems, EW, multi-band radar, satellite communications

**Scalability:** Start development with a narrowband system, then scale to wideband by changing the daughter board while reusing HDL and software.

FMC-Compatible Ecosystem
^^^^^^^^^^^^^^^^^^^^^^^^^

**FMC (FPGA Mezzanine Card)** is the VITA 57 standard for modular FPGA expansion:

**Benefits:**

* **Vendor Independence:** Same ADI daughter board works with Xilinx, Intel, AMD FPGAs
* **FPGA Resource Scaling:** Choose carrier board based on logic, memory, and I/O needs
* **Future-Proof:** Upgrade to newer FPGAs without redesigning RF front-end
* **Cost Optimization:** Use lower-cost FPGAs for prototyping, scale up for production

**ADI FMC Boards:**

* ADRV9009-FMC
* AD9081-FMCA-EBZ, AD9082-FMCA-EBZ
* AD9208-FMC, AD9172-FMC
* Many more across ADI's portfolio

Software and Infrastructure Building Blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The hardware modularity is matched by **software and HDL modularity**, ensuring the same code and IP works across platforms.

1. Device-Level Drivers
^^^^^^^^^^^^^^^^^^^^^^^^

**No-OS Drivers (Bare Metal)**

* **Purpose:** Minimal-footprint drivers for microcontrollers and bare-metal FPGA
* **Language:** C
* **Repository:** https://github.com/analogdevicesinc/no-OS
* **Features:**

  * No operating system dependencies
  * Minimal resource requirements
  * Example applications included
  * SPI, I2C, GPIO abstraction layer

**Linux Kernel Drivers**

* **Purpose:** Production-quality drivers for Linux systems
* **Repository:** https://github.com/analogdevicesinc/linux
* **Features:**

  * IIO subsystem integration
  * DMA support for high-speed streaming
  * sysfs attributes for configuration
  * Character device for data access
  * Mainline kernel compatibility

**ADI Kuiper Linux Distribution:**

* Pre-built Linux distribution for ADI evaluation boards
* Includes all necessary kernel drivers, libiio, and tools
* SSH access for remote development
* Based on Raspberry Pi OS (Debian)

2. HDL/FPGA Reference Designs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Repository:** https://github.com/analogdevicesinc/hdl

**Architecture:** Modular IP cores with standardized AXI interfaces

**Key IP Cores:**

* **JESD204 Framework:** Physical layer, link layer, transport layer IP
* **ADC/DAC Interfaces:** Device-specific HDL for all ADI parts
* **DMA Engines:** High-performance AXI-DMA for data streaming
* **Clock Distribution:** Clock management and synchronization
* **SPI Engine:** High-speed SPI controller for converter configuration
* **Utilities:** FIFOs, clock converters, data width converters

**Reference Designs Available For:**

* All ADI evaluation boards
* All major FPGA vendors (Xilinx, Intel)
* Vivado and Quartus projects
* Example constraints files (pin assignments, timing)

**Modular Design Philosophy:**

.. code-block:: text

   ┌──────────────────────────────────────────┐
   │ Application Logic (Your Custom HDL)      │
   └───────────────┬──────────────────────────┘
                   │ AXI-Stream
   ┌───────────────▼──────────────────────────┐
   │ ADI DMA IP (axi_dmac)                    │
   └───────────────┬──────────────────────────┘
                   │ AXI-Stream
   ┌───────────────▼──────────────────────────┐
   │ ADI Transport/Link/Physical Layer IP     │
   │ (JESD204 or Parallel Interface)          │
   └───────────────┬──────────────────────────┘
                   │ Serial or Parallel
   ┌───────────────▼──────────────────────────┐
   │ ADI Device (ADC/DAC/Transceiver)         │
   └──────────────────────────────────────────┘

**Integration Points:** Insert custom signal processing between DMA and transport layer.

3. MATLAB Toolbox Support
^^^^^^^^^^^^^^^^^^^^^^^^^^

**ADI MATLAB Toolboxes:** https://github.com/analogdevicesinc/HighSpeedConverterToolbox

Available Toolboxes:

* **ADI-TRX:** Transceiver Toolbox (AD9361, ADRV9002, ADRV9009, etc.)
* **ADI-HSX:** High-Speed Converter Toolbox (AD9081, AD9082, AD9208, AD9172)
* **ADI-SENSOR:** Sensor Toolbox (IMUs, accelerometers)
* **ADI-TOF:** Time-of-Flight Toolbox

**Features:**

* IIO System Objects for Simulink
* MATLAB functions for device configuration
* Streaming interfaces (transmit/receive)
* HDL Coder and Embedded Coder targeting support
* Examples and tutorials

4. ADI libiio
^^^^^^^^^^^^^

**Repository:** https://github.com/analogdevicesinc/libiio

**Cross-Platform Library** for interfacing with IIO devices:

**Platforms Supported:**

* Windows (32-bit, 64-bit)
* Linux (x86, ARM, RISC-V)
* macOS
* FreeBSD
* Embedded Linux (ARM Cortex-A)

**Language Bindings:**

* C (native)
* C++
* C# (.NET)
* Python (via ctypes/cffi)
* MATLAB

**Backends:**

* **Local:** Direct kernel access via sysfs (Linux only)
* **Network:** TCP/IP remote access via iiod server
* **USB:** USB communication (context-based)
* **Serial:** UART-based communication for minimal systems

**Key APIs:**

* Context enumeration and creation
* Device discovery
* Attribute read/write
* Buffer allocation and data streaming
* Trigger configuration

5. ADI IIO-Oscilloscope
^^^^^^^^^^^^^^^^^^^^^^^

**Cross-platform GUI application** for device control and visualization:

**Features:**

* Time/frequency/constellation plots
* Device attribute control
* Plugin architecture for device-specific GUIs
* Export data to files
* Save/load configurations

**Plugin System:**

* FMComms2/3/4 plugins
* ADRV9009 plugin
* AD9081/AD9082 plugin
* Custom plugins for specialized boards

6. Third-Party Tool Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IIO ecosystem enables integration with industry-standard tools:

**PyADI-IIO (Python)**

* Repository: https://github.com/analogdevicesinc/pyadi-iio
* Pythonic abstraction layer over libiio
* NumPy integration
* Device-specific classes

**GNU Radio (gr-iio)**

* Open-source SDR framework
* IIO source/sink blocks
* Flowgraph-based development

**MATLAB/Simulink**

* Native IIO System Objects
* HDL Coder for FPGA targeting

**SDRangel**

* Third-party SDR application
* Supports ADI hardware via IIO

JESD204 Interface Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For high-speed converters, the **JESD204 Interface Framework** is a critical building block:

**Components:**

#. **HDL IP:**

   * Physical layer (transceiver management)
   * Link layer (8b/10b encoding, alignment, scrambling)
   * Transport layer (frame assembly)
   * Application layer interfaces

#. **Software Drivers:**

   * Linux kernel JESD204 framework
   * Link status monitoring
   * Eye scan and BER testing

#. **Hardware Reference Designs:**

   * Complete JESD204B and JESD204C examples
   * Multi-device synchronization (MCS)
   * Subclass 1 deterministic latency support

#. **Diagnostics and Debugging Tools:**

   * Lane status monitoring
   * Eye diagram capture
   * Bit error rate testing
   * Clock quality monitoring

**PyADI-JIF (JESD Interface Framework Configurator):**

* Python tool for automatic JESD204 configuration
* Calculates valid parameter combinations
* Generates device tree overlays
* Validates timing requirements

**Benefit:** Eliminates manual calculation of complex JESD204 parameters.

DeviceTree Management (PyADI-DT / Nebula)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**PyADI-DT** is a Python toolset for managing Linux device trees for ADI platforms:

**Features:**

* Automatic device tree generation for custom hardware
* Overlay support for runtime configuration changes
* Integration with PyADI-JIF for JESD204 systems
* Validation against hardware constraints

**Use Case:** Quickly generate correct device tree configuration when changing JESD204 parameters or adding new devices.

IIO Framework Deep Dive
~~~~~~~~~~~~~~~~~~~~~~~~

The **Industrial I/O (IIO) framework** is the foundational building block for all software integration:

IIO Device Model
^^^^^^^^^^^^^^^^

**Hierarchy:**

.. code-block:: text

   Context (Hardware platform or remote connection)
   └── Device (e.g., "ad9361-phy", "cf-ad9361-lpc")
       ├── Channel (e.g., "voltage0", "altvoltage0")
       │   ├── Attribute (e.g., "frequency", "gain", "filter")
       │   └── Scan Element (for buffered capture)
       ├── Buffer (DMA interface for high-speed data)
       └── Trigger (timing/synchronization)

**Example Device Structure (AD9361):**

.. code-block:: text

   ad9361-phy (Configuration device)
   ├── voltage0 (RX1)
   │   ├── hardwaregain (read/write)
   │   ├── rssi (read-only)
   │   └── filter_fir_en (enable FIR filter)
   ├── altvoltage0 (RX LO)
   │   └── frequency (RX frequency)
   └── altvoltage1 (TX LO)
       └── frequency (TX frequency)

   cf-ad9361-lpc (Data streaming device)
   ├── voltage0_i (RX I data)
   ├── voltage0_q (RX Q data)
   └── buffer (DMA buffer for streaming)

**sysfs Interface (Linux):**

.. code-block:: bash

   # Configuration via sysfs
   cd /sys/bus/iio/devices/iio:device2/

   # Read RX LO frequency
   cat altvoltage0_RX_LO_frequency

   # Set TX attenuation
   echo -5000 > voltage0_hardwaregain

   # Enable buffer for streaming
   echo 1 > scan_elements/voltage0_i_en
   echo 1 > scan_elements/voltage0_q_en
   echo 1 > buffer/enable

**Character Device (High-Speed Data):**

.. code-block:: bash

   # Stream data from /dev/iio:device3
   cat /dev/iio:device3 > capture.bin

**DMA Buffer Support:**

* Zero-copy streaming via DMA
* Kernel-allocated buffers
* Low CPU overhead for high sample rates
* Configurable buffer sizes

libiio Architecture
^^^^^^^^^^^^^^^^^^^

**Abstraction Layers:**

.. code-block:: text

   ┌─────────────────────────────────────────┐
   │ Application (User Code)                 │
   └───────────────┬─────────────────────────┘
                   │ High-Level API
   ┌───────────────▼─────────────────────────┐
   │ libiio Core                             │
   │ - Context management                    │
   │ - Device/channel/attribute abstraction  │
   │ - Buffer management                     │
   └───────────────┬─────────────────────────┘
                   │ Backend API
   ┌───────────────▼─────────────────────────┐
   │ Backend (Local/Network/USB/Serial)      │
   └───────────────┬─────────────────────────┘
                   │
   ┌───────────────▼─────────────────────────┐
   │ Transport (sysfs/iiod/libusb/tty)       │
   └───────────────┬─────────────────────────┘
                   │
   ┌───────────────▼─────────────────────────┐
   │ Hardware / Kernel                       │
   └─────────────────────────────────────────┘

**Example C Code (libiio):**

.. code-block:: c

   #include <iio.h>

   // Create context (network backend)
   struct iio_context *ctx = iio_create_network_context("192.168.2.1");

   // Get device
   struct iio_device *dev = iio_context_find_device(ctx, "cf-ad9361-lpc");

   // Get channel
   struct iio_channel *ch0_i = iio_device_find_channel(dev, "voltage0_i", false);

   // Enable channel for buffered capture
   iio_channel_enable(ch0_i);

   // Create buffer (1M samples)
   struct iio_buffer *buf = iio_device_create_buffer(dev, 1024*1024, false);

   // Refill buffer (receive data)
   iio_buffer_refill(buf);

   // Access data
   void *data = iio_buffer_start(buf);

   // Cleanup
   iio_buffer_destroy(buf);
   iio_context_destroy(ctx);

Revenue Stream Enablers
~~~~~~~~~~~~~~~~~~~~~~~~

The modular building block approach enables multiple revenue opportunities:

**1. Faster Time-to-Market**

* Reuse proven HDL and software components
* Reduced development and validation time
* Lower NRE (Non-Recurring Engineering) costs

**2. Risk Reduction**

* Prototype with low-cost hardware (ADALM-PLUTO ~$150)
* Validate algorithms before custom hardware investment
* Proven reference designs reduce integration risk

**3. Platform Reuse**

* Same software works across product lines
* HDL portability between FPGA vendors
* Amortize development cost across multiple products

**4. Multi-Tier Product Lines**

* **Entry:** ADALM-PLUTO-based products ($150 hardware cost)
* **Mid-Range:** Jupiter/Navassa-based systems ($1000-5000 range)
* **High-End:** MxFE/Multi-channel systems ($10000+ range)
* **Same core software/HDL across all tiers**

**5. Customization Services**

* Offer custom HDL signal processing
* Provide application-specific firmware
* Develop specialized host software
* Based on proven ADI building blocks

**6. Ecosystem Partnerships**

* Integrate with customer tools via IIO
* Support third-party software vendors
* Enable value-added resellers

**7. Rapid Prototyping Services**

* Quick proof-of-concept for customers
* Leverage FMC ecosystem for flexibility
* Demonstrate feasibility before commitment

Key Takeaway
~~~~~~~~~~~~

ADI's building block approach provides **maximum flexibility with minimum risk**. By combining modular hardware, open-source HDL, comprehensive driver support, and multi-language bindings, developers can:

* **Start fast** - Get data streaming in minutes
* **Develop efficiently** - Use familiar tools and languages
* **Scale confidently** - Clear path from prototype to production
* **Reuse extensively** - Same code across platforms and products

This ecosystem approach accelerates development timelines and opens new revenue opportunities that wouldn't be feasible with custom, single-purpose solutions.


Common Architecture Patterns for Easy Transition Between Platforms
-------------------------------------------------------------------

One of the most powerful aspects of ADI's ecosystem is the **consistent architecture across all platforms**, from entry-level development boards to production-grade custom hardware. This consistency enables you to start development on low-cost hardware and seamlessly transition to higher-performance platforms as your project matures - all while reusing the same software, HDL, and development workflows.

Platform Transition Path
~~~~~~~~~~~~~~~~~~~~~~~~

ADI's platform portfolio is designed with a clear progression path that balances cost, performance, and complexity:

Platform Comparison
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20 20

   * - Platform
     - Device
     - FPGA
     - Connectivity
     - Target Use Case
   * - **ADALM-PLUTO**
     - AD9363
     - Zynq-7010
     - USB 2.0
     - Learning, algorithm development
   * - **Jupiter SDR**
     - ADRV9002 (2x)
     - ZynqMP-ZU3EG
     - USB3, Ethernet
     - Mid-range prototyping
   * - **MxFE Boards**
     - AD9081/AD9082
     - Various (ZCU102, VCU118, etc.)
     - PCIe, Ethernet, Aurora
     - High-performance development
   * - **QUAD-MxFE**
     - 4× AD9081/9082
     - VCU118 (VU9P)
     - PCIe Gen3, 100G Ethernet
     - Multi-channel, synchronized systems
   * - **ADRV9009-ZU11EG**
     - 2× ADRV9009
     - ZynqMP-ZU11EG
     - Ethernet, custom
     - Production-ready SOM
   * - **Custom Design**
     - Any ADI device
     - Customer choice
     - Application-specific
     - Production deployment

**Differentiation Across Platforms:**

Platforms are differentiated by:

* **Form factor:** Development board vs. SOM vs. chip-down custom
* **Number of channels:** 1 RX/TX to 8+ channels
* **Connectivity:** USB, Ethernet, PCIe, custom
* **Expandability:** FMC connectors, GPIO, custom expansion
* **FPGA resources:** Logic cells, DSP blocks, BRAM, transceivers
* **CPU resources:** Single-core ARM to quad-core Cortex-A53/A72

**What Stays the Same:**

Despite these differences, all platforms share:

* Same HDL IP cores and reference designs
* Same Linux kernel and IIO drivers
* Same libiio software library
* Same MATLAB/Python/GNU Radio interfaces
* Compatible development tools (Vivado, IIO Oscilloscope, etc.)

Transition Strategy: Start Small, Scale Up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended development strategy leverages this commonality:

Stage 1: Algorithm Development (ADALM-PLUTO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Hardware:** ADALM-PLUTO ($149)

**Capabilities:**

* Up to 20 MHz RF bandwidth
* 325 MHz - 3.8 GHz tuning range
* 1 RX + 1 TX (half or full duplex)
* 128-tap FIR filters
* USB 2.0 connectivity (<500 MB/s)
* <2W power consumption

**Activities:**

* Stream data to MATLAB, Python, or GNU Radio
* Develop and validate signal processing algorithms
* Test communication protocols, radar algorithms, SIGINT processing
* Capture data in the field for offline analysis
* Validate basic hardware-in-the-loop workflows

**Example (Python):**

.. code-block:: python

   import adi
   import numpy as np

   # Connect to Pluto
   sdr = adi.Pluto("ip:192.168.2.1")

   # Configure
   sdr.sample_rate = int(2e6)
   sdr.rx_lo = int(915e6)
   sdr.tx_lo = int(915e6)
   sdr.tx_hardwaregain_chan0 = -30

   # Transmit and receive
   sdr.tx_cyclic_buffer = True
   sdr.tx(tx_waveform)
   rx_samples = sdr.rx()

**Key Benefit:** Low cost and minimal setup enable rapid algorithm iteration.

Stage 2: Enhanced Prototyping (Jupiter or Talise)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Hardware:** Jupiter (ADRV9002), Navassa (ADRV9002), or Talise (ADRV9009)

**Enhanced Capabilities:**

* Wider RF bandwidth (70-200 MHz)
* More channels (2-4 RX/TX)
* Higher sample rates
* Better performance specifications
* Ethernet and USB3 connectivity
* More FPGA resources for custom processing

**Activities:**

* Validate algorithms with more realistic bandwidth and channels
* Test multi-channel synchronization
* Begin FPGA-based signal processing
* Develop embedded software on ARM
* Performance characterization closer to production specs

**Same Code, Better Hardware:**

.. code-block:: python

   import adi
   import numpy as np

   # Same code, different device class
   sdr = adi.adrv9002("ip:analog.local")  # Was adi.Pluto()

   # Same configuration pattern
   sdr.sample_rate = int(10e6)  # Higher sample rate supported
   sdr.rx_lo = int(915e6)
   sdr.tx_lo = int(915e6)
   sdr.tx_hardwaregain_chan0 = -10

   # Same transmit/receive workflow
   sdr.tx_cyclic_buffer = True
   sdr.tx(tx_waveform)
   rx_samples = sdr.rx()

**Key Benefit:** Minimal code changes, significant performance upgrade.

Stage 3: High-Performance Development (MxFE/FMC Boards)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Hardware:** AD9081/AD9082 on ZCU102, VCU118, or similar carriers

**Maximum Capabilities:**

* Ultra-wideband (200+ MHz channels)
* Highest sample rates (up to 12 GSPS DAC, 4 GSPS ADC)
* Multi-channel with JESD204C
* Large FPGA resources for complex processing
* PCIe Gen3 for maximum host throughput
* Multi-chip synchronization support

**Activities:**

* Full-scale system prototyping
* Complex FPGA processing (beamforming, channelization, etc.)
* Multi-channel synchronization and phased arrays
* System integration and validation
* Performance optimization

**HDL Integration:**

At this stage, you'll likely integrate custom HDL processing:

.. code-block:: verilog

   // Insert custom processing in ADI reference design
   // Between DMA and transceiver interface

   axi_dmac i_dma (
       .s_axis_data(custom_processing_output),  // Your custom HDL
       // ... DMA connections
   );

   custom_signal_processor i_custom (
       .s_axis_data(axi_ad9081_rx_data),  // From ADI IP
       .m_axis_data(custom_processing_output)  // To DMA
   );

**Same Software Stack:**

Even with custom HDL, the software stack remains the same:

.. code-block:: python

   # Python code remains similar
   import adi

   mxfe = adi.ad9081("ip:10.48.65.123")
   mxfe.sample_rate = int(4e9)  # 4 GSPS
   rx_samples = mxfe.rx()

Stage 4: Production Deployment (SOM or Custom)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Hardware:** ADRV9009-ZU11EG SOM or custom chip-down design

**Production Features:**

* Optimized form factor
* Production-qualified components
* Custom power supply and thermals
* Application-specific connectivity
* Manufacturing test infrastructure

**Reuse from Development:**

* **HDL:** Same IP cores from github.com/analogdevicesinc/hdl
* **Linux Kernel:** Same drivers from github.com/analogdevicesinc/linux
* **Application Software:** Same MATLAB/Python/C code
* **Device Trees:** Adapted from reference designs

**Key Benefit:** Minimal validation risk - you're deploying proven components.

Common Software Architecture Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IIO Device Abstraction
^^^^^^^^^^^^^^^^^^^^^^^

All ADI platforms use the **same IIO device model**:

**Example: Simple VGA (AD8366)**

.. code-block:: text

   ad8366 (Voltage-controlled gain amplifier)
   └── voltage0
       └── hardwaregain (read/write attribute)

**Example: Complex Transceiver (AD9361)**

.. code-block:: text

   ad9361-phy (Configuration)
   ├── voltage0 (RX1)
   │   ├── hardwaregain
   │   ├── rssi
   │   ├── filter_fir_en
   │   └── ...
   ├── altvoltage0 (RX_LO)
   │   └── frequency
   └── ...

   cf-ad9361-lpc (Data streaming)
   ├── voltage0_i
   ├── voltage0_q
   └── buffer

**Pattern:** Simple or complex, all devices use device/channel/attribute hierarchy.

**Benefit:** Once you understand the IIO model for Pluto, you understand it for all ADI devices.

Software Stack Layering
^^^^^^^^^^^^^^^^^^^^^^^^

The software stack architecture is identical across all platforms:

.. code-block:: text

   ┌──────────────────────────────────────────────────┐
   │ Application Layer                                │
   │ (MATLAB, Python, GNU Radio, Custom C/C++)        │
   └────────────────────┬─────────────────────────────┘
                        │ API Calls
   ┌────────────────────▼─────────────────────────────┐
   │ libiio (Cross-platform abstraction)              │
   │ - C API with language bindings                   │
   └────────────────────┬─────────────────────────────┘
                        │ Backend Protocol
   ┌────────────────────▼─────────────────────────────┐
   │ Backend (Local/Network/USB/Serial)               │
   └────────────────────┬─────────────────────────────┘
                        │ Transport
   ┌────────────────────▼─────────────────────────────┐
   │ iiod Server (Optional, for remote access)        │
   └────────────────────┬─────────────────────────────┘
                        │ syscalls/TCP-IP
   ┌────────────────────▼─────────────────────────────┐
   │ Linux Kernel IIO Subsystem                       │
   │ - Device drivers                                 │
   │ - sysfs (configuration)                          │
   │ - Character device (data streaming)              │
   └────────────────────┬─────────────────────────────┘
                        │ SPI/I2C/DMA
   ┌────────────────────▼─────────────────────────────┐
   │ Hardware (ADC/DAC/Transceiver)                   │
   └──────────────────────────────────────────────────┘

**Key Pattern:** Applications talk to libiio, which abstracts all platform differences.

**Portability Example:**

.. code-block:: python

   # This code works on ANY ADI platform with minor changes
   import adi

   # Change only this line for different platforms:
   # sdr = adi.Pluto("ip:192.168.2.1")
   # sdr = adi.adrv9002("ip:analog.local")
   sdr = adi.ad9081("ip:10.48.65.123")

   # Everything else is the same:
   sdr.rx_lo = int(2.4e9)
   samples = sdr.rx()

Common HDL Architecture Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI's HDL reference designs share a common architecture across all platforms and devices.

Modular IP Core Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   ┌──────────────────────────────────────────────────┐
   │ Processing System (PS)                           │
   │ - ARM CPU running Linux                          │
   │ - Boots from SD/QSPI/eMMC                        │
   │ - Runs IIO drivers                               │
   └────────────────┬─────────────────────────────────┘
                    │ AXI4-Lite (Control)
                    │ HP/HPC ports (DMA data)
   ┌────────────────▼─────────────────────────────────┐
   │ Programmable Logic (PL) / FPGA Fabric            │
   │                                                   │
   │  ┌───────────────────────────────────────────┐   │
   │  │ Application / User Logic                  │   │
   │  │ (Custom signal processing)                │   │
   │  │  - AXI-Stream input/output                │   │
   │  └──────────────┬───────────┬────────────────┘   │
   │                 │           │                     │
   │  ┌──────────────▼───────────▼────────────────┐   │
   │  │ AXI DMAC (DMA Controller)                 │   │
   │  │  - axi_dmac IP core                       │   │
   │  │  - High-speed memory transfers            │   │
   │  │  - Scatter-gather support                 │   │
   │  └──────────────┬───────────┬────────────────┘   │
   │                 │ TX        │ RX                  │
   │  ┌──────────────▼───────────▼────────────────┐   │
   │  │ Transport/Link/Physical Layer             │   │
   │  │  - JESD204 or parallel interface          │   │
   │  │  - Clock management                       │   │
   │  │  - Data path FIFOs                        │   │
   │  └──────────────┬───────────┬────────────────┘   │
   │                 │           │                     │
   └─────────────────┼───────────┼─────────────────────┘
                     │ Serial    │ Parallel
   ┌─────────────────▼───────────▼─────────────────────┐
   │ ADI Device (ADC/DAC/Transceiver)                  │
   │  - JESD204B/C or LVDS/CMOS interface              │
   │  - SPI/I2C for control                            │
   └───────────────────────────────────────────────────┘

**Integration Pattern:**

#. **ADI provides:** Transport/Link/Physical layer + DMA + Reference constraints
#. **You add:** Custom signal processing between DMA and transport
#. **Interface:** Standard AXI-Stream (TDATA, TVALID, TREADY)

**Example Integration:**

.. code-block:: verilog

   // ADI Reference Design provides:
   axi_ad9081_rx_jesd i_jesd_rx (
       .rx_data(adc_data)  // From JESD RX
   );

   // You insert custom processing:
   my_fir_filter #(
       .NUM_TAPS(128)
   ) i_filter (
       .s_axis_tdata(adc_data),
       .m_axis_tdata(filtered_data)
   );

   my_channelizer i_channelizer (
       .s_axis_tdata(filtered_data),
       .m_axis_tdata(channelized_data)
   );

   // ADI Reference Design continues:
   axi_dmac i_dmac (
       .s_axis_data(channelized_data)  // To DMA for Linux
   );

**Key Benefit:** You work with familiar AXI interfaces, ADI handles the complex device-specific logic.

Standardized Register Maps
^^^^^^^^^^^^^^^^^^^^^^^^^^^

ADI IP cores use **consistent AXI-Lite register maps**:

**Common Registers (all IP cores):**

* `0x0000`: VERSION - IP core version identification
* `0x0004`: ID - Unique instance identifier
* `0x0008`: SCRATCH - Read/write test register
* `0x000C`: CONFIG - Configuration and enable bits

**Device-Specific Registers:**

* Documented in IP core documentation
* Accessible via `/dev/mem` or UIO from Linux
* Can be controlled via custom kernel modules

**Software Access:**

.. code-block:: c

   // Access IP registers from userspace (via UIO)
   #include <sys/mman.h>

   int fd = open("/dev/uio0", O_RDWR);
   void *regs = mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0);

   // Read VERSION register
   uint32_t version = ((uint32_t*)regs)[0x0000/4];

JESD204 Framework Portability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **JESD204 Interface Framework** works identically across all platforms:

**HDL Layers:**

* **Physical Layer:** GTX/GTH/GTY transceiver configuration (Xilinx) or Intel equivalent
* **Link Layer:** 8b/10b encoding, lane alignment, scrambling
* **Transport Layer:** Frame assembly, multi-frame boundary detection
* **Application Layer:** Sample unpacking and AXI-Stream interface

**Software Configuration:**

.. code-block:: python

   from adi import ad9081
   from pyadi_jif import jif

   # Configure JESD204 link parameters
   config = jif.AD9081()
   config.sample_clock = 4e9
   config.jesd_mode = "204C"
   config.lanes = 8
   config.L = 8  # Lanes
   config.M = 16  # Converters
   config.F = 4  # Octets per frame
   config.S = 1  # Samples per converter per frame

   # Solver finds valid configuration
   config.solve()

   # Deploy to hardware
   sdr = ad9081("ip:analog.local")
   sdr.apply_jesd_config(config)

**Key Benefit:** The framework handles JESD204 complexity, you just specify parameters.

Workflow Portability Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example 1: Loopback Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Transmit a known signal, receive it back, and validate.

**Pluto (Entry Level):**

.. code-block:: python

   import adi
   import numpy as np

   sdr = adi.Pluto("ip:192.168.2.1")
   sdr.sample_rate = int(2e6)
   sdr.tx_cyclic_buffer = True

   # Generate test signal
   tx_signal = np.exp(1j * 2 * np.pi * 100e3 * np.arange(1024) / sdr.sample_rate)

   sdr.tx(tx_signal * 2**14)
   rx_signal = sdr.rx()

**MxFE (High Performance):**

.. code-block:: python

   import adi
   import numpy as np

   sdr = adi.ad9081("ip:10.48.65.123")  # Only this line changes!
   sdr.sample_rate = int(4e9)  # Higher sample rate
   sdr.tx_cyclic_buffer = True

   # Same pattern - generate test signal
   tx_signal = np.exp(1j * 2 * np.pi * 100e6 * np.arange(4096) / sdr.sample_rate)

   sdr.tx(tx_signal * 2**14)
   rx_signal = sdr.rx()

**Code Reuse:** ~95% identical

Example 2: Spectrum Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Capture data and display power spectrum.

**Universal Code (works on all platforms):**

.. code-block:: python

   import adi
   import numpy as np
   import matplotlib.pyplot as plt

   # Change this line for different platforms:
   sdr = adi.Pluto("ip:192.168.2.1")
   # sdr = adi.adrv9002("ip:analog.local")
   # sdr = adi.ad9081("ip:10.48.65.123")

   # Configure (same pattern across all platforms)
   sdr.rx_lo = int(2.4e9)
   sdr.sample_rate = int(10e6)  # Adjust for platform capability
   sdr.rx_buffer_size = 2**14

   # Capture
   samples = sdr.rx()

   # Process (identical across all platforms)
   spectrum = np.fft.fftshift(np.fft.fft(samples))
   freq_axis = np.fft.fftshift(np.fft.fftfreq(len(samples), 1/sdr.sample_rate))
   spectrum_db = 20 * np.log10(np.abs(spectrum) / len(spectrum))

   # Visualize
   plt.figure(figsize=(10, 6))
   plt.plot(freq_axis / 1e6, spectrum_db)
   plt.xlabel("Frequency (MHz)")
   plt.ylabel("Magnitude (dB)")
   plt.title(f"Power Spectrum - Center: {sdr.rx_lo/1e9:.2f} GHz")
   plt.grid(True)
   plt.show()

**Code Reuse:** 100% identical except device instantiation

Example 3: MATLAB Simulink Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Stream data from hardware into Simulink for processing.

**Simulink Model (works on all platforms):**

#. Add **IIO System Object** source block
#. Configure URI: `ip:192.168.2.1` (Pluto) or `ip:analog.local` (other platforms)
#. Set sample rate, center frequency, gain
#. Connect to processing blocks (filters, demodulators, etc.)
#. Add scopes and sinks for visualization

**To change platforms:** Only update the URI and adjust sample rate parameters.

**Key Benefit:** Same Simulink model works from Pluto to MxFE.

Example 4: GNU Radio Flowgraph
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Create a visual flowgraph for signal processing.

**Flowgraph (platform-independent):**

.. code-block:: text

   [IIO Source] → [Low Pass Filter] → [FFT] → [GUI Sink]
        ↓
   [Configuration: URI, Sample Rate, Frequency]

**To switch platforms:**

* Open IIO Source block properties
* Change URI from `ip:192.168.2.1` (Pluto) to `ip:analog.local` (others)
* Adjust sample rate if needed
* Re-run flowgraph

**No flowgraph structure changes needed.**

Platform-Specific Optimizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While the API and architecture remain consistent, each platform has optimization opportunities:

ADALM-PLUTO Optimizations
^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Bandwidth:** Limited to ~20 MHz, use decimation filters
* **Sample Rate:** Max 61.44 MSPS, choose efficiently
* **FIR Filters:** 128 taps available, use for anti-aliasing or channelization
* **USB 2.0 Bandwidth:** Limit sustained rates to <40 MB/s to avoid drops

Jupiter/ADRV9002 Optimizations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Dual Transceivers:** Leverage both channels for MIMO or diversity
* **Wider Bandwidth:** Up to 40 MHz channels
* **Advanced Calibrations:** Use ADRV9002 tracking calibrations for stability
* **Custom Profiles:** Generate custom profiles with TES (Transceiver Evaluation Software)

MxFE/High-Performance Optimizations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Channelization:** Use internal NCOs for multi-band operation
* **Datapath Modes:** Configure for real, complex, or multi-carrier
* **JESD204C:** Leverage 64b/66b encoding for efficiency
* **FPGA Processing:** Implement custom channelizers, beamformers, etc. in PL
* **PCIe DMA:** Use high-throughput DMA for sustained multi-GSPS streaming

Migration Checklist
~~~~~~~~~~~~~~~~~~~~

When transitioning from one platform to another, use this checklist:

Hardware Migration
^^^^^^^^^^^^^^^^^^

☑ **Verify sample rate compatibility** - Ensure new platform supports required rates

☑ **Check RF frequency range** - Validate LO tuning range covers your application

☑ **Validate bandwidth requirements** - Confirm instantaneous bandwidth is sufficient

☑ **Review channel count** - Ensure sufficient RX/TX channels

☑ **Check interface bandwidth** - USB, Ethernet, or PCIe bandwidth adequate for data rates

☑ **Verify power budget** - Especially critical for embedded/portable applications

Software Migration
^^^^^^^^^^^^^^^^^^

☑ **Update device class** - Change from `adi.Pluto()` to `adi.ad9081()`, etc.

☑ **Adjust sample rates** - Update to values supported by new platform

☑ **Review buffer sizes** - Larger platforms may support larger buffers

☑ **Update network URIs** - Change IP addresses or hostnames

☑ **Test attribute compatibility** - Some advanced features may differ

☑ **Validate data types** - Check if sample format changes (int16 vs int32)

HDL Migration
^^^^^^^^^^^^^

☑ **Port IP cores** - Use same ADI IP cores from hdl repository

☑ **Update constraints** - Use reference constraints from ADI project for new platform

☑ **Check FPGA resources** - Verify your custom logic fits in new FPGA

☑ **Validate timing** - Re-run timing analysis on new platform

☑ **Update clocking** - Adjust PLLs for different JESD204 lane rates or sample rates

☑ **Test JESD204 links** - Use IIO oscilloscope and eye scan to validate links

Key Takeaways
~~~~~~~~~~~~~

**1. Start Small, Think Big**

Begin development on ADALM-PLUTO ($150) and validate algorithms before committing to expensive custom hardware.

**2. Code Portability is Real**

The same Python, MATLAB, or GNU Radio code works across platforms with minimal changes (often just the device class and sample rate).

**3. HDL Reuse**

ADI's HDL reference designs provide proven IP cores that port cleanly across Xilinx and Intel FPGAs.

**4. Consistent Tools**

The same development tools (Vivado, IIO Oscilloscope, MATLAB, Python) work across the entire platform range.

**5. Reduced Risk**

Platform progression reduces development risk - validate each stage before moving to higher complexity and cost.

**6. Clear Path to Production**

From Pluto to custom chip-down designs, there's a clear technology path with reusable components at every stage.

**7. Community and Support**

ADI's open-source ecosystem (GitHub HDL, Linux drivers, PyADI-IIO) ensures long-term support and community contributions.

Real-World Example: Complete Platform Migration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Scenario:** Developing a wideband spectrum monitoring system

**Stage 1: Algorithm Development (Pluto - 2 weeks)**

.. code-block:: python

   # Develop energy detection algorithm
   import adi
   import numpy as np

   sdr = adi.Pluto()
   sdr.sample_rate = 20e6  # Max for Pluto

   while True:
       samples = sdr.rx()
       power_spectrum = np.abs(np.fft.fft(samples))**2
       energy = np.sum(power_spectrum > threshold)
       if energy > detection_threshold:
           log_detection()

**Result:** Validated algorithm concept, detection thresholds, false alarm rates.

**Stage 2: Extended Bandwidth (Jupiter - 2 weeks)**

.. code-block:: python

   # Same algorithm, wider bandwidth
   import adi
   import numpy as np

   sdr = adi.adrv9002()  # Changed device
   sdr.sample_rate = 70e6  # Higher bandwidth

   # Same algorithm code!
   while True:
       samples = sdr.rx()
       power_spectrum = np.abs(np.fft.fft(samples))**2
       energy = np.sum(power_spectrum > threshold)
       if energy > detection_threshold:
           log_detection()

**Result:** Validated algorithm with realistic bandwidth, identified need for FPGA-based channelization.

**Stage 3: FPGA Integration (MxFE - 6 weeks)**

* Developed custom channelizer HDL using ADI reference design as base
* Integrated between DMA and JESD204 transport layer
* Used same Python control software with `adi.ad9081()`
* Achieved 200 MHz instantaneous bandwidth with 40 channels

**Stage 4: Production (Custom Board - 8 weeks)**

* Designed custom carrier board with AD9082
* Reused HDL from MxFE development
* Reused Linux kernel drivers
* Reused Python application software
* Added production-specific power, RF, and thermal design

**Total Development Time:** 18 weeks from concept to production

**Code Reuse:** >90% of Python code, >80% of HDL

**Risk Mitigation:** Each stage validated before next investment

This example demonstrates the power of ADI's common architecture - what could have been a 12-18 month development cycle with multiple dead-ends was reduced to ~4 months with high confidence at each stage.
