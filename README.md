<p align="center"><a href="https://github.com/BlueBrain/nexus-sdk-js" target="_blank" rel="noopener noreferrer"><img src="/docs/_static/Blue-Brain-Nexus-Python-SDK-Github-Banner.jpg" alt="Nexus JS Banner"></a></p>

# Nexus Python SDK

Python SDK for [Blue Brain Nexus](https://github.com/BlueBrain/nexus) v1.

[Status](#status) |
[Getting Started](#getting-started) |
[Upgrade](#upgrade) |
[Releases](#releases) |
[Contributing](#contributing)

---

## Status

Beta.

## Getting Started

### Usage

````python
import nexussdk as nexus

nexus.config.set_environment(DEPLOYMENT)
nexus.config.set_token(TOKEN)

nexus.permissions.fetch()
````

More examples in the folder [notebooks](./notebooks) and [tests](./tests).

Documentation: https://bluebrain.github.io/nexus-python-sdk/.

### Installation

```bash
pip install nexus-sdk
```

**Development version**

```bash
pip install git+https://github.com/BlueBrain/nexus-python-sdk
```

**Development mode**

```bash
git clone https://github.com/bluebrain/nexus-python-sdk
pip install --editable nexus-python-sdk
```

**Requirements**

- [requests](http://docs.python-requests.org)

## Upgrade

```bash
pip install --upgrade nexus-sdk
```

## Releases

Versions and their notable changes are listed in the [releases section](
https://github.com/BlueBrain/nexus-python-sdk/releases/).

## Contributing

### Styling

Follow [PEP 20](https://www.python.org/dev/peps/pep-0020/),
[PEP 8](https://www.python.org/dev/peps/pep-0008/), and
[PEP 257](https://www.python.org/dev/peps/pep-0257/), at least.

### Documentation

The documentation is auto-generated with [Sphinx](http://www.sphinx-doc.org).
To install it:

```bash
pip install nexus-sdk[doc]
```

**Update**

To add a new module to the API Reference, add the corresponding section in the
files `admin-reference.rst`, `kg-reference.rst`, or `iam-reference.rst` which 
are in the directory `docs-sources/sphix/source/`.

**Generate**

```bash
cd docs-source/sphinx
make html
```

**Deploy**

```bash
cp -R build/html/ ../../docs/
```

### Releasing

**Setup**

```bash
pip install --upgrade pip setuptools wheel twine
```

**Tagging**

```bash
git checkout master
git pull upstream master
git tag -a v<x>.<y>.<z> HEAD
git push upstream v<x>.<y>.<z>
```

**Building**

```bash
python setup.py sdist bdist_wheel
```

**Upload**

```bash
twine upload dist/*
```

**Cleaning**

```bash
rm -R build dist *.egg-info
```

## Funding & Acknowledgment

This study was supported by funding to the Blue Brain Project, a research center of the École polytechnique fédérale de Lausanne (EPFL), from the Swiss government’s ETH Board of the Swiss Federal Institutes of Technology.

Copyright © 2015-2022 Blue Brain Project/EPFL

