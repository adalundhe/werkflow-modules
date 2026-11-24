from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_search_index_field import CloudSearchIndexField


class CloudSearchDefineIndexFieldRequest(BaseModel):
    DomainName: StrictStr
    IndexField: CloudSearchIndexField
