.. _m1k-libsmu:

LibSMU Library
===============================================================================

libsmu is a C++ library containing abstractions for streaming data to and from
USB-connected analog interface devices, currently supporting the Analog Devices
ADALM1000.

Features
-------------------------------------------------------------------------------

* Sourcing of repeated waveforms
* Hardware configuration capabilities
* Signal measurement functionality
* Python bindings through the pysmu module
* Cross-platform support via LibUSB

Installation
-------------------------------------------------------------------------------

Pre-built Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Windows:**
Executable installers (32-bit and 64-bit versions) with optional driver and
development support are available from the
`libsmu releases page <https://github.com/analogdevicesinc/libsmu/releases>`__.

**Linux:**
Debian packages are available for Ubuntu distributions.

**macOS:**
.pkg installers and .tar.gz archives are available.

**Conda:**
Cross-platform package management option:

.. code-block:: bash

   conda install -c conda-forge libsmu

Building from Source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Dependencies (Linux/macOS):**

* libusb development files
* Boost libraries
* CMake and pkg-config
* Python 3 (for bindings)
* Doxygen (for documentation)

**Build Process:**

.. code-block:: bash

   git clone https://github.com/analogdevicesinc/libsmu.git
   cd libsmu
   mkdir build && cd build
   cmake .. -DBUILD_PYTHON=ON
   make
   sudo make install

**CMake Options:**

* ``BUILD_CLI`` - Build command-line tools
* ``BUILD_PYTHON`` - Build Python bindings
* ``WITH_DOC`` - Generate documentation
* ``BUILD_EXAMPLES`` - Build example programs
* ``INSTALL_UDEV_RULES`` - Install udev rules (Linux)

Post-Installation (Linux)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Regenerate the runtime linker cache:

.. code-block:: bash

   sudo ldconfig

Reload udev rules:

.. code-block:: bash

   sudo udevadm control --reload-rules

Documentation
-------------------------------------------------------------------------------

Full API documentation is available at
https://analogdevicesinc.github.io/libsmu/
