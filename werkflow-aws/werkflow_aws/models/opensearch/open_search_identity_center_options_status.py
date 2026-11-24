from __future__ import annotations
from pydantic import BaseModel
from .open_search_identity_center_options import OpenSearchIdentityCenterOptions
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchIdentityCenterOptionsStatus(BaseModel):
    Options: OpenSearchIdentityCenterOptions | None = None
    Status: OpenSearchOptionStatus | None = None
