from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_batch_config import IoTBatchConfig
from .io_t_http_action_header import IoTHttpActionHeader
from .io_t_http_authorization import IoTHttpAuthorization


class IoTHttpAction(BaseModel):
    url: StrictStr | None = None
    confirmationUrl: StrictStr | None = None
    headers: list[IoTHttpActionHeader] | None = None
    auth: IoTHttpAuthorization | None = None
    enableBatching: StrictBool | None = None
    batchConfig: IoTBatchConfig | None = None
