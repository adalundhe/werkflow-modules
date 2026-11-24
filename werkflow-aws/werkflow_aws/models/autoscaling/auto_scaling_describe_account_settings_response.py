from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_account_setting import AutoScalingAccountSetting


class AutoScalingDescribeAccountSettingsResponse(BaseModel):
    Settings: list[AutoScalingAccountSetting] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
