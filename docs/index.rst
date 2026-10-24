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

         System level designs, from mixed signal hardware to software drivers
         and algorithms.

      .. card:: Products
         :ref: products

         .. container:: landing-icon icon-products

            ..

         Evaluation boards, processors and lab tools.

      .. card:: ADC Platforms
         :ref: adc-platforms

         .. container:: landing-icon icon-adc-platforms

            ..

         Complete evaluation and demonstration systems for data converters.

      .. card:: Single Pair Ethernet Hub
         :ref: single-pair-ethernet-hub

         .. container:: landing-icon icon-single-pair-ethernet-hub

            ..

         MQTT-based evaluation platform to monitor and control SPE devices.

   Firmware & Software
   -------------------

   .. grid::
      :columns: 4

      .. card:: Kuiper
         :ref: kuiper

         .. container:: landing-icon icon-kuiper

            ..

         Debian-based Linux distribution, ready to use with evaluation hardware.

      .. card:: Kernel and devicetrees
         :ref: linux-kernel

         .. container:: landing-icon icon-linux-kernel

            ..

         Build the Linux kernel and devicetrees for each platform and host.

      .. card:: Linux drivers
         :ref: linux drivers

         .. container:: landing-icon icon-linux-drivers

            ..

         Device drivers in the Linux kernel.

      .. card:: Software
         :ref: software

         .. container:: landing-icon icon-software

            ..

         Libraries, toolboxes and applications.

   Learning
   --------

   .. grid::
      :columns: 2

      .. card:: Tutorials & Workshops
         :ref: learning

         .. container:: landing-icon icon-learning

            ..

         Mixed signal basics, system design and hands-on workshops.

      .. card:: University Program
         :ref: university

         .. container:: landing-icon icon-university

            ..

         Hands-on learning tools and courses for the next generation of design
         engineers.

.. toctree::
   :caption: Apps & Solutions
   :maxdepth: 4
   :glob:
   :hidden:

   solutions/reference-designs/index
   products/index
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
