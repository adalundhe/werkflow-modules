from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CancelConversionTaskRequest(BaseModel):
    ConversionTaskId: StrictStr
    DryRun: StrictBool | None = None
    ReasonMessage: StrictStr | None = None
