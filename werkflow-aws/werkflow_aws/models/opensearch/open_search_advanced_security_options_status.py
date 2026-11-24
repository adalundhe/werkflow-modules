from __future__ import annotations
from pydantic import BaseModel
from .open_search_advanced_security_options import OpenSearchAdvancedSecurityOptions
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchAdvancedSecurityOptionsStatus(BaseModel):
    Options: OpenSearchAdvancedSecurityOptions | None = None
    Status: OpenSearchOptionStatus | None = None
