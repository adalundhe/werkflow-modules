from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class LambdaSendDurableExecutionCallbackSuccessRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    CallbackId: StrictStr
    Result: StrictBytes | BinaryIO | StrictStr | None = None
