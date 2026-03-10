:orphan:

.. _linux axi_dmac:

AXI-DMAC DMA Controller Linux Driver
====================================

The AXI DMAC is a high-speed, high-throughput, general purpose DMA controller
designed for transferring data between system memory and peripherals such as
high-speed converters.

Supported Hardware
------------------

- :ref:`High-Speed DMA Controller Peripheral <fpga axi_dmac>`

Capabilities
------------

The controller supports multiple interface architectures:

- AXI3/4 memory-mapped interfaces
- AXI4 Streaming connections
- ADI FIFO interface

Notable architectural features include:

- Zero-latency transfer switch-over for continuous streaming
- Hardware-based cyclic transfer support
- 2D transfer capability

Source Code
-----------

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Component
     - File
     - Status
   * - Driver
     - ``drivers/dma/dma-axi-dmac.c``
     - Mainlined
   * - Headers
     - ``include/dt-bindings/dma/axi-dmac.h``
     - —
   * - Bindings
     - ``Documentation/devicetree/bindings/dma/adi,axi-dmac.txt``
     - —

Device Tree Configuration
-------------------------

The driver operates as a platform driver instantiated via device tree only.

Required Properties
~~~~~~~~~~~~~~~~~~~

- ``compatible`` - Must specify ``"adi,axi-dmac-1.00.a"``
- ``reg`` - Memory-mapped register address space
- ``interrupts`` - Controller interrupt specification
- ``clocks`` - AXI interface clock reference
- ``#dma-cells`` - Must be 1

Channel Configuration
~~~~~~~~~~~~~~~~~~~~~

The ``adi,channels`` sub-node contains channel definitions with these
requirements:

**Node-level properties:**

- ``#size-cells`` - 0
- ``#address-cells`` - 1

**Per-channel properties:**

- ``reg`` - Channel index
- ``adi,length-width`` - Transfer length register width
- ``adi,source-bus-width``, ``adi,destination-bus-width`` - Bus widths in bits
- ``adi,source-bus-type``, ``adi,destination-bus-type`` - Bus type enumeration

**Bus Type Values:**

- 0: ``AXI_DMAC_TYPE_AXI_MM`` (Memory-mapped)
- 1: ``AXI_DMAC_TYPE_AXI_STREAM`` (Streaming)
- 2: ``AXI_DMAC_TYPE_AXI_FIFO`` (FIFO)

**Optional properties:**

- ``adi,cyclic`` - Enable hardware cyclic transfers
- ``adi,2d`` - Enable 2D transfer support

Example Device Tree
~~~~~~~~~~~~~~~~~~~

.. code-block:: dts

   dma: dma@7c420000 {
       compatible = "adi,axi-dmac-1.00.a";
       reg = <0x7c420000 0x10000>;
       interrupts = <0 57 0>;
       clocks = <&clkc 16>;
       #dma-cells = <1>;

       adi,channels {
           #size-cells = <0>;
           #address-cells = <1>;

           dma-channel@0 {
               reg = <0>;
               adi,source-bus-width = <32>;
               adi,source-bus-type = <ADI_AXI_DMAC_TYPE_MM_AXI>;
               adi,destination-bus-width = <64>;
               adi,destination-bus-type = <ADI_AXI_DMAC_TYPE_FIFO>;
           };
       };
   };

Kernel Configuration
--------------------

Enable support through the kernel menuconfig::

   Device Drivers → DMA → DMA Engine support →
       Analog Devices AXI-DMAC DMA support

Related Documentation
---------------------

- :ref:`AXI DMAC IP Core <fpga axi_dmac>`
- Linux DMAEngine API documentation
- DMA client binding specifications
