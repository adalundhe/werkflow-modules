from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeFeatureTransformationRequest(BaseModel):
    featureTransformationArn: StrictStr
