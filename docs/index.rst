System Level Documentation
==========================

.. attention::

   Work-in-progress, not all content available at the
   `wiki <https://wiki.analog.com/resources/eval/user-guides/>`_
   has been imported yet.

.. only:: html

   .. rubric:: Software, documentation and reference designs for Analog Devices
      products.

   The System Level documentation provides developers using Analog Devices
   products with software and documentation, including HDL interface code,
   software drivers, and reference project examples for FPGA connectivity.
   It also contains user guides for some Analog Devices evaluation boards to
   help developers get up and running fast.

   Apps & Solutions
   ----------------

   .. grid::
      :columns: 4

      .. card:: Reference Designs
         :ref: reference-designs

         .. container:: landing-icon icon-reference-designs

            ..

         Reference designs combining mixed signal hardware, software and
         algorithms.

      .. card:: Products
         :ref: products

         .. container:: landing-icon icon-products

            ..

         Evaluation boards, embedded processors and lab tools for hardware
         development.

      .. card:: ADC Platforms
         :ref: adc-platforms

         .. container:: landing-icon icon-adc-platforms

            ..

         Integrated evaluation and demonstration platforms for data converter
         systems.

      .. card:: Application Software
         :ref: application-software

         .. container:: landing-icon icon-application-software

            ..

         Applications for device evaluation, system integration and solution
         development.

   Firmware & Software
   -------------------

   .. grid::
      :columns: 4

      .. card:: Kuiper
         :ref: kuiper

         .. container:: landing-icon icon-kuiper

            ..

         Debian-based Linux distribution with tools and drivers for evaluation
         hardware.

      .. card:: Kernel and devicetrees
         :ref: linux-kernel

         .. container:: landing-icon icon-linux-kernel

            ..

         Build guides for the Linux kernel and devicetrees across supported
         platforms.

      .. card:: Linux drivers
         :ref: linux drivers

         .. container:: landing-icon icon-linux-drivers

            ..

         Linux kernel drivers for connecting devices and accessing their
         functionality.

      .. card:: Software
         :ref: software

         .. container:: landing-icon icon-software

            ..

         Libraries, toolboxes and applications for device control and data
         acquisition.

   Learning
   --------

   .. grid::
      :columns: 2

      .. card:: Tutorials & Workshops
         :ref: learning

         .. container:: landing-icon icon-learning

            ..

         Hands-on tutorials and workshops covering mixed signal basics and
         system design.

      .. card:: University Program
         :ref: university

         .. container:: landing-icon icon-university

            ..

         Learning tools and practical courses for the next generation of design
         engineers.

.. toctree::
   :caption: Apps & Solutions
   :maxdepth: 4
   :glob:
   :hidden:

   solutions/reference-designs/index
   products/index
   tools/index
   solutions/application-software/index
   ADC Platforms <solutions/platforms/index>

.. toctree::
   :caption: Firmware & Software
   :maxdepth: 1
   :glob:
   :hidden:

   linux/*/index
   software/index

.. toctree::
   :caption: Learning
   :maxdepth: 4
   :hidden:

   learning/index
   university/index

.. toctree::
   :caption: Contributing and Guidelines
   :maxdepth: 4
   :glob:
   :hidden:

   contributing/*
