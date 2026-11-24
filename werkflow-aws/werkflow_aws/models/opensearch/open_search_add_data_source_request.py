from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_data_source_type import OpenSearchDataSourceType


class OpenSearchAddDataSourceRequest(BaseModel):
    DomainName: StrictStr
    Name: StrictStr
    DataSourceType: OpenSearchDataSourceType
    Description: StrictStr | None = None
