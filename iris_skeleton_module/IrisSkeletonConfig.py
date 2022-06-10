#!/usr/bin/env python3
#
#
#  IRIS Skeleton Source Code
#  Copyright (C) 2022 - DFIR IRIS Team
#  contact@dfir-iris.org
#  Created by ekt0 - 2022-06-09
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

module_name = "IrisSkeleton"
module_description = ""
interface_version = 1.1
module_version = 1.0
pipeline_support = True
pipeline_info = {
    "pipeline_internal_name": "skeleton_pipeline",
    "pipeline_human_name": "Skeleton Pipeline",
    "pipeline_args": [
        ['skeleton_arg', 'optional']
    ],
    "pipeline_update_support": True,
    "pipeline_import_support": True
}
module_configuration = [
    {
        "param_name": "skeleton_url",
        "param_human_name": "Skeleton URL",
        "param_description": "",
        "default": None,
        "mandatory": True,
        "type": "string"
    },
    {
        "param_name": "skeleton_key",
        "param_human_name": "Skeleton key",
        "param_description": "Skeleton API key",
        "default": None,
        "mandatory": True,
        "type": "sensitive_string"
    }
]