from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2ExportTransitGatewayRoutesRequest(BaseModel):
    TransitGatewayRouteTableId: StrictStr
    S3Bucket: StrictStr
    Filters: list[EC2FilterModel] | None = None
    DryRun: StrictBool | None = None
