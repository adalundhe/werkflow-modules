from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_destination_options_request import EC2DestinationOptionsRequest
from .ec2_tag_field_specification_request import EC2TagFieldSpecificationRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateFlowLogsRequest(BaseModel):
    ResourceIds: list[StrictStr]
    ResourceType: Literal['VPC', 'Subnet', 'NetworkInterface', 'TransitGateway', 'TransitGatewayAttachment', 'RegionalNatGateway', 'CoreNetwork', 'CoreNetworkEdge', 'CoreNetworkAttachment']
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
    DeliverLogsPermissionArn: StrictStr | None = None
    DeliverCrossAccountRole: StrictStr | None = None
    LogGroupName: StrictStr | None = None
    TrafficType: Literal['ACCEPT', 'REJECT', 'ALL'] | None = None
    LogDestinationType: Literal['cloud-watch-logs', 's3', 'kinesis-data-firehose'] | None = None
    LogDestination: StrictStr | None = None
    LogFormat: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    MaxAggregationInterval: StrictInt | None = None
    DestinationOptions: EC2DestinationOptionsRequest | None = None
    TagFieldSpecifications: list[EC2TagFieldSpecificationRequest] | None = None
