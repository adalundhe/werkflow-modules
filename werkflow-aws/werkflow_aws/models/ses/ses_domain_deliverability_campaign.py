from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SESDomainDeliverabilityCampaign(BaseModel):
    CampaignId: StrictStr | None = None
    ImageUrl: StrictStr | None = None
    Subject: StrictStr | None = None
    FromAddress: StrictStr | None = None
    SendingIps: list[StrictStr] | None = None
    FirstSeenDateTime: datetime.datetime | StrictStr | None = None
    LastSeenDateTime: datetime.datetime | StrictStr | None = None
    InboxCount: StrictInt | None = None
    SpamCount: StrictInt | None = None
    ReadRate: StrictFloat | StrictInt | None = None
    DeleteRate: StrictFloat | StrictInt | None = None
    ReadDeleteRate: StrictFloat | StrictInt | None = None
    ProjectedVolume: StrictInt | None = None
    Esps: list[StrictStr] | None = None
