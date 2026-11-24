from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTSnsAction(BaseModel):
    targetArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    messageFormat: StrictStr | None = None
