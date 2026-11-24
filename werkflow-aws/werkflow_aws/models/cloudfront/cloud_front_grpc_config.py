from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CloudFrontGrpcConfig(BaseModel):
    Enabled: StrictBool | None = None
