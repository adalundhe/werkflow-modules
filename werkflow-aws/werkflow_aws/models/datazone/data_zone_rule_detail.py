from __future__ import annotations
from pydantic import BaseModel
from .data_zone_glossary_term_enforcement_detail import DataZoneGlossaryTermEnforcementDetail
from .data_zone_metadata_form_enforcement_detail import DataZoneMetadataFormEnforcementDetail


class DataZoneRuleDetail(BaseModel):
    metadataFormEnforcementDetail: DataZoneMetadataFormEnforcementDetail | None = None
    glossaryTermEnforcementDetail: DataZoneGlossaryTermEnforcementDetail | None = None
