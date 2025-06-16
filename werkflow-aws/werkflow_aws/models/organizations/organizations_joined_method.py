from enum import Enum
from typing import Literal


AWSJoinedMethod = Literal[
    "INVITED",
    "CREATED",
]


JoinedMethodName = Literal[
    "invited",
    "created",
]


class OrganizationsJoinedMethod(Enum):
    INVITED='INVITED'
    CREATED='CREATED'


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