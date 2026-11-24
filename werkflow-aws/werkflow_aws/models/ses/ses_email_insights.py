from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_insights_event import SESInsightsEvent


class SESEmailInsights(BaseModel):
    Destination: StrictStr | None = None
    Isp: StrictStr | None = None
    Events: list[SESInsightsEvent] | None = None
