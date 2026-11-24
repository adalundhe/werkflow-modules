from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessCreateAnonymousWebExperienceUrlRequest(BaseModel):
    applicationId: StrictStr
    webExperienceId: StrictStr
    sessionDurationInMinutes: StrictInt | None = None
