from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class PinpointAddressConfiguration(BaseModel):
    BodyOverride: StrictStr | None = None
    ChannelType: Literal['PUSH', 'GCM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'ADM', 'SMS', 'VOICE', 'EMAIL', 'BAIDU', 'CUSTOM', 'IN_APP'] | None = None
    Context: dict[StrictStr, StrictStr] | None = None
    RawContent: StrictStr | None = None
    Substitutions: dict[StrictStr, list[StrictStr]] | None = None
    TitleOverride: StrictStr | None = None
