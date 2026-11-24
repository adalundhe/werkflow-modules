from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailSubdomainAttachableResource(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    attachedAt: datetime.datetime | StrictStr | None = None
