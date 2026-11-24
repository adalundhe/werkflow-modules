from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class SESDkimAttributes(BaseModel):
    SigningEnabled: StrictBool | None = None
    Status: StrictStr | None = None
    Tokens: list[StrictStr] | None = None
    SigningHostedZone: StrictStr | None = None
    SigningAttributesOrigin: StrictStr | None = None
    NextSigningKeyLength: StrictStr | None = None
    CurrentSigningKeyLength: StrictStr | None = None
    LastKeyGenerationTimestamp: datetime.datetime | StrictStr | None = None
