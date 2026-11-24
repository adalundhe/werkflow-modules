from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_metadata_generation_run_target import DataZoneMetadataGenerationRunTarget


class DataZoneStartMetadataGenerationRunRequest(BaseModel):
    domainIdentifier: StrictStr
    target: DataZoneMetadataGenerationRunTarget
    owningProjectIdentifier: StrictStr
    type: Literal['BUSINESS_DESCRIPTIONS', 'BUSINESS_NAMES', 'BUSINESS_GLOSSARY_ASSOCIATIONS'] | None = None
    types: list[Literal['BUSINESS_DESCRIPTIONS', 'BUSINESS_NAMES', 'BUSINESS_GLOSSARY_ASSOCIATIONS']] | None = None
    clientToken: StrictStr | None = None
