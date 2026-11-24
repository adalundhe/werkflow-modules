from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceRemediationException(BaseModel):
    ConfigRuleName: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    Message: StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
