from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EndUserMessagingVerifiedDestinationNumberInformation(BaseModel):
    VerifiedDestinationNumberArn: StrictStr | None = None
    VerifiedDestinationNumberId: StrictStr | None = None
    DestinationPhoneNumber: StrictStr | None = None
    Status: StrictStr | None = None
    RcsAgentId: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
