from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .iam_context_entry import IAMContextEntry
from .iam_policy_identifier import IAMPolicyIdentifier


class IAMSimulatePrincipalPolicyRequest(BaseModel):
    PolicySourceArn: StrictStr
    ActionNames: list[StrictStr]
    PolicyInputList: list[StrictStr] | None = None
    PermissionsBoundaryPolicyInputList: list[StrictStr] | None = None
    PolicyExclusionList: list[IAMPolicyIdentifier] | None = None
    ResourceArns: list[StrictStr] | None = None
    ResourcePolicy: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
    CallerArn: StrictStr | None = None
    ContextEntries: list[IAMContextEntry] | None = None
    ResourceHandlingOption: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
