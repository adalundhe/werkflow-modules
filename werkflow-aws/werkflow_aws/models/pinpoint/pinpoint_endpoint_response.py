from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .pinpoint_endpoint_demographic import PinpointEndpointDemographic
from .pinpoint_endpoint_location import PinpointEndpointLocation
from .pinpoint_endpoint_user import PinpointEndpointUser


class PinpointEndpointResponse(BaseModel):
    Address: StrictStr | None = None
    ApplicationId: StrictStr | None = None
    Attributes: dict[StrictStr, list[StrictStr]] | None = None
    ChannelType: StrictStr | None = None
    CohortId: StrictStr | None = None
    CreationDate: StrictStr | None = None
    Demographic: PinpointEndpointDemographic | None = None
    EffectiveDate: StrictStr | None = None
    EndpointStatus: StrictStr | None = None
    Id: StrictStr | None = None
    Location: PinpointEndpointLocation | None = None
    Metrics: dict[StrictStr, StrictFloat | StrictInt] | None = None
    OptOut: StrictStr | None = None
    RequestId: StrictStr | None = None
    User: PinpointEndpointUser | None = None
