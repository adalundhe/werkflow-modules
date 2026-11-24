from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionDescribeStreamProcessorRequest(BaseModel):
    Name: StrictStr
