from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .fms_resource_tag import FMSResourceTag
from .fms_security_service_policy_data import FMSSecurityServicePolicyData


class FMSPolicy(BaseModel):
    PolicyId: StrictStr | None = None
    PolicyName: StrictStr | None = None
    PolicyUpdateToken: StrictStr | None = None
    SecurityServicePolicyData: FMSSecurityServicePolicyData | None = None
    ResourceType: StrictStr | None = None
    ResourceTypeList: list[StrictStr] | None = None
    ResourceTags: list[FMSResourceTag] | None = None
    ExcludeResourceTags: StrictBool | None = None
    RemediationEnabled: StrictBool | None = None
    DeleteUnusedFMManagedResources: StrictBool | None = None
    IncludeMap: dict[StrictStr, list[StrictStr]] | None = None
    ExcludeMap: dict[StrictStr, list[StrictStr]] | None = None
    ResourceSetIds: list[StrictStr] | None = None
    PolicyDescription: StrictStr | None = None
    PolicyStatus: StrictStr | None = None
    ResourceTagLogicalOperator: StrictStr | None = None
