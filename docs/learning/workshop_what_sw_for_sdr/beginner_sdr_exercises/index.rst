Beginner SDR Exercises
======================

The following hands-on exercises demonstrate real-world software-defined radio applications using ADI's SDR platforms.
These exercises showcase the power of reconfigurable software running on specialized hardware, allowing you to implement
complex signal processing algorithms without custom hardware design.

**Hardware Platforms Used:**

Throughout these exercises, you will work with three ADI SDR platforms, each offering different capabilities:

* :adi:`ADALM-PLUTO <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html>`:
   Entry-level SDR ideal for learning and prototyping

   - 2x Tx and 2x Rx ports (50 Ohm matched)
   - LO Frequency Range: 70MHz → 6GHz
   - Bandwidth: 56MHz
   - Sample rate: 61.44MSPS; 14 bits
   - Interfaces: USB2, UART

* :adi:`Jupiter (AD-JUPITER-EBZ) <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-jupiter-ebz.html>`:
   Mid-range platform for advanced development

   - 2x Tx and 2x Rx ports (50 Ohm matched)
   - LO Frequency Range: 30MHz → 6GHz
   - Bandwidth: 40MHz
   - Sample rate: 61.44MSPS; 16 bits
   - Interfaces: USB3, 1Gb Ethernet, Display Port, UART

* :adi:`Talise SOM (ADRV9009-ZU11EG) <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adrv9009-zu11eg.html>`:
   High-performance platform for production-grade applications

   - 4x Tx and 4x Rx (expandable to 8 TRx)
   - LO Frequency Range: 75MHz → 6GHz
   - RX Bandwidth: 200MHz, TX Bandwidth: 450MHz
   - Interfaces: USB3, 1Gb Ethernet, Display Port, PCIe 3.0, SFP, QSFP, UART

All three platforms share the same software stack and HDL architecture, demonstrating ADI's platform scalability—algorithms
developed on the entry-level Pluto can be seamlessly transferred to production-grade hardware with minimal code changes.

.. note::

   The following exercises should be run on a PC booted from the provided USB bootable image (available in the FTC2023 workshop Downloads section).
   The USB bootable image contains all necessary software pre-installed, including Python, GNU Radio, Thonny IDE, and all required libraries.
   Boot your PC from the USB drive with the mouse, keyboard, and monitor connected.
   Connect your SDR hardware (Pluto, Jupiter, or Talise) to the PC via USB before starting the exercises.

Transmit and receive a complex sinusoid (Sinewave Loopback)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A complex sinusoid is a fundamental building block in software-defined radio. Unlike a real sinusoid
(which oscillates in a single dimension), a complex sinusoid consists of two components:

* **In-phase (I) component**: Real part of the signal
* **Quadrature (Q) component**: Imaginary part of the signal

Together, they form a single tone in the frequency domain. This exercise transmits a complex sinusoid
and receives it back via a loopback connection, allowing you to observe both the transmitted
signal and its frequency spectrum representation.

   .. figure:: images/exercises/sinewave_loopback/complex_sinusoid.png
      :alt: Complex Sinusoid
      :align: center
      :width: 40em

      Complex sinusoid with in-phase (I) and quadrature (Q) components

   .. figure:: images/exercises/sinewave_loopback/complex_sinusoid_constellation_plot.png
      :alt: Complex Sinusoid Constellation Plot
      :align: center
      :width: 40em

      Constellation plot of a complex sinusoid

The following subsections demonstrate different implementations of this exercise using various tools and platforms.

Using PyADI-IIO with Pluto
^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the next steps:

#. Make the following setup using Pluto and connect it to your PC:

   .. figure:: images/exercises/sinewave_loopback/pluto_setup.png
      :alt: Pluto SDR Setup
      :align: center
      :width: 40em

      Pluto SDR setup with loopback connections

#. Download the SDR Lab Source Code from the FTC2023 workshop link and unzip it on your desktop.

#. Open **workshop_exercises** folder on your desktop.

#. Go to **python->sinewave_loopback** subfolder.

