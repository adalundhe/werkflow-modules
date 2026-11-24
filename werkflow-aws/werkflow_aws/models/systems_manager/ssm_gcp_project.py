from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGcpProject(BaseModel):
    ProjectId: StrictStr | None = None
    ProjectDisplayName: StrictStr | None = None
