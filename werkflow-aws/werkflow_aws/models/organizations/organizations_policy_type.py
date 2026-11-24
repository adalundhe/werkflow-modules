from __future__ import annotations
from typing import Literal


OrganizationsPolicyType = Literal[
    'SERVICE_CONTROL_POLICY',
    'RESOURCE_CONTROL_POLICY',
    'TAG_POLICY',
    'BACKUP_POLICY',
    'AISERVICES_OPT_OUT_POLICY',
    'CHATBOT_POLICY',
    'DECLARATIVE_POLICY_EC2',
]
