from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DirectoryServiceDeleteTrustRequest(BaseModel):
    TrustId: StrictStr
    DeleteAssociatedConditionalForwarder: StrictBool | None = None