#. Right click on **python_loopback_sine_pluto.py -> Open with Other Application** and
   select **Thonny Python IDE** (or any other Python IDE you have installed) from the
   Recommended Applications list.

   .. figure:: images/exercises/sinewave_loopback/python_ide.png
      :alt: Open Python Script with IDE
      :align: center
      :width: 40em

      Open the Python script with Thonny Python IDE

#. To run the script, press the green round button from the top left corner in Thonny IDE as shown below.

   .. figure:: images/exercises/sinewave_loopback/run_script.png
      :alt: Run Python Script
      :align: center
      :width: 40em

      Run the Python script in Thonny IDE

#. To zoom on a plot, you can use the zoom option as depicted below. Encircle holding left click the area you want to zoom.
   On this example, if you zoom at the figure below on the received signal, you should see a harmonic at 20KHz.

   .. figure:: images/exercises/sinewave_loopback/zoom_plot.png
      :alt: Zoom on Plot
      :align: center
      :width: 40em

      Zoom on the plot to see the harmonic at 20KHz

#. To stop running the Python script (if you want to run it again or run another script), close all the tabs by **right clicking on the
   taskbar icon -> Quit x windows** as shown depicted below or close them manually one by one.

   .. figure:: images/exercises/sinewave_loopback/close_tabs.png
      :alt: Close Tabs
      :align: center
      :width: 40em

      Close all tabs to stop the Python script


Using PyADI-IIO with Jupiter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This demonstrates **platform portability**—running the same algorithm on higher-performance hardware with minimal code changes.

Follow these steps:

#. Go to **workshop_exercises→python→sinewave_loopback** and open **python_loopback_sine_jupiter.py** using **Thonny Python IDE**.

#. Observe that only the "Configure SDR" section changed compared to **python_loopback_sine_pluto.py**:

   .. figure:: images/exercises/tx_rx_jupiter_talise/jupiter_config_code.png
      :alt: Configure SDR Code Section
      :align: center
      :width: 40em

      Configure SDR code for Jupiter platform

#. Insert the IP address on line 12 to remotely connect to Jupiter:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ sdr = adi.adrv9002(uri="ip:10.48.65.212") # Create Radio object for Jupiter

#. Run the script. In this example, a sinusoid at 15.360 KHz is transmitted and received (chosen to have an integer
   number of periods at the sample rate of 15.36 Msps).


Using PyADI-IIO with Talise
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow these steps:

#. Go to **workshop_exercises→python→sinewave_loopback** and open **python_loopback_sine_talise_zu11eg.py** using **Thonny Python IDE**.

#. Make the following hardware setup with TX1A_P/N connected to RX1A_P/N via loopback cables.

   .. TODO: Add Talise hardware setup image when available
   .. .. figure:: images/exercises/sinewave_loopback_talise/talise_setup.png
   ..    :alt: Talise Hardware Setup
   ..    :align: center
   ..    :width: 40em
   ..
   ..    Talise hardware setup with loopback connections

#. Observe the "Configure SDR" section for Talise:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ # Configure properties
      $ sample_rate = 30720000  # Sample rate
      $ center_freq = 2000000000  # Center frequency
      $ num_samps = 100000  # Number of samples per call to rx()
      $ frequency = 3000000  # Frequency of complex sinusoid
      $ fc0 = int(center_freq / (sample_rate / 2) * 2**15)  # Digital frequency for TX1
      $
      $ # Create radio object
      $ sdr = adi.adrv9009_zu11eg("ip:10.48.65.182")  # IP address of Talise
      $
      $ # Configure Tx properties
      $ sdr.tx_hardwaregain_chan0 = -10  # TX attenuation in dB
      $ sdr.tx_enabled_channels = [0]
      $ sdr.dds_single_tone(fc0, 0.8, 0)  # Generate tone: freq, scale, channel
      $
      $ # Configure Rx properties
      $ sdr.gain_control_mode_chan0 = "slow_attack"
      $ sdr.rx_enabled_channels = [0]
      $ sdr.rx_buffer_size = num_samps

#. Run the script and observe the output plots showing transmitted and received signals.

   .. TODO: Add Talise output plots image when available
   .. .. figure:: images/exercises/sinewave_loopback_talise/talise_output.png
   ..    :alt: Talise Output Plots
   ..    :align: center
   ..    :width: 40em
   ..
   ..    Output showing transmitted and received signals


Using GNU Radio with Jupiter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This exercise implements the same complex sinusoid loopback using GNU Radio Companion's visual flowgraph environment instead of Python code.

Follow these steps:

#. Make the following hardware setup using Jupiter SDR with TX1A connected to RX1A via loopback cable.

   .. TODO: Add Jupiter hardware setup image when available
   .. .. figure:: images/exercises/gnuradio_sinewave_loopback/jupiter_setup.png
   ..    :alt: Jupiter SDR Hardware Setup
   ..    :align: center
   ..    :width: 40em
   ..
   ..    Jupiter SDR setup with TX1A connected to RX1A via loopback cable

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In GNU Radio Companion, open **Desktop → workshop_exercises → gnuradio → sinewave_loopback_jupiter.grc**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

   .. TODO: Add flowgraph execution screenshot when available
   .. .. figure:: images/exercises/gnuradio_sinewave_loopback/run_flowgraph.png
   ..    :alt: Run GNU Radio Flowgraph
   ..    :align: center
   ..    :width: 40em
   ..
   ..    Click the green arrow to execute the flowgraph

#. Observe the output plots showing transmitted/received samples, spectrum, and constellation diagram.

   .. TODO: Add output plots screenshot when available
   .. .. figure:: images/exercises/gnuradio_sinewave_loopback/output_plots.png
   ..    :alt: GNU Radio Output Plots
   ..    :align: center
   ..    :width: 40em
   ..
   ..    Output plots showing transmitted/received samples, spectrum, and constellation diagram

#. Use the sliders to adjust parameters in real-time:

   * **Frequency slider**: Changes the offset frequency of the complex sinusoid
   * **TX Attenuation slider**: Controls transmit power
   * **RX Gain slider**: Controls receiver gain

#. Click the **Stop** button (red square) when finished.


Doppler Radar with GNU Radio (Pluto)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise demonstrates the Doppler radar effect using GNU Radio Companion, a visual programming environment
for building software-defined radio applications. You will create a continuous-wave (CW) radar system that can
detect motion and measure relative velocity by observing frequency shifts in the received signal.

**What is GNU Radio?**

GNU Radio is a free, open-source software development toolkit that provides signal processing blocks to implement
software-defined radios. It uses a visual flowgraph paradigm where signal processing blocks are connected together
to create complete radio systems. GNU Radio Companion (GRC) provides a graphical interface for building these flowgraphs
without requiring extensive programming knowledge.

**Key features:**

* Visual flowgraph-based development environment
* Extensive library of signal processing blocks
* Hardware integration via gr-iio blocks for ADI devices
* Real-time visualization and debugging tools
* Python-based backend for custom block development

**The Doppler Effect in Radar**

The Doppler effect causes a frequency shift when there is relative motion between the radar and a target.
When an object moves toward the radar, the reflected signal has a higher frequency (positive Doppler shift).
When it moves away, the frequency decreases (negative Doppler shift).

**Doppler Frequency Shift:**

.. math::

   f_d = \frac{2 \cdot v \cdot f_c}{c}

where:

* :math:`f_d` = Doppler frequency shift
* :math:`v` = relative velocity of the target
* :math:`f_c` = carrier frequency
* :math:`c` = speed of light

**How This Exercise Works:**

#. **Transmit**: The Pluto SDR transmits a continuous wave (CW) signal at 2.5 GHz
#. **Reflection**: The signal reflects off your moving hand
#. **Receive**: The Pluto receives the reflected signal with a Doppler-shifted frequency
#. **Processing**: GNU Radio processes the signal to extract the Doppler shift
#. **Visualization**: Real-time plots show the frequency shift, and audio output lets you hear the Doppler tone

   .. figure:: images/exercises/doppler_radar/filter_frequency_diagram.png
      :alt: Band Pass and Reject Filters
      :align: center
      :width: 40em

      Frequency domain filtering: Band Reject Filter removes carrier, Band Pass Filter isolates Doppler shift

**What You Will Observe:**

* Moving your hand toward the antenna increases the frequency (higher pitch sound)
* Moving away decreases the frequency (lower pitch sound)
* The faster the motion, the larger the frequency shift
* Real-time FFT plots visualize the Doppler shift

This is the same principle used in police speed radar guns, weather radar, and automotive collision avoidance systems.

Follow these steps to run the Doppler radar experiment:

#. Make the following setup using Pluto and connect it to your PC:

   .. figure:: images/exercises/doppler_radar/pluto_doppler_setup.png
      :alt: Pluto SDR Doppler Radar Setup
      :align: center
      :width: 40em

      Pluto SDR setup for Doppler radar experiment

#. Open the terminal by simultaneously pressing **Ctrl + Alt + T** on your keyboard.

#. Type the following command in the terminal to open GNU Radio Companion and press Enter:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In *gnuradio-companion*, click on the **File->Open**, and open from **Desktop->workshop_exercises->gnuradio** the
**doppler_radar_pluto.grc** file.

#. To run the flowgraph, press on the grey arrow from the top function bar as indicated below.

   .. figure:: images/exercises/doppler_radar/run_grc.png
      :alt: Run GNU Radio Flowgraph
      :align: center
      :width: 40em

      Run the GNU Radio flowgraph for Doppler radar experiment

#. Move your hand toward and away from the antennas and observe how the sound and the frequency of the received harmonic changes
in real time plots.

The six plots show the received signal at different processing stages: top row displays time-domain waveforms,
while the bottom row shows frequency-domain FFT plots where you can see the Doppler shift peak move left (hand moving away) or
right (hand moving toward) from the center frequency.

   .. figure:: images/exercises/doppler_radar/doppler_plots.png
      :alt: Doppler Radar Plots
      :align: center
      :width: 40em

      Real-time plots of the Doppler radar experiment


Binary Phase Shift Keying (BPSK) in Python using Pluto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise demonstrates Binary Phase Shift Keying (BPSK), a fundamental digital modulation technique used in modern communication
systems. You will transmit digital data (binary bits) through the Pluto SDR, receive it back via a loopback connection, and observe
how software-based signal processing recovers the original data despite real-world impairments.

**What is BPSK?**

Binary Phase Shift Keying is a type of phase modulation where digital information is encoded by shifting the phase of a carrier signal.
In BPSK:

* **Bit 0** is represented by a phase of 180° (or -1 in the I/Q plane)
* **Bit 1** is represented by a phase of 0° (or +1 in the I/Q plane)

This creates two distinct constellation points on the real axis of the I/Q diagram, making BPSK one of the most robust digital
modulation schemes against noise.

   .. figure:: images/exercises/bpsk_loopback/bpsk_modulation_concept.png
      :alt: BPSK Modulation Concept
      :align: center
      :width: 40em

      BPSK modulation: binary bits modulate the phase of the carrier signal

   .. figure:: images/exercises/bpsk_loopback/bpsk_constellation.png
      :alt: BPSK Constellation Diagram
      :align: center
      :width: 40em

      BPSK constellation diagram showing two points at -1 and +1 on the real axis

**Where is BPSK Used?**

BPSK and its variants are used in numerous communication systems:

* **GSM** - Mobile phone networks
* **Satellite Television** - DVB-S and other satellite broadcasting standards
* **Wi-Fi** - Lower data rate modes (802.11b DSSS)
* **GPS and GNSS** - Satellite navigation systems
* **RFID and NFC** - Contactless communication
* **Deep space communications** - Where robustness is critical

**Challenges in Demodulating BPSK Signals**

When receiving BPSK signals in real-world conditions, several impairments must be corrected:

* **Phase Offset**: The local oscillator (LO) at the receiver may have a phase difference from the transmitter
* **Frequency Offset**: Small differences in carrier frequency between TX and RX oscillators
* **Timing Offset**: Clock differences require symbol timing recovery to sample at the right moment
* **Variation with time, distance, and temperature**: These offsets change dynamically

