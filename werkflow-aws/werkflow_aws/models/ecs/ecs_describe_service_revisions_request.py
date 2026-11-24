from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDescribeServiceRevisionsRequest(BaseModel):
    serviceRevisionArns: list[StrictStr]
