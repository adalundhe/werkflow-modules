from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_via import NetworkManagerVia
from .network_manager_when_sent_to import NetworkManagerWhenSentTo


class NetworkManagerServiceInsertionAction(BaseModel):
    Action: StrictStr | None = None
    Mode: StrictStr | None = None
    WhenSentTo: NetworkManagerWhenSentTo | None = None
    Via: NetworkManagerVia | None = None
