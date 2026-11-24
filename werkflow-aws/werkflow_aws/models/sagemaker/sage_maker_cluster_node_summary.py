from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_instance_status_details import SageMakerClusterInstanceStatusDetails
from .sage_maker_ultra_server_info import SageMakerUltraServerInfo


class SageMakerClusterNodeSummary(BaseModel):
    InstanceGroupName: StrictStr | None = None
    InstanceId: StrictStr | None = None
    NodeLogicalId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    LaunchTime: datetime.datetime | StrictStr | None = None
    LastSoftwareUpdateTime: datetime.datetime | StrictStr | None = None
    InstanceStatus: SageMakerClusterInstanceStatusDetails | None = None
    UltraServerInfo: SageMakerUltraServerInfo | None = None
    PrivateDnsHostname: StrictStr | None = None
    CurrentImageReleaseVersion: StrictStr | None = None
    ImageVersionStatus: StrictStr | None = None
