from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogDescribeRecordRequest(BaseModel):
    Id: StrictStr
    AcceptLanguage: StrictStr | None = None
    PageToken: StrictStr | None = None
    PageSize: StrictInt | None = None
