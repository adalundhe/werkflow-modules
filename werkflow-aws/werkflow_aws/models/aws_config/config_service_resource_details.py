from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceResourceDetails(BaseModel):
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceConfiguration: StrictStr | None = None
    ResourceConfigurationSchemaType: StrictStr | None = None
