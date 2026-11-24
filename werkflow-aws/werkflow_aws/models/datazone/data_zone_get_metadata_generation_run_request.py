from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneGetMetadataGenerationRunRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    type: Literal['BUSINESS_DESCRIPTIONS', 'BUSINESS_NAMES', 'BUSINESS_GLOSSARY_ASSOCIATIONS'] | None = None
