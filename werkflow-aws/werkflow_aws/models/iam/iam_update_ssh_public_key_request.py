from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IAMUpdateSSHPublicKeyRequest(BaseModel):
    UserName: StrictStr
    SSHPublicKeyId: StrictStr
    Status: Literal['Active', 'Inactive', 'Expired']
