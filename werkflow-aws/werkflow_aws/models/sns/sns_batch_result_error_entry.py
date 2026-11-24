from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SNSBatchResultErrorEntry(BaseModel):
    Id: StrictStr | None = None
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    SenderFault: StrictBool | None = None
