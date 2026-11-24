from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_patch_filter_group import SSMPatchFilterGroup


class SSMPatchRule(BaseModel):
    PatchFilterGroup: SSMPatchFilterGroup | None = None
    ComplianceLevel: StrictStr | None = None
    ApproveAfterDays: StrictInt | None = None
    ApproveUntilDate: StrictStr | None = None
    EnableNonSecurity: StrictBool | None = None
