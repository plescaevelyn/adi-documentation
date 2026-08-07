.. _m1k-hardware:

ADALM1000 Hardware
===============================================================================

Introduction
-------------------------------------------------------------------------------

The ADALM1000 is a learning tool designed to make interacting with the world
around you easier and more intuitive. It features two analog channels for
sourcing and measuring waveforms in voltage or current modes, operating from
0-5V with current capabilities of ±200mA.

USB Interface
-------------------------------------------------------------------------------

The ADALM1000 uses an ARM Cortex M3 microcontroller as the interface between
the USB connection and the analog systems. Key features include:

* SPI buses for DAC and ADC communication
* Timer-counters and PWM outputs
* I2C interface
* Programmable I/O pins
* 32KB SRAM
* 128KB NAND flash memory

Power Architecture
-------------------------------------------------------------------------------

The ADALM1000 operates entirely from USB power using a sophisticated voltage
regulation architecture:

* **ADP7118** - Linear regulator providing 3.3V supply
* **ADM1177** - Hot-swap controller with overcurrent protection
* **ADP1614** - Boost converter generating 6.5V rail
* **ADM7171** - Adjustable regulator providing 6V output
* **ADP2442** - Inverting buck-boost converter for -1V rail
* **ADR381** - Precision 2.5V voltage reference

Analog Front End
-------------------------------------------------------------------------------

Digital-to-Analog Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADALM1000 uses an AD5663R dual-channel 16-bit DAC with SPI-based serial
interface. Low-pass filtering shapes the output waveforms.

Analog-to-Digital Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two AD7682 quad-channel 16-bit ADCs provide simultaneous voltage and current
measurements on both channels.

Servo Loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A feedback control architecture using ADA4661 op-amp and ADG719 analog switch
implements the voltage/current sourcing modes. A high-bandwidth power amplifier
stage with current feedback topology drives the output.

Current Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An AD8210 current-sense amplifier addresses common-mode rejection challenges.
A 0.5Ω current sense resistor maps the full ±200mA range to a 2.5V-centered
output signal.

Output Stage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A four-channel analog switch provides 50Ω tie resistors for voltage/current
division and external measurement range extension.

Design Resources
-------------------------------------------------------------------------------

Design files including schematic, PCB layout, bill of materials, and Allegro
CAD project are available from the
`ADALM1000 product page <https://www.analog.com/ADALM1000>`__.
