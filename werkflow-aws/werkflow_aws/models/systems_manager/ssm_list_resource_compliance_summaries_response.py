from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_resource_compliance_summary_item import SSMResourceComplianceSummaryItem


class SSMListResourceComplianceSummariesResponse(BaseModel):
    ResourceComplianceSummaryItems: list[SSMResourceComplianceSummaryItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
