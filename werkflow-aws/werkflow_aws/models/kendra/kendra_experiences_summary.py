from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kendra_experience_endpoint import KendraExperienceEndpoint


class KendraExperiencesSummary(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Endpoints: list[KendraExperienceEndpoint] | None = None
