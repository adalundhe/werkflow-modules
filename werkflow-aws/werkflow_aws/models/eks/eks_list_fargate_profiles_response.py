from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSListFargateProfilesResponse(BaseModel):
    fargateProfileNames: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
