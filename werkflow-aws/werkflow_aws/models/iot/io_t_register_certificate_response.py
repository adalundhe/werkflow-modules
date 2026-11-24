from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTRegisterCertificateResponse(BaseModel):
    certificateArn: StrictStr | None = None
    certificateId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
