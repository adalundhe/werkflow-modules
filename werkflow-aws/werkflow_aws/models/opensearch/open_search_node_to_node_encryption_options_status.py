from __future__ import annotations
from pydantic import BaseModel
from .open_search_node_to_node_encryption_options import OpenSearchNodeToNodeEncryptionOptions
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchNodeToNodeEncryptionOptionsStatus(BaseModel):
    Options: OpenSearchNodeToNodeEncryptionOptions | None = None
    Status: OpenSearchOptionStatus | None = None
