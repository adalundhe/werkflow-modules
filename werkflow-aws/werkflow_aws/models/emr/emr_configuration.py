from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRConfiguration(BaseModel):
    Classification: StrictStr | None = None
    Configurations: list[EMRConfiguration] | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
