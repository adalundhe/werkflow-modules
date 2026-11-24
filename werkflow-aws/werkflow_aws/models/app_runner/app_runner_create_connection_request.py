from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_runner_tag import AppRunnerTag


class AppRunnerCreateConnectionRequest(BaseModel):
    ConnectionName: StrictStr
    ProviderType: Literal['GITHUB', 'BITBUCKET']
    Tags: list[AppRunnerTag] | None = None
