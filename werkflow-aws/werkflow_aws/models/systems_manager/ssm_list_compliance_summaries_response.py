from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_compliance_summary_item import SSMComplianceSummaryItem


class SSMListComplianceSummariesResponse(BaseModel):
    ComplianceSummaryItems: list[SSMComplianceSummaryItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
