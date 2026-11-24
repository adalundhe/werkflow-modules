from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_actor_session import SecurityHubActorSession
from .security_hub_actor_user import SecurityHubActorUser


class SecurityHubActor(BaseModel):
    Id: StrictStr | None = None
    User: SecurityHubActorUser | None = None
    Session: SecurityHubActorSession | None = None
