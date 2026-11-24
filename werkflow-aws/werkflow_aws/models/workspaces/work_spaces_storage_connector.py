from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesStorageConnector(BaseModel):
    ConnectorType: StrictStr | None = None
    Status: StrictStr | None = None
