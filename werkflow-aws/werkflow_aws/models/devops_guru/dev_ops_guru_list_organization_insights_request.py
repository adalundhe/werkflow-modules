from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dev_ops_guru_list_insights_status_filter import DevOpsGuruListInsightsStatusFilter


class DevOpsGuruListOrganizationInsightsRequest(BaseModel):
    StatusFilter: DevOpsGuruListInsightsStatusFilter
    MaxResults: StrictInt | None = None
    AccountIds: list[StrictStr] | None = None
    OrganizationalUnitIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
