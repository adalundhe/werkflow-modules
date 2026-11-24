from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMDeleteAcmeExternalAccountBindingRequest(BaseModel):
    AcmeExternalAccountBindingArn: StrictStr
