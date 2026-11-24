from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_patch_filter_group import SSMPatchFilterGroup
from .ssm_patch_rule_group import SSMPatchRuleGroup
from .ssm_patch_source import SSMPatchSource


class SSMGetPatchBaselineResponse(BaseModel):
    BaselineId: StrictStr | None = None
    Name: StrictStr | None = None
    OperatingSystem: StrictStr | None = None
    GlobalFilters: SSMPatchFilterGroup | None = None
    ApprovalRules: SSMPatchRuleGroup | None = None
    ApprovedPatches: list[StrictStr] | None = None
    ApprovedPatchesComplianceLevel: StrictStr | None = None
    ApprovedPatchesEnableNonSecurity: StrictBool | None = None
    RejectedPatches: list[StrictStr] | None = None
    RejectedPatchesAction: StrictStr | None = None
    PatchGroups: list[StrictStr] | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    ModifiedDate: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Sources: list[SSMPatchSource] | None = None
    AvailableSecurityUpdatesComplianceStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
