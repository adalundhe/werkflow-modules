from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .emr_instance_fleet_config import EMRInstanceFleetConfig
from .emr_instance_group_config import EMRInstanceGroupConfig
from .emr_placement_type import EMRPlacementType


class EMRJobFlowInstancesConfig(BaseModel):
    MasterInstanceType: StrictStr | None = None
    SlaveInstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    InstanceGroups: list[EMRInstanceGroupConfig] | None = None
    InstanceFleets: list[EMRInstanceFleetConfig] | None = None
    Ec2KeyName: StrictStr | None = None
    Placement: EMRPlacementType | None = None
    KeepJobFlowAliveWhenNoSteps: StrictBool | None = None
    TerminationProtected: StrictBool | None = None
    UnhealthyNodeReplacement: StrictBool | None = None
    HadoopVersion: StrictStr | None = None
    Ec2SubnetId: StrictStr | None = None
    Ec2SubnetIds: list[StrictStr] | None = None
    EmrManagedMasterSecurityGroup: StrictStr | None = None
    EmrManagedSlaveSecurityGroup: StrictStr | None = None
    ServiceAccessSecurityGroup: StrictStr | None = None
    AdditionalMasterSecurityGroups: list[StrictStr] | None = None
    AdditionalSlaveSecurityGroups: list[StrictStr] | None = None
