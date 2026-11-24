from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetWebExperienceRequest(BaseModel):
    applicationId: StrictStr
    webExperienceId: StrictStr
