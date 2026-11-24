from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESPutEmailIdentityConfigurationSetAttributesRequest(BaseModel):
    EmailIdentity: StrictStr
    ConfigurationSetName: StrictStr | None = None
