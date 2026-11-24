from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .wa_fv2_tag import WAFv2Tag


class WAFv2MobileSdkRelease(BaseModel):
    ReleaseVersion: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    ReleaseNotes: StrictStr | None = None
    Tags: list[WAFv2Tag] | None = None
