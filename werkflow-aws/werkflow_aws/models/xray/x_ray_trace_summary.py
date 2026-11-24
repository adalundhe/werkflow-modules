from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .x_ray_availability_zone_detail import XRayAvailabilityZoneDetail
from .x_ray_error_root_cause import XRayErrorRootCause
from .x_ray_fault_root_cause import XRayFaultRootCause
from .x_ray_http import XRayHttp
from .x_ray_instance_id_detail import XRayInstanceIdDetail
from .x_ray_resource_arn_detail import XRayResourceARNDetail
from .x_ray_response_time_root_cause import XRayResponseTimeRootCause
from .x_ray_service_id import XRayServiceId
from .x_ray_trace_user import XRayTraceUser
from .x_ray_value_with_service_ids import XRayValueWithServiceIds


class XRayTraceSummary(BaseModel):
    Id: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Duration: StrictFloat | StrictInt | None = None
    ResponseTime: StrictFloat | StrictInt | None = None
    HasFault: StrictBool | None = None
    HasError: StrictBool | None = None
    HasThrottle: StrictBool | None = None
    IsPartial: StrictBool | None = None
    Http: XRayHttp | None = None
    Annotations: dict[StrictStr, list[XRayValueWithServiceIds]] | None = None
    Users: list[XRayTraceUser] | None = None
    ServiceIds: list[XRayServiceId] | None = None
    ResourceARNs: list[XRayResourceARNDetail] | None = None
    InstanceIds: list[XRayInstanceIdDetail] | None = None
    AvailabilityZones: list[XRayAvailabilityZoneDetail] | None = None
    EntryPoint: XRayServiceId | None = None
    FaultRootCauses: list[XRayFaultRootCause] | None = None
    ErrorRootCauses: list[XRayErrorRootCause] | None = None
    ResponseTimeRootCauses: list[XRayResponseTimeRootCause] | None = None
    Revision: StrictInt | None = None
    MatchedEventTime: datetime.datetime | StrictStr | None = None
