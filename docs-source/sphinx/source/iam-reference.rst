Identity & Access Management
============================

Table of Contents:

* :ref:`main-interface`
* :ref:`lower-interface`

.. _main-interface:

Main Interface
--------------

* :ref:`main-realms`
* :ref:`main-permissions`
* :ref:`main-identities`
* :ref:`main-acls`

.. _main-realms:

Realms
^^^^^^

.. automodule:: nexussdk.realms
  :members: create, fetch, list, replace, deprecate

.. _main-permissions:

Permissions
^^^^^^^^^^^

.. automodule:: nexussdk.permissions
  :members: fetch, replace, append, subtract, delete

.. _main-identities:

Identities
^^^^^^^^^^

.. automodule:: nexussdk.identities
  :members: fetch

.. _main-acls:

Access Control Lists
^^^^^^^^^^^^^^^^^^^^

.. automodule:: nexussdk.acls
  :members: fetch, list, replace, append, subtract, delete

.. _lower-interface:

Lower-Level Interface
---------------------

* :ref:`lower-realms`
* :ref:`lower-permissions`
* :ref:`lower-identities`
* :ref:`lower-acls`

.. _lower-realms:

Realms
^^^^^^

.. automodule:: nexussdk.realms
  :members: create_, fetch_, list_, replace_, deprecate_
  :noindex:

.. _lower-permissions:

Permissions
^^^^^^^^^^^

.. automodule:: nexussdk.permissions
  :members: fetch_, replace_, append_, subtract_, delete_
  :noindex:

.. _lower-identities:

Identities
^^^^^^^^^^

.. automodule:: nexussdk.identities
  :members: fetch_
  :noindex:

.. _lower-acls:

Access Control Lists
^^^^^^^^^^^^^^^^^^^^

.. automodule:: nexussdk.acls
  :members: fetch_, list_, replace_, append_, subtract_, delete_
  :noindex:
