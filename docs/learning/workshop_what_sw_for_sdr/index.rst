What software do I need for my SDR?
===============================================================================

.. contents:: Contents
   :local:
   :depth: 2

Theoretical Concepts and Practical Foundations
----------------------------------------------

Typical Customer Design Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software-defined radio development follows a progressive, stage-based approach that takes designs from initial research through to production deployment.
The key advantage of ADI's approach is that the **same HDL, software, and infrastructure components are used throughout the entire flow**,
reducing the learning curve and development risk at each stage.

.. figure:: images/theoretical_content/customer_design_flow.png
   :alt: Customer Design Flow
   :align: center
   :width: 40em

   Typical Customer Design Flow

The typical customer design flow consists of 5 progressive stages, each building upon the previous one.

In the **research** phase, engineers validate that the chosen ADI device meets application requirements through simulation and measurement.

Key activities include:

* **Behavioral Simulation**: Model the system before building hardware
* **Device Evaluation**: Test actual hardware performance using evaluation boards
* **Measurements**: Characterize critical performance metrics such as SFDR (Spurious-Free Dynamic Range), SNR (Signal-to-Noise Ratio), EVM (Error Vector Magnitude),
  NF (Noise Figure), and NSD (Noise Spectral Density)

Tools used: Evaluation boards, IIO Oscilloscope, ACE software, bench test equipment.

During the **Algorithm Development** phase, engineers implement signal processing algorithms using high-level languages while streaming real data
from hardware.
Here, the focus is on rapid prototyping and validation of algorithms in realistic conditions via **MATLAB/Python/GRC Reference Implementation**,
**Hardware Streaming**, and **Iterative Development**.

Development environments at this stage include MATLAB, Simulink with ADI toolboxes, Python with PyADI-IIO, GNU Radio Companion with gr-iio blocks.

The **Design Elaboration** phase refines algorithms for embedded deployment through modeling and optimization. This stage include modeling using the same
development tools, validating optimized algorithms with real hardware data, and transitioning from floating-point to fixed-point arithmetic
for efficient hardware implementation.

Critical considerations include fixed-point precision, filter coefficient quantization, timing budgets, and FPGA resource utilization.

While *prototyping*, algorithms are deployed to development hardware for integration and optimization. This stage includes:

* **Deployment to Development Board**: Move algorithms to actual hardware (PlutoSDR, Jupiter, or FMC boards)
* **Design Optimization**: Tune for performance and resource efficiency
* **HDL Integration**: Integrate custom signal processing with ADI reference designs

The final stage, **Production**, includes deployment to custom hardware with complete system validation.

Throughout all stages, the same HDL IP cores, Linux kernel drivers, and application software are reused, dramatically reducing development risk and
time-to-market.


Software in the Design-in Journey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI's software ecosystem provides a cohesive solution across the entire design-in journey, supporting multiple development environments
while maintaining a common underlying infrastructure. The ecosystem enables engineers to work in their preferred tools—whether GUI-based applications,
scripting environments, or modeling platforms—all leveraging the same drivers, libraries, and hardware abstraction layers.

**Common Software Infrastructure:**

* `libiio <https://github.com/analogdevicesinc/libiio>`_: Cross-platform library providing unified hardware access
* **IIO Kernel Drivers**: Linux drivers for ADI converters and transceivers
* **iiod Server**: Network-transparent access to hardware
* **Language Bindings**: Support for C, C++, Python, MATLAB, and more

**Development Tools and Environments:**

