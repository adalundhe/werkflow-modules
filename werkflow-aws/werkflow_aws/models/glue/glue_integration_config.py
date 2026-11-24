from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueIntegrationConfig(BaseModel):
    RefreshInterval: StrictStr | None = None
    SourceProperties: dict[StrictStr, StrictStr] | None = None
    ContinuousSync: StrictBool | None = None
    TargetNamespace: StrictStr | None = None
