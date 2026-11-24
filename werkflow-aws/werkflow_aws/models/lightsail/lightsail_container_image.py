from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailContainerImage(BaseModel):
    image: StrictStr | None = None
    digest: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
