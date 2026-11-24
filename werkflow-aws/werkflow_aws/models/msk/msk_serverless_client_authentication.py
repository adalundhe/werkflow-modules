from __future__ import annotations
from pydantic import BaseModel
from .msk_serverless_sasl import MSKServerlessSasl


class MSKServerlessClientAuthentication(BaseModel):
    Sasl: MSKServerlessSasl | None = None
