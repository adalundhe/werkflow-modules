from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OrganizationsEffectivePolicy(BaseModel):
    PolicyContent: StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    TargetId: StrictStr | None = None
    PolicyType: StrictStr | None = None
