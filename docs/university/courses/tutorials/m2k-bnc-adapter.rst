.. _m2k-bnc-adapter:

ADALM2000 BNC Adapter Board
===============================================================================

The :adi:`AD-M2KBNC-EBZ` is an :adi:`ADALM2000` add-on board which allows the
user to connect oscilloscope probes and other test leads to the analog inputs
of M2K.

.. figure:: images/ad-m2kbnc-ebz-top-web.png
   :align: center
   :width: 300

   AD-M2KBNC-EBZ Top view

.. figure:: images/ad-m2kbnc-ebz-bottom-web.png
   :align: center
   :width: 300

   AD-M2KBNC-EBZ Bottom view

Features
-------------------------------------------------------------------------------

- AC or DC coupling on all channels
- Possibility to reconfigure the analog inputs as differential input channels
- Access to all other ADALM2000 output pins
- Oscilloscope probes, BNC to grabber cables and mini grabber test clips are
  included in the package

Description
-------------------------------------------------------------------------------

The AD-M2KBNC-EBZ has 2 single ended input channels and 2 single ended output
channels. All these channels are terminated in a right-angle BNC connector
which provides quick connection and a locking mechanism.

The single ended input channels can be reconfigured as differential input
channels by modifying a solder jumper on the bottom of the board. In this way,
all 4 BNC connectors will be used for the analog input section and the output
of the M2K is still available on the 30 pin header of the board.

Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Electronic test and measurement equipment
- General-purpose signal processing applications
- Automated test equipment
- Educational applications

Package Contents
-------------------------------------------------------------------------------

- AD-M2KBNC-EBZ
- 2 x Oscilloscope Probes (PA360 60MHz x1 & x10 Passive Probe)
- 2 x BNC to grabber cables
- 10 x mini grabber test clips

.. figure:: images/ad-m2kbnc-ebz-angle-web.png
   :align: center
   :width: 600

   AD-M2KBNC-EBZ Isometric view

.. figure:: images/ad-m2kbnc-ebz_oscilloscope_probes-web.png
   :align: center
   :width: 250

   Oscilloscope Probes

.. figure:: images/ad-m2kbnc-ebz_bnc_to_grabber_cables-web.png
   :align: center
   :width: 250

   BNC to grabber cables

.. figure:: images/ad-m2kbnc-ebz_mini_grabber_test_clips-web.png
   :align: center
   :width: 250

   Mini grabber test clips

Getting Started
-------------------------------------------------------------------------------

The BNC adapter board is simply plugged into the ADALM2000 and can be used
straight away. It does not need any supply or additional circuitry.

.. figure:: images/20220314_104919.jpg
   :align: center
   :width: 400

   AD-M2KBNC-EBZ connected to ADALM2000

AC/DC Coupling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/coupling_highlight.png
   :align: center
   :width: 400

   AD-M2KBNC-EBZ jumpers for AC/DC coupling

The input and output channels of this board can be AC or DC coupled using the
shunt jumpers. The following table presents the jumper configuration:

.. list-table::
   :header-rows: 1
   :widths: 30 25 25 20

   * - Jumper
     - Missing
     - Jumper 1-2 shorted
     - Jumper 2-3 shorted
   * - S1 - Analog In channel 1
     - inoperable/disconnected
     - DC coupled
     - AC Coupled
   * - S2 - Analog In channel 2
     - inoperable/disconnected
     - DC coupled
     - AC Coupled
   * - P4 - Analog Out channel 1
     - inoperable/disconnected
     - DC coupled
     - AC Coupled
   * - P5 - Analog Out channel 2
     - inoperable/disconnected
     - DC coupled
     - AC Coupled

Differential Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD-M2KBNC-EBZ` inputs are reconfigurable. By default 1+ and 2+
channels are referenced to the GND of the board and are single ended input
channels. There are some solder jumpers on the bottom of the board that allow
the user to change the default configuration and use the differential inputs,
as ADALM2000 allows this. If the jumpers are soldered as in the table below,
the BNC connectors J3 and J4 correspond to channels 1- and 2- of the ADALM2000.

.. list-table::
   :header-rows: 1
   :widths: 10 10 10 10 10 10 10 10

   * - JP1
     - JP2
     - JP3
     - JP4
     - J1
     - J2
     - J3
     - J4
   * - 1-2
     - 1-2
     - 1-2
     - 1-2
     - 1+
     - 2+
     - W1
     - W2
   * - 2-3
     - 2-3
     - 2-3
     - 2-3
     - 1+
     - 2+
     - 1-
     - 2-

.. figure:: images/input_path_single_ended.png
   :align: center
   :width: 400

   AD-M2KBNC-EBZ bottom solder jumpers - Single ended inputs

.. figure:: images/input_path_differential.png
   :align: center
   :width: 400

   AD-M2KBNC-EBZ bottom solder jumpers - Differential inputs
