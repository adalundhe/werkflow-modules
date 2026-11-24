from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_agent_config import ConnectAgentConfig
from .connect_sign_in_config import ConnectSignInConfig
from .connect_telephony_config import ConnectTelephonyConfig


class ConnectGetTrafficDistributionResponse(BaseModel):
    TelephonyConfig: ConnectTelephonyConfig | None = None
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    SignInConfig: ConnectSignInConfig | None = None
    AgentConfig: ConnectAgentConfig | None = None
    LastFailoverTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
