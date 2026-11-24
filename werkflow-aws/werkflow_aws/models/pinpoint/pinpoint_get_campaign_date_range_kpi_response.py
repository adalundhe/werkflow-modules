from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_campaign_date_range_kpi_response import PinpointCampaignDateRangeKpiResponse


class PinpointGetCampaignDateRangeKpiResponse(BaseModel):
    CampaignDateRangeKpiResponse: PinpointCampaignDateRangeKpiResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
