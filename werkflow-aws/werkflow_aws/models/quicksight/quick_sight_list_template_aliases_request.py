from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListTemplateAliasesRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
