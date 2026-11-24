from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EndUserMessagingRegistrationInformation(BaseModel):
    RegistrationArn: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    RegistrationType: StrictStr | None = None
    RegistrationStatus: StrictStr | None = None
    CurrentVersionNumber: StrictInt | None = None
    ApprovedVersionNumber: StrictInt | None = None
    LatestDeniedVersionNumber: StrictInt | None = None
    AdditionalAttributes: dict[StrictStr, StrictStr] | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
