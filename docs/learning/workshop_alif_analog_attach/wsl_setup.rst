.. _alif-analog-attach wsl-setup:

WSL setup
=========

This page describes how to prepare a Windows machine with the Windows Subsystem
for Linux (WSL), so it can be used for the workshop.

Requirements
------------

- Windows 10 version 2004 or later, or Windows 11
- Administrator rights on the machine
- Virtualization enabled in BIOS/UEFI, see :ref:`alif-analog-attach wsl-setup-virtualization`

.. _alif-analog-attach wsl-setup-virtualization:

Enable virtualization
---------------------

WSL 2 runs a lightweight virtual machine, so hardware virtualization must be
enabled on the computer. On most recent machines it already is, so check first.

Check if virtualization is enabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open **Task Manager** (``Ctrl + Shift + Esc``).
#. Go to the **Performance** tab and select **CPU**.
#. Look at the **Virtualization** field, at the bottom right.

If it says **Enabled**, skip to `Enable the Windows features`_. If it says
**Disabled**, enable it from the BIOS/UEFI as described below.

.. note::

   If the field is missing, and the computer is already running WSL or other
   virtual machines, Windows is using the hypervisor and virtualization is
   enabled.

Enable virtualization in BIOS/UEFI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Save your work. The computer will restart.
#. Open the firmware settings from Windows:

   - **Windows 11**: **Settings** > **System** > **Recovery** > **Advanced
     startup** > **Restart now**.
   - **Windows 10**: **Settings** > **Update & Security** > **Recovery** >
     **Advanced startup** > **Restart now**.

#. After the restart, select **Troubleshoot** > **Advanced options** >
   **UEFI Firmware Settings** > **Restart**.

   .. tip::

      If this option is not listed, restart the computer and repeatedly press
      the BIOS key during boot. It depends on the manufacturer, usually
      ``F2``, ``F10``, ``F12``, ``Del`` or ``Esc``.

#. In the BIOS/UEFI menu, find the virtualization option. The menu and the
   option name depend on the manufacturer, look under **Advanced**,
   **Configuration**, **CPU Configuration** or **Security**:

   .. list-table::
      :header-rows: 1

      * - CPU
        - Option name
      * - Intel
        - **Intel Virtualization Technology**, **Intel VT-x**
      * - AMD
        - **SVM Mode**, **AMD-V**

#. Set the option to **Enabled**.
#. Save the changes and exit, usually with ``F10``. The computer restarts into
   Windows.
#. Check again in **Task Manager** that **Virtualization** is **Enabled**.

.. note::

   Some computers are locked by the IT department, and the BIOS may be password
   protected. In that case, ask your administrator to enable virtualization.

Enable the Windows features
~~~~~~~~~~~~~~~~~~~~~~~~~~~

WSL also needs the **Windows Subsystem for Linux** and **Virtual Machine
Platform** features. Open PowerShell as administrator (right click on the icon
> **Run as administrator**) and run:

.. code:: powershell

   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux,VirtualMachinePlatform

Or, from Command Prompt as administrator:

.. code:: batch

   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all

Restart the computer when asked.

.. tip::

   If WSL still reports that virtualization is not enabled, check that
   **Virtual Machine Platform** is ticked in **Turn Windows features on or
   off** (``optionalfeatures.exe``), and that no third party tool is
   blocking the Windows hypervisor.

Install WSL
-----------

(Optional) Install the Terminal app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the Microsoft Store, search for **Terminal** and install the app. It might
come pre-installed on some machines. It is used later to create a profile that
opens the workshop image directly.

Download WSL from the Microsoft Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the Microsoft Store, search for **Windows Subsystem for Linux** and
install it. Alternatively, from PowerShell as administrator:

.. code:: powershell

   wsl --install --no-distribution

.. note::

   Depending on your Windows version, WSL might already be installed on your
   machine. In that case, you can skip this step.

Switch to WSL 2
~~~~~~~~~~~~~~~

After you ensured WSL is installed on your system, you need to set WSL 2 as the
default version. This is done by running, in PowerShell:

.. code:: powershell

   wsl --set-default-version 2

Update the kernel
~~~~~~~~~~~~~~~~~

Update WSL and its Linux kernel to the latest version:

.. code:: powershell

   wsl --update

Import the Alif_Training image
------------------------------

The workshop uses a prepared Ubuntu 24.04 image, named ``Alif_Training``, with
all the required tools already installed. You do not need to install Ubuntu
from the Microsoft Store, you only need to import the provided image.

Download the image
~~~~~~~~~~~~~~~~~~

Please download the archive containing the WSL image from
`TBD <https://TBD>`__. Unzip it at a desired location, for example
``C:\WSL``.

