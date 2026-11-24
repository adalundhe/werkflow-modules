from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_compliance_string_filter import SSMComplianceStringFilter


class SSMListComplianceItemsRequest(BaseModel):
    Filters: list[SSMComplianceStringFilter] | None = None
    ResourceIds: list[StrictStr] | None = None
    ResourceTypes: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
