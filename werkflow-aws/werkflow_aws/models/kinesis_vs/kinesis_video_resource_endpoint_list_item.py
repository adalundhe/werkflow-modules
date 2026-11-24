from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoResourceEndpointListItem(BaseModel):
    Protocol: StrictStr | None = None
    ResourceEndpoint: StrictStr | None = None
