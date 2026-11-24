from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SESListConfigurationSetsRequest(BaseModel):
    Filter: dict[Literal['CONFIGURATION_SET_NAME_CONTAINS'], StrictStr] | None = None
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
