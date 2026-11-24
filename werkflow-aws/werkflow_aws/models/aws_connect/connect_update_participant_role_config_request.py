from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_update_participant_role_config_channel_info import ConnectUpdateParticipantRoleConfigChannelInfo


class ConnectUpdateParticipantRoleConfigRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    ChannelConfiguration: ConnectUpdateParticipantRoleConfigChannelInfo
