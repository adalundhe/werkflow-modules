from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneIamUserProfileDetails(BaseModel):
    arn: StrictStr | None = None
    principalId: StrictStr | None = None
    sessionName: StrictStr | None = None
    groupProfileId: StrictStr | None = None
