from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateOTAUpdateResponse(BaseModel):
    otaUpdateId: StrictStr | None = None
    awsIotJobId: StrictStr | None = None
    otaUpdateArn: StrictStr | None = None
    awsIotJobArn: StrictStr | None = None
    otaUpdateStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
