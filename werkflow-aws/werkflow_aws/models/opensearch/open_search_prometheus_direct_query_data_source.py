from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchPrometheusDirectQueryDataSource(BaseModel):
    RoleArn: StrictStr | None = None
    WorkspaceArn: StrictStr | None = None
