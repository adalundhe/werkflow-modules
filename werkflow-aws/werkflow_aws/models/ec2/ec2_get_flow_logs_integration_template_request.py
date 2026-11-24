from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_integrate_services import EC2IntegrateServices


class EC2GetFlowLogsIntegrationTemplateRequest(BaseModel):
    FlowLogId: StrictStr
    ConfigDeliveryS3DestinationArn: StrictStr
    IntegrateServices: EC2IntegrateServices
    DryRun: StrictBool | None = None
