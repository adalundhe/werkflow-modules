from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_metadata_model_reference import DMSMetadataModelReference


class DMSDescribeMetadataModelResponse(BaseModel):
    MetadataModelName: StrictStr | None = None
    MetadataModelType: StrictStr | None = None
    TargetMetadataModels: list[DMSMetadataModelReference] | None = None
    Definition: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
