# iris-skeleton-module

This repository is an IRIS module generator based on cookiecutter and inspired by [python-package-template](https://github.com/TezRomacH/python-package-template).

This tool is in its early phase. Other input variables will be integrated.

## How to use

### Installation

> Python requirements : >3.7

First, install pip and cookiecutter:
```commandline
pip install -U cookiecutter
```

Then go to a directory where you want to create your project and run:

```commandline
cookiecutter gh:dfir-iris/iris-skeleton-module
```

Follow the instructions and voilà! Now you can start developing your module without dealing with all the boilerplate code! :tada:

### Input variables

Template generator will ask you to fill some variables.

The input variables, with their default values:

|    **Parameter**     |                         **Default value**                          | **Description**                                                                                                      |
|:--------------------:|:------------------------------------------------------------------:|----------------------------------------------------------------------------------------------------------------------|
|    `module_name`     |                 As an example : `iris-toto-module`                 | [Check the availability of possible name](http://ivantomic.com/projects/ospnc/) before creating the project.         |
|      `keyword`       | based on the `module_name` or `toto` if `module_name` is malformed | Set the keyword name (e.g the tool you want to interface IRIS with or the type of artefact you want to ingest        |
| `module_description` |                     based on the `module_name`                     | Brief description of your project.                                                                                   |
|    `organization`    |                     based on the `module_name`                     | Name of the organization. We need to generate LICENCE and to specify ownership in `pyproject.toml`.                  |
|      `license`       |                               `MIT`                                | One of `MIT`, `BSD-3`, `GNU GPL v3.0`, `Lesser GNU GPL v3.0` and `Apache Software License 2.0`.                      |
|    `github_name`     |                    based on the `organization`                     | GitHub username for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for GitHub.        |
|       `email`        |                    based on the `organization`                     | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`. |
|      `version`       |                              `0.1.0`                               | Initial version of the package. Make sure it follows the [Semantic Versions](https://semver.org/) specification.     |
|      `support`       |                             `pipeline`                             | The created module will have boilerplate code for either `pipeline` or `processor` module.                           |

Once generated, the template modules can be installed on IRIS and are working ;). For the processor template module, you still need to change the following value :
- From `\{\{ results| tojson(indent=4) \}\}` (I had to do this, else cookiecutter would interpret this as its jinja field)
- To `{{ results| tojson(indent=4) }}`

Once setup, check the post-generation instructions output in the CLI 

## Documentation

For more information on how to develop IRIS modules, please consider reading the documentation: https://docs.dfir-iris.org/development/modules/.

## Help

You can reach us on [Discord](https://discord.gg/76tM6QUJza), [Element](https://matrix.to/#/#dfir-iris:matrix.org) or by [mail](contact@dfir-iris.org) if you have any question, issue, or idea!

## Author and license

Copyright 2022, Théo Letailleur a.k.a ekt0 - at DFIR-IRIS, under the License AGPLv3

