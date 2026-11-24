from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointTemplateCreateMessageBody(BaseModel):
    Arn: StrictStr | None = None
    Message: StrictStr | None = None
    RequestID: StrictStr | None = None
