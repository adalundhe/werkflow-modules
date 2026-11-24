from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .verified_permissions_policy_definition_detail import VerifiedPermissionsPolicyDefinitionDetail


class VerifiedPermissionsBatchGetPolicyOutputItem(BaseModel):
    policyStoreId: StrictStr | None = None
    policyId: StrictStr | None = None
    policyType: StrictStr | None = None
    definition: VerifiedPermissionsPolicyDefinitionDetail | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
