.. pytest DV Flow Extension documentation master file, created by
   sphinx-quickstart on Sat May 10 15:48:32 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

########################
pytest DV Flow Extension
########################

`pytest-dfm` is a DV Flow extension for the `pytest` testing framework.
`pytest-dfm` allows unit tests to run tools encapsulated as DV Flow tasks 
and tasks graphs composed of those tasks. This is useful when developing
tests for a DV-targeted Python package. Test and debug is most easily 
done in the context of Python (and pytest). However, artifacts created
by running the packaging being tested need to be processed by tools
available as DV Flow tasks. The `pytest-dfm` extension simplifies the
task of using `DV Flow Manager` as a part of a `pytest` test suite.

.. contents::
    :depth: 2

dvflow Test Fixture
===================

`pytest` uses `fixtures <https://docs.pytest.org/en/6.2.x/fixture.html>`_ to 
construct and provide services to tests. The `pytest-dfm` extension provides 
the `dvflow` fixture.

The `dvflow` fixture infers a temporary directory in which to run DV Flow
tasks, and is a proxy for the `DvFlow` class.

.. autoclass:: pytest_dfm.DvFlow
    :members:
    :show-inheritance:



