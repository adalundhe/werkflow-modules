from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSParameter(BaseModel):
    ParameterName: StrictStr | None = None
    ParameterValue: StrictStr | None = None
    Description: StrictStr | None = None
    Source: StrictStr | None = None
    ApplyType: StrictStr | None = None
    DataType: StrictStr | None = None
    AllowedValues: StrictStr | None = None
    IsModifiable: StrictBool | None = None
    MinimumEngineVersion: StrictStr | None = None
    ApplyMethod: StrictStr | None = None
    SupportedEngineModes: list[StrictStr] | None = None
