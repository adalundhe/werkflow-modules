from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubListOrganizationAdminAccountsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Feature: Literal['SecurityHub', 'SecurityHubV2'] | None = None
