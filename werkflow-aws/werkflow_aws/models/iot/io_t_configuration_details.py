from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTConfigurationDetails(BaseModel):
    configurationStatus: StrictStr | None = None
    errorCode: StrictStr | None = None
    errorMessage: StrictStr | None = None
