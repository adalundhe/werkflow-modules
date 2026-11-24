from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_patch_filter_group import SSMPatchFilterGroup
from .ssm_patch_rule_group import SSMPatchRuleGroup
from .ssm_patch_source import SSMPatchSource
from .ssm_tag import SSMTag


class SSMCreatePatchBaselineRequest(BaseModel):
    Name: StrictStr
    OperatingSystem: Literal['WINDOWS', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'UBUNTU', 'REDHAT_ENTERPRISE_LINUX', 'SUSE', 'CENTOS', 'ORACLE_LINUX', 'DEBIAN', 'MACOS', 'RASPBIAN', 'ROCKY_LINUX', 'ALMA_LINUX', 'AMAZON_LINUX_2023'] | None = None
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
    ClientToken: StrictStr | None = None
    Tags: list[SSMTag] | None = None
