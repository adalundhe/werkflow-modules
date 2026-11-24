from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubStartAppAssessmentRequest(BaseModel):
    appArn: StrictStr
    appVersion: StrictStr
    assessmentName: StrictStr
    clientToken: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
