from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class SecurityHubParameterValue(BaseModel):
    Integer: StrictInt | None = None
    IntegerList: list[StrictInt] | None = None
    Double: StrictFloat | StrictInt | None = None
    String: StrictStr | None = None
    StringList: list[StrictStr] | None = None
    Boolean: StrictBool | None = None
    Enum: StrictStr | None = None
    EnumList: list[StrictStr] | None = None
