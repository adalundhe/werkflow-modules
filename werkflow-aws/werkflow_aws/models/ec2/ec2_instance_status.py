from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_application_status_summary import EC2ApplicationStatusSummary
from .ec2_ebs_status_summary import EC2EbsStatusSummary
from .ec2_instance_state_model import EC2InstanceStateModel
from .ec2_instance_status_event import EC2InstanceStatusEvent
from .ec2_instance_status_summary import EC2InstanceStatusSummary
from .ec2_operator_response import EC2OperatorResponse
from .ec2_performance_status_summary import EC2PerformanceStatusSummary


class EC2InstanceStatus(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    Operator: EC2OperatorResponse | None = None
    Events: list[EC2InstanceStatusEvent] | None = None
    InstanceId: StrictStr | None = None
    InstanceState: EC2InstanceStateModel | None = None
    InstanceStatus: EC2InstanceStatusSummary | None = None
    SystemStatus: EC2InstanceStatusSummary | None = None
    AttachedEbsStatus: EC2EbsStatusSummary | None = None
    ApplicationStatus: EC2ApplicationStatusSummary | None = None
    PerformanceStatus: EC2PerformanceStatusSummary | None = None
