from __future__ import annotations
from pydantic import BaseModel
from .open_search_ebs_options import OpenSearchEBSOptions
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchEBSOptionsStatus(BaseModel):
    Options: OpenSearchEBSOptions | None = None
    Status: OpenSearchOptionStatus | None = None
