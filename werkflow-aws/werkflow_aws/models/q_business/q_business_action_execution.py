from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_action_execution_payload_field import QBusinessActionExecutionPayloadField


class QBusinessActionExecution(BaseModel):
    pluginId: StrictStr | None = None
    payload: dict[StrictStr, QBusinessActionExecutionPayloadField] | None = None
    payloadFieldNameSeparator: StrictStr | None = None
