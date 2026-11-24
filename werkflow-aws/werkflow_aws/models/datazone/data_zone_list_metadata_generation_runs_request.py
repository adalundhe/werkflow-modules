from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListMetadataGenerationRunsRequest(BaseModel):
    domainIdentifier: StrictStr
    status: Literal['SUBMITTED', 'IN_PROGRESS', 'CANCELED', 'SUCCEEDED', 'FAILED', 'PARTIALLY_SUCCEEDED'] | None = None
    type: Literal['BUSINESS_DESCRIPTIONS', 'BUSINESS_NAMES', 'BUSINESS_GLOSSARY_ASSOCIATIONS'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    targetIdentifier: StrictStr | None = None
