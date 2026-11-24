from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .data_zone_attribute_error import DataZoneAttributeError
from .data_zone_batch_get_attribute_output import DataZoneBatchGetAttributeOutput


class DataZoneBatchGetAttributesMetadataResponse(BaseModel):
    attributes: list[DataZoneBatchGetAttributeOutput] | None = None
    errors: list[DataZoneAttributeError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
