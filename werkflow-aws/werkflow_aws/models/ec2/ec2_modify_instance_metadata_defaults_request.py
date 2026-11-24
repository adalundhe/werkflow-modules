from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt


class EC2ModifyInstanceMetadataDefaultsRequest(BaseModel):
    HttpTokens: Literal['optional', 'required', 'no-preference'] | None = None
    HttpPutResponseHopLimit: StrictInt | None = None
    HttpEndpoint: Literal['disabled', 'enabled', 'no-preference'] | None = None
    InstanceMetadataTags: Literal['disabled', 'enabled', 'no-preference'] | None = None
    DryRun: StrictBool | None = None
    HttpTokensEnforced: Literal['disabled', 'enabled', 'no-preference'] | None = None
