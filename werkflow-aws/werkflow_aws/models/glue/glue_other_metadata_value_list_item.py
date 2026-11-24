from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueOtherMetadataValueListItem(BaseModel):
    MetadataValue: StrictStr | None = None
    CreatedTime: StrictStr | None = None
