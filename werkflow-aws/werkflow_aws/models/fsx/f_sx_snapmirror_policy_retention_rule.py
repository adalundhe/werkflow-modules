from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxSnapmirrorPolicyRetentionRule(BaseModel):
    Label: StrictStr | None = None
    Count: StrictInt | None = None
    CreationSchedule: StrictStr | None = None
