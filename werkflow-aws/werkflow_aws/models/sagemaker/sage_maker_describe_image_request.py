from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeImageRequest(BaseModel):
    ImageName: StrictStr
