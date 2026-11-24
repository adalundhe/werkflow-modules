from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_asset_scope import DataZoneAssetScope
from .data_zone_detailed_glossary_term import DataZoneDetailedGlossaryTerm
from .data_zone_permissions import DataZonePermissions


class DataZoneSubscribedAssetListing(BaseModel):
    entityId: StrictStr | None = None
    entityRevision: StrictStr | None = None
    entityType: StrictStr | None = None
    forms: StrictStr | None = None
    glossaryTerms: list[DataZoneDetailedGlossaryTerm] | None = None
    assetScope: DataZoneAssetScope | None = None
    permissions: DataZonePermissions | None = None
