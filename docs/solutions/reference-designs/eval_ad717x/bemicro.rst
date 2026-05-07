.. _eval_ad717x bemicro:

BeMicro SDK Reference Design for AD7176-2
===============================================================================

Supported Devices:

- :adi:`AD7176-2`

Evaluation Boards:

- :adi:`EVAL-AD7176-2SDZ`

Overview
-------------------------------------------------------------------------------

This lab presents the steps to setup an environment for using the
:adi:`EVAL-AD7176-2SDZ` evaluation board together with the
`BeMicro SDK <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`_
USB stick and the Nios II Embedded Development Suite (EDS). Below is
presented a picture of the EVAL-AD7176-2SDZ Evaluation Board with the
BeMicro SDK Platform.

.. image:: images/ad7176_2_bemicro.jpg
   :width: 400

For component evaluation and performance purposes, as opposed to quick
prototyping, the user is directed to use the part evaluation setup. This
consists of:

#. A controller board like the SDP-B (EVAL-SDP-CS1Z)
#. The component SDP compatible product evaluation board
#. Corresponding PC software (shipped with the product evaluation board)

The SDP-B controller board is part of Analog Devices System Demonstration
Platform (SDP). It provides a high speed USB 2.0 connection from the PC to
the component evaluation board. The PC runs the evaluation software. Each
evaluation board, which is an SDP compatible daughter board, includes the
necessary installation file required for performance testing.

The :adi:`EVAL-AD7176-2SDZ` evaluation board is a member of a growing
number of boards available for the SDP. It was designed to help customers
evaluate performance or quickly prototype new AD7176-2 circuits and reduce
design time.

The :adi:`AD7176-2` is a fast settling, highly accurate, high resolution,
multiplexed Σ-Δ analog-to-digital converter (ADC) for low band-width input
signals. Its inputs can be configured as two fully differential or four
pseudo differential inputs via the integrated crosspoint multiplexer. An
integrated precision, 2.5 V, low drift (2 ppm/°C), band gap internal
reference (with an output reference buffer) adds functionality and reduces
the external component count.

More Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`AD7176-2 Product Info <AD7176-2>` — pricing, samples, datasheet
- :adi:`EVAL-AD7176-2SDZ evaluation board user guide
  <static/imported-files/user_guides/UG-478.pdf>`
- `BeMicro SDK
  <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`_
- `Nios II Embedded Development Suite (EDS)
  <http://www.altera.com/devices/processor/nios2>`_

Getting Started
-------------------------------------------------------------------------------

The first objective is to ensure that you have all of the items needed and
to install the software tools so that you are ready to create and run the
evaluation project.

Hardware Items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is presented the list of required hardware items:

- Arrow Electronics
  `BeMicro SDK <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`_
  FPGA-based MCU Evaluation Board
- :adi:`BeMicro SDK/SDP Interposer <sdp-bemicro>` adapter board
- **EVAL-AD7176-2SDZ** evaluation board
- Intel Pentium III or compatible Windows PC, running at 866MHz or faster,
  with a minimum of 512MB of system memory

Software Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is presented the list of required software tools:

- `Quartus II Web Edition
  <http://www.altera.com/products/software/quartus-ii/web-edition/qts-we-index.html>`_
  design software v12.0sp2
- `Nios II EDS <https://www.altera.com/download/software/nios-ii>`_ v12.0sp2

The Quartus II design software and the Nios II EDS is available via the
Altera Complete Design Suite DVD or by downloading from the web.

Downloads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:download:`Lab Design Files <images/ad7176_2_evalboardlab.zip>`

Extract the Lab Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a folder called **ADIEvalBoardLab** on your PC and extract the
**ad7176-2_evalboardlab.zip** archive to this folder. Make sure that there
are **NO SPACES** in the directory path. After extracting the archive the
following folders should be present in the **ADIEvalBoardLab** folder:

.. list-table::
   :header-rows: 1

   * - Folder
     - Description
   * - FPGA
     - Contains all the files necessary to program the BeMicro FPGA board in
       order to run the evaluation project. By executing the script
       ``program_fpga.bat`` the FPGA will be programmed with the evaluation
       project. New NIOS II applications can be created using the files from
       this folder. The ``ip`` subfolder contains the AD7176-2 NIOS II
       peripheral's source code.
   * - Hdl
     - Contains the source files for the AD7176-2 HDL driver. The ``doc``
       subfolder contains a brief documentation for the driver. The ``src``
       subfolder contains the HDL source files. The ``tb`` folder contains
       the sources of the driver's testbench.
   * - NiosCpu
     - Contains the Quartus evaluation project source files. The ``ip``
       subfolder contains the AD7176-2 Nios2 peripheral source code.
   * - Software
     - Contains the source files of the Nios2 SBT evaluation project.
   * - DataCapture
     - Contains the script files used for data acquisition.

