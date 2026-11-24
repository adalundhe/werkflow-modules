from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BulkChangeOwnerDetails(BaseModel):
    autofixName: StrictBool | None = None
    newOwner: StrictStr | None = None
