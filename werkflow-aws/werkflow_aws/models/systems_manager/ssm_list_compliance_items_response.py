from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_compliance_item import SSMComplianceItem


class SSMListComplianceItemsResponse(BaseModel):
    ComplianceItems: list[SSMComplianceItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
