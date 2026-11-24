from __future__ import annotations
from pydantic import BaseModel, StrictBool


class AccessAnalyzerS3PublicAccessBlockConfiguration(BaseModel):
    ignorePublicAcls: StrictBool | None = None
    restrictPublicBuckets: StrictBool | None = None
