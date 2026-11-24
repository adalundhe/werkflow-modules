from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ses_message_insights_filters import SESMessageInsightsFilters


class SESMessageInsightsDataSource(BaseModel):
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    Include: SESMessageInsightsFilters | None = None
    Exclude: SESMessageInsightsFilters | None = None
    MaxResults: StrictInt | None = None
