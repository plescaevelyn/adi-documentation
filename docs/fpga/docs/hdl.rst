:orphan:

.. _fpga hdl:

ADI Reference Designs HDL User Guide
====================================

This guide provides documentation for Analog Devices' FPGA reference designs
and HDL resources, supporting both Intel/Altera and Xilinx platforms.

.. note::

   The HDL documentation is being migrated to GitHub. The updated version is
   available at the
   `HDL repository documentation <https://analogdevicesinc.github.io/hdl/>`_.

Table of Contents
-----------------

#. Introduction
#. Git Repository
#. Releases and supported tool versions
#. Building & Generating programming files
#. Running software on hardware
#. Architecture
#. IP Cores
#. Using and modifying the HDL design
#. Third party forks with derived work

IP Cores
--------

The following IP cores are commonly used in ADI reference designs:

- :ref:`AXI_AD9361 <fpga axi_ad9361>` - AD9361 transceiver interface
- :ref:`AXI_DMAC <fpga axi_dmac>` - High-speed DMA controller

Supported Carriers
------------------

**Xilinx Platforms:**

- Zynq: ZC702, ZC706, ZED, CORAZ7S
- Zynq UltraScale+: ZCU102, ZCU104
- Kintex: KC705, KCU105
- Virtex: VC707, VCU118
- Versal: VCK190, VPK180

**Intel Platforms:**

- Arria 10: A10SoC
- Cyclone V: C5SoC, DE10-Nano
- Stratix 10: S10SoC

Source Code
-----------

The HDL source code is available on GitHub:

- `HDL Repository <https://github.com/analogdevicesinc/hdl>`_

Related Resources
-----------------

- :ref:`AD9361 Linux Device Driver <ad9361>`
- :ref:`AXI ADC HDL Linux Driver <linux axi_adc_hdl>`
- :ref:`AXI DAC HDL Linux Driver <linux axi_dac_hdl>`
- :ref:`AXI-DMAC Linux Driver <linux axi_dmac>`
