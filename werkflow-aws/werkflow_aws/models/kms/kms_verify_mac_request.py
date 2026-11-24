from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class KMSVerifyMacRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Message: StrictBytes | BinaryIO | StrictStr
    KeyId: StrictStr
    MacAlgorithm: Literal['HMAC_SHA_224', 'HMAC_SHA_256', 'HMAC_SHA_384', 'HMAC_SHA_512']
    Mac: StrictBytes | BinaryIO | StrictStr
    GrantTokens: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
