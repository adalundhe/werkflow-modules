from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_participant_details_to_add import ConnectParticipantDetailsToAdd


class ConnectCreateParticipantRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    ParticipantDetails: ConnectParticipantDetailsToAdd
    ClientToken: StrictStr | None = None
