from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingTestingAgentInformation(BaseModel):
    Status: StrictStr | None = None
    TestingAgentId: StrictStr | None = None
    RegistrationId: StrictStr | None = None
