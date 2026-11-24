from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTVersionUpdateByJobsConfig(BaseModel):
    enabled: StrictBool | None = None
    roleArn: StrictStr | None = None
