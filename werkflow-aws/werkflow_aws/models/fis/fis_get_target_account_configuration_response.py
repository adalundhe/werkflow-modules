from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .fis_target_account_configuration import FISTargetAccountConfiguration


class FISGetTargetAccountConfigurationResponse(BaseModel):
    targetAccountConfiguration: FISTargetAccountConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
