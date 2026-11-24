from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_view_input_content import ConnectViewInputContent


class ConnectCreateViewRequest(BaseModel):
    InstanceId: StrictStr
    Status: Literal['PUBLISHED', 'SAVED']
    Content: ConnectViewInputContent
    Name: StrictStr
    ClientToken: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
