from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationListImportsRequest(BaseModel):
    ExportName: StrictStr
    NextToken: StrictStr | None = None
