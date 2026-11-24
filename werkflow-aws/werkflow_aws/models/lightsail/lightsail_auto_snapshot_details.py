from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_attached_disk import LightsailAttachedDisk


class LightsailAutoSnapshotDetails(BaseModel):
    date: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    fromAttachedDisks: list[LightsailAttachedDisk] | None = None
