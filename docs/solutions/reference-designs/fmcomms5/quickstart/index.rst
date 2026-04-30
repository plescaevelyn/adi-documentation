.. _fmcomms5-quickstart:

Quick Start
===========

The following guides provide step-by-step instructions for an initial
system setup of the :adi:`AD-FMCOMMS5-EBZ <AD-FMCOMMS5-EBZ>` on
various FPGA development boards. They cover bitstream loading, booting
a Linux distribution, and launching the IIO Oscilloscope for RF
waveform capture and playback.

.. toctree::
   :hidden:

   zc702
   zc706
   zcu102

Supported carriers
------------------

The :adi:`AD-FMCOMMS5-EBZ <AD-FMCOMMS5-EBZ>` connects to a carrier
board via **two adjacent FMC connectors**.

.. list-table::
   :header-rows: 1

   -  - Carrier board
      - Connector
   -  - :xilinx:`ZC706`
      - Dual FMC (HPC)
   -  - :xilinx:`ZC702`
      - Dual FMC (LPC)
   -  - :xilinx:`ZCU102`
      - Dual FMC (HPC)

Supported environments
----------------------

.. list-table::
   :header-rows: 1

   -  - Carrier board
      - HDL
      - Linux
      - No-OS
   -  - :xilinx:`ZC706`
      - Yes
      - Yes
      - ---
   -  - :xilinx:`ZC702`
      - Yes
      - Yes
      - ---
   -  - :xilinx:`ZCU102`
      - Yes
      - Yes
      - ---

Hardware setup
--------------

.. warning::

   The AD-FMCOMMS5-EBZ uses a dual FMC connector. Ensure your carrier
   board has two adjacent FMC connectors before proceeding.

Connect the AD-FMCOMMS5-EBZ to the carrier's FMC connectors. The
carrier setup requires power, UART (115200 baud), Ethernet, and HDMI
(if available) connections.

.. image:: ../images/fmcomms5-loopback.jpg
   :alt: AD-FMCOMMS5-EBZ loopback configuration

AD-FMCOMMS5-EBZ + ZC706
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/zc706_fmcomms5.jpg
   :width: 500

#. Insert the prepared SD card into connector J30.
#. Plug the AD-FMCOMMS5-EBZ into the FMC connectors.
#. Connect an HDMI display to P1.
#. Connect USB keyboard/mouse to J49.
#. Connect 12 V power to J22.
#. Set boot mode switch SW11: 1-Down, 2-Down, 3-Up, 4-Up, 5-Down.
#. Power on and wait ~60 seconds for the system to boot.

AD-FMCOMMS5-EBZ + ZC702
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/zc702_fmcomms5.jpg
   :width: 500

#. Insert the prepared SD card into J64.
#. Plug the AD-FMCOMMS5-EBZ into the FMC connectors.
#. Connect an HDMI display to J3.
#. Connect USB keyboard/mouse to J17.
#. Connect 12 V power to J1.
#. Set boot mode switch SW16 to SD boot position.
#. Power on and wait ~60 seconds for the system to boot.

AD-FMCOMMS5-EBZ + ZCU102
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/zcu102_fmcomms5.jpg
   :width: 500

.. warning::

   The ZCU102 requires two FMC spacers to accommodate the
   AD-FMCOMMS5-EBZ. Ensure the spacers are installed before
   connecting the board.

   .. image:: ../images/fmc_spacers.jpg
      :width: 500

#. Insert the prepared SD card into connector J100.
#. Plug the AD-FMCOMMS5-EBZ into the dual FMC connectors (HPC0 and
   HPC1).
#. Connect USB UART J83 (Micro-USB) to your host PC.
#. Connect Ethernet cable.
#. (Optional) Connect a DisplayPort display to J12.
#. (Optional) Connect USB keyboard/mouse to J96.
#. Set SD card boot mode: SW6[4:1] = OFF, OFF, OFF, ON.
#. Connect 12 V power to J52.
#. Power on and wait ~60 seconds for the system to boot.

Getting started
---------------

-  :doc:`ZC702 quick start guide <zc702>`
-  :doc:`ZC706 quick start guide <zc706>`
-  :doc:`ZCU102 quick start guide <zcu102>`
