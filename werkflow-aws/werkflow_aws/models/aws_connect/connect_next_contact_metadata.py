from __future__ import annotations
from pydantic import BaseModel
from .connect_quick_connect_contact_data import ConnectQuickConnectContactData


class ConnectNextContactMetadata(BaseModel):
    QuickConnectContactData: ConnectQuickConnectContactData | None = None
