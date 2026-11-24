from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_tag import AppRunnerTag


class AppRunnerCreateVpcConnectorRequest(BaseModel):
    VpcConnectorName: StrictStr
    Subnets: list[StrictStr]
    SecurityGroups: list[StrictStr] | None = None
    Tags: list[AppRunnerTag] | None = None
