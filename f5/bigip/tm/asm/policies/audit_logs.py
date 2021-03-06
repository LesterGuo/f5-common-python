# coding=utf-8
#
# Copyright 2017 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from f5.sdk_exception import UnsupportedOperation
from f5.bigip.resource import AsmResource
from f5.bigip.resource import Collection


class Audit_Logs_s(Collection):
    """BIG-IP® ASM Audit Logs sub-collection."""
    def __init__(self, policy):
        super(Audit_Logs_s, self).__init__(policy)
        self._meta_data['object_has_stats'] = False
        self._meta_data['minimum_version'] = '12.0.0'
        self._meta_data['allowed_lazy_attributes'] = [Audit_Log]
        self._meta_data['required_json_kind'] = 'tm:asm:policies:audit-logs:audit-logcollectionstate'
        self._meta_data['attribute_registry'] = {
            'tm:asm:policies:audit-logs:audit-logstate': Audit_Log
        }


class Audit_Log(AsmResource):
    """BIG-IP® ASM Audit Logs Resource."""
    def __init__(self, audit_logs_s):
        super(Audit_Log, self).__init__(audit_logs_s)
        self._meta_data['required_json_kind'] = 'tm:asm:policies:audit-logs:audit-logstate'

    def create(self, **kwargs):
        """Modify is not supported for Audit Logs resource

        :raises: UnsupportedOperation
        """
        raise UnsupportedOperation(
            "%s does not support the create method" % self.__class__.__name__
        )

    def modify(self, **kwargs):
        """Modify is not supported for Audit Logs resource

        :raises: UnsupportedOperation
        """
        raise UnsupportedOperation(
            "%s does not support the modify method" % self.__class__.__name__
        )

    def delete(self, **kwargs):
        """Delete is not supported for Audit Logs resource

        :raises: UnsupportedOperation
        """
        raise UnsupportedOperation(
            "%s does not support the delete method" % self.__class__.__name__
        )