As demonstrated in the previous Doppler radar exercise, frequency varies with distance and motion. These same effects impact digital communications.

**The Power of Software-Defined Radio: All These Problems Can Be Solved by Software!**

This exercise demonstrates how modern SDR systems correct all these impairments in software using sophisticated algorithms:

   .. figure:: images/exercises/bpsk_loopback/tx_rx_flow_diagram.png
      :alt: BPSK Transmitter and Receiver Architecture
      :align: center
      :width: 40em

      BPSK system architecture showing transmitter and receiver signal processing chain

**How the BPSK System Works:**

**Transmitter Chain:**

#. **Configure SDR**: Set center frequency, sample rate, and gain
#. **Create array of bits**: Generate the digital data to transmit (0s and 1s)
#. **Interpolate and remap symbols**: Repeat each bit 16 times for pulse shaping, map bit 0 → -1, bit 1 → +1
#. **Call tx() function**: Transmit the modulated signal

**Receiver Chain:**

#. **Call rx() function**: Receive the modulated signal
#. **Coarse frequency adjustment**: Square the received signal to measure 2× frequency offset, then correct it
#. **Symbol timing recovery**: Use Mueller and Muller clock recovery to select the correct sample from each 16-sample group
#. **Fine frequency and phase adjustment**: Apply Costas loop to lock onto the correct phase and remove residual frequency offset
#. **Plot data**: Visualize constellation diagrams and waveforms to observe signal quality

**Key Signal Processing Techniques:**

* **Frequency Offset Correction**: The received signal is squared (raising phase errors to become visible as frequency offsets), an FFT identifies the peak at 2× the offset frequency, and samples are corrected by multiplying by :math:`e^{-j2\pi f_{offset} t}`

* **Symbol Timing Recovery (Mueller and Muller)**: Since each bit is transmitted as 16 samples, the receiver must identify which of the 16 samples represents the optimal sampling point. The Mueller and Muller algorithm iteratively adjusts the timing offset to lock onto the correct samples.

* **Costas Loop (Fine Synchronization)**: Functions like a phase-locked loop (PLL) that multiplies I × Q samples. For ideal BPSK where Q = 0, this error function is minimized when there is no phase or frequency offset, allowing the loop to lock onto the correct carrier phase.

**What You Will Observe:**

Starting from a noisy, offset constellation with scattered points, you will see the signal progressively improve:

#. **Raw received signal**: Shows significant phase and frequency offset
#. **After coarse frequency correction**: Frequency offset mostly removed, but phase offset remains
#. **After symbol timing recovery**: Correct samples selected, reducing mid-constellation points
#. **After Costas loop**: Clean constellation with two tight clusters at -1 and +1

   .. figure:: images/exercises/bpsk_loopback/bpsk_constellation_progression.png
      :alt: BPSK Signal Recovery Progression
      :align: center
      :width: 40em

      Progression from noisy received signal to clean demodulated constellation

This exercise demonstrates the power of software-defined radio: complex signal processing algorithms running in software can correct real-world impairments that would be difficult or impossible to handle in analog hardware alone.

Follow these steps to run the BPSK transmission and reception experiment:

#. Make the setup from *Figure 15* using Pluto and connect it to your PC.

#. Open the **workshop_exercises** folder from your desktop.

#. Go to **python->bpsk_loopback** subfolder.

#. Right click on **bpsk_pluto_loopback_pluto.py -> Open With Other Application** and select **Thonny Python IDE**
(or any other Python IDE you have installed) from the Recommended Applications list as in *Figure 16*.

#. To run the script, press the green round button from the top left corner in Thonny IDE as in *Figure 17*.

#. To zoom on a plot, use the instructions shown in *Figure 18*.

#. To stop running the Python script (if you want to run it again or run another script), close all the tabs by **right clicking on the
   taskbar icon -> Quit x windows** as shown depicted below in *Figure 19* or close them manually one by one.


