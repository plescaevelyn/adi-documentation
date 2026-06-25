.. _m1k-firmware:

Firmware Upgrade Procedures
===============================================================================

The ADALM1000 firmware can be updated using two methods: the smu command-line
tool or the Pixelpulse graphical interface.

Update Using smu
-------------------------------------------------------------------------------

The ``smu`` tool from the libsmu library enables firmware flashing from the
command line.

1. Download the latest ``m1000.bin`` file from the
   `m1k-fw GitHub releases <https://github.com/analogdevicesinc/m1k-fw/releases>`__

2. Flash the firmware:

   .. code-block:: bash

      smu -f /path/to/m1000.bin

Command-line options:

* ``-f, --flash <firmware image>`` - Flash firmware to the device

Automatic Update from Pixelpulse
-------------------------------------------------------------------------------

Pixelpulse provides automated firmware management:

* Detects outdated firmware on connected devices
* Downloads latest firmware automatically if internet connectivity exists
* Accessible through the Device Manager interface (version 0.86+)

Device states displayed in Pixelpulse:

* **Firmware is up to date** - No action required
* **Device has older firmware** - Update recommended
* **Device in programming mode** - Firmware update in progress

Windows Driver Troubleshooting
-------------------------------------------------------------------------------

For proper firmware upgrades on Windows, verify the device appears correctly
in Device Manager.

**Correct configuration** - Devices appear under "Universal Serial Bus devices":

* ``ADALM1000 SAM-BA WinUSB`` (programming mode)
* ``ADALM1000 WinUSB`` (normal operation)

**Incorrect configuration** - Device appears under "Ports (COM & LPT)":

This requires manual driver update through Windows Device Manager. Right-click
the device and select "Update driver" to install the correct WinUSB driver.
