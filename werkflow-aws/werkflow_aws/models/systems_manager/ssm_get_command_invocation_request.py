from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetCommandInvocationRequest(BaseModel):
    CommandId: StrictStr
    InstanceId: StrictStr
    PluginName: StrictStr | None = None
