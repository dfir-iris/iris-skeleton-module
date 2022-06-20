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
{% if cookiecutter.support == 'pipeline' %}
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
{% else %}
pipeline_support = False
pipeline_info = {}
{% endif %}

module_configuration = [
    {
        "param_name": "{{ cookiecutter.keyword.lower() }}_url",
        "param_human_name": "{{ cookiecutter.keyword }} URL",
        "param_description": "",
        "default": None,
        "mandatory": True,
        "type": "string"
    },
    {
        "param_name": "{{ cookiecutter.keyword.lower() }}_key",
        "param_human_name": "{{ cookiecutter.keyword }} key",
        "param_description": "{{ cookiecutter.keyword }} API key",
        "default": None,
        "mandatory": True,
        "type": "sensitive_string"
    },
    {% if cookiecutter.support == 'processor' %}
    {
        "param_name": "{{ cookiecutter.keyword.lower() }}_manual_hook_enabled",
        "param_human_name": "Manual triggers on IOCs",
        "param_description": "Set to True to offers possibility to manually triggers the module via the UI",
        "default": True,
        "mandatory": True,
        "type": "bool",
        "section": "Triggers"
    },
    {
        "param_name": "{{ cookiecutter.keyword.lower() }}_on_create_hook_enabled",
        "param_human_name": "Triggers automatically on IOC create",
        "param_description": "Set to True to automatically add a {{ cookiecutter.keyword }} insight each time an IOC is created",
        "default": False,
        "mandatory": True,
        "type": "bool",
        "section": "Triggers"
    },
    {
        "param_name": "{{ cookiecutter.keyword.lower() }}_on_update_hook_enabled",
        "param_human_name": "Triggers automatically on IOC update",
        "param_description": "Set to True to automatically add a {{ cookiecutter.keyword }} insight each time an IOC is updated",
        "default": False,
        "mandatory": True,
        "type": "bool",
        "section": "Triggers"
    },
    {
        "param_name": "{{ cookiecutter.keyword.lower() }}_report_as_attribute",
        "param_human_name": "Add {{ cookiecutter.keyword }} report as new IOC attribute",
        "param_description": "Creates a new attribute on the IOC, base on the {{ cookiecutter.keyword }} report. Attributes are based "
                             "on the templates of this configuration",
        "default": True,
        "mandatory": True,
        "type": "bool",
        "section": "Insights"
    },# TODO: careful here, remove backslashes from \{\{ results| tojson(indent=4) \}\}
    {
        "param_name": "{{ cookiecutter.keyword.lower() }}_domain_report_template",
        "param_human_name": "Domain report template",
        "param_description": "Domain report template used to add a new custom attribute to the target IOC",
        "default": "<div class=\"row\">\n    <div class=\"col-12\">\n        <div "
                   "class=\"accordion\">\n            <h3>{{ cookiecutter.keyword }} raw results</h3>\n\n           "
                   " <div class=\"card\">\n                <div class=\"card-header "
                   "collapsed\" id=\"drop_r_{{ cookiecutter.keyword.lower() }}\" data-toggle=\"collapse\" "
                   "data-target=\"#drop_raw_{{ cookiecutter.keyword.lower() }}\" aria-expanded=\"false\" "
                   "aria-controls=\"drop_raw_{{ cookiecutter.keyword.lower() }}\" role=\"button\">\n                    <div "
                   "class=\"span-icon\">\n                        <div "
                   "class=\"flaticon-file\"></div>\n                    </div>\n              "
                   "      <div class=\"span-title\">\n                        {{ cookiecutter.keyword }} raw "
                   "results\n                    </div>\n                    <div "
                   "class=\"span-mode\"></div>\n                </div>\n                <div "
                   "id=\"drop_raw_{{ cookiecutter.keyword.lower() }}\" class=\"collapse\" aria-labelledby=\"drop_r_{{ cookiecutter.keyword.lower() }}\" "
                   "style=\"\">\n                    <div class=\"card-body\">\n              "
                   "          <div id='{{ cookiecutter.keyword.lower() }}_raw_ace'>\{\{ results| tojson(indent=4) \}\}</div>\n  "
                   "                  </div>\n                </div>\n            </div>\n    "
                   "    </div>\n    </div>\n</div> \n<script>\nvar {{ cookiecutter.keyword.lower() }}_in_raw = ace.edit("
                   "\"{{ cookiecutter.keyword.lower() }}_raw_ace\",\n{\n    autoScrollEditorIntoView: true,\n    minLines: "
                   "30,\n});\n{{ cookiecutter.keyword.lower() }}_in_raw.setReadOnly(true);\n{{ cookiecutter.keyword.lower() }}_in_raw.setTheme("
                   "\"ace/theme/tomorrow\");\n{{ cookiecutter.keyword.lower() }}_in_raw.session.setMode("
                   "\"ace/mode/json\");\n{{ cookiecutter.keyword.lower() }}_in_raw.renderer.setShowGutter("
                   "true);\n{{ cookiecutter.keyword.lower() }}_in_raw.setOption(\"showLineNumbers\", "
                   "true);\n{{ cookiecutter.keyword.lower() }}_in_raw.setOption(\"showPrintMargin\", "
                   "false);\n{{ cookiecutter.keyword.lower() }}_in_raw.setOption(\"displayIndentGuides\", "
                   "true);\n{{ cookiecutter.keyword.lower() }}_in_raw.setOption(\"maxLines\", "
                   "\"Infinity\");\n{{ cookiecutter.keyword.lower() }}_in_raw.session.setUseWrapMode("
                   "true);\n{{ cookiecutter.keyword.lower() }}_in_raw.setOption(\"indentedSoftWrap\", "
                   "true);\n{{ cookiecutter.keyword.lower() }}_in_raw.renderer.setScrollMargin(8, 5);\n</script> ",
        "mandatory": False,
        "type": "textfield_html",
        "section": "Templates"
    }
    {% endif %}
]