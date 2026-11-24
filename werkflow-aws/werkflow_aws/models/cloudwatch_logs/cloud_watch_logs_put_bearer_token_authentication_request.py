from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsPutBearerTokenAuthenticationRequest(BaseModel):
    logGroupIdentifier: StrictStr
    bearerTokenAuthenticationEnabled: StrictBool
