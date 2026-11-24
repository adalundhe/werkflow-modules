from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_action_execution_payload_field import QBusinessActionExecutionPayloadField


class QBusinessActionExecutionEvent(BaseModel):
    pluginId: StrictStr
    payload: dict[StrictStr, QBusinessActionExecutionPayloadField]
    payloadFieldNameSeparator: StrictStr
