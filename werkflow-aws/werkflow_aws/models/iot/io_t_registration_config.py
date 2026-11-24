from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTRegistrationConfig(BaseModel):
    templateBody: StrictStr | None = None
    roleArn: StrictStr | None = None
    templateName: StrictStr | None = None
