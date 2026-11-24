from __future__ import annotations
from .aws_joined_method import AWSJoinedMethod
from .joined_method_name import JoinedMethodName
from .organizations_joined_method import OrganizationsJoinedMethod


class OrganizationsJoinedMethodMap:

    def __init__(self):
        self._joined_method_map: dict[
            JoinedMethodName,
            OrganizationsJoinedMethod
        ] = {
            'created': OrganizationsJoinedMethod.CREATED,
            'invited': OrganizationsJoinedMethod.INVITED,
        }

        self._joined_method_reverse_map: dict[
            AWSJoinedMethod,
            JoinedMethodName,
        ] = {
            'CREATED': 'created',
            'INVITED': 'invited',
        }

    def get(self, joined_method: JoinedMethodName):
        return self._joined_method_map[joined_method]
    
    def get_joined_method_name(self, joined_method_name: AWSJoinedMethod):
        return self._joined_method_reverse_map[joined_method_name]
