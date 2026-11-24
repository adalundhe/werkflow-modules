from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_asset_item_additional_attributes import DataZoneAssetItemAdditionalAttributes


class DataZoneAssetItem(BaseModel):
    domainId: StrictStr | None = None
    identifier: StrictStr | None = None
    name: StrictStr | None = None
    typeIdentifier: StrictStr | None = None
    typeRevision: StrictStr | None = None
    externalIdentifier: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    firstRevisionCreatedAt: datetime.datetime | StrictStr | None = None
    firstRevisionCreatedBy: StrictStr | None = None
    glossaryTerms: list[StrictStr] | None = None
    owningProjectId: StrictStr | None = None
    additionalAttributes: DataZoneAssetItemAdditionalAttributes | None = None
    governedGlossaryTerms: list[StrictStr] | None = None
