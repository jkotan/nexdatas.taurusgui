Welcome to nxstaurusgui's documentation!
========================================

Authors: Jan Kotanski

NXS TaurusGUI is taurusgui Configuration for Component Selector

.. figure:: png/nxstaurusgui.png
   :alt: NeXus Taurus GUI


| Source code: https://github.com/nexdatas/taurusgui/
| Web page: https://nexdatas.github.io/taurusgui/
| NexDaTaS Web page: https://nexdatas.github.io



------------
Installation
------------

Install the dependencies:

|    Sardana, PyTango, sphinx, Taurus, NXSRecSelector, Selector

From sources
^^^^^^^^^^^^

Download the latest version of NeXuS Configuration Server from

|    https://github.com/nexdatas/taurusgui/

Extract the sources and run

.. code:: bash

	  $ python setup.py install

Debian packages
^^^^^^^^^^^^^^^

Debian Jessie (and Wheezy) packages can be found in the HDRI repository.

To install the debian packages, add the PGP repository key

.. code:: bash

	  $ sudo su
	  $ wget -q -O - http://repos.pni-hdri.de/debian_repo.pub.gpg | apt-key add -

and then download the corresponding source list

.. code:: bash

	  $ cd /etc/apt/sources.list.d
	  $ wget http://repos.pni-hdri.de/jessie-pni-hdri.list

Finally,

.. code:: bash

	  $ apt-get update
	  $ apt-get install python-nxsrecselector nxselector nxstaurusgui

To instal other NexDaTaS packages

.. code:: bash

	  $ apt-get install python-nxswriter nxsconfigtool nxstools python-nxsconfigserver nxsconfigserver-db

and

.. code:: bash

	  $ apt-get install python-sardana-nxsrecorder

for NeXus recorder.

-------------------
Setting environment
-------------------


Setting Saradna
^^^^^^^^^^^^^^^
If sardana is not yet set up run


.. code:: bash

	  $ Pool

- enter a new instance name
- create the new instance

Then wait a while until Pool is started and in a new terminal run

.. code:: bash

	  $ MacroServer

- enter a new instance name
- create the new instance
- connect pool

Next, run Astor and change start-up levels: for Pool to 2,
for MacroServer to 3 and restart servers.

Alternatively, terminate Pool and MacroServer in the terminals and run

.. code:: bash

          $ nxsetup -s Pool -l2

wait until Pool is started and run

.. code:: bash

          $ nxsetup -s MacroServer -l3


Additionally, one can create dummy devices by running `sar_demo` in

.. code:: bash

	  $ spock



Setting NeXus Servers
^^^^^^^^^^^^^^^^^^^^^

To set up  NeXus Servers run

.. code:: bash

	  $ nxsetup -x

or

.. code:: bash

          $ nxsetup -x NXSDataWriter
          $ nxsetup -x NXSConfigServer
	  $ nxsetup -x NXSRecSelector

for specific servers.

If the `RecoderPath` property of MacroServer is not set one can do it by

.. code:: bash

	  $ nxsetup -a /usr/lib/python2.7/dist-packages/sardananxsrecorder

where the path should point the `sardananxsrecorder` package.

