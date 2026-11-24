from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_custom_tag_key_value_response_pair import EC2CustomTagKeyValueResponsePair
from .ec2_health_check_path_response_object import EC2HealthCheckPathResponseObject
from .ec2_tag_model import EC2TagModel


class EC2ApplicationStatusCheckResponseObject(BaseModel):
    ApplicationStatusCheckId: StrictStr | None = None
    Aggregation: StrictStr | None = None
    HealthCheckPaths: list[EC2HealthCheckPathResponseObject] | None = None
    Protocol: StrictStr | None = None
    Port: StrictInt | None = None
    Path: StrictStr | None = None
    DeviceIndex: StrictInt | None = None
    IpVersion: StrictStr | None = None
    IpScope: StrictStr | None = None
    Interval: StrictInt | None = None
    Timeout: StrictInt | None = None
    FailureThreshold: StrictInt | None = None
    SuccessThreshold: StrictInt | None = None
    StatusCodeMatcher: StrictStr | None = None
    InitializationGracePeriodSeconds: StrictInt | None = None
    LastUpdatedAt: datetime.datetime | StrictStr | None = None
    TargetTagAssociations: list[EC2CustomTagKeyValueResponsePair] | None = None
    Tags: list[EC2TagModel] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ModifyTime: datetime.datetime | StrictStr | None = None
    DeletionTime: datetime.datetime | StrictStr | None = None
