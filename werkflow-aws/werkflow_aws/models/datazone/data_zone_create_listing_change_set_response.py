from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneCreateListingChangeSetResponse(BaseModel):
    listingId: StrictStr | None = None
    listingRevision: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
