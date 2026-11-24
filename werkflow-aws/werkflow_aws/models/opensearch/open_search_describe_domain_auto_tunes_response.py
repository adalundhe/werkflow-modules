from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_auto_tune import OpenSearchAutoTune


class OpenSearchDescribeDomainAutoTunesResponse(BaseModel):
    AutoTunes: list[OpenSearchAutoTune] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
