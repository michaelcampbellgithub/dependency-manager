# dependency-manager

This is a tool to manage your dependencies, much like [Dependabot](https://dependabot.com/), but for free!

## Environments supported

Currently, we are only working on supporting Python

Future releases are scoped for:
* Golang
* Javascript
* Docker images
* Helm charts
* Whatever else people want

However, please feel free to branch off & add support for your chosen stack if we're taking too long

## Usage

### Python script

The only required arg is the name of the config file you wish to use (denoted below by `$CONFIG_FILE`)
```bash
$PYTHON_BIN ./main.py --config=$CONFIG_FILE
```

There are additional, optional args:
* `--log`: If True, logs to the ./logs directory. If False (default), prints to stdout
* `--username`: Username for accessing SCM (required if `--password` is provided)
* `--password`: Password for accessing SCM (required if `--username` is provided)
* `--scm_key`: SSH key for accessing SCM

### Python package

Coming soon

### Docker

Coming soon

### Helm

Coming soon
