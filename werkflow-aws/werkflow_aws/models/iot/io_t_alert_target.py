from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAlertTarget(BaseModel):
    alertTargetArn: StrictStr | None = None
    roleArn: StrictStr | None = None
