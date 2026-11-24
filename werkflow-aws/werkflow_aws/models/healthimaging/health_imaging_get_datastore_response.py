from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .health_imaging_datastore_properties import HealthImagingDatastoreProperties


class HealthImagingGetDatastoreResponse(BaseModel):
    datastoreProperties: HealthImagingDatastoreProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
