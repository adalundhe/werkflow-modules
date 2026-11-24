from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_after_contact_work_config import ConnectAfterContactWorkConfig


class ConnectAfterContactWorkConfigPerChannel(BaseModel):
    Channel: StrictStr | None = None
    AfterContactWorkConfig: ConnectAfterContactWorkConfig | None = None
    AgentFirstCallbackAfterContactWorkConfig: ConnectAfterContactWorkConfig | None = None
