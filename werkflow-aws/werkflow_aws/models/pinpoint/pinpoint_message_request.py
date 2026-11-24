from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_address_configuration import PinpointAddressConfiguration
from .pinpoint_direct_message_configuration import PinpointDirectMessageConfiguration
from .pinpoint_endpoint_send_configuration import PinpointEndpointSendConfiguration
from .pinpoint_template_configuration import PinpointTemplateConfiguration


class PinpointMessageRequest(BaseModel):
    MessageConfiguration: PinpointDirectMessageConfiguration
    Addresses: dict[StrictStr, PinpointAddressConfiguration] | None = None
    Context: dict[StrictStr, StrictStr] | None = None
    Endpoints: dict[StrictStr, PinpointEndpointSendConfiguration] | None = None
    TemplateConfiguration: PinpointTemplateConfiguration | None = None
    TraceId: StrictStr | None = None
