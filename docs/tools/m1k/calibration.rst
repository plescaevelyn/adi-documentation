.. _m1k-calibration:

ADALM1000 Calibration Procedure
===============================================================================

.. note::

   Revision F of the ADALM1000 is calibrated at the factory and does not
   require user calibration.

Requirements
-------------------------------------------------------------------------------

Calibration requires:

* Digital Multimeter (DMM)
* Resistor valued between 2.5Ω and 25Ω
* Pixelpulse v0.88 or later
* Firmware version v2.06 or later

Calibration Points
-------------------------------------------------------------------------------

The calibration procedure measures at these reference points:

**Voltage Calibration:**

* 0V
* 2.5V

**Current Calibration:**

* 0A
* +100mA
* -100mA

Calibration File
-------------------------------------------------------------------------------

The calibration data is stored in a text file with reference-value pairs
organized by channel (A/B) and measurement type (voltage/current measurement
and sourcing).

Storing Calibration Data
-------------------------------------------------------------------------------

Use the smu binary to write calibration data to the device:

.. code-block:: bash

   smu --write-calibration /path/to/calibration/file

Semi-Automated Procedure
-------------------------------------------------------------------------------

The ALICE 1.3 Desktop Software includes a semi-automated calibration method
using an AD584 precision voltage reference from the ADALP2000 parts kit.

This method simplifies the calibration process by guiding the user through
each step and automatically calculating correction factors.
