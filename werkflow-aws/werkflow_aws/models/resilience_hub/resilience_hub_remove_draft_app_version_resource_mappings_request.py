from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubRemoveDraftAppVersionResourceMappingsRequest(BaseModel):
    appArn: StrictStr
    appRegistryAppNames: list[StrictStr] | None = None
    eksSourceNames: list[StrictStr] | None = None
    logicalStackNames: list[StrictStr] | None = None
    resourceGroupNames: list[StrictStr] | None = None
    resourceNames: list[StrictStr] | None = None
    terraformSourceNames: list[StrictStr] | None = None
