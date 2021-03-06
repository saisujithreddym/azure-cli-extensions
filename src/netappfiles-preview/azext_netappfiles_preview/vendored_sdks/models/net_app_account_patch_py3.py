# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NetAppAccountPatch(Model):
    """NetApp account patch resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param location: Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: object
    :ivar provisioning_state: Azure lifecycle management
    :vartype provisioning_state: str
    :param active_directories: Active Directories
    :type active_directories: list[~azure.mgmt.netapp.models.ActiveDirectory]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'active_directories': {'key': 'properties.activeDirectories', 'type': '[ActiveDirectory]'},
    }

    def __init__(self, *, location: str=None, tags=None, active_directories=None, **kwargs) -> None:
        super(NetAppAccountPatch, self).__init__(**kwargs)
        self.location = location
        self.id = None
        self.name = None
        self.type = None
        self.tags = tags
        self.provisioning_state = None
        self.active_directories = active_directories
