from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2SecurityGroupPrefixListId(BaseModel):
    PrefixListId: StrictStr | None = None
