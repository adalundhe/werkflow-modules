from __future__ import annotations
from pydantic import BaseModel
from .msk_iam import MSKIam


class MSKServerlessSasl(BaseModel):
    Iam: MSKIam | None = None
