from __future__ import annotations
from pydantic import BaseModel
from .cloud_search_index_field import CloudSearchIndexField
from .cloud_search_option_status import CloudSearchOptionStatus


class CloudSearchIndexFieldStatus(BaseModel):
    Options: CloudSearchIndexField | None = None
    Status: CloudSearchOptionStatus | None = None
