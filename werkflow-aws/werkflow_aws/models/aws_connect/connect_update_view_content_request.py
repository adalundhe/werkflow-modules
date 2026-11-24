from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_view_input_content import ConnectViewInputContent


class ConnectUpdateViewContentRequest(BaseModel):
    InstanceId: StrictStr
    ViewId: StrictStr
    Status: Literal['PUBLISHED', 'SAVED']
    Content: ConnectViewInputContent
