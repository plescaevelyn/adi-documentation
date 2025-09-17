Temperature Controller Application
==================================

This sample application demonstrates a basic **Temperature Controller** using the
AD-CN0591-RPIZ board, two AD-SWIOT1L-SL boards, and a Raspberry Pi.
The system reads temperature data and adjusts fan speed (via SWIOT1L output)
based on configurable thresholds and hysteresis.

Prerequisites
-------------

- **Raspberry Pi** with Kuiper 2 image installed.  
  Follow the instructions in the `Kuiper 2 User Guide <https://github.com/analogdevicesinc/adi-kuiper-gen/releases>`_
  to prepare the Raspberry Pi.
- ``pyadi-iio`` package cloned from GitHub (steps below).

Hardware Setup
--------------

.. figure:: temp_controller_system.png
   :align: center
   :width: 500

   Temperature Controller System

**Equipment Needed**

- 1x AD-CN0591-RPIZ Board
- 2x AD-SWIOT1L-SL Boards
- 1x Raspberry Pi running Kuiper 2
- 1x TMP01 Temperature Sensor
- 1x Fan actuator
- 1x Raspberry Pi Power Supply (5V, 3A)

**Setup Procedure**

1. Connect the CN0591 board to the Raspberry Pi via the 40-pin header
2. Connect the two SWIOT1L boards to the CN0591 board via T1L
3. Connect the first SWIOT1L board to the TMP01 temperature sensor
4. Connect the second SWIOT1L board to the fan actuator
5. Power the Raspberry Pi with a 5V/3A supply

Software Setup
--------------

Firmware Flashing
~~~~~~~~~~~~~~~~~

Firmware images and flashing steps for the AD-SWIOT1L-SL boards are provided in the repository
under ``host_setup/config/firmware``.

Network Setup
~~~~~~~~~~~~~

The SWIOT1L boards require static IP addresses to be accessible by the
application. There are **two modes** in which the static IPs can be configured:

- **Manual configuration** – follow the steps described in the
  :doc:`../cn0591/index` page to assign the IP addresses manually.

- **NetworkManager configuration** – use the provided configuration files
  and steps described in the `README from the pyadi-iio repository
  <https://github.com/plescaevelyn/pyadi-iio/tree/swiot/examples/cn0591>`_
  to apply static IPs via NetworkManager.

Repository Cloning & Application Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/analogdevicesinc/pyadi-iio.git
      cd pyadi-iio

2. Install Python dependencies:

   .. code-block:: bash

      cd examples/cn0591
      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt

3. Run the Temperature Controller example with a configuration file:

   .. code-block:: bash

      python3 temperature_controller.py --config config/static_ip_example.yaml

4. Example configuration file (``config/static_ip_example.yaml``):

   .. code-block:: yaml

      sensor_primary: TMP01
      sensor_backup: ADT75
      threshold_high: 30.0
      threshold_low: 25.0
      hysteresis: 1.0
      fan_output_device: SWIOT1L-1/output0
      log_file: logs/temp_fan.log

5. Optional: visualize results with the plotting script:

   .. code-block:: bash

      python3 plot_temp_fan.py logs/temp_fan.log