Binary Shift Keying (BPSK) in Python using Jupiter or Talise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. From **workshop_exercises->python->bpsk_loopback** subfolder, open **bpsk_jupiter_loopback_jupiter.py (for Jupiter)**
   or **bpsk_talise_loopback_talise_zu11eg.py (for Talise)** using **Thonny Python IDE** as in *Figure 15*.

#. Observe in the script that only the "Configure SDR" code section was changed in **bpsk_jupiter_loopback_jupiter.py** and **bpsk_talise_loopback_talise_zu11eg.py**
   compared to **bpsk_pluto_loopback_pluto.py** from the previous exercise.

   .. figure:: images/exercises/bpsk_loopback/jupiter_config_code.png
      :alt: Configure SDR Code Section
      :align: center
      :width: 40em

      Configure SDR code for Jupiter platform

   .. figure:: images/exercises/bpsk_loopback/talise_config_code.png
      :alt: Configure SDR Code Section
      :align: center
      :width: 40em

      Configure SDR code for Talise platform

#. Insert the IP address given for Jupiter (in **bpsk_jupiter_loopback_jupiter.py**) or for Talise (in **bpsk_talise_loopback_talise_zu11eg.py**)
   to remotely connect to Jupiter or Talise.

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ # For Jupiter (in bpsk_jupiter_loopback_jupiter.py):
      $ sdr = adi.adrv9002(uri="ip:10.48.65.212") # Create Radio object for Jupiter

      $ # For Talise (in bpsk_talise_loopback_talise_zu11eg.py):
      $ sdr = adi.adrv9009_zu11eg("ip:10.48.65.182") # Create Radio object for Talise

#. Run the script as indicated in *Figure 17*.

#. To zoom on the generated figures, use the instructions shown in *Figure 18*.

#. To stop running the Python script or if you want to run it again, use the instructions shown in *Figure 19*.

Quadrature Phase Shift Keying (QPSK) in GNU Radio using Pluto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise demonstrates Quadrature Phase Shift Keying (QPSK), a digital modulation scheme that transmits 2 bits per symbol instead of BPSK's 1 bit per symbol. QPSK uses four phase positions in the I/Q plane to encode data, effectively doubling the data rate in the same bandwidth.

**What is QPSK?**

QPSK encodes two bits into each symbol using four constellation points at 45°, 135°, 225°, and 315°:

* **00**, **01**, **10**, **11** → Four distinct phase positions

This creates twice the spectral efficiency of BPSK while maintaining good noise immunity.

   .. figure:: images/exercises/qpsk_gnuradio/qpsk_constellation.png
      :alt: QPSK Constellation
      :align: center
      :width: 40em

      QPSK constellation (4 points, 2 bits/symbol)

   .. figure:: images/exercises/qpsk_gnuradio/qpsk_ho_modulation.png
      :alt: QPSK Higher Order Modulation Constellation
      :align: center
      :width: 40em

      QPSK higher-order modulation schemes (16-QAM, 32-QAM, 64-QAM, 256-QAM)

**Where is QPSK Used?**

* Satellite communications (DVB-S, GPS)
* Wireless standards (CDMA, LTE, 5G)
* Cable modems (DOCSIS)
* Point-to-point microwave links

**How This Exercise Works:**

You will receive QPSK-modulated data packets containing hexadecimal values using GNU Radio. The flowgraph performs symbol synchronization,
frequency locking, and constellation decoding to recover the transmitted data.

   .. figure:: images/exercises/qpsk_gnuradio/qpsk_gnuradio_flowgraph.png
      :alt: QPSK GNU Radio Flowgraph
      :align: center
      :width: 40em

      GNU Radio flowgraph for receiving QPSK-modulated data using Pluto SDR

Follow these steps to receive QPSK-modulated data:

#. Make the following setup using Pluto and connect it to your PC:

   .. figure:: images/exercises/qpsk_pluto/qpsk_pluto_setup.png
      :alt: QPSK Pluto Setup
      :align: center
      :width: 40em

      QPSK Pluto Setup

