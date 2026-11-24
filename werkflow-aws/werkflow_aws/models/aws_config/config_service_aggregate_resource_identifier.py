from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceAggregateResourceIdentifier(BaseModel):
    SourceAccountId: StrictStr | None = None
    SourceRegion: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceName: StrictStr | None = None
