from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_health_check_path_request_object import EC2HealthCheckPathRequestObject


class EC2ModifyApplicationStatusCheckRequest(BaseModel):
    ApplicationStatusCheckId: StrictStr
    Aggregation: Literal['included', 'excluded'] | None = None
    HealthCheckPaths: list[EC2HealthCheckPathRequestObject] | None = None
    Protocol: Literal['http', 'https'] | None = None
    Port: StrictInt | None = None
    Path: StrictStr | None = None
    DeviceIndex: StrictInt | None = None
    IpVersion: Literal['ipv4', 'ipv6'] | None = None
    IpScope: Literal['private'] | None = None
    Interval: StrictInt | None = None
    Timeout: StrictInt | None = None
    FailureThreshold: StrictInt | None = None
    SuccessThreshold: StrictInt | None = None
    StatusCodeMatcher: StrictStr | None = None
    InitializationGracePeriodSeconds: StrictInt | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
