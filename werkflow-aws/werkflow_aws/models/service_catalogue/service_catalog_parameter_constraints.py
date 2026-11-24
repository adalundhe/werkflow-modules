from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogParameterConstraints(BaseModel):
    AllowedValues: list[StrictStr] | None = None
    AllowedPattern: StrictStr | None = None
    ConstraintDescription: StrictStr | None = None
    MaxLength: StrictStr | None = None
    MinLength: StrictStr | None = None
    MaxValue: StrictStr | None = None
    MinValue: StrictStr | None = None
