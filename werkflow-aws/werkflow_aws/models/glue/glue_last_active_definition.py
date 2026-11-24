from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueLastActiveDefinition(BaseModel):
    Description: StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    ParameterSpec: StrictStr | None = None
    BlueprintLocation: StrictStr | None = None
    BlueprintServiceLocation: StrictStr | None = None
