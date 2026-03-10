:orphan:

.. _linux axi_adc_hdl:

AXI ADC HDL Linux Driver
========================

This driver provides Linux IIO framework support for FPGA-based ADC transport
layer cores.

Supported Devices
-----------------

The driver supports the following ADC devices:

- AD6676, AD9208, AD9234, AD9250, AD9265
- AD9361, AD9364, AD9371
- AD9434, AD9467, AD9625, AD9643, AD9649
- AD9652, AD9680, AD9683, AD9684

Supported Evaluation Boards
---------------------------

- AD-FMCOMMS series (1-6 variants)
- AD-FMCJESDADC1-EBZ
- AD-FMCADC2-EBZ
- AD-FMCDAQ2-EBZ
- AD9467/AD9250/AD9265 Native FMC Cards
- ADRV9371 FMC Card

Driver Architecture
-------------------

The driver comprises two components:

1. **SPI-ADC control driver** - Configures converter internal registers via
   SPI bus
2. **AXI-ADC capture driver** - Controls AXI HDL core registers and DMA
   functionality

Device probing for the data capture driver is delayed until the SPI control
driver is fully probed.

Source Code
-----------

Core driver files:

- ``cf_axi_adc_core.c`` - Main driver
- ``cf_axi_adc_ring_stream.c`` - Ring buffer support
- ``cf_axi_adc.h`` - Header file
- Device-specific drivers: ``ad6676.c``, ``ad9208.c``, ``ad9467.c``,
  ``ad9680.c``, ``ad9361_conv.c``, ``ad9371_conv.c``

Device Tree Configuration
-------------------------

Required Properties
~~~~~~~~~~~~~~~~~~~

- ``compatible`` - Device identifier string
- ``reg`` - Base address and register area size
- ``spibus-connected`` - Phandle to SPI device
- ``dmas`` - DMA controller references
- ``dma-names`` - "tx" and "rx" identifiers

Example Device Tree Entry
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: dts

   cf_ad9467_core_0: cf-ad9467-core-lpc@44a00000 {
       compatible = "xlnx,cf-ad9467-core-1.00.a";
       reg = <0x44A00000 0x10000>;
       dmas = <&rx_dma 0>;
       dma-names = "rx";
       spibus-connected = <&adc_ad9467>;
   };

Kernel Configuration
--------------------

Enable via menuconfig:

- Industrial I/O support
- Ring buffer support
- Triggered sampling support
- "Analog Devices High-Speed AXI ADC driver core"

Driver Attributes
-----------------

Device attributes are located in ``/sys/bus/iio/devices/iio:deviceX/``.

Calibration Controls
~~~~~~~~~~~~~~~~~~~~

- ``in_voltage0_calibscale`` / ``in_voltage1_calibscale`` - Range: 0-1.999999
- ``in_voltage0_calibbias`` / ``in_voltage1_calibbias`` - Range: +/- 16384

Scale Management
~~~~~~~~~~~~~~~~

- ``in_voltage_scale`` - Conversion factor to millivolts
- ``in_voltage_scale_available`` - Lists available scale values

Test Mode
~~~~~~~~~

- ``in_voltage_test_mode_available`` - Lists modes (off, midscale_short,
  pos_fullscale, etc.)
- ``in_voltage0_test_mode`` / ``in_voltage1_test_mode`` - Set test patterns

Sampling
~~~~~~~~

- ``in_voltage_sampling_frequency`` - Clock rate configuration

External Synchronization
~~~~~~~~~~~~~~~~~~~~~~~~

The ADC TPL HDL core supports the EXT_SYNC feature, allowing synchronization
of multiple channels within an ADC or across instances.

Attributes:

- ``sync_start_enable`` - Arm/disarm trigger mechanism
- ``sync_start_enable_available`` - Lists available modes including
  "trigger_manual"

Buffer Management
-----------------

Buffer sysfs Interface
~~~~~~~~~~~~~~~~~~~~~~

Located at ``/sys/bus/iio/devices/iio:deviceX/buffer/``:

- ``length`` - Sample set count capacity
- ``enable`` - Activate/deactivate buffer (write last)
- ``watermark`` - Maximum wait count for poll operations
- ``data_available`` - Available bytes for reading
- ``length_align_bytes`` - DMA alignment requirements

Scan Elements
~~~~~~~~~~~~~

Located at ``/sys/bus/iio/devices/iio:deviceX/scan_elements/``:

- ``in_voltageX_en`` - Enable/disable channel capture (1/0)
- ``in_voltageX_type`` - Storage format [s|u]bits/storage-bits
- ``in_voltageX_index`` - Position in buffer (non-contiguous)

Related Documentation
---------------------

- :ref:`IIO Subsystem <iio>`
- :ref:`libiio <libiio>`
- :ref:`AXI_AD9361 IP Core <fpga axi_ad9361>`
