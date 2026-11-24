from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class IoTCommandExecutionResult(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    S: StrictStr | None = None
    B: StrictBool | None = None
    BIN: StrictBytes | Any | None = None
