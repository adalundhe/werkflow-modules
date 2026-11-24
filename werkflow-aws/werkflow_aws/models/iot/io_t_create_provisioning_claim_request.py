from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTCreateProvisioningClaimRequest(BaseModel):
    templateName: StrictStr
