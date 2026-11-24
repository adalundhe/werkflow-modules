from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iamssh_public_key import IAMSSHPublicKey


class IAMUploadSSHPublicKeyResponse(BaseModel):
    SSHPublicKey: IAMSSHPublicKey | None = None
    ResponseMetadata: dict[str, Any] | None = None
