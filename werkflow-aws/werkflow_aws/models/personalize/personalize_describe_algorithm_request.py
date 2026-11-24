from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeAlgorithmRequest(BaseModel):
    algorithmArn: StrictStr
