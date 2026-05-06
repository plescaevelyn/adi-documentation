.. _sc598-som-boot-guide:
.. _adsp program:

Booting Linux from SPI Flash
==============================

We explain the common development flow after the board already has a
stable U-Boot in SPI flash.

The idea is simple:

* ``u-boot-spl.ldr`` and ``u-boot.ldr`` stay in SPI flash
* You update the Linux payload as needed
* The Linux payload is made of three pieces:
  ``<device-tree>.dtb``, ``Image``, and ``rootfs.ubi``

If you are still bringing up a blank board, start with
:ref:`Getting Started <adsp setup>` first.

What "stable U-Boot" means
--------------------------

In this context, "stable U-Boot" means the early boot chain is already working:

* The ROM can load ``u-boot-spl.ldr`` from SPI flash
* SPL can load ``u-boot.ldr``
* U-Boot reaches its prompt and can access the network and SPI flash

Once that is working, you usually do not need to rewrite U-Boot every time you
change Linux. You can keep the bootloader in place and only refresh the Linux
artifacts.

Files produced by the debug build
---------------------------------

In the current tree under ``br2-external``, the relevant files are:

* ``<device-tree>.dtb``: board description used by the kernel
* ``Image``: the ARM64 Linux kernel image used by ``booti``
* ``rootfs.ubi``: the root filesystem image for the SPI flash rootfs partition
* ``flash.img``: a complete 128 MB SPI flash image containing all pieces

What the debug ``Image`` is
---------------------------

``Image`` is the Linux kernel binary. It is not the whole
flash image, and it is not the device tree.

For SPI boot, U-Boot uses it like this:

1. Load the device tree into RAM
2. Load ``Image`` into RAM
3. Set Linux boot arguments
4. Start the kernel with ``booti``

The relevant U-Boot environment values from
``buildroot/board/adi/patches/uboot/uboot.env`` are ``fdt_addr_r``,
``kernel_addr_r``, and ``fdtfile``.

That means:

* The DTB is loaded into RAM at ``fdt_addr_r``
* The kernel ``Image`` is loaded into RAM at ``kernel_addr_r``
* U-Boot boots the kernel with ``booti ${kernel_addr_r} - ${fdt_addr_r}``

What goes into SPI flash
------------------------

The full SPI image layout is defined in ``genimage.cfg`` under Buildroot.

For Linux bring-up, the important offsets for EV-SC598-SOM are:

.. list-table::
   :header-rows: 1

   * - Item
     - SPI offset
     - Reserved size
     - File
   * - U-Boot SPL
     - ``0x000000``
     - ``256K``
     - ``u-boot-spl.ldr``
   * - U-Boot
     - ``0x040000``
     - ``768K``
     - ``u-boot.ldr``
   * - Device tree
     - ``0x100000``
     - ``64K``
     - ``<device-tree>.dtb``
   * - Kernel
     - ``0x110000``
     - ``32M``
     - ``Image``
   * - Root filesystem
     - ``0x2110000``
     - remainder of flash
     - ``rootfs.ubi``

The practical takeaway is that once U-Boot is already installed, the three
Linux pieces you care about are:

* DTB at ``0x100000``
* Kernel ``Image`` at ``0x110000``
* ``rootfs.ubi`` at ``0x2110000``

How U-Boot boots from SPI flash
-------------------------------

The SPI boot command in the current U-Boot environment is:

.. code-block:: console

   sf probe; sf read ${fdt_addr_r} 0x100000 0x9000; sf read ${kernel_addr_r} 0x110000 0xf00000; setenv bootargs ${bootargs} rootfstype=ubifs root=ubi0:rootfs ubi.mtd=3 rw; booti ${kernel_addr_r} - ${fdt_addr_r}

Broken into steps, this means:

* ``sf probe`` initializes the SPI flash device
* ``sf read ${fdt_addr_r} 0x100000 0x9000`` reads the DTB from SPI into RAM
* ``sf read ${kernel_addr_r} 0x110000 0xf00000`` reads the kernel from SPI into RAM
* ``setenv bootargs ...`` tells Linux to mount a UBIFS root filesystem
* ``booti`` starts the ARM64 kernel

Even though the kernel partition reserves 32 MB in the flash image, U-Boot
currently reads a fixed ``0xf00000`` bytes, which is enough for the current
``Image`` size in this tree.

Programming only the Linux payload
----------------------------------

This is the normal flow when U-Boot is already good and you only want to
replace Linux.

Start a file server on your host:

.. shell:: sh

   $ cd buildroot/output/images
   $ python3 -m http.server

Find your host IP address:

.. shell:: sh

   $ ip a

Then stop at the U-Boot prompt and program the files one by one. Replace
``<build-host-ip>`` with your host IP address.

Program the DTB:

.. code-block:: console

   => dhcp
   => wget ${fdt_addr_r} <build-host-ip>/<device-tree>.dtb
   => sf update ${fdt_addr_r} 0x100000 ${filesize}

Program the kernel ``Image``:

.. code-block:: console

   => wget ${kernel_addr_r} <build-host-ip>/Image
   => sf update ${kernel_addr_r} 0x110000 ${filesize}

Program the UBIFS root filesystem:

.. code-block:: console

   => wget ${kernel_addr_r} <build-host-ip>/rootfs.ubi
   => sf update ${kernel_addr_r} 0x2110000 ${filesize}

The separate RAM address ``${kernel_addr_r}`` is used here as a temporary download
buffer for the root filesystem image.

Programming the whole SPI image
-------------------------------

If you want to refresh everything at once, use ``flash.img`` instead:

.. code-block:: console

   => dhcp
   => wget ${kernel_addr_r} <build-host-ip>/flash.img
   => printenv filesize
   => sf update ${kernel_addr_r} 0x0 ${filesize}

This rewrites the entire 128 MB SPI flash, including U-Boot.

Boot test
---------

After programming the Linux payload, boot it directly from the U-Boot prompt:

.. code-block:: console

   => run sfboot

If the board should boot from SPI flash automatically after reset, make sure
the hardware boot mode switch is set to the SPI position described in
:ref:`Getting Started <adsp setup>`.

Related pages
-------------

* :ref:`Getting Started <adsp setup>` explains how to get initial U-Boot onto
  the board
* :ref:`Linux support <adsp linux-support>` covers repositories and release
  branches
