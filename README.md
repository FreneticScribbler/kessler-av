# kramerav - Kramer Protcol 2000 video switch library

Python library for controlling a Kramer HDMI switch that uses [Protocol
2000][p2000] over a TCP connection.

It's primarily intended for use as a device driver for a [Home Assistant][ha]
integration.

## USAGE

TODO: Write this.

## Limitations

The library was tested and developed using a Kramer VS-161HDMI switch, but
_should_ work for any Kramer switch using Protocol 2000.

It does _not_ currently support:

+ _Matrix_ switch operations, since I don't have a device to test with
+ Serial communication, since TCP is the more likely control mechanism for home
automation purposes

## Development workflow

### Python environment

Workflow scripts assume a working Python environment, including `pip`.

Remember to be kind to yourself and use a virtual environment.

```sh
python3 -m venv env
env/bin/activate
```

### Setup

Install development and runtime dependencies. This also installs the library as an
editable path, so that it can be loaded in the REPL and `pytest`.

```sh
script/setup
```

### Publishing

Build the distribution.

```sh
script/build
```

Publish the library to TestPyPI.

```sh
script/publish_test
```

Publish the library to PyPI.

```sh
script/publish
```

[ha]: https://www.home-assistant.io/
[p2000]: https://cdn.kramerav.com/web/downloads/tech-papers/protocol_2000_rev0_51.pdf
