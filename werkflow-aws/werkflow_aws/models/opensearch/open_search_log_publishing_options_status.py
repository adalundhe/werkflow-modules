from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_log_publishing_option import OpenSearchLogPublishingOption
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchLogPublishingOptionsStatus(BaseModel):
    Options: dict[StrictStr, OpenSearchLogPublishingOption] | None = None
    Status: OpenSearchOptionStatus | None = None
