from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IAMOpenIDConnectProviderListEntry(BaseModel):
    Arn: StrictStr | None = None
    IsTrustedIdentityPropagationEnabled: StrictBool | None = None
