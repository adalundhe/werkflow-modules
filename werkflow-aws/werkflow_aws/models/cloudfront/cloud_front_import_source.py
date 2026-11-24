from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFrontImportSource(BaseModel):
    SourceType: Literal['S3']
    SourceARN: StrictStr
