from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchMigrationWorkspace(BaseModel):
    workspaceId: StrictStr | None = None
    createWorkspace: StrictBool | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
