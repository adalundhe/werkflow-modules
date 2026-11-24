from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteServiceLinkedConfigurationRecorderRequest(BaseModel):
    ServicePrincipal: StrictStr | None = None
    Arn: StrictStr | None = None
