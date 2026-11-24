from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDataSource(BaseModel):
    dataSourceArn: StrictStr | None = None
    dataSourceDescription: StrictStr | None = None
    iamRoleForDataSourceArn: StrictStr | None = None
