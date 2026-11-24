from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ResilienceHubDeleteAppAssessmentResponse(BaseModel):
    assessmentArn: StrictStr | None = None
    assessmentStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
