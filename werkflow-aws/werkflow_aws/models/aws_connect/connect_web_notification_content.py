from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_content_attributes import ConnectContentAttributes


class ConnectWebNotificationContent(BaseModel):
    Type: Literal['WIDGET_VIEW', 'WIDGET_ACTION']
    ViewArn: StrictStr | None = None
    Attributes: ConnectContentAttributes | None = None
