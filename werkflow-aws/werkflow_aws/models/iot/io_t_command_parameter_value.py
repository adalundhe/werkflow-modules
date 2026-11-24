from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictFloat, StrictInt, StrictStr


class IoTCommandParameterValue(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    S: StrictStr | None = None
    B: StrictBool | None = None
    I: StrictInt | None = None
    L: StrictInt | None = None
    D: StrictFloat | StrictInt | None = None
    BIN: StrictBytes | Any | None = None
    UL: StrictStr | None = None
