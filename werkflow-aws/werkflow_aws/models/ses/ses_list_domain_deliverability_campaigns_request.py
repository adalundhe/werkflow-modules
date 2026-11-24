from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SESListDomainDeliverabilityCampaignsRequest(BaseModel):
    StartDate: datetime.datetime | StrictStr
    EndDate: datetime.datetime | StrictStr
    SubscribedDomain: StrictStr
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
