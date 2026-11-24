from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_remediation_string_filter_condition import SecurityHubRemediationStringFilterCondition


class SecurityHubRemediationStringFilter(BaseModel):
    FieldName: Literal['Resource.Type', 'Priority', 'Status', 'Resource.Id', 'Resource.ResourceOwnerAccountId', 'Resource.CloudProvider']
    Filter: SecurityHubRemediationStringFilterCondition
