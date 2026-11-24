from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ssm_service_setting import SSMServiceSetting


class SSMGetServiceSettingResponse(BaseModel):
    ServiceSetting: SSMServiceSetting | None = None
    ResponseMetadata: dict[str, Any] | None = None
