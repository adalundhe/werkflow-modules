from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPCompromisedCredentialsActionsType(BaseModel):
    EventAction: StrictStr | None = None
