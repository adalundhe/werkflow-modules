from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogExecutionParameter(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    DefaultValues: list[StrictStr] | None = None
