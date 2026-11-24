from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationOutput(BaseModel):
    OutputKey: StrictStr | None = None
    OutputValue: StrictStr | None = None
    Description: StrictStr | None = None
    ExportName: StrictStr | None = None
