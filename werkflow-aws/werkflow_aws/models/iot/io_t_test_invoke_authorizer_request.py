from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_http_context import IoTHttpContext
from .io_t_mqtt_context import IoTMqttContext
from .io_t_tls_context import IoTTlsContext


class IoTTestInvokeAuthorizerRequest(BaseModel):
    authorizerName: StrictStr
    token: StrictStr | None = None
    tokenSignature: StrictStr | None = None
    httpContext: IoTHttpContext | None = None
    mqttContext: IoTMqttContext | None = None
    tlsContext: IoTTlsContext | None = None
