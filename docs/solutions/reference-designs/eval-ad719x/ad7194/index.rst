AD7194 Evaluation Board User Guide
==================================

.. toctree::
   :hidden:

   hardwareguide
   Using the System with ACE Software <softwareguide>

The EVAL-AD7194-ASDZ evaluation kit features the AD7194 which is 4.8 kHz
ultralow noise 24-bit sigma-delta (Σ-Δ) ADCs. The on-chip low noise gain stage
means that signals of small amplitude can interface directly to the ADC. The
internal clock option provides a compact solution for low BW requirements.

The AD7194 ACE Plugin fully configures the AD7194 device register functionality
and provides dc time domain analysis in the form of waveform graphs, histograms,
and associated noise analysis for ADC performance evaluation.

Full specifications on the AD7194 are available in the product data sheet, which
should be consulted in conjunction with this user guide when working with the
evaluation board.

.. image:: ../images/ad7194_blockdiag.png
   :align: center
   :width: 600

Features
--------

-  Full featured evaluation board for the AD7194
-  PC control in conjunction with the system demonstration platform
   (EVAL-SDP-CB1Z/EVAL-SDP-CK1Z)
-  PC software for control and data analysis (time and frequency domain)

Related Documents
-----------------

-  :adi:`AD7194 Data Sheet <media/en/technical-documentation/data-sheets/ad7194.pdf>`

Required Software
-----------------

-  :adi:`ACE Software <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7194asdz.html#eb-documentation>`
-  :adi:`AD7194 ACE Plugin <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7194asdz.html#eb-documentation>`

Quick Start Guide
~~~~~~~~~~~~~~~~~

The following steps highlight the process to begin using the evaluation board.

Equipment Required
------------------

-  :adi:`EVAL-AD7194-ASDZ evaluation board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD7194.html>`
-  PC running Windows with a USB2.0 port and software installed.
-  Controller Board

   -  Option A: :adi:`EVAL-SDP-CK1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`
      and a USB-C cable
   -  Option B: :adi:`EVAL-SDP-CB1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-b.html>`
      and a Micro-USB cable

Getting started
---------------

.. warning::

   Ensure the SDP board is not connected to the USB port of the PC

-  Install the :adi:`ACE Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html?doc=EVAL-AD7383FMCZ-ug-1770.pdf>`
-  :doc:`Ace Plugin Install guide available here <softwareguide>`
-  If :adi:`ACE Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html?doc=EVAL-AD7383FMCZ-ug-1770.pdf>`
   is already installed, update the Plugins to download AD719x Plugin.

-  Connect the EVAL-AD7194-ASDZ to the controller board

   -  **Option A:** Connect the EVAL-AD7194-ASDZ to the EVAL-SDP-CK1Z

      -  Using the 120 pin connector

         -  Screw the two boards together using the plastic screw-washer set
            included in the evaluation board kit to ensure that the boards
            are connected firmly together.
         -  Using the Arduino Connectors

.. image:: ../images/sdp_connect.png
   :align: center
   :width: 400

-  **Option B:** Connect the EVAL-AD7194-ASDZ to the EVAL-SDP-CB1Z

   -  Using the 120 pin connector

      -  Screw the two boards together using the plastic screw-washer set
         included in the evaluation board kit to ensure that the boards are
         connected firmly together.

-  If using Windows® XP, it may be needed to search for the controller board
   drivers. Choose to automatically search for the drivers for the controller
   board if prompted by the operating system.
-  Launch the ACE plugin from the Analog Devices subfolder in the Programs
   Menu.

.. image:: ../images/ace_plugin_open.png
   :align: center
   :width: 300

-  The :doc:`ACE Plugin software <softwareguide>` is a useful tool to ensure
   that the Evaluation board is communicating correctly.

Hardware Guide
~~~~~~~~~~~~~~

:doc:`Visit the hardware guide chapter here <hardwareguide>`
**Contents of the Hardware guide:**

-  :doc:`Set-up Procedures <hardwareguide>`
-  :doc:`Block Diagram <hardwareguide>`
-  :doc:`Hardware Link Options <hardwareguide>`
-  :doc:`On Board Connections <hardwareguide>`
-  :doc:`Power Supplies <hardwareguide>`
-  :doc:`Serial Interface <hardwareguide>`
-  :doc:`Reference Options <hardwareguide>`
-  :doc:`GPIOs <hardwareguide>`
-  :doc:`Schematics <hardwareguide>`
-  :doc:`Bill of Materials <hardwareguide>`

Software Guide
~~~~~~~~~~~~~~

:doc:`Visit the software guide chapter here <softwareguide>`
**Contents of the Software guide:**

-  :doc:`Ace Plugin <softwareguide>`

   -  :doc:`Ace Plugin Install <softwareguide>`

      -  :doc:`Ace Plugin Operation <softwareguide>`

-  :doc:`Virtual Eval Guide <softwareguide>`
