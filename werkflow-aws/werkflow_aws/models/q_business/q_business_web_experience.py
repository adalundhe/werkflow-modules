from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QBusinessWebExperience(BaseModel):
    webExperienceId: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    defaultEndpoint: StrictStr | None = None
    status: StrictStr | None = None
