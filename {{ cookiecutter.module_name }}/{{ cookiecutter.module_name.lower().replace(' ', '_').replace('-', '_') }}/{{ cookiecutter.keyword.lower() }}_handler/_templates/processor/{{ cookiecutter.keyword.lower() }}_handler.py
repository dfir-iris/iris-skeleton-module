#!/usr/bin/env python3
#
#
#  IRIS {{ cookiecutter.keyword }} Source Code
#  Copyright (C) {% now 'utc', '%Y' %} - {{ cookiecutter.organization }}
#  {{ cookiecutter.email}}
#  Created by {{ cookiecutter.organization }} - {% now 'utc', '%Y-%m-%d' %}
#
#  License {{ cookiecutter.license }}


import traceback
from jinja2 import Template

import iris_interface.IrisInterfaceStatus as InterfaceStatus
from app.datamgmt.manage.manage_attribute_db import add_tab_attribute_field


class {{ cookiecutter.keyword[0].upper() + cookiecutter.keyword[1:].lower() }}Handler(object):
    def __init__(self, mod_config, server_config, logger):
        self.mod_config = mod_config
        self.server_config = server_config
        self.{{ cookiecutter.keyword.lower() }} = self.get_{{ cookiecutter.keyword.lower() }}_instance()
        self.log = logger

    def get_{{ cookiecutter.keyword.lower() }}_instance(self):
        """
        Returns an {{ cookiecutter.keyword }} API instance depending if the key is premium or not

        :return: { cookiecutter.keyword }} Instance
        """
        url = self.mod_config.get('{{ cookiecutter.keyword.lower() }}_url')
        key = self.mod_config.get('{{ cookiecutter.keyword.lower() }}_key')
        proxies = {}

        if self.server_config.get('http_proxy'):
            proxies['https'] = self.server_config.get('HTTPS_PROXY')

        if self.server_config.get('https_proxy'):
            proxies['http'] = self.server_config.get('HTTP_PROXY')

        # TODO!
        # Here get your {{ cookiecutter.keyword }} instance and return it
        # ex: return {{ cookiecutter.keyword.lower() }}Api(url, key)
        return "<TODO>"

    def gen_domain_report_from_template(self, html_template, {{ cookiecutter.keyword.lower() }}_report) -> InterfaceStatus:
        """
        Generates an HTML report for Domain, displayed as an attribute in the IOC

        :param html_template: A string representing the HTML template
        :param misp_report: The JSON report fetched with {{ cookiecutter.keyword }} API
        :return: InterfaceStatus
        """
        template = Template(html_template)
        context = {{ cookiecutter.keyword.lower() }}_report
        pre_render = dict({"results": []})

        for {{ cookiecutter.keyword.lower() }}_result in context:
            pre_render["results"].append({{ cookiecutter.keyword.lower() }}_result)

        try:
            rendered = template.render(pre_render)

        except Exception:
            print(traceback.format_exc())
            log.error(traceback.format_exc())
            return InterfaceStatus.I2Error(traceback.format_exc())

        return InterfaceStatus.I2Success(data=rendered)

    def handle_domain(self, ioc):
        """
        Handles an IOC of type domain and adds VT insights

        :param ioc: IOC instance
        :return: IIStatus
        """

        self.log.info(f'Getting domain report for {ioc.ioc_value}')

        # TODO! do your stuff, then report it to the element (here an IOC)

        if self.mod_config.get('{{ cookiecutter.keyword.lower() }}_report_as_attribute') is True:
            self.log.info('Adding new attribute {{ cookiecutter.keyword }} Domain Report to IOC')

            report = ["<TODO> report from {{cookiecutter.keyword.lower()}}"]

            status = self.gen_domain_report_from_template(self.mod_config.get('{{ cookiecutter.keyword.lower() }}_domain_report_template'), report)

            if not status.is_success():
                return status

            rendered_report = status.get_data()

            try:
                add_tab_attribute_field(ioc, tab_name='{{ cookiecutter.keyword }} Report', field_name="HTML report", field_type="html",
                                        field_value=rendered_report)

            except Exception:

                self.log.error(traceback.format_exc())
                return InterfaceStatus.I2Error(traceback.format_exc())
        else:
            self.log.info('Skipped adding attribute report. Option disabled')

        return InterfaceStatus.I2Success()
