from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeCustomWorkspaceImageImportRequest(BaseModel):
    ImageId: StrictStr
