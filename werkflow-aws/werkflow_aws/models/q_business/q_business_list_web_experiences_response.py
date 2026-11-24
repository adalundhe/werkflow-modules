from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_web_experience import QBusinessWebExperience


class QBusinessListWebExperiencesResponse(BaseModel):
    webExperiences: list[QBusinessWebExperience] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