#. In *gnuradio-companion*, open **qpsk_point_to_point_rx_console.grc** from **workshop_exercises->gnuradio->qpsk_point_to_point_console**.

   Run the flowgraph and observe the received message stored in "msg_var" variable as depicted below.

   .. figure:: images/exercises/qpsk_pluto/qpsk_point_to_point_rx_console.png
      :alt: QPSK Point to Point RX Console
      :align: center
      :width: 40em

      QPSK Point to Point RX Console

Receiving QPSK modulated Video with SDRs using Pluto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise demonstrates a real-world application of QPSK modulation: receiving Digital Amateur Television (DATV). Using the open-source `SDRangel <https://www.sdrangel.org/>`_ software, you will receive and display live video transmitted over the air using QPSK modulation, the same technique used in satellite TV broadcasting.

**What is DATV?**

Digital Amateur Television (DATV) is a form of amateur radio that transmits video and audio using digital modulation schemes like QPSK. Unlike analog TV, DATV provides:

* Better quality with less interference
* More efficient use of bandwidth
* Error correction capabilities
* Multiple audio/video streams in a single channel

**How This Exercise Works:**

`SDRangel <https://www.sdrangel.org/>`_ is a powerful open-source SDR application that implements a complete DATV receiver chain including QPSK demodulation, Forward Error Correction (FEC), and MPEG-2/H.264 video decoding. The Pluto SDR receives the RF signal, and SDRangel processes it to display the video in real-time.

Follow these steps to receive QPSK-modulated video:

#. Make the setup using Pluto and connect it to your PC as depicted in *Figure 35*:

   .. figure:: images/exercises/qpsk_pluto/qpsk_pluto_setup.png
      :alt: QPSK Pluto Setup
      :align: center
      :width: 40em

      QPSK Pluto Setup

#. Open the terminal by pressing at the same time **Ctrl + Alt + T** on your keyboard.

#. Type the following command in the terminal and press Enter:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ sdrangel

#. The application should be preconfigured. Run the program by pressing the purple arrow as depicted below.

   .. figure:: images/exercises/qpsk_video/sdrangel_run.png
      :alt: Run SDRangel
      :align: center
      :width: 40em

      Run SDRangel to receive QPSK modulated video

#. On DATV window, **check and then uncheck Viterbi** to synchronize the qpsk data **while the program is running** (as shown below).

   .. figure:: images/exercises/qpsk_video/viterbi_sync.png
      :alt: Viterbi Sync
      :align: center
      :width: 40em

      Check and then uncheck Viterbi to synchronize the QPSK data in SDRangel

Spectrum Paint using Pluto
~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise demonstrates a creative application of SDR: "painting" images in the frequency spectrum. By transmitting signals at different frequencies over time, you can create visible patterns on a waterfall display, which shows frequency on the horizontal axis and time on the vertical axis.

**How Spectrum Paint Works:**

A waterfall display is a spectrogram that shows:

* **Frequency** (horizontal axis): Different colors represent signal strength at each frequency
* **Time** (vertical axis): Each new row represents a new time snapshot
* **Amplitude** (color intensity): Brighter colors indicate stronger signals

By carefully controlling which frequencies are transmitted at each moment, you can "draw" images, text, or patterns that become visible as the waterfall scrolls down.

**Applications:**

While spectrum paint is primarily a demonstration, the underlying technique is used in:

* Frequency-hopping spread spectrum (FHSS)
* Chirp radar systems
* Multi-carrier communications
* Signal identification and watermarking

This exercise showcases the flexibility of software-defined radio: the same hardware can transmit any arbitrary frequency pattern by simply changing the software.

Follow these steps to create a spectrum painting:

#. Make the following setup using Pluto and connect it to your PC.

#. Open in *gnuradio-companion* the **paint_tx.grc** file from **workshop_exercises->gnuradio->spectrum_paint** and run the flowgraph.

#. Observe the waterfall display as the spectrum painting appears, created by the Pluto SDR transmitting the frequency pattern.

   .. figure:: images/exercises/spectrum_paint/paint_tx.png
      :alt: Spectrum Paint Waterfall Display
      :align: center
      :width: 40em

      Waterfall display showing the spectrum painting created by transmitting controlled frequency patterns
