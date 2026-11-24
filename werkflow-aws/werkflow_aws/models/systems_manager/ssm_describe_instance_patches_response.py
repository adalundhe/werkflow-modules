from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_patch_compliance_data import SSMPatchComplianceData


class SSMDescribeInstancePatchesResponse(BaseModel):
    Patches: list[SSMPatchComplianceData] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
