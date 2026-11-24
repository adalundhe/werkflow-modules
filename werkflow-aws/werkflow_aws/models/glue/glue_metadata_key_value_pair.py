from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueMetadataKeyValuePair(BaseModel):
    MetadataKey: StrictStr | None = None
    MetadataValue: StrictStr | None = None
