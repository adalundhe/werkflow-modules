from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteWebExperienceRequest(BaseModel):
    applicationId: StrictStr
    webExperienceId: StrictStr
