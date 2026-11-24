from __future__ import annotations
from pydantic import BaseModel
from .cloud_search_option_status import CloudSearchOptionStatus
from .cloud_search_suggester import CloudSearchSuggester


class CloudSearchSuggesterStatus(BaseModel):
    Options: CloudSearchSuggester | None = None
    Status: CloudSearchOptionStatus | None = None
