from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectUpdateInstanceAttributeRequest(BaseModel):
    InstanceId: StrictStr
    AttributeType: Literal['INBOUND_CALLS', 'OUTBOUND_CALLS', 'CONTACTFLOW_LOGS', 'CONTACT_LENS', 'AUTO_RESOLVE_BEST_VOICES', 'USE_CUSTOM_TTS_VOICES', 'EARLY_MEDIA', 'MULTI_PARTY_CONFERENCE', 'AUTO_MUTE_AGENT_ON_HOLD', 'HIGH_VOLUME_OUTBOUND', 'ENHANCED_CONTACT_MONITORING', 'ENHANCED_CHAT_MONITORING', 'MULTI_PARTY_CHAT_CONFERENCE', 'MESSAGE_STREAMING']
    Value: StrictStr
    ClientToken: StrictStr | None = None
