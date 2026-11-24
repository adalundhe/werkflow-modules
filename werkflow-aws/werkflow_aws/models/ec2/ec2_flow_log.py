from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_destination_options_response import EC2DestinationOptionsResponse
from .ec2_tag_field_specification_response import EC2TagFieldSpecificationResponse
from .ec2_tag_model import EC2TagModel


class EC2FlowLog(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    DeliverLogsErrorMessage: StrictStr | None = None
    DeliverLogsPermissionArn: StrictStr | None = None
    DeliverCrossAccountRole: StrictStr | None = None
    DeliverLogsStatus: StrictStr | None = None
    FlowLogId: StrictStr | None = None
    FlowLogStatus: StrictStr | None = None
    LogGroupName: StrictStr | None = None
    ResourceId: StrictStr | None = None
    TrafficType: StrictStr | None = None
    LogDestinationType: StrictStr | None = None
    LogDestination: StrictStr | None = None
    LogFormat: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    MaxAggregationInterval: StrictInt | None = None
    DestinationOptions: EC2DestinationOptionsResponse | None = None
    TagFieldSpecifications: list[EC2TagFieldSpecificationResponse] | None = None
