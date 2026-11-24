from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneCreateListingChangeSetRequest(BaseModel):
    domainIdentifier: StrictStr
    entityIdentifier: StrictStr
    entityType: Literal['ASSET', 'DATA_PRODUCT']
    action: Literal['PUBLISH', 'UNPUBLISH']
    entityRevision: StrictStr | None = None
    clientToken: StrictStr | None = None
