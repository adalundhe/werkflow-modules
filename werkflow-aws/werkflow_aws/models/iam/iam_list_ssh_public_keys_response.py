from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iamssh_public_key_metadata import IAMSSHPublicKeyMetadata


class IAMListSSHPublicKeysResponse(BaseModel):
    SSHPublicKeys: list[IAMSSHPublicKeyMetadata] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
