from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_agent_config import ConnectAgentConfig
from .connect_sign_in_config import ConnectSignInConfig
from .connect_telephony_config import ConnectTelephonyConfig


class ConnectUpdateTrafficDistributionRequest(BaseModel):
    Id: StrictStr
    TelephonyConfig: ConnectTelephonyConfig | None = None
    SignInConfig: ConnectSignInConfig | None = None
    AgentConfig: ConnectAgentConfig | None = None
