from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAwsLocation(BaseModel):
    accessRole: StrictStr | None = None
    awsAccountId: StrictStr | None = None
    awsRegion: StrictStr | None = None
    iamConnectionId: StrictStr | None = None
