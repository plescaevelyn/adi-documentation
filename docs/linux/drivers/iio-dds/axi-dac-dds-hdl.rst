:orphan:

.. _linux axi_dac_hdl:

AXI DAC HDL Linux Driver
========================

This driver provides Linux IIO framework support for FPGA-based DAC transport
layer cores.

Supported Devices
-----------------

The driver supports the following DAC converter models:

- AD9122, AD9136, AD9144, AD9152, AD9154, AD9162
- AD9171, AD9172, AD9173, AD9174, AD9175, AD9176
- AD9361, AD9364, AD9371, AD9739A, AD9783

Supported Evaluation Boards
---------------------------

- AD-FMCOMMS series (1-5, 11-EBZ)
- AD-FMCDAQ2/3-EBZ
- AD9739A Native FMC and Interposer variants
- AD9783 Evaluation Board configurations
- ADRV9371/9009/9008 platforms
- AD9171-9176 Evaluation Board

Supported HDL Cores
-------------------

- Generic AXI DAC
- DAC JESD204B Transport Peripheral
- AXI_AD9144, AXI_AD9361, AXI_AD9371, AXI_AD9783

Operation Modes
---------------

Standalone Mode
~~~~~~~~~~~~~~~

Driver controls FPGA transport layer only; converter configured separately via
independent driver. Linux clock framework manages sampling frequency awareness.

Linked Mode
~~~~~~~~~~~

Converter device (typically SPI-connected) instantiates first. AXI-DAC driver
probes subsequently via deferred probe mechanism. Both register as unified IIO
device with common attributes/channels. Device tree ``spibus-connected``
phandle connects drivers.

Core Functionality
------------------

The transport layer implements:

- Polyphase dual-tone DDS (Direct Digital Synthesis) per channel
- DMA-based waveform buffer mechanism
- Arbitrary data loading with cyclic/streaming modes
- Register map accessible via common base addresses

Device Tree Configuration
-------------------------

Required Properties
~~~~~~~~~~~~~~~~~~~

- ``compatible`` - Specifies device variant (e.g., "adi,axi-ad9361-dds-6.00.a")
- ``reg`` - Base address and register space size

Optional Properties
~~~~~~~~~~~~~~~~~~~

- ``adi,axi-dds-default-scale`` - Power-up DDS scale (16-bit fractional)
- ``adi,axi-dds-default-frequency`` - Startup DDS frequency
- ``adi,axi-dds-parity-enable`` - Enable parity mode (default: frame mode)
- ``adi,axi-dds-parity-type-odd`` - Use odd parity (default: even)
- ``adi,axi-dds-1-rf-channel`` - Single RF channel (default: 2 channels)
- ``adi,axi-interpolation-core-available`` - Interpolation filter present
- ``adi,axi-pl-fifo-enable`` - PL FIFO support
- ``dmas`` / ``dma-names`` - DMA channel specifications ("tx" naming)
- ``spibus-connected`` - Phandle reference to SPI control interface

Device Interface Attributes
---------------------------

DDS Frequency Control
~~~~~~~~~~~~~~~~~~~~~

Located at ``/sys/bus/iio/devices/iio:deviceX/``:

``out_altvoltage[0-7]_TX[1-2]_[I|Q]_F[1-2]_frequency``

Frequency values specified in Hz; driver adjusts to nearest supported rate.

Phase Adjustment
~~~~~~~~~~~~~~~~

``out_altvoltage[0-7]_TX[1-2]_[I|Q]_F[1-2]_phase``

Values in millidegrees; range 0-360000 mD.

Channel Enable/Disable
~~~~~~~~~~~~~~~~~~~~~~

``out_altvoltage[0-7]_TX[1-2]_[I|Q]_F[1-2]_raw``

Writing 1 enables tone, 0 disables.

.. note::

   HDL v7.00+ introduces channel MUX (REG_CHAN_CNTRL_7) with side effects in
   buffer mode.

Amplitude Scaling
~~~~~~~~~~~~~~~~~

``out_altvoltage[0-7]_TX[1-2]_[I|Q]_F[1-2]_scale``

Range: 0.00 to 1.00 (full scale); reading provides available discrete levels.

Sampling Frequency
~~~~~~~~~~~~~~~~~~

``out_altvoltage_sampling_frequency``, ``out_voltage_sampling_frequency``

Propagates clock information from connected converter devices.

External Synchronization
~~~~~~~~~~~~~~~~~~~~~~~~

For systems with EXT_SYNC synthesis parameter enabled:

- ``sync_start_enable`` - Activate trigger mechanism
- ``sync_start_enable_available`` - Lists available modes

Modes:

- **arm** - Activate trigger mechanism for external sync signal
- **disarm** - Deactivate trigger mechanism
- **trigger_manual** - Issue manual external sync event

Buffer Management
-----------------

sysfs Interface
~~~~~~~~~~~~~~~

Located at ``/sys/bus/iio/devices/iio:deviceX/buffer/``:

- ``length`` - Number of sample sets buffer can hold; set before enabling
- ``enable`` - Activates/deactivates buffer; write last after configuration
- ``watermark`` - Maximum samples to wait before poll returns
- ``data_available`` - Bytes available for reading (input) or empty space
  (output)
- ``length_align_bytes`` - Reports DMA alignment requirement

Scan Elements
~~~~~~~~~~~~~

Located at ``/sys/bus/iio/devices/iio:deviceX/scan_elements/``:

- ``out_voltage[0-1]_en`` - Enable channel for buffer capture
- ``out_voltage[0-1]_type`` - Storage format descriptor (e.g., "s12/16" for
  signed 12-bit in 16-bit storage)
- ``out_voltage[0-1]_index`` - Position in buffer

Register Access via Debugfs
---------------------------

Access ``/sys/kernel/debug/iio/iio:deviceX/direct_reg_access`` (requires root).

Reading Registers
~~~~~~~~~~~~~~~~~

.. code:: console

   # echo 0x7 > direct_reg_access
   # cat direct_reg_access

Writing Registers
~~~~~~~~~~~~~~~~~

.. code:: console

   # echo 0x7 0x50 > direct_reg_access

HDL Core Register Access
~~~~~~~~~~~~~~~~~~~~~~~~

Set BIT31 when accessing AXI core registers (distinguishing from SPI control
space):

.. code:: console

   # echo 0x80000000 > direct_reg_access

Kernel Configuration
--------------------

Dependencies:

- ``CONFIG_SPI`` (may be required)
- ``CONFIG_IIO`` (Industrial I/O support)
- ``CONFIG_IIO_BUFFER`` (ring buffer support)
- ``CONFIG_IIO_SW_RING`` (software ring implementation)
- ``CONFIG_IIO_TRIGGERED_SAMPLING`` (triggered data acquisition)

Menuconfig Path::

   Device Drivers → Industrial I/O support → Direct Digital Synthesis
   → [*] Analog Devices CoreFPGA AXI DDS driver
   → [*] Analog Devices AD9122 DAC

Related Documentation
---------------------

- :ref:`IIO Subsystem <iio>`
- :ref:`libiio <libiio>`
- :ref:`AXI_AD9361 IP Core <fpga axi_ad9361>`
