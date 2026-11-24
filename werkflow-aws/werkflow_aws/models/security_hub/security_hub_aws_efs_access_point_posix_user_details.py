from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEfsAccessPointPosixUserDetails(BaseModel):
    Gid: StrictStr | None = None
    SecondaryGids: list[StrictStr] | None = None
    Uid: StrictStr | None = None
