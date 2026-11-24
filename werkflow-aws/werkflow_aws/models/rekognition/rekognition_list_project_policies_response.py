from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_project_policy import RekognitionProjectPolicy


class RekognitionListProjectPoliciesResponse(BaseModel):
    ProjectPolicies: list[RekognitionProjectPolicy] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
