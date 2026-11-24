from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_health_check_path_request_object import EC2HealthCheckPathRequestObject
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateApplicationStatusCheckRequest(BaseModel):
    Protocol: Literal['http', 'https']
    Port: StrictInt
    HealthCheckPaths: list[EC2HealthCheckPathRequestObject] | None = None
    Aggregation: Literal['included', 'excluded'] | None = None
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
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
