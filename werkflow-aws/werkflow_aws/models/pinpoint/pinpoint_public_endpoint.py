from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .pinpoint_endpoint_demographic import PinpointEndpointDemographic
from .pinpoint_endpoint_location import PinpointEndpointLocation
from .pinpoint_endpoint_user import PinpointEndpointUser


class PinpointPublicEndpoint(BaseModel):
    Address: StrictStr | None = None
    Attributes: dict[StrictStr, list[StrictStr]] | None = None
    ChannelType: Literal['PUSH', 'GCM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'ADM', 'SMS', 'VOICE', 'EMAIL', 'BAIDU', 'CUSTOM', 'IN_APP'] | None = None
    Demographic: PinpointEndpointDemographic | None = None
    EffectiveDate: StrictStr | None = None
    EndpointStatus: StrictStr | None = None
    Location: PinpointEndpointLocation | None = None
    Metrics: dict[StrictStr, StrictFloat | StrictInt] | None = None
    OptOut: StrictStr | None = None
    RequestId: StrictStr | None = None
    User: PinpointEndpointUser | None = None
