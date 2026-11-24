from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSWebACLHasOutOfScopeResourcesViolation(BaseModel):
    WebACLArn: StrictStr | None = None
    OutOfScopeResourceList: list[StrictStr] | None = None
