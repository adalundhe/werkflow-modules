from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoMappedResourceConfigurationListItem(BaseModel):
    Type: StrictStr | None = None
    ARN: StrictStr | None = None
