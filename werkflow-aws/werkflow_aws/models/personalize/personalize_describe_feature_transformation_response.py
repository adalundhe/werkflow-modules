from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_feature_transformation import PersonalizeFeatureTransformation


class PersonalizeDescribeFeatureTransformationResponse(BaseModel):
    featureTransformation: PersonalizeFeatureTransformation | None = None
    ResponseMetadata: dict[str, Any] | None = None
