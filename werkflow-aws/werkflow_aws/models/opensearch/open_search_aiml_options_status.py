from __future__ import annotations
from pydantic import BaseModel
from .open_search_aiml_options_output import OpenSearchAIMLOptionsOutput
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchAIMLOptionsStatus(BaseModel):
    Options: OpenSearchAIMLOptionsOutput | None = None
    Status: OpenSearchOptionStatus | None = None
