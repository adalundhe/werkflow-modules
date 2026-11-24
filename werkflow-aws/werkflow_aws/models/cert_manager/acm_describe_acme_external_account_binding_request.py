from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMDescribeAcmeExternalAccountBindingRequest(BaseModel):
    AcmeExternalAccountBindingArn: StrictStr
