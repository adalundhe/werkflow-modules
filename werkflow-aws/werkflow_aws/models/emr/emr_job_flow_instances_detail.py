from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .emr_instance_group_detail import EMRInstanceGroupDetail
from .emr_placement_type import EMRPlacementType


class EMRJobFlowInstancesDetail(BaseModel):
    MasterInstanceType: StrictStr | None = None
    MasterPublicDnsName: StrictStr | None = None
    MasterInstanceId: StrictStr | None = None
    SlaveInstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    InstanceGroups: list[EMRInstanceGroupDetail] | None = None
    NormalizedInstanceHours: StrictInt | None = None
    Ec2KeyName: StrictStr | None = None
    Ec2SubnetId: StrictStr | None = None
    Placement: EMRPlacementType | None = None
    KeepJobFlowAliveWhenNoSteps: StrictBool | None = None
    TerminationProtected: StrictBool | None = None
    UnhealthyNodeReplacement: StrictBool | None = None
    HadoopVersion: StrictStr | None = None
