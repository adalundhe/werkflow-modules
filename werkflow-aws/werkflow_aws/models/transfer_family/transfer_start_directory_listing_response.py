from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class TransferStartDirectoryListingResponse(BaseModel):
    ListingId: StrictStr | None = None
    OutputFileName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
