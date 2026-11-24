from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServicePutResourceConfigRequest(BaseModel):
    ResourceType: StrictStr
    SchemaVersionId: StrictStr
    ResourceId: StrictStr
    Configuration: StrictStr
    ResourceName: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