* **IIO Oscilloscope** (`link <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_): Cross-platform GUI for visualizing and controlling IIO devices
* **MATLAB and Simulink**: ADI toolboxes for algorithm development and modeling
* **Python**, **Jupyter** and **PyADI-IIO** (`link <https://github.com/analogdevicesinc/pyadi-iio>`_): Python library for rapid prototyping with ADI hardware
* **GNU Radio** with **gr-iio** (`link <https://github.com/analogdevicesinc/gr-iio>`_) blocks for flowgraph-based development
* **ACE Software** (`link <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`_): Plugin-based framework for evaluation board control
* **Scopy** (`link <https://analogdevicesinc.github.io/scopy/>`_): Modern multi-instrument software suite


Evaluation, Test and Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analog Devices provides a single cohesive software solution, meeting customers in their ecosystem or at their tools of choice.

   .. figure:: images/theoretical_content/sw_solution.png
      :alt: Software Solution Architecture
      :align: center
      :width: 40em

      Single cohesive software solution supporting multiple user personas and tools

**Product Evaluation** uses hardware and software tools to verify that the Converter meets Application requirements.

Time investment is (very roughly) proportional to complexity and how application specific it needs to be

**Tools:** IIO Oscilloscope, ACE software, Scopy, bench test equipment


Algorithmic Development, Modeling and Prototyping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Product Prototyping** provides Plug 'n' Play hardware and software to see the key features and performance of the part.

It can configure, capture signals, or generate waveforms in 10-15 minutes, stream real data from hardware into development
environments (MATLAB, Python, GNU Radio) and develop and validate algorithms with hardware-in-the-loop

**Development Environments:** MATLAB, Simulink, Python, `PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`_, GNU Radio Companion

**Tools:** MATLAB, Simulink, Python, `PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`_, GNU Radio


Building Blocks for Development and New Revenue Streams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI's modular architecture provides reusable building blocks that accelerate development and create opportunities for new applications and revenue streams.

   .. figure:: images/theoretical_content/building_blocks.png
      :alt: Building Blocks for Development
      :align: center
      :width: 40em

      Modular building blocks

Modular building blocks enable rapid development and platform scalability. Signal processing components including filters, decimators, interpolators,
and other DSP primitives are standard offerings that accelerate algorithm implementation. Protocol implementations such as OFDM, QPSK, and FSK
are pre-implemented for rapid deployment, while pre-validated HDL provides high-performance streaming and buffering for demanding applications.

Efficient clock and power distribution features enable portable and battery-powered applications. Multiple libraries and frameworks provide flexible
hardware access and algorithm development: `PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`_ for rapid Python prototyping with hardware-in-the-loop,
MATLAB and Simulink toolboxes for system-level modeling and deployment, GNU Radio with `gr-iio <https://github.com/analogdevicesinc/gr-iio>`_ blocks
for flowgraph-based signal processing, and standardized Linux drivers that reduce integration effort.

The business benefits are compelling. Faster time-to-market results from pre-validated components that reduce development cycles, while proven building
blocks minimize integration challenges and eliminate redundant design work through IP reuse. Platform scalability allows you to start with ADALM-PLUTO
and scale seamlessly to production platforms.

Revenue opportunities emerge through application-specific solutions for vertical markets, proprietary algorithm development, custom hardware transitions
with unified software stacks, and IP licensing of optimized implementations.

Common Architecture for Easy Platform Transition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The common architecture across ADI's platforms makes it easy to transition between hardware as your project evolves from prototype to production.

   .. figure:: images/theoretical_content/common_architecture.png
      :alt: Common Architecture Makes It Easy to Transition Between Platforms
      :align: center
      :width: 40em

      Common architecture enables seamless transitions between platforms

**Shared Software and HDL Stack:**

* **Same libraries**: libiio, PyADI-IIO, and hardware drivers work across all platforms
* **Common Linux image**: ADI Kuiper Linux brings up the same software stack whether on a laptop or embedded board
* **Unified HDL**: Common FPGA designs across all SDR platforms
* **Consistent drivers**: Same drivers whether accessing hardware locally or via USB

**Platform Progression:**

* Start with :adi:`ADALM-PLUTO <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html>`:
   Provides quick verification, rapid algorithm development, and SIGINT applications at very low cost
* **Scale to production**:
   Same software and HDL seamlessly transfer to higher-performance platforms
* **Use modules for clean design**:
   Leverage ADI's reference designs and IP cores

**Open Source Repositories:**

* Common Linux kernel and drivers: https://github.com/analogdevicesinc/linux
* Common HDL IP cores: https://github.com/analogdevicesinc/hdl

This architecture ensures that code developed on entry-level hardware like ADALM-PLUTO can be reused on production platforms with minimal changes,
dramatically reducing development risk and time-to-market.

Analysis | Control | Evaluation
-------------------------------

Once you have the IIO framework set up, you need tools to analyze, control, and evaluate your hardware. ADI provides several software tools that
work seamlessly with IIO devices, from simple command-line utilities to full-featured graphical applications.

ACE Software and Plugins
~~~~~~~~~~~~~~~~~~~~~~~~

**ACE (Analysis, Control, Evaluation)** is ADI's original software framework for interacting with evaluation boards and development platforms.
It provides a plugin-based architecture where different modules can control specific hardware features.

**ADGenericIIOBoard Plugin** is a key plugin within ACE that enables interaction with any IIO-compatible device.
This generic approach means you can use the same plugin to control different ADI evaluation boards without requiring board-specific software.

   .. figure:: images/analysis_control_eval/adgeneric_iio_board_plugin.png
      :alt: ADGenericIIOBoard Plugin Interface
      :align: center
      :width: 40em

      ADGenericIIOBoard Plugin showing IIO device control

IIO Oscilloscope
~~~~~~~~~~~~~~~~

**IIO Oscilloscope (IIO-Scope)** is a powerful cross-platform application for visualizing and controlling IIO devices.
It provides both time-domain and frequency-domain visualization along with device configuration capabilities.

**Key Features:**

* **Multi-platform support**: Runs on Linux, Windows, and macOS
* **Time and frequency domain plots**: View signals in both domains simultaneously
* **Device configuration**: Modify hardware parameters in real-time
* **Plugin architecture**: Extensible with generic and device-specific plugins
* **Remote operation**: Can connect to IIO devices over network using iiod

   .. figure:: images/analysis_control_eval/iio_scope.png
      :alt: IIO Oscilloscope Main Interface
      :align: center
      :width: 40em

      IIO Oscilloscope showing time and frequency domain plots

**Generic Plugins:**

IIO-Scope includes several generic plugins that work with any IIO device:

* **DMM (Digital Multimeter) Plugin**:
   Displays real-time numerical values from device channels, useful for monitoring DC values, temperatures, voltages, and other scalar measurements

   .. figure:: images/analysis_control_eval/dmm_plugin.png
      :alt: DMM Plugin Interface
      :align: center
      :width: 40em

      DMM Plugin showing real-time channel values

* **Debug Tab/Plugin**:
   Provides low-level access to all IIO device attributes, allowing direct read/write operations on any device parameter for advanced debugging and development

   .. figure:: images/analysis_control_eval/debug_tab.png
      :alt: Debug Tab Interface
      :align: center
      :width: 40em

      Debug Tab showing device attributes tree

**Specific Control Plugins:**

For more complex devices, IIO-Scope offers specialized plugins:

* **FPGA Settings Plugin**:
   Controls FPGA-specific parameters such as clock configurations, data path settings, and interface modes
* **High Level Device Control Plugins**:
   Provide intuitive interfaces for complex RF transceivers, DACs, and ADCs with features like frequency tuning, gain control, and filter configuration

   .. figure:: images/analysis_control_eval/fpga_settings.png
      :alt: FPGA Settings Plugin
      :align: center
      :width: 40em

      FPGA Settings Plugin for controlling FPGA-specific parameters

   .. figure:: images/analysis_control_eval/high_level_device_ctrl.png
      :alt: High Level Device Control Plugin
      :align: center
      :width: 40em

      High Level Device Control Plugin providing intuitive interfaces for RF transceivers

IIO Command Line Tools
~~~~~~~~~~~~~~~~~~~~~~~

For automation, scripting, and headless operation, the IIO framework includes command-line utilities:

* **iio_info**: Lists all available IIO devices and their attributes
* **iio_attr**: Reads or writes device/channel attributes
* **iio_readdev**: Captures samples from device channels
* **iio_writedev**: Transmits samples to device channels
* **iio_reg**: Direct register access for low-level debugging

These tools are particularly useful for:

* Automated testing and continuous integration
* Remote device control via SSH
* Scripting complex measurement sequences
* Quick parameter verification without GUI overhead

**iio_info**

Displays information about all available IIO devices and their attributes, channels, and triggering capabilities.

.. code-block:: bash

   iio_info
   iio_info -n 192.168.1.100

**iio_attr**

Reads or writes device and channel attributes for configuration and control.

.. code-block:: bash

   iio_attr -d cf-ad9361-lpc
   iio_attr -c voltage0 frequency
   iio_attr -c voltage0 frequency 2400000000

**iio_readdev**

Captures samples from device channels and saves to file for analysis.

.. code-block:: bash

   iio_readdev -d cf-ad9361-lpc -c voltage0 -s 1024 > samples.raw

**iio_writedev**

Transmits samples from file to device channels.

.. code-block:: bash

   iio_writedev -d cf-ad9361-lpc -c voltage0 < samples.raw

**Remote Access via iiod**

Connect to IIO devices over network using the iiod server:

.. code-block:: bash

   iio_info -n 10.48.65.212

Scopy: Next-Generation Analysis Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Scopy <https://analogdevicesinc.github.io/scopy/>`_ is ADI's modern, next-generation instrument software that supersedes IIO-Scope with enhanced
capabilities and a more intuitive interface. It transforms your PC into a complete laboratory instrument suite.

**Scopy provides:**

* **Multiple instrument views**: Oscilloscope, spectrum analyzer, network analyzer, signal generator, logic analyzer, pattern generator, and more
* **Modern UI/UX**: Contemporary interface with improved usability
* **Enhanced visualization**: Advanced plotting with zoom, cursors, measurements, and annotations
* **Cross-platform**: Available for Windows, Linux, and macOS
* **Generic IIO support**: Works with any IIO-compatible device, not just ADI hardware
* **Export capabilities**: Save data, screenshots, and configurations for documentation

   .. figure:: images/analysis_control_eval/scopy_interface.png
      :alt: Scopy Main Interface
      :align: center
      :width: 40em

      Scopy interface showing multiple instrument views

Scopy is the recommended tool for new projects, offering a more complete and modern experience than the older IIO-Scope application.

qIQ Receiver
~~~~~~~~~~~~

qIQ Receiver is a specialized application for analyzing and demodulating various wireless communication standards.
It's particularly useful for RF engineers working with:

* **Digital modulation analysis**: BPSK, QPSK, QAM, and other modulation schemes
* **Constellation diagrams**: Real-time visualization of modulation quality
* **Spectrum analysis**: Detailed frequency domain analysis
* **Recording and playback**: Capture RF signals for offline analysis

   .. figure:: images/analysis_control_eval/qiq_receiver.png
      :alt: qIQ Receiver Interface
      :align: center
      :width: 40em

      qIQ Receiver showing constellation diagram and spectrum

qIQ Receiver bridges the gap between generic oscilloscope tools and specialized protocol analyzers, making it easier to develop and debug wireless communication systems with ADI SDR platforms.


Hands on exercises
------------------

The following workshops provide hands-on exercises demonstrating real-world software-defined radio applications using ADI's SDR platforms:

FTC2023 Pluto Workshop
~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   workshop_just_enough_sw_and_hdl_for_high_speed_designs/index

This workshop demonstrates hands-on exercises including:

* Transmitting and receiving complex sinusoids with Python
* Doppler radar with GNU Radio
* BPSK and QPSK modulation techniques
* Spectrum painting
* Platform portability between Pluto, Jupiter, and Talise

FTC2024 Jupiter Workshop
~~~~~~~~~~~~~~~~~~~~~~~~~
- RPi400 SD Card image is available `here <https://swdownloads.analog.com/cse/kuiper/Kuiper_rpi400_FTC2024_SDR.zip>`__
- Jupiter SD Card image is available `here <https://swdownloads.analog.com/cse/kuiper/Kuiper_jupiter_FTC2024_SDR.zip>`__
- Documentation is available `here <https://swdownloads.analog.com/cse/workshops/ftc2024/jupiter_sdr/ftc24_SDR_jupiter.zip>`__ (PPT, lab instructions and exercises)

FTC2025 Pluto Workshop
~~~~~~~~~~~~~~~~~~~~~~
- Title: Software hands-on training kit: Getting started with SDR using ADALM-PLUTO
- RPi5 SD Card image with Kuiper v2.0 available `here <https://swdownloads.analog.com/cse/kuiper/FTC25_SDR_Kuiper.zip>`__
- Documentation is available `here <https://swdownloads.analog.com/cse/workshops/ftc2025/ftc2025_sdr_exercises.zip>`__ (PPT, lab instructions and exercises)

Beginner SDR Exercises
~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   beginner_sdr_exercises/index

Step-by-step hands-on exercises for learning SDR fundamentals:

* Transmitting and receiving complex sinusoids with Python (Pluto, Jupiter, and Talise)
* Doppler radar with GNU Radio
* BPSK modulation and demodulation in Python
* QPSK modulation with GNU Radio
* Receiving QPSK video with SDRangel
* Spectrum painting
