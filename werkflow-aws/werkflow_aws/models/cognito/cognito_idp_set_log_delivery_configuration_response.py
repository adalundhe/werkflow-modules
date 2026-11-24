from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_log_delivery_configuration_type import CognitoIDPLogDeliveryConfigurationType


class CognitoIDPSetLogDeliveryConfigurationResponse(BaseModel):
    LogDeliveryConfiguration: CognitoIDPLogDeliveryConfigurationType | None = None
    ResponseMetadata: dict[str, Any] | None = None
