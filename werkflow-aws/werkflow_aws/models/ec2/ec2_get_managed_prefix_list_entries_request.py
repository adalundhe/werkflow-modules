from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2GetManagedPrefixListEntriesRequest(BaseModel):
    PrefixListId: StrictStr
    DryRun: StrictBool | None = None
    TargetVersion: StrictInt | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
