from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .data_zone_attribute_error import DataZoneAttributeError
from .data_zone_batch_put_attribute_output import DataZoneBatchPutAttributeOutput


class DataZoneBatchPutAttributesMetadataResponse(BaseModel):
    errors: list[DataZoneAttributeError] | None = None
    attributes: list[DataZoneBatchPutAttributeOutput] | None = None
    ResponseMetadata: dict[str, Any] | None = None
