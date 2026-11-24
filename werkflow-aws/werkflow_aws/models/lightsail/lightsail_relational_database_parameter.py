from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailRelationalDatabaseParameter(BaseModel):
    allowedValues: StrictStr | None = None
    applyMethod: StrictStr | None = None
    applyType: StrictStr | None = None
    dataType: StrictStr | None = None
    description: StrictStr | None = None
    isModifiable: StrictBool | None = None
    parameterName: StrictStr | None = None
    parameterValue: StrictStr | None = None
