.. _InstallationGuide:
.. _RollingInstall:

Installation
============

Options for installing ROS 2 Rolling Ridley:

.. toctree::
   :hidden:
   :glob:

   Installation/Linux-Development-Setup
   Installation/Linux-Install-Binary
   Installation/Linux-Install-Debians
   Installation/macOS-Development-Setup
   Installation/macOS-Install-Binary
   Installation/Windows-Development-Setup
   Installation/Windows-Install-Binary
   Installation/Fedora-Development-Setup
   Installation/Latest-Development-Setup
   Installation/Maintaining-a-Source-Checkout
   Installation/Prerelease-Testing
   Installation/DDS-Implementations

Binary packages
---------------

We currently provide ROS 2 binary packages for the following platforms:

* Linux (Ubuntu Focal(20.04))

  * `Debian packages <Installation/Linux-Install-Debians>`
  * `"fat" archive <Installation/Linux-Install-Binary>`

* `macOS <Installation/macOS-Install-Binary>`
* `Windows <Installation/Windows-Install-Binary>`

As defined in `REP 2000 <https://www.ros.org/reps/rep-2000.html>`_


.. _building-from-source:

Building from source
--------------------

We support building ROS 2 from source on the following platforms:

<<<<<<< HEAD
+---------------------------------------------------+------------------------------------------+
| `ROS 2 Dashing Diademata <Installation/Dashing>`  | `ROS 2 Foxy Fitzroy <Installation/Foxy>` |
+---------------------------------------------------+------------------------------------------+
| Released May 2019                                 | Released June 2020                       |
+---------------------------------------------------+------------------------------------------+
| Supported until May 2021                          | Supported until May 2023                 |
+---------------------------------------------------+------------------------------------------+
=======
>>>>>>> 90525686d2ffcb274b161c805188141f33c0304e

* `Linux <Installation/Linux-Development-Setup>`
* `macOS <Installation/macOS-Development-Setup>`
* `Windows <Installation/Windows-Development-Setup>`


Which install should you choose?
--------------------------------

Installing from binary packages or from source will both result in a fully-functional and usable ROS 2 install.
Differences between the options depend on what you plan to do with ROS 2.

**Binary packages** are for general use and provide an already-built install of ROS 2.
This is great for people who want to dive in and start using ROS 2 as-is, right away.

Linux users have two options for installing binary packages:

- Debian packages
- "fat" archive

Installing from Debian packages is the recommended method.
It's more convenient because it installs its necessary dependencies automatically.
It also updates alongside regular system updates.

However, you need root access in order to install Debian packages.
If you don't have root access, the "fat" archive is the next best choice.

macOS and Windows users who choose to install from binary packages only have the "fat" archive option
(Debian packages are exclusive to Ubuntu/Debian).

**Building from source** is meant for developers looking to alter or explicitly omit parts of ROS 2's base.
It is also recommended for platforms that don't support binaries.
Building from source also gives you the option to install the absolute latest version of ROS 2.

Contributing to ROS 2 core?
^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you plan to contribute directly to ROS 2 core packages, you can install the `latest development from source <Installation/Latest-Development-Setup>` which shares installation instructions with the `Rolling distribution <rolling_distribution>`.
