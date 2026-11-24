from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCapabilities(BaseModel):
    SupportedAuthenticationTypes: list[StrictStr] | None = None
    SupportedDataOperations: list[StrictStr] | None = None
    SupportedComputeEnvironments: list[StrictStr] | None = None