USB Blaster Driver Installation
-------------------------------------------------------------------------------

The USB Blaster is used to program the FPGA on the BeMicro board and also
for data exchange between the system and a PC. To install the driver, plug
the Terasic USB Blaster into one of the PC's USB ports. Your Windows PC
will find the new hardware and try to install the driver.

.. image:: images/image007.png
   :width: 350

Since Windows cannot locate the driver for the device, the automatic
installation will fail and the driver has to be installed manually. In the
**Device Manager** right click on the **USB-Blaster** device and select
**Update Driver Software**.

.. image:: images/image009.png
   :width: 700

In the next dialog box select the option **Browse my computer for driver
software**. A new dialog will open where it is possible to point to the
driver's location. Set the location to
``altera\11.0\quartus\drivers\usb-blaster`` and press **Next**.

+------------------------------------------+------------------------------------------+
| .. image:: images/image011.png           | .. image:: images/image013.png           |
|    :width: 400                           |    :width: 400                           |
+------------------------------------------+------------------------------------------+

.. tip::

   If Windows presents you with a message that the drivers have not passed
   Windows Logo testing, please click **Install this driver software
   anyway**. Upon installation completion a message will be displayed to
   inform that the installation is finished.

+------------------------------------------+------------------------------------------+
| .. image:: images/image017.png           | .. image:: images/image016.jpg           |
|    :width: 400                           |    :width: 400                           |
+------------------------------------------+------------------------------------------+

AD7176-2 Evaluation Project Overview
-------------------------------------------------------------------------------

The evaluation project contains all the source files needed to build a
system that can be used to configure the AD7176-2 and capture data from it.
The system consists of a Nios II softcore processor that is implemented in
the FPGA found on the BeMicro board and a PC application. The softcore
controls the communication with the Device Under Test (DUT) and the data
capture process. The captured data is saved into the onchip RAM of the
BeMicro board and afterwards it is read by the PC application and saved
into a comma separated values (.csv) file that can be used for further data
analysis.

The following components are implemented in the FPGA design:

.. list-table:: System Components
   :header-rows: 1

   * - Name
     - Address
     - IRQ
   * - CPU
     - 0x00000800
     - —
   * - JTAG UART
     - 0x00000090
     - 0
   * - uC-Probe UART
     - 0x000000A0
     - 1
   * - EPCS Flash Controller
     - 0x00001800
     - 2
   * - OnChip RAM
     - 0x00010000
     - —
   * - LED GPIO
     - 0x00000100
     - —
   * - GPIO
     - 0x00002080
     - —
   * - CTRL GPIO
     - 0x000020A0
     - —
   * - SYS ID
     - 0x00000040
     - —
   * - Timer
     - 0x00000060
     - 3
   * - Avalon Master
     - —
     - —
   * - Main PLL
     - 0x00000080
     - —
   * - AD7176_2 0
     - 0x00000120
     - —

The Nios II processor contains a peripheral that implements the
communication protocol with the DUT. The peripheral is divided into three
logical modules: a module which implements the interface with the Avalon bus
and the communication with the onchip RAM, a module which implements an
Avalon master interface which is used to write data directly in the onchip
RAM and a module which is the actual driver of the DUT. The driver can also
be used as standalone in FPGA designs which do not contain a softcore.
Following is presented a block diagram of the HDL driver and a description
of the driver's interface signals.

.. image:: images/ad7176-2_block_diagram.png
   :width: 400
   :alt: HDL driver block diagram

Quick Evaluation
-------------------------------------------------------------------------------

The next sections of this lab present all the steps needed to create a
fully functional project that can be used for evaluating the operation of
the ADI platform. It is possible to skip these steps and load into the FPGA
an image that contains a fully functional system.

The first step of the quick evaluation process is to program the FPGA with
the image provided in the lab files. Before the image can be loaded the
**Quartus II Web Edition** tool or the
`Quartus II Programmer <https://www.altera.com/download/programming/quartus2/pq2-index.jsp>`_
must be installed on your computer.

