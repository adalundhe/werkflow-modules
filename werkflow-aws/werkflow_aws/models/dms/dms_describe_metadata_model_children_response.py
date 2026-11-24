from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_metadata_model_reference import DMSMetadataModelReference


class DMSDescribeMetadataModelChildrenResponse(BaseModel):
    Marker: StrictStr | None = None
    MetadataModelChildren: list[DMSMetadataModelReference] | None = None
    ResponseMetadata: dict[str, Any] | None = None
