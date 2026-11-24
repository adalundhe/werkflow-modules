from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_plugin_type_metadata_summary import QBusinessPluginTypeMetadataSummary


class QBusinessListPluginTypeMetadataResponse(BaseModel):
    nextToken: StrictStr | None = None
    items: list[QBusinessPluginTypeMetadataSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
