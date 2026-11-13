.. collection:: Analog Attach on Alif
   :subtitle: Linux and Zephyr on the Alif E8 DevKit with ADI DataX™.
   :label: workshop

   Bring up an accelerometer and an ADAC on the Alif E8 DevKit, under Linux
   and Zephyr, and access them over IIO.

   system-level:
     - .

Analog Attach on Alif
=====================

Introduction
------------

Analog Attach is a hands-on training on bringing up ADI devices on the Alif
Ensemble E8 DevKit, using the ADI DataX™ software stack. You will run the same
two Click boards, an accelerometer and an ADAC, under two different operating
systems: Linux on the A32 cores and Zephyr on the M55-HE core. Both expose the
devices over the network using IIO, so you can read them with the same tools.

.. contents:: Workshop Contents
   :local:
   :depth: 2

Prerequisites
-------------

Hardware
~~~~~~~~

- Alif E8 DevKit
- USB-C cable
- Ethernet cable
- Shuttle Click, to plug the Click boards in the mikroBUS socket
- Accel Click (ADXL345)
- ADAC Click (AD5593R)
- Windows PC with an Ethernet port

Software
~~~~~~~~

- Windows 10 or Windows 11, with the Alif_Training WSL image, see
  :doc:`wsl_setup`
- `VS Code <https://code.visualstudio.com/>`__ with the WSL extension
- `Scopy <https://github.com/analogdevicesinc/scopy/releases>`__ on Windows

.. note::

   The Alif_Training WSL image already contains the workspace, the toolchains
   and the build results for both demos. If you follow the workshop with the
   image, you do not need to run the time consuming build commands. They are
   marked in the text, so you can skip them and focus on the DataX™ workflow
   without worrying about build times.

.. warning::

   **DO NOT run** ``make clean``, ``make mrproper``, ``make distclean``,
   ``git clean`` or any similar command that deletes build results in the
   **Buildroot tree** (``$WS/br2-external/buildroot``). This is the prebuilt
   tree: the WSL image already contains the finished Linux build, and cleaning
   it means rebuilding everything from scratch, which takes a very long time. If something looks wrong, ask the instructor instead
   of cleaning.

Learning Objectives
-------------------

By the end of this workshop, you will:

#. Understand how a device driver, a device tree and the IIO subsystem work
   together to expose a device to applications.
#. Understand the role of Buildroot and west in building a Linux and a Zephyr
   image.
#. Flash a Linux image and a Zephyr image to the MRAM of an Alif E8 DevKit.
#. Access an accelerometer and an ADAC over the network, using the IIO tools
   and Scopy.

Setup
-----

.. toctree::
   :maxdepth: 1

   wsl_setup

Workshop
--------

.. warning::

   **DO NOT run** ``make clean``, ``make mrproper`` or any similar command in
   the Buildroot tree, see the warning above.

Overview
~~~~~~~~

There are two demos. Only one of them is on the board at a time, flashing one
replaces the other. Both expose an Accel Click (ADXL345) and an ADAC Click
(AD5593R) over IIO.

.. list-table::
   :header-rows: 1

   * - Demo
     - Runs on
     - Board IP
     - Accel Click I2C jumper
   * - A: Linux
     - A32 cores
     - ``192.0.2.10``
     - ``0x53``
   * - B: Zephyr
     - M55-HE core
     - ``192.0.2.1``
     - ``0x1D``

The workshop follows these steps:

#. Hardware: Click boards, cables and jumper.
#. PC setup: USB into WSL, PC IP address and environment.
#. Demo A: Linux on the A32 cores.
#. Demo B: Zephyr on the M55-HE core.

Each hands-on follows the same loop: **build**, **flash**, **run**, **test**.

Background
~~~~~~~~~~

**Device driver**
   Code that knows how to handle a particular device. It gives user space the
   right interfaces to access the device, and hides the hardware details from
   applications. In Linux, drivers are written in C and live in the kernel tree,
   for example ``drivers/iio/accel/adxl345_core.c``.

**Device tree**
   A data structure and language that describes the hardware connected to the
   system. It is compiled to a ``.dtb`` and passed to the kernel at boot. The
   ``compatible`` string of a node selects the driver for it. Zephyr uses
   device trees too: boards and shields are device tree overlays.

**IIO**
   The Linux Industrial Input/Output subsystem supports ADCs, DACs,
   accelerometers, gyroscopes, RF transceivers and other sensors. Each device
   shows up in sysfs, under ``/sys/bus/iio/devices/``, as one folder per device
   and one file per attribute. ``libiio`` gives access to the same devices
   locally or over the network, with tools such as ``iio_info``, and
   applications such as Scopy.

**Buildroot**
   A cross-build tool that generates a complete embedded Linux image
   (toolchain, bootloader, kernel and root filesystem) from one configuration.
   It runs on the PC and builds for the target.

**west**
   The Zephyr meta-tool. It fetches the projects listed in the manifest, runs
   the build and can flash. The application and the kernel are built together
   into one small firmware image.

Golden rules
~~~~~~~~~~~~

Read these once, and follow them every time you flash.

