#!/usr/bin/env python3
#
#
#  IRIS {{ cookiecutter.artefact }} Source Code
#  Copyright (C) {% now 'utc', '%Y' %} - {{ cookiecutter.organization }}
#  {{ cookiecutter.email}}
#  Created by {{ cookiecutter.organization }} - {% now 'utc', '%Y%m%d' %}
#
#  License {{ cookiecutter.license }}

module_name = "Iris{{ cookiecutter.artefact }}"
module_description = ""
interface_version = 1.1
module_version = 1.0
pipeline_support = True
pipeline_info = {
    "pipeline_internal_name": "{{ cookiecutter.artefact }}_pipeline",
    "pipeline_human_name": "{{ cookiecutter.artefact }} Pipeline",
    "pipeline_args": [
        ['{{ cookiecutter.artefact }}_arg', 'optional']
    ],
    "pipeline_update_support": True,
    "pipeline_import_support": True
}
module_configuration = [
    {
        "param_name": "{{ cookiecutter.artefact }}_url",
        "param_human_name": "{{ cookiecutter.artefact }} URL",
        "param_description": "",
        "default": None,
        "mandatory": True,
        "type": "string"
    },
    {
        "param_name": "{{ cookiecutter.artefact }}_key",
        "param_human_name": "{{ cookiecutter.artefact }} key",
        "param_description": "{{ cookiecutter.artefact }} API key",
        "default": None,
        "mandatory": True,
        "type": "sensitive_string"
    }
]