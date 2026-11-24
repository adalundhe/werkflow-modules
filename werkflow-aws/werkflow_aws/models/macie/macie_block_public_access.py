from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MacieBlockPublicAccess(BaseModel):
    blockPublicAcls: StrictBool | None = None
    blockPublicPolicy: StrictBool | None = None
    ignorePublicAcls: StrictBool | None = None
    restrictPublicBuckets: StrictBool | None = None
