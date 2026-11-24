from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_attribute_input import DataZoneAttributeInput


class DataZoneBatchPutAttributesMetadataRequest(BaseModel):
    domainIdentifier: StrictStr
    entityType: Literal['ASSET', 'LISTING']
    entityIdentifier: StrictStr
    attributes: list[DataZoneAttributeInput]
    clientToken: StrictStr | None = None
