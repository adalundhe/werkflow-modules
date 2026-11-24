from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_list_insights_any_status_filter import DevOpsGuruListInsightsAnyStatusFilter
from .dev_ops_guru_list_insights_closed_status_filter import DevOpsGuruListInsightsClosedStatusFilter
from .dev_ops_guru_list_insights_ongoing_status_filter import DevOpsGuruListInsightsOngoingStatusFilter


class DevOpsGuruListInsightsStatusFilter(BaseModel):
    Ongoing: DevOpsGuruListInsightsOngoingStatusFilter | None = None
    Closed: DevOpsGuruListInsightsClosedStatusFilter | None = None
    Any: DevOpsGuruListInsightsAnyStatusFilter | None = None
