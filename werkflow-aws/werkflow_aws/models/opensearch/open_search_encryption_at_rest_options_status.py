from __future__ import annotations
from pydantic import BaseModel
from .open_search_encryption_at_rest_options import OpenSearchEncryptionAtRestOptions
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchEncryptionAtRestOptionsStatus(BaseModel):
    Options: OpenSearchEncryptionAtRestOptions | None = None
    Status: OpenSearchOptionStatus | None = None
