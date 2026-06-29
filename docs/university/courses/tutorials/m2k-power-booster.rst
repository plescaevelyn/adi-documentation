.. _m2k-power-booster:

ADALM2000 Power Booster Board
===============================================================================

Overview
-------------------------------------------------------------------------------

The AD-M2KPWR-EBZ is an ADALM2000 add-on board which increases the output
current capability up to 700mA. This board can also be used as a standalone
benchtop power supply with positive and negative outputs.

.. figure:: images/ad-m2kpwr-ebz-top-web.png
   :align: center
   :width: 400

   AD-M2KPWR-EBZ Top view

.. figure:: images/ad-m2kpwr-ebz-bottom-web.png
   :align: center
   :width: 400

   AD-M2KPWR-EBZ Bottom view

Features
-------------------------------------------------------------------------------

- ADALM2000 compatible
- USB Type-C powered (no Power Delivery included)
- Provides two outputs with increased current sourcing capabilities

Description
-------------------------------------------------------------------------------

The AD-M2KPWR-EBZ is a USB Type-C powered board capable of increasing the
output current of ADALM2000's power supplies.

Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **USB Type-C**: 4 - 18 V (validated with RPI USB-C power supply - not
  provided in the kit), 15W (power supply permitting)
- **External (screw terminal connector)**: 4 - 18V; 20W (power supply
  permitting)

Outputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The board supports two control modes:

**Mode 1: M2K Tracking Mode**

Two variable power supplies that track M2K user supplies:

- 0V to 5V (400mA in USB power mode)
- -5V to 0V (400mA in USB power mode)

**Mode 2: POT Mode (Standalone)**

Two independent variable power supplies, adjusted by potentiometers:

- 1.5V to 15V (up to 700mA if powered with 18V)
- -15V to -1.5V (up to 700mA if powered with 18V)

Applications
-------------------------------------------------------------------------------

- General-purpose electronic systems
- Educational applications
- Automated test equipment

Package Contents
-------------------------------------------------------------------------------

- AD-M2KPWR-EBZ board
- Standoffs and screws

.. figure:: images/ad-m2kpwr-ebz-angle-web.png
   :align: center
   :width: 600

   AD-M2KPWR-EBZ Isometric view - Package contents

Getting Started
-------------------------------------------------------------------------------

The AD-M2KPWR-EBZ must be supplied either from a 5.1V 3A USB Type-C power
adapter or from a lab supply using the screw terminal connector. Make sure
that the jumper on the P2 connector is in the position corresponding to the
chosen supply.

.. figure:: images/m2kpwr_supply_jumper.png
   :align: center
   :width: 600

   AD-M2KPWR-EBZ supply select jumper

.. list-table:: P2 Jumper Configuration
   :header-rows: 1
   :widths: 30 70

   * - P2 Position
     - Selected Supply Method
   * - Jumper 1-2 shorted
     - Vext - for external lab supply
   * - Jumper 2-3 shorted
     - Vusb - for USB Type-C power adapter

M2K and POT Modes
-------------------------------------------------------------------------------

M2K Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In M2K mode, the board is plugged into the ADALM2000. After that, the
programmable user supplies of ADALM2000 can be used as usual, but they will
source more current.

- The jumper on connector P7 must be in the M2K- position
- The jumper on connector P6 must be in the M2K+ position

.. figure:: images/m2kpwr_pot_control.png
   :align: center
   :width: 600

   AD-M2KPWR-EBZ POT/M2K mode setup jumpers

.. list-table:: P6 Jumper Configuration (Positive Supply)
   :header-rows: 1
   :widths: 30 40 30

   * - P6 Position
     - Output Voltage
     - Range
   * - Jumper 1-2 shorted
     - Positive supply adjusted by R20
     - 1.5V to 15V
   * - Jumper 2-3 shorted
     - Positive supply of M2K
     - 0V to 5V

.. list-table:: P7 Jumper Configuration (Negative Supply)
   :header-rows: 1
   :widths: 30 40 30

   * - P7 Position
     - Output Voltage
     - Range
   * - Jumper 1-2 shorted
     - Negative supply adjusted by R19
     - -15V to -1.5V
   * - Jumper 2-3 shorted
     - Negative supply of M2K
     - -5V to 0V

POT Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In POT mode, the board can be used as a standalone benchtop power supply. The
output voltage is adjusted with potentiometers R19 and R20. The output voltage
will be available at the same pins: V+ and V-.

Gain Configuration
-------------------------------------------------------------------------------

The board can be adjusted such that the output voltage is double or triple the
value set from the M2K. This feature is only available in M2K mode, and it is
activated by soldering or desoldering the solder jumpers on the bottom of the
board according to the table.

.. note::

   You can find the table with the soldering instructions on the bottom of the
   board.

Schematics and CAD Files
-------------------------------------------------------------------------------

- :adi:`Rev B Schematics <media/en/university/tools/m2k/accessories/02-065173-01-b.pdf>`
- :adi:`Rev B Gerbers <media/en/university/tools/m2k/accessories/09-065173-01b.zip>`
- :adi:`Rev B Cadence Project <media/en/university/tools/m2k/accessories/20-065173-01b.zip>`
