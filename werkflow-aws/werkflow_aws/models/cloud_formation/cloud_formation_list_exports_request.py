from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationListExportsRequest(BaseModel):
    NextToken: StrictStr | None = None
