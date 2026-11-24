from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class IAMSAMLProviderListEntry(BaseModel):
    Arn: StrictStr | None = None
    ValidUntil: datetime.datetime | StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    IsTrustedIdentityPropagationEnabled: StrictBool | None = None
