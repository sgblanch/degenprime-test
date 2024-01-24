# degenprime-test
Experiment in python frontends and packaging using [Setuptools](https://setuptools.pypa.io/en/latest/setuptools.html)

## Using "Editable Install" for Development
VSCode should detect venv if run this at root of this project.  You will also likely need to re-run the `pip install --editable .` if you add/remove files

```console
% python3.12 -m venv venv
% venv/bin/pip3 install build
% venv/bin/pip3 install --editable .
% venv/bin/degenprime-validate
```

> **Note:**
>
> There are two ways to run the application
>
> - `degenprime-validate` excutable defined in `pypackage.toml`
> - `python3 -m degenprime.validate` defined in `__main__.py`

## Building and installing wheel

> **Note:** Needed for testing `pypackage.toml`

```console
% venv/bin/python3 -m build .
% venv/bin/python3 -m pip install --force-reinstall dist/degenprime_test-0.1.1-py3-none-any.whl
```

