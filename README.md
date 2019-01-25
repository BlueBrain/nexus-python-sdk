[Status](#status) |
[Getting Started](#getting-started) |
[Upgrade](#upgrade) |
[Documentation](#documentation) |
[Releases](#releases)

# Nexus Python SDK

Python SDK for [Blue Brain Nexus](https://github.com/BlueBrain/nexus) v1.

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

## Documentation

- [API documentation](./docs/md/doc.md)

## Releases

Versions and their notable changes are listed in the [releases section](
https://github.com/BlueBrain/nexus-python-sdk/releases/).
