from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_node_config import OpenSearchNodeConfig


class OpenSearchNodeOption(BaseModel):
    NodeType: StrictStr | None = None
    NodeConfig: OpenSearchNodeConfig | None = None
