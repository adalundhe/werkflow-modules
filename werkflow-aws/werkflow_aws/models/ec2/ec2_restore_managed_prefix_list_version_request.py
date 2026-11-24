from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2RestoreManagedPrefixListVersionRequest(BaseModel):
    PrefixListId: StrictStr
    PreviousVersion: StrictInt
    CurrentVersion: StrictInt
    DryRun: StrictBool | None = None
