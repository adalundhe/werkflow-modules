from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeCampaignSummary(BaseModel):
    name: StrictStr | None = None
    campaignArn: StrictStr | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
