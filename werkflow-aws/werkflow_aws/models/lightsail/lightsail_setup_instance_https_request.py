from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LightsailSetupInstanceHttpsRequest(BaseModel):
    instanceName: StrictStr
    emailAddress: StrictStr
    domainNames: list[StrictStr]
    certificateProvider: Literal['LetsEncrypt']
