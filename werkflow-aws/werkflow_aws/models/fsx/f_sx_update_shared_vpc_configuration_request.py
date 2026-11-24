from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxUpdateSharedVpcConfigurationRequest(BaseModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
