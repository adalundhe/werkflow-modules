from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_compliance_string_filter import SSMComplianceStringFilter


class SSMListResourceComplianceSummariesRequest(BaseModel):
    Filters: list[SSMComplianceStringFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
