# Starship ICE Plugin

A starship plugin to display information about the ICE you are sitting in.

## Installation

### Install the module

```shell
pip install .
```

### Configure the plugin

Append this to you `~/.config/starship.toml`:

```toml
[custom.ice]
format = "on $output"
command = "python -m starship-ice"
when = "python -m starship-ice"
```
