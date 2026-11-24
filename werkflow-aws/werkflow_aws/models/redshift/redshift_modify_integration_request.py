from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftModifyIntegrationRequest(BaseModel):
    IntegrationArn: StrictStr
    Description: StrictStr | None = None
    IntegrationName: StrictStr | None = None
