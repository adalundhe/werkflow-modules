from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .open_search_data_source_type import OpenSearchDataSourceType


class OpenSearchUpdateDataSourceRequest(BaseModel):
    DomainName: StrictStr
    Name: StrictStr
    DataSourceType: OpenSearchDataSourceType
    Description: StrictStr | None = None
    Status: Literal['ACTIVE', 'DISABLED'] | None = None
