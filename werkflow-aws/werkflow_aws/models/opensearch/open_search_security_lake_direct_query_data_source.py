from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchSecurityLakeDirectQueryDataSource(BaseModel):
    RoleArn: StrictStr | None = None
