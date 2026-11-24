from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .iam_context_entry import IAMContextEntry
from .iam_ordered_organization_policy_type import IAMOrderedOrganizationPolicyType


class IAMSimulateCustomPolicyRequest(BaseModel):
    PolicyInputList: list[StrictStr]
    ActionNames: list[StrictStr]
    PermissionsBoundaryPolicyInputList: list[StrictStr] | None = None
    OrderedOrganizationPolicyInputList: list[IAMOrderedOrganizationPolicyType] | None = None
    ResourceArns: list[StrictStr] | None = None
    ResourcePolicy: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
    CallerArn: StrictStr | None = None
    ContextEntries: list[IAMContextEntry] | None = None
    ResourceHandlingOption: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
