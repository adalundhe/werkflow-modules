from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_patch_filter_group import SSMPatchFilterGroup
from .ssm_patch_rule_group import SSMPatchRuleGroup
from .ssm_patch_source import SSMPatchSource


class SSMUpdatePatchBaselineRequest(BaseModel):
    BaselineId: StrictStr
    Name: StrictStr | None = None
    GlobalFilters: SSMPatchFilterGroup | None = None
    ApprovalRules: SSMPatchRuleGroup | None = None
    ApprovedPatches: list[StrictStr] | None = None
    ApprovedPatchesComplianceLevel: Literal['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFORMATIONAL', 'UNSPECIFIED'] | None = None
    ApprovedPatchesEnableNonSecurity: StrictBool | None = None
    RejectedPatches: list[StrictStr] | None = None
    RejectedPatchesAction: Literal['ALLOW_AS_DEPENDENCY', 'BLOCK'] | None = None
    Description: StrictStr | None = None
    Sources: list[SSMPatchSource] | None = None
    AvailableSecurityUpdatesComplianceStatus: Literal['COMPLIANT', 'NON_COMPLIANT'] | None = None
    Replace: StrictBool | None = None
