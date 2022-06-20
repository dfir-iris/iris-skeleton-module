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
from pathlib import Path

import iris_interface.IrisInterfaceStatus as InterfaceStatus
from iris_interface.IrisModuleInterface import IrisPipelineTypes, IrisModuleInterface, IrisModuleTypes

import iris_{{ cookiecutter.keyword.lower() }}_module.Iris{{ cookiecutter.keyword[0].upper() + cookiecutter.keyword[1:].lower() }}Config as interface_conf
from iris_{{ cookiecutter.keyword.lower() }}_module.{{ cookiecutter.keyword.lower() }}_handler.{{ cookiecutter.keyword.lower() }}_handler import {{ cookiecutter.keyword[0].upper() + cookiecutter.keyword[1:].lower() }}Handler


class Iris{{ cookiecutter.keyword[0].upper() + cookiecutter.keyword[1:].lower() }}Interface(IrisModuleInterface):
    """
    Provide the interface between Iris and {{ cookiecutter.keyword }}Handler
    """
    name = "Iris{{ cookiecutter.keyword[0].upper() + cookiecutter.keyword[1:].lower() }}Interface"
    _module_name = interface_conf.module_name
    _module_description = interface_conf.module_description
    _interface_version = interface_conf.interface_version
    _module_version = interface_conf.module_version
    _pipeline_support = interface_conf.pipeline_support
    _pipeline_info = interface_conf.pipeline_info
    _module_configuration = interface_conf.module_configuration
    {% if cookiecutter.support == 'pipeline' %}
    _module_type = IrisModuleTypes.module_pipeline
    {% else %}
    _module_type = IrisModuleTypes.module_processor
    {% endif %}
    {% if cookiecutter.support == 'pipeline' %}
    def pipeline_handler(self, pipeline_type, pipeline_data):
        """
        Receive data from the main pipeline and dispatch to {{ cookiecutter.keyword }} handler
        :param pipeline_type:
        :param pipeline_data:
        :return:
        """

        if pipeline_type == IrisPipelineTypes.pipeline_type_import:
            #  Call the import chain as task chain
            return self.task_files_import(input_data=pipeline_data)

        elif pipeline_type == IrisPipelineTypes.pipeline_type_update:
            # Call the update chain as task chain
            return self.task_files_import(input_data=pipeline_data)

        else:
            return InterfaceStatus.I2Error('Unrecognized pipeline type')

    def pipeline_files_upload(self, base_path, file_handle, case_customer, case_name, is_update):
        """
        Handle the files for a specific
        :return:
        """

        if base_path and Path(base_path).is_dir:
            file_handle.save(Path(base_path, file_handle.filename))
            return InterfaceStatus.I2Success("Successfully saved file {} to {}".format(file_handle.filename, base_path))

        else:
            return InterfaceStatus.I2Error("Directory {} not found. Can't save file".format(base_path))

    def task_files_import(self, input_data):

        try:
            configuration = self.get_configuration_dict()
            if self._evidence_storage:

                if configuration.is_success():

                    {{ cookiecutter.keyword.lower() }}_handler = {{ cookiecutter.keyword[0].upper() + cookiecutter.keyword[1:].lower() }}Handler(mod_config=self.module_dict_conf,
                                                       server_config=self.server_dict_conf,
                                                       evidence_storage=self._evidence_storage,
                                                       input_data=input_data,
                                                       logger=self.log)

                    ret = {{ cookiecutter.keyword.lower() }}_handler.import_evidence()
                    if not ret:
                        return InterfaceStatus.I2Error(logs=list(self.message_queue))

                    return InterfaceStatus.I2Success(logs=list(self.message_queue))

                else:
                    self.log.error(logs=[configuration.get_message()])
                    logs = [configuration.get_message()]
            else:
                self.log.error('Evidence storage not available')
                logs = ['Evidence storage not available']

            return InterfaceStatus.I2Error(logs=logs)

        except Exception as e:
            traceback.print_exc()
            return InterfaceStatus.I2Error(logs=[traceback.print_exc()])
    {% endif %} {% if cookiecutter.support == 'processor' %}
    def register_hooks(self, module_id: int):
        """
        Registers all the hooks

        :param module_id: Module ID provided by IRIS
        :return: Nothing
        """
        self.module_id = module_id
        module_conf = self.module_dict_conf
        if module_conf.get('{{ cookiecutter.keyword.lower() }}_on_create_hook_enabled'):
            status = self.register_to_hook(module_id, iris_hook_name='on_postload_ioc_create')
            if status.is_failure():
                self.log.error(status.get_message())
                self.log.error(status.get_data())

            else:
                self.log.info("Successfully registered on_postload_ioc_create hook")
        else:
            self.deregister_from_hook(module_id=self.module_id, iris_hook_name='on_postload_ioc_create')

        if module_conf.get('{{ cookiecutter.keyword.lower() }}_on_update_hook_enabled'):
            status = self.register_to_hook(module_id, iris_hook_name='on_postload_ioc_update')
            if status.is_failure():
                self.log.error(status.get_message())
                self.log.error(status.get_data())

            else:
                self.log.info("Successfully registered on_postload_ioc_update hook")
        else:
            self.deregister_from_hook(module_id=self.module_id, iris_hook_name='on_postload_ioc_update')

        if module_conf.get('{{ cookiecutter.keyword.lower() }}_manual_hook_enabled'):
            status = self.register_to_hook(module_id, iris_hook_name='on_manual_trigger_ioc',
                                           manual_hook_name='Get {{ cookiecutter.keyword }} insight')
            if status.is_failure():
                self.log.error(status.get_message())
                self.log.error(status.get_data())

            else:
                self.log.info("Successfully registered on_manual_trigger_ioc hook")

        else:
            self.deregister_from_hook(module_id=self.module_id, iris_hook_name='on_manual_trigger_ioc')


    def hooks_handler(self, hook_name: str, hook_ui_name: str, data: any):
        """
        Hooks handler table. Calls corresponding methods depending on the hooks name.

        :param hook_name: Name of the hook which triggered
        :param hook_ui_name: Name of the ui hook
        :param data: Data associated with the trigger.
        :return: Data
        """

        self.log.info(f'Received {hook_name}')
        if hook_name in ['on_postload_ioc_create', 'on_postload_ioc_update', 'on_manual_trigger_ioc']:
            status = self._handle_ioc(data=data)

        else:
            self.log.critical(f'Received unsupported hook {hook_name}')
            return InterfaceStatus.I2Error(data=data, logs=list(self.message_queue))

        if status.is_failure():
            self.log.error(f"Encountered error processing hook {hook_name}")
            return InterfaceStatus.I2Error(data=data, logs=list(self.message_queue))

        self.log.info(f"Successfully processed hook {hook_name}")
        return InterfaceStatus.I2Success(data=data, logs=list(self.message_queue))


    def _handle_ioc(self, data) -> InterfaceStatus.IIStatus:
        """
        Handle the IOC data the module just received. The module registered
        to on_postload hooks, so it receives instances of IOC object.
        These objects are attached to a dedicated SQlAlchemy session so data can
        be modified safely.

        :param data: Data associated to the hook, here IOC object
        :return: IIStatus
        """

        {{ cookiecutter.keyword.lower() }}_handler = {{ cookiecutter.keyword[0].upper() + cookiecutter.keyword[1:].lower() }}Handler(mod_config=self.module_dict_conf,
                               server_config=self.server_dict_conf,
                               logger=self.log)

        in_status = InterfaceStatus.IIStatus(code=InterfaceStatus.I2CodeNoError)

        for element in data:
            # Check that the IOC we receive is of type the module can handle and dispatch
            if 'domain' in element.ioc_type.type_name:
                status = {{ cookiecutter.keyword.lower() }}_handler.handle_domain(ioc=element)
                in_status = InterfaceStatus.merge_status(in_status, status)

            #elif element.ioc_type.type_name in ['md5', 'sha224', 'sha256', 'sha512']:
            #    status = {{ cookiecutter.keyword.lower() }}_handler.handle_hash(ioc=element)
            #    in_status = InterfaceStatus.merge_status(in_status, status)
            #
            # elif element.ioc_type.type_name in etc...

            else:
                self.log.error(f'IOC type {element.ioc_type.type_name} not handled by {{ cookiecutter.keyword }} module. Skipping')

        return in_status(data=data)
    {% endif %}
