from __future__ import annotations
from pydantic import BaseModel
from .open_search_option_status import OpenSearchOptionStatus
from .open_search_software_update_options import OpenSearchSoftwareUpdateOptions


class OpenSearchSoftwareUpdateOptionsStatus(BaseModel):
    Options: OpenSearchSoftwareUpdateOptions | None = None
    Status: OpenSearchOptionStatus | None = None