To load the FPGA image run the **program_fpga.bat** batch file located in
the **ADIEvalBoardLab/FPGA/** folder. After the image was loaded the system
must be reset. Now the FPGA contains a fully functional system and it is
possible to skip directly to the
`Demonstration Project User Interface`_ section of this lab.

NIOS II Software Design
-------------------------------------------------------------------------------

This section presents the steps for developing a software application that
will run on the **BeMicroSDK** system and will be used for controlling and
monitoring the operation of the ADI evaluation board.

Create a New Project Using the NIOS II Software Build Tools for Eclipse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launch the **Nios II SBT** from **Start → All Programs → Altera 12.0sp2 →
Nios II EDS 12.0sp2 → Nios II 12.0sp2 Software Build Tools for Eclipse
(SBT)**.

.. tip::

   Windows 7 users will need to right-click and select **Run as
   administrator**. Another method is to right-click and select
   **Properties**, click on the **Compatibility** tab and select the
   **Run This Program As An Administrator** checkbox, which will make
   this a permanent change.

1. Initialize Eclipse Workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When Eclipse first launches, a dialog box appears asking what directory it
should use for its workspace. It is useful to have a separate Eclipse
workspace associated with each hardware project that is created in SOPC
Builder. Browse to the **ADIEvalBoardLab** directory and click **Make New
Folder** to create a folder for the software project. Name the new folder
**eclipse_workspace**. After selecting the workspace directory, click
**OK** and Eclipse will launch and the workbench will appear in the
**Nios II** perspective.

.. image:: images/eclipseworkspace.png
   :width: 500

2. Create a New Software Project in the SBT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Select **File → New → Nios II Application and BSP from Template**.

.. image:: images/image025.png
   :width: 400

- Click the **Browse** button in the **SOPC Information File Name** dialog
  box.
- Select the **uC.sopcinfo** file located in the **ADIEvalBoardLab/FPGA/**
  directory.
- Set the name of the Application project to **ADIEvalBoard**.
- Select the **Blank Project** template under **Project template**.
- Click the **Finish** button.

.. image:: images/eclipseblankproject.png
   :width: 400

The tool will create two new software project directories. Each Nios II
application has 2 project directories in the Eclipse workspace:

- The application software project itself — this is where the application
  lives.
- The **Board Support Package (BSP)** project associated with the main
  application software project. This project will build the system library
  drivers for the specific SOPC system. This project inherits the name from
  the main software project and appends **_bsp** to it.

.. image:: images/eclipseprojects.png
   :width: 300

Since you chose the blank project template, there are no source files in
the application project directory at this time. The BSP contains a
directory of software drivers as well as a system.h header file, system
initialization source code and other software infrastructure.

Configure the Board Support Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the board support package to specify the properties of this
software system by using the **BSP Editor** tool. These properties include
what interface should be used for *stdio* and *stderr* messages, the memory
in which stack and heap should be allocated and whether an operating system
or network stack should be included with this BSP.

- Right click on the **ADIEvalBoard_bsp** project and select **Nios II →
  BSP Editor…** from the right-click menu.

.. image:: images/eclipsebspmenu.png
   :width: 400

The software project provided in this lab does not make use of an operating
system. All *stdout*, *stdin* and *stderr* messages will be directed to the
*jtag_uart*.

- Select the **Common** settings view. In the **Common** settings view,
  change the following settings:

  - Select the **jtag_uart** for *stdin*, *stdout* and *stderr* messages.
    Note that you have more than one choice.
  - Select **none** for the *sys_clk_timer* and *timestamp_timer*.

.. image:: images/image033.png
   :width: 500

- Select **File → Save** to save the board support package configuration
  to the *settings.bsp* file.
- Click the **Generate** button to update the BSP.
- When the generate has completed, select **File → Exit** to close the
  BSP Editor.

Configure BSP Project Build Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the board support package settings configured using the
**BSP Editor**, there are other compilation settings managed by the Eclipse
environment such as compiler flags and optimization level.

- Right click on the **ADIEvalBoard_bsp** software project and select
  **Properties** from the right-click menu.
- On the left-hand menu, select **Nios II BSP Properties**.
- During compilation, the code may have various levels of optimization
  which is a tradeoff between code size and performance. Change the
  **Optimization level** setting to **Level 2**.
- Since our software does not make use of C++, uncheck **Support C++**.
- Check the **Reduced device drivers** option.
- Check the **Small C library** option.
- Press **Apply** and **OK** to regenerate the BSP and close the
  **Properties** window.

.. image:: images/eclipsebspproperties.png
   :width: 500

Add Source Code to the Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Windows Explorer locate the project directory which contains a directory
called **Software**. Select all the files and directories from the
**Software** folder and drag and drop them into the Eclipse software project
**ADIEvalBoard**.

- Select all the files and folders and drag them over the **ADIEvalBoard**
  project in the SBT window and drop the files onto the project folder.

.. image:: images/eclipsecopysources.png
   :width: 600

- A dialog box will appear to select the desired operation. Select the
  option **Copy files and folders** and press **OK**.

.. image:: images/copyfileconfirmation.png
   :width: 400

- This should cause the source files to be physically copied into the file
  system location of the software project directory and register these
  source files within the Eclipse workspace so that they appear in the
  Project Explorer file listing.

.. image:: images/eclipseprojectstructure.png
   :width: 300

Configure Application Project Build Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just as you configured the optimization level for the BSP project, you
should set the optimization level for the application software project
**ADIEvalBoard** as well.

- Right click on the **ADIEvalBoard** software project and select
  **Properties** from the right-click menu.
- On the left-hand menu, select the **Nios II Application Properties** tab.
- Change the **Optimization level** setting to **Level 2**.
- Press **Apply** and **OK** to save the changes.

.. image:: images/eclipseprojectproperties12.png
   :width: 500

Compile, Download and Run the Software Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Build the Application and BSP Projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Right click the **ADIEvalBoard_bsp** software project and choose **Build
  Project** to build the board support package.
- When that build completes, right click the **ADIEvalBoard** application
  software project and choose **Build Project** to build the Nios II
  application.

These 2 steps will compile and build the associated board support package,
then the actual application software project itself. The result of the
compilation process will be an Executable and Linked Format (.elf) file for
the application, the **ADIEvalBoard.elf** file.

+------------------------------------------+------------------------------------------+
| .. image:: images/eclipsebuildbsp.png    | .. image:: images/eclipsebuildproj.png   |
|    :width: 400                           |    :width: 400                           |
+------------------------------------------+------------------------------------------+

2. Verify the Board Connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **BeMicroSDK** hardware is designed with a *System ID* peripheral. This
peripheral is assigned a unique value based on when the hardware design was
last modified in the SOPC Builder tool. SOPC Builder also places this
information in the *.sopcinfo* hardware description file. The BSP is built
based on the information in the *.sopcinfo* file.

- Select the **ADIEvalBoard** application software project.
- Select **Run → Run Configurations…**
- Select the **Nios II Hardware** configuration type.
- Press the **New** button to create a new configuration.
- Change the configuration name to **BeMicroSDK** and click **Apply**.
- On the **Target Connection** tab, press the **Refresh Connections**
  button. You may need to expand the window or scroll to the right to see
  this button.
- Select the **jtag_uart** as the **Byte Stream Device** for *stdio*.
- Check the **Ignore mismatched system ID option**.
- Check the **Ignore mismatched system timestamp option**.

+------------------------------------------+------------------------------------------+
| .. image:: images/eclipserunconfig.png   | .. image:: images/image059.png           |
|    :width: 400                           |    :width: 400                           |
+------------------------------------------+------------------------------------------+

.. image:: images/ignoreid.png
   :width: 500

3. Run the Software Project on the Target
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run the software project on the Nios II processor:

- Press the **Run** button in the **Run Configurations** window.

This will re-build the software project to create an up-to-date executable
and then download the code into memory on the **BeMicroSDK** hardware. The
debugger resets the Nios II processor, and it executes the downloaded code.
Note that the code is verified in memory before it is executed.

.. image:: images/image063.png
   :width: 400

.. tip::

   The code size and start address might be different than the ones
   displayed in the above screenshot.

Demonstration Project User Interface
-------------------------------------------------------------------------------

After the FPGA is correctly programmed the data acquisition process can
start by executing the ``data_capture.bat`` script. The
``data_capture.tcl`` file can be modified to acquire a variable number of
channels.

.. tip::

   The configuration from ``data_capture.tcl`` is performed the first time
   the script is executed. If changes are performed after that, the system
   must be reinitialized by reprogramming the FPGA.

.. image:: images/cmd_interface.png
   :width: 500
   :alt: Demonstration Project Command Interface

If the resulting csv file is opened with Microsoft Excel, the data will be
displayed on a different number of columns, each column corresponding to a
channel.

.. note::

   If several consecutive data acquisitions are performed the captured data
   is appended to the **Acquisition.csv** file.

Troubleshooting
-------------------------------------------------------------------------------

In case there is a communication problem with the board the following
actions can be performed in order to try to fix the issues:

- Check that the evaluation board is powered.
- Check that the USB connection cable is properly connected to the device
  and to the computer and that the **USB Blaster Device Driver** is
  installed correctly. If the driver is not correctly installed, perform
  the steps described in the `USB Blaster Driver Installation`_ section.

More Information
-------------------------------------------------------------------------------

- :ez:`Ask questions about the FPGA reference design <community/fpga>`

.. include:: /common/ez_common.rst
