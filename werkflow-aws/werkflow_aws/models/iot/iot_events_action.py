from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IotEventsAction(BaseModel):
    inputName: StrictStr | None = None
    messageId: StrictStr | None = None
    batchMode: StrictBool | None = None
    roleArn: StrictStr | None = None
