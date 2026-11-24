from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSAvailableProcessorFeature(BaseModel):
    Name: StrictStr | None = None
    DefaultValue: StrictStr | None = None
    AllowedValues: StrictStr | None = None
