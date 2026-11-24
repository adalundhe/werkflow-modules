from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerDescribeModelCardRequest(BaseModel):
    ModelCardName: StrictStr
    ModelCardVersion: StrictInt | None = None
    IncludedData: Literal['AllData', 'MetadataOnly'] | None = None
