:orphan:

.. _fpga axi_dmac:

AXI DMAC - High-Speed DMA Controller
====================================

The AXI DMAC is a specialized data transfer controller designed for high-speed,
high-throughput operations between system memory and peripherals like
high-speed converters.

.. note::

   This documentation is being migrated to GitHub. The updated version is
   available at the
   `HDL library documentation <https://analogdevicesinc.github.io/hdl/library/axi_dmac/index.html>`_.

Features
--------

The controller supports:

- Multiple interface types (AXI3/4 memory-mapped, AXI4 Streaming, ADI FIFO)
- Zero-latency transfer switching for continuous streaming
- Cyclic transfer modes
- 2D transfer capabilities
- Scatter-Gather transfer operations

Configuration Parameters
------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Parameter
     - Default
     - Purpose
   * - ``DMA_DATA_WIDTH_SRC``
     - 64 bits
     - Source interface data width
   * - ``DMA_DATA_WIDTH_DEST``
     - 64 bits
     - Destination interface data width
   * - ``DMA_LENGTH_WIDTH``
     - 24 bits
     - Transfer length register width
   * - ``DMA_2D_TRANSFER``
     - 0
     - 2D transfer support
   * - ``DMA_SG_TRANSFER``
     - 0
     - Scatter-Gather support
   * - ``CYCLIC``
     - 1
     - Cyclic transfer support
   * - ``MAX_BYTES_PER_BURST``
     - 128
     - Maximum burst size
   * - ``FIFO_SIZE``
     - 4
     - Internal buffer size in bursts

Signal and Interface Pins
-------------------------

Control Signals
~~~~~~~~~~~~~~~

- ``s_axi_aclk`` - Configuration interface clock
- ``s_axi_aresetn`` - Active-low synchronous reset
- ``s_axi`` - AXI4-Lite configuration bus
- ``irq`` - Level-high interrupt output

Data Interfaces
~~~~~~~~~~~~~~~

- ``m_src_axi`` - AXI master for source (when DMA_TYPE_SRC = 0)
- ``m_dest_axi`` - AXI master for destination (when DMA_TYPE_DEST = 0)
- ``m_sg_axi`` - AXI master for scatter-gather descriptors
- ``s_axis`` / ``m_axis`` - AXI Streaming interfaces
- ``fifo_wr`` / ``fifo_rd`` - FIFO write/read interfaces

Register Map
------------

Identification Registers (0x000-0x00C)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- VERSION: Semantic versioning (current 4.05.61)
- PERIPHERAL_ID: Instance identification
- SCRATCH: Debug register
- IDENTIFICATION: Constant value "DMAC"

Interrupt Registers (0x080-0x088)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- IRQ_MASK: Enable/disable interrupt masking
- IRQ_PENDING: Active interrupt status
- IRQ_SOURCE: Interrupt event recording

Transfer Configuration (0x100-0x12F)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- CONTROL: Enable, pause, scatter-gather mode
- TRANSFER_ID: Identifier for tracking
- TRANSFER_SUBMIT: Queue submission trigger
- FLAGS: Cyclic and TLAST control
- DEST_ADDRESS / SRC_ADDRESS: Memory addresses
- X_LENGTH / Y_LENGTH: Transfer dimensions
- DEST_STRIDE / SRC_STRIDE: Row padding offsets

Status Registers
~~~~~~~~~~~~~~~~

- TRANSFER_DONE: Completion status per ID
- ACTIVE_TRANSFER_ID: Currently processing transfer
- CURRENT_DEST_ADDRESS / CURRENT_SRC_ADDRESS: Runtime pointers
- TRANSFER_PROGRESS: Bytes transferred so far

Theory of Operation
-------------------

Buffer Management
~~~~~~~~~~~~~~~~~

The internal store-and-forward buffer dimensions:

- **Width**: Maximum of source and destination interface widths
- **Depth**: ``FIFO_SIZE`` × ``MAX_BYTES_PER_BURST`` / buffer width in bytes
- **Purpose**: Equalize rate mismatches between interfaces

Transfer Types
~~~~~~~~~~~~~~

**2D Transfers:**

When enabled, transfers process multiple rows with configurable padding between
them using stride parameters.

**Cyclic Transfers:**

Automatically restart after completion without software intervention. No
end-of-transfer interrupts generated.

**Scatter-Gather Transfers:**

Access non-contiguous memory areas through descriptor chains. Descriptors
include:

- Flags (last descriptor, interrupt enable)
- Source/destination addresses (64-bit)
- Next descriptor address
- Transfer dimensions and strides

Interrupt Handling
~~~~~~~~~~~~~~~~~~

Two interrupt types:

1. ``TRANSFER_QUEUED`` - Transfer moved from registers to internal queue
2. ``TRANSFER_COMPLETED`` - Transfer finished (all bytes transferred or error)

Software must poll ``TRANSFER_DONE`` register to identify which transfer(s)
completed.

Operational Limitations
-----------------------

4kB Address Boundary
~~~~~~~~~~~~~~~~~~~~

AXI bursts cannot cross 4kB boundaries:

- Starting address must be aligned to ``MAX_BYTES_PER_BURST``
- Transfer cannot exceed remaining space to boundary

Address Alignment
~~~~~~~~~~~~~~~~~

- Source address must align to source bus width
- Destination address must align to destination bus width

Transfer Length Alignment
~~~~~~~~~~~~~~~~~~~~~~~~~

- Length must be multiple of maximum bus width
- Relaxed for MM interfaces using strobe masking

Software Support
----------------

Analog Devices provides Linux driver support for AXI-DMAC integration with ADI
components. See :ref:`AXI-DMAC Linux Driver <linux axi_dmac>`.
