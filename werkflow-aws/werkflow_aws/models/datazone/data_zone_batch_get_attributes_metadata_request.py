from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneBatchGetAttributesMetadataRequest(BaseModel):
    domainIdentifier: StrictStr
    entityType: Literal['ASSET', 'LISTING']
    entityIdentifier: StrictStr
    attributeIdentifiers: list[StrictStr]
    entityRevision: StrictStr | None = None
