from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchSAMLIdp(BaseModel):
    MetadataContent: StrictStr | None = None
    EntityId: StrictStr | None = None
