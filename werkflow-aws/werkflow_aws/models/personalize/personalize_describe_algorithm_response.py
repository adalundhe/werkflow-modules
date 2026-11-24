from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_algorithm import PersonalizeAlgorithm


class PersonalizeDescribeAlgorithmResponse(BaseModel):
    algorithm: PersonalizeAlgorithm | None = None
    ResponseMetadata: dict[str, Any] | None = None
