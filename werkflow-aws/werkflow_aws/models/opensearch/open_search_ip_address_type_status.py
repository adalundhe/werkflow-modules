from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchIPAddressTypeStatus(BaseModel):
    Options: StrictStr | None = None
    Status: OpenSearchOptionStatus | None = None
