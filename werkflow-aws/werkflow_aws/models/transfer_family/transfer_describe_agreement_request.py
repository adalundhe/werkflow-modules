from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeAgreementRequest(BaseModel):
    AgreementId: StrictStr
    ServerId: StrictStr
