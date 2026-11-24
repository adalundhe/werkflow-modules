from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubDescribeStandardsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Providers: list[Literal['AWS', 'Azure', 'GCP']] | None = None
