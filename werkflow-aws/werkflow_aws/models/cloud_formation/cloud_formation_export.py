from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationExport(BaseModel):
    ExportingStackId: StrictStr | None = None
    Name: StrictStr | None = None
    Value: StrictStr | None = None