#. **SW4 = SE** to flash, **SW4 = U2** to run. SE is the flashing port, U2 is
   the demo console.
#. **Exit picocom before every flash**, with ``Ctrl-A`` then ``Ctrl-X``, or
   replug the USB cable. The flasher needs the serial port for itself.
#. **Press RESET (SW1) after every flash**. The new image only starts after a
   reset.

The flash cycle is: exit picocom, set SW4 = SE, flash, set SW4 = U2, open
picocom, press RESET, test.

Assemble the hardware
~~~~~~~~~~~~~~~~~~~~~

#. Plug the Shuttle Click into the mikroBUS socket. The Accel Click and the
   ADAC Click go on it.
#. Set the Accel Click I2C jumper: ``0x1D`` for Zephyr, ``0x53`` for Linux.
#. Connect the Ethernet cable from the board to the PC.
#. Connect the USB-C cable to **J3 "PRG USB"**. It also powers the board.

The PC talks to the board over two links. The USB-C cable is used for the
console, flashing and power. The Ethernet cable is used for ``ping``,
``iio_info`` and Scopy.

Set up the PC
~~~~~~~~~~~~~

Bring the USB serial port into WSL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is done once per session. Install ``usbipd`` once, see
:ref:`alif-analog-attach wsl-setup-usb`. Then, from PowerShell:

.. code:: powershell

   # find "USB Serial Device (COMx), BULK interface", note its BUSID
   usbipd list

   # once per PC, PowerShell as Administrator
   usbipd bind --busid <BUSID>

   # keep this window open
   usbipd attach --wsl --busid <BUSID> --auto-attach

From WSL, check that the port is available:

.. code:: bash

   ls /dev/ttyACM*          # expect /dev/ttyACM0

Give the PC an Ethernet address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is done once per session. Find the name of your Ethernet adapter, then
give it a fixed address, in PowerShell as administrator:

.. code:: powershell

   # find your Ethernet adapter name, e.g. "Ethernet 2"
   Get-NetAdapter

   New-NetIPAddress -InterfaceAlias "Ethernet 2" -IPAddress 192.0.2.2 -PrefixLength 24

Replace ``Ethernet 2`` with the name of your adapter. The addresses are PC
``192.0.2.2``, Zephyr board ``192.0.2.1`` and Linux board ``192.0.2.10``.

Set up the WSL environment
^^^^^^^^^^^^^^^^^^^^^^^^^^

Do this in every new WSL terminal:

.. code:: bash

   export WS=~/demo-electronica
   export SETOOLS=$WS/app-release-exec-linux
   export PATH=$WS/libiio/build/utils:$PATH      # libiio v1 tools
   export LD_LIBRARY_PATH=$WS/libiio/build

   iio_info -V

The expected version is ``1.0.0``. Open two WSL terminals: one to build and
flash, and one for ``picocom``.

Demo A: Linux
~~~~~~~~~~~~~

Build the Linux image with Buildroot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   If you are following along with the Alif_Training WSL image, **skip this
   step**. The image is already built, and ``output/images`` contains
   the results. Go to `Flash Linux to MRAM`_.

.. code:: bash

   export PATH=$(echo "$PATH" | tr ':' '\n' | grep -v '^/mnt/' | grep -v ' ' | paste -sd:)
   cd $WS/br2-external
   git submodule init
   git submodule update
   cd buildroot
   make BR2_EXTERNAL="${PWD}/.." alif_devkit_e8_defconfig
   support/kconfig/merge_config.sh .config ../configs/alif.fragment ../configs/buildroot.fragment
   make -j$(nproc)

The first line removes the Windows paths from ``PATH``, Buildroot fails without
it. The build is finished when ``output/images`` contains ``xipImage`` and
``rootfs.cramfs``.

Flash Linux to MRAM
^^^^^^^^^^^^^^^^^^^

First exit picocom (``Ctrl-A`` ``Ctrl-X``), then set **SW4 = SE**.

.. code:: bash

   cd $WS/buildroot/output/images
   cp bl32.bin *.dtb xipImage rootfs.cramfs  $SETOOLS/build/images/
   cp atoc.json se-device-config.json        $SETOOLS/build/config/
   cd $SETOOLS
   ./app-gen-toc -f build/config/atoc.json
   ./app-write-mram -p

The flashing is done when ``app-write-mram`` finishes without
``Target did not respond``.

Run and test Linux
^^^^^^^^^^^^^^^^^^

#. Set **SW4 = U2**.
#. Open the console in the second terminal:

   .. code:: bash

      picocom -b 115200 /dev/ttyACM0

#. Press **RESET (SW1)** and wait for Linux to boot.
#. From the first terminal, check that the board answers and lists its devices:

   .. code:: bash

      ping -c 3 192.0.2.10
      iio_info -u ip:192.0.2.10

Demo B: Zephyr
~~~~~~~~~~~~~~

Build the Zephyr firmware
^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   If you are following along with the Alif_Training WSL image, **skip all the
   build commands in this section**: creating the workspace, fetching the
   sources and the toolchain, and building. The workspace is already set up and
   the firmware is built, so go to `Flash Zephyr to MRAM`_.

