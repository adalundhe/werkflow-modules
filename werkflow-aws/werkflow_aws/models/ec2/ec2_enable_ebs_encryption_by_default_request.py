from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2EnableEbsEncryptionByDefaultRequest(BaseModel):
    DryRun: StrictBool | None = None
