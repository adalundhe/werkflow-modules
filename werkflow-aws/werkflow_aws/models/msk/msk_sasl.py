from __future__ import annotations
from pydantic import BaseModel
from .msk_iam import MSKIam
from .msk_scram import MSKScram


class MSKSasl(BaseModel):
    Scram: MSKScram | None = None
    Iam: MSKIam | None = None