.. important::

   Do not move or delete the file after importing it, as WSL uses it directly
   from this location.

Import the image
~~~~~~~~~~~~~~~~

Open PowerShell, go to the folder where you unzipped the image, and import it:

.. code:: powershell

   cd <Drive>:\<Path to where your file is>
   wsl --import-in-place Alif_Training .\Alif_Training.vhdx

This will import the prepared workshop image. To check that it was imported
and that it runs with WSL 2, run:

.. code:: powershell

   wsl --list --verbose

The output should list ``Alif_Training`` with version ``2``.

Start the image
~~~~~~~~~~~~~~~

Open the image from PowerShell with:

.. code:: powershell

   wsl -d Alif_Training

The image has a default user, which is used to log in automatically:

- **Username**: ``analog``
- **Password**: ``analog``

The password is needed when running commands with ``sudo``.

(Optional) Set a profile in the Terminal app
--------------------------------------------

You can add a separate profile in the Terminal app, to open the workshop image
directly, without typing the command each time.

#. Open the **Terminal** app and expand the menu from the arrow button, next to
   the tabs.
#. Select **Settings**.
#. From the left-side menu, click **Add new profile**.
#. Click **New empty profile**. In the window that opens, you only have to edit
   the **Name** and **Command line** fields:

   - **Name**: ``Alif_Training``
   - **Command line**: ``wsl -d Alif_Training``

#. Click **Save**. After adding the profile, you must restart the application
   to see it.

Verify the tools
----------------

The image already includes the packages required by the workshop. From
the ``Alif_Training`` terminal, check that they are available:

.. code:: bash

   dtc --version
   git --version
   ssh -V
   sshpass -V

.. tip::

   If a command is not found, install the packages with:

   .. code:: bash

      sudo apt update
      sudo apt install -y build-essential device-tree-compiler openssh-client sshpass git

Install VS Code and the WSL extension
-------------------------------------

#. If you do not have Visual Studio Code on your machine, download it from
   `code.visualstudio.com <https://code.visualstudio.com/>`__ and install it
   on Windows.
#. In VS Code, open the **Extensions** menu from the left side bar.
#. In the search bar, search for ``WSL``.
#. Install the `WSL extension
   <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl>`__
   from Microsoft.

Open VS Code from WSL
~~~~~~~~~~~~~~~~~~~~~

Open the ``Alif_Training`` terminal and run:

.. code:: bash

   cd ~
   code .

VS Code opens on Windows, connected to WSL. The bottom left corner should show
**WSL: Alif_Training**.

.. note::

   For ``code`` to work, WSL must be able to see the Windows apps. If you get
   ``code: command not found``, open ``~/.bashrc`` with ``nano ~/.bashrc`` and
   check the ``export PATH=...`` line towards the end of the file. If it
   contains a Windows user name, such as
   ``/mnt/c/Users/analog/AppData/Local/Microsoft/WindowsApps``, replace it with
   your own user name. Save with ``Ctrl+S``, close with ``Ctrl+X``, then close
   and reopen WSL.

.. _alif-analog-attach wsl-setup-usb:

Attach USB devices
------------------

WSL does not see USB devices by default. To use a board connected to the host,
you need the ``usbipd-win`` tool on Windows. The ``usbip`` package is already
installed in the image.

Install usbipd
~~~~~~~~~~~~~~

Install ``usbipd-win`` from the
`releases page <https://github.com/dorssel/usbipd-win/releases>`__, or from
PowerShell as administrator:

.. code:: powershell

   winget install --interactive --exact dorssel.usbipd-win

Restart PowerShell after the installation.

Attach a device
~~~~~~~~~~~~~~~

#. Connect the board to the computer.
#. In PowerShell as administrator, list the USB devices and note the
   ``BUSID`` of your board, for example ``3-2``:

   .. code:: powershell

      usbipd list

#. Share the device. This is needed only once per device:

   .. code:: powershell

      usbipd bind --busid <BUSID>

   .. tip::

      If the operation is not successful, try
      ``usbipd bind --force --busid <BUSID>``.

#. Attach the device to WSL. WSL must be running, so keep the
   ``Alif_Training`` terminal open:

   .. code:: powershell

      usbipd attach --wsl Alif_Training --busid <BUSID>

#. Check in the ``Alif_Training`` terminal that the device is recognized:

   .. code:: bash

      lsusb

.. note::

   The device is detached when it is unplugged or when WSL is shut down. Run the
   ``attach`` command again to reconnect it. Use ``--auto-attach`` to
   reattach it automatically.

More information:

- `Connect USB devices to WSL <https://learn.microsoft.com/en-us/windows/wsl/connect-usb>`__
