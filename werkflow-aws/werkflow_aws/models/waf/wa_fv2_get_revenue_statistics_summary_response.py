from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_revenue_breakdown import WAFv2RevenueBreakdown


class WAFv2GetRevenueStatisticsSummaryResponse(BaseModel):
    RevenueBreakdown: WAFv2RevenueBreakdown | None = None
    ResponseMetadata: dict[str, Any] | None = None
