from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_source_access_type import LambdaSourceAccessType


class LambdaSourceAccessConfiguration(BaseModel):
    Type: LambdaSourceAccessType | None = None
    URI: StrictStr | None = None
