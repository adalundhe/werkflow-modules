from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_direct_message_configuration import PinpointDirectMessageConfiguration
from .pinpoint_endpoint_send_configuration import PinpointEndpointSendConfiguration
from .pinpoint_template_configuration import PinpointTemplateConfiguration


class PinpointSendUsersMessageRequest(BaseModel):
    MessageConfiguration: PinpointDirectMessageConfiguration
    Users: dict[StrictStr, PinpointEndpointSendConfiguration]
    Context: dict[StrictStr, StrictStr] | None = None
    TemplateConfiguration: PinpointTemplateConfiguration | None = None
    TraceId: StrictStr | None = None