#. Create the workspace and initialize west:

   .. code:: bash

      mkdir zephyr-alif
      cd zephyr-alif
      python3 -m venv .venv
      source .venv/bin/activate
      pip install --upgrade pip
      pip install west pyelftools jsonschema
      west init -m git@github.com:adi-innersource/zephyr.git --mr alif-electronica-demo

   The virtual environment keeps west and its Python packages isolated from the
   system Python. The ``git@`` URL needs your GitHub SSH access.

#. Add the libiio module to the manifest, by creating
   ``zephyr/submanifests/libiio.yml`` with:

   .. code:: yaml

      manifest:
        remotes:
          - name: adi-innersource
            url-base: git@github.com:adi-innersource
        projects:
          - name: libiio
            remote: adi-innersource
            revision: 8a1e8c88f9d802832db5c6015e26babccacd5aec
            path: modules/lib/libiio

#. Fetch the sources and the toolchain:

   .. code:: bash

      west update
      west packages pip --install
      west zephyr-export
      west sdk install --gnu-toolchains arm-zephyr-eabi

   ``west update`` downloads all the projects, including libiio. ``west
   packages pip --install`` installs the Python dependencies of Zephyr,
   ``west zephyr-export`` registers this Zephyr for CMake, and ``west sdk
   install`` installs the Arm GNU toolchain only.

#. Build the firmware, as a single line:

   .. code:: bash

      west build -p -d build-alif-shuttle -b ensemble_e8_dk/ae822fa0e5597ls0/rtss_he modules/lib/libiio/zephyr/samples/iiod -T sample.iiod.alif_shuttle_click

   .. list-table::
      :header-rows: 1

      * - Option
        - Meaning
      * - ``-p``
        - Pristine build, start clean
      * - ``-d build-alif-shuttle``
        - Build directory
      * - ``-b ensemble_e8_dk/.../rtss_he``
        - Target: E8 DevKit, M55-HE core
      * - ``modules/lib/libiio/zephyr/samples/iiod``
        - The application: IIO daemon sample
      * - ``-T sample.iiod.alif_shuttle_click``
        - Sample variant for the Shuttle Click

   The build is finished when it ends without errors and creates ``zephyr.bin``.

Flash Zephyr to MRAM
^^^^^^^^^^^^^^^^^^^^

First exit picocom (``Ctrl-A`` ``Ctrl-X``), then set **SW4 = SE**.

.. code:: bash

   cp $WS/libiio/build-alif-shuttle/zephyr/zephyr.bin $SETOOLS/build/images/
   cp $WS/iiod-alif-shuttle/iiod-he-cpu.json          $SETOOLS/build/config/
   cd $SETOOLS
   ./app-gen-toc -f build/config/iiod-he-cpu.json
   ./app-write-mram -p

``iiod-he-cpu.json`` is the boot table. It tells the Secure Enclave (SE) to boot
``zephyr.bin`` on the HE core from MRAM. The same file works for your own build
and for the prebuilt image. The flashing is done when ``app-write-mram``
finishes without ``Target did not respond``.

Run and test Zephyr
^^^^^^^^^^^^^^^^^^^

#. Set **SW4 = U2**.
#. Open the console in the second terminal:

   .. code:: bash

      picocom -b 115200 /dev/ttyACM0

#. Press **RESET (SW1)**. You should see:

   .. code:: text

      *** Booting Zephyr OS build v4.5.0-rc1-... ***
      <inf> phy_mii: PHY (1) Link
      speed 100 Mb, full duplex

#. From the first terminal, test the board:

   .. code:: bash

      ping -c 3 192.0.2.1
      iio_info -u ip:192.0.2.1
      iio_attr -u ip:192.0.2.1 -c adxl345 accel_x raw

   ``ping`` should answer, ``iio_info`` should list ``adxl345`` and
   ``ad5593r``. Tilt the board and run ``iio_attr`` again, the value should
   change.

See the accelerometer live in Scopy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Open Scopy on Windows.
#. Add the device ``ip:192.0.2.1``.
#. Plot ``adxl345`` ``accel_x``, ``accel_y`` and ``accel_z``.
#. Tilt the board and watch the traces move.

No-OS
~~~~~

The same ADI devices can also be used without an operating system, with the
`no-OS <https://github.com/analogdevicesinc/no-os>`__ drivers. They are written
in C, with no dependencies other than the C runtime, and use a hardware
abstraction layer (HAL) for the platform, so the same driver can run on
different platforms.

Conclusion
----------

You ran the same Accel Click and ADAC Click under Linux and Zephyr, and read
them over IIO with the same tools. The device driver, the device tree and IIO
are the same concepts in both cases, only the way the image is built and
flashed changes.

Resources
---------

- `Buildroot <https://buildroot.org/>`__
- `Zephyr documentation <https://docs.zephyrproject.org/>`__
- `libiio <https://github.com/analogdevicesinc/libiio>`__
- `no-OS <https://github.com/analogdevicesinc/no-os>`__
