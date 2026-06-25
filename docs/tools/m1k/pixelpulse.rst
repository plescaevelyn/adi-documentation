.. _m1k-pixelpulse:

Pixelpulse 2
===============================================================================

Pixelpulse is an open source application that provides a user interface for
visualizing and manipulating signals while exploring systems attached to
affordable analog interface devices.

The software supports Analog Devices' ADALM1000 across Windows, Linux, and
macOS platforms using the Qt5 graphics toolkit with OpenGL acceleration.

Features
-------------------------------------------------------------------------------

**Signal Manipulation:**

* Click-and-drag signal manipulation
* Voltage and current sourcing
* Function generation (sawtooth, triangle, sinusoidal, square)
* Scroll wheel and multitouch zoom (Shift for Y-axis)
* Temporal panning via X-axis drag

**Device Management:**

Multiple connected ADALM1000 devices can be identified through GUI labels
that trigger LED blinking on the corresponding hardware.

Acquisition Settings
-------------------------------------------------------------------------------

Enables delayed acquisition capture, useful for circuits with delayed
responses:

* Adjustable delay (10 microsecond minimum increment)
* PageUp/PageDown for 1ms steps
* Status bar display option

Display Settings
-------------------------------------------------------------------------------

Customizable visualization parameters:

* Brightness and contrast sliders
* Dot brightness and size adjustment
* Separate time plot and XY plot toggles
* Session save/restore functionality

Data Logging
-------------------------------------------------------------------------------

Long-duration capture capability with CSV export containing minimum, maximum,
and average current/voltage readings at 1 or 10-second intervals per device
channel.

**Log File Locations:**

* **Windows:** ``C:/Users/<User>/AppData/Roaming/ADI/Pixelpulse2/logging``
* **Linux:** ``~/.local/share/ADI/Pixelpulse2/logging``
* **macOS:** ``~/Library/Application Support/ADI/Pixelpulse2/logging``

Download
-------------------------------------------------------------------------------

Pre-compiled binaries are available on the
`Pixelpulse GitHub releases page <https://github.com/analogdevicesinc/Pixelpulse2/releases>`__
for Windows and macOS.

Linux users can build from source. Root privileges may be required for
device access unless udev rules are configured.
