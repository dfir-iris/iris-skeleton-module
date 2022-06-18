#!/usr/bin/env python3
#
#
#  IRIS {{ cookiecutter.keyword }} Source Code
#  Copyright (C) {% now 'utc', '%Y' %} - {{ cookiecutter.organization }}
#  {{ cookiecutter.email}}
#  Created by {{ cookiecutter.organization }} - {% now 'utc', '%Y-%m-%d' %}
#
#  License {{ cookiecutter.license }}

module_name = "Iris{{ cookiecutter.keyword[0].upper() + cookiecutter.keyword[1:] }}"
module_description = ""
interface_version = 1.1
module_version = 1.0
pipeline_support = True
pipeline_info = {
    "pipeline_internal_name": "{{ cookiecutter.keyword }}_pipeline",
    "pipeline_human_name": "{{ cookiecutter.keyword }} Pipeline",
    "pipeline_args": [
        ['{{ cookiecutter.keyword }}_arg', 'optional']
    ],
    "pipeline_update_support": True,
    "pipeline_import_support": True
}
module_configuration = [
    {
        "param_name": "{{ cookiecutter.keyword }}_url",
        "param_human_name": "{{ cookiecutter.keyword }} URL",
        "param_description": "",
        "default": None,
        "mandatory": True,
        "type": "string"
    },
    {
        "param_name": "{{ cookiecutter.keyword }}_key",
        "param_human_name": "{{ cookiecutter.keyword }} key",
        "param_description": "{{ cookiecutter.keyword }} API key",
        "default": None,
        "mandatory": True,
        "type": "sensitive_string"
    }
]