from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyTrafficMirrorFilterNetworkServicesRequest(BaseModel):
    TrafficMirrorFilterId: StrictStr
    AddNetworkServices: list[Literal['amazon-dns']] | None = None
    RemoveNetworkServices: list[Literal['amazon-dns']] | None = None
    DryRun: StrictBool | None = None
