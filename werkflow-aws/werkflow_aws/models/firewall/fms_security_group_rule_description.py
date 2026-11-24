from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FMSSecurityGroupRuleDescription(BaseModel):
    IPV4Range: StrictStr | None = None
    IPV6Range: StrictStr | None = None
    PrefixListId: StrictStr | None = None
    Protocol: StrictStr | None = None
    FromPort: StrictInt | None = None
    ToPort: StrictInt | None = None
