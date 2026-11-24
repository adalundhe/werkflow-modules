from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DescribePrincipalIdFormatRequest(BaseModel):
    DryRun: StrictBool | None = None
    Resources: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
