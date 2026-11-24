from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_waf_acfp_config import LightsailWafAcfpConfig
from .lightsail_waf_atp_config import LightsailWafAtpConfig
from .lightsail_waf_bot_control_config import LightsailWafBotControlConfig


class LightsailWafRule(BaseModel):
    name: StrictStr | None = None
    atpConfig: LightsailWafAtpConfig | None = None
    acfpConfig: LightsailWafAcfpConfig | None = None
    botControlConfig: LightsailWafBotControlConfig | None = None
