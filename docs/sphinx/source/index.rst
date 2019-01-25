Nexus Python SDK
================

A Python wrapper for the `Blue Brain Nexus <https://bluebrain.github.io/nexus>`_
REST API.

Getting Started
---------------

Installation
^^^^^^^^^^^^

.. code-block:: shell

   pip install nexus-sdk

Usage
^^^^^

.. code-block:: python

  import nexussdk as nexus

  nexus.config.set_environment(DEPLOYMENT)
  nexus.config.set_token(TOKEN)

  nexus.permissions.fetch()

User Guide
----------

.. toctree::
  :maxdepth: 2

  api-reference

* :ref:`modindex`
