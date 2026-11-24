from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .wa_fv2_tag import WAFv2Tag


class WAFv2CreateIPSetRequest(BaseModel):
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    IPAddressVersion: Literal['IPV4', 'IPV6']
    Addresses: list[StrictStr]
    Description: StrictStr | None = None
    Tags: list[WAFv2Tag] | None = None
