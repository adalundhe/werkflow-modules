from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_investigation_ec2_instance import GuardDutyInvestigationEc2Instance
from .guard_duty_investigation_ecs_cluster import GuardDutyInvestigationEcsCluster
from .guard_duty_investigation_eks_cluster import GuardDutyInvestigationEksCluster
from .guard_duty_lambda_function import GuardDutyLambdaFunction
from .guard_duty_rds_db_instance import GuardDutyRdsDbInstance
from .guard_duty_rds_db_user import GuardDutyRdsDbUser


class GuardDutyInvestigationResourceData(BaseModel):
    Ec2Instance: GuardDutyInvestigationEc2Instance | None = None
    LambdaFunction: GuardDutyLambdaFunction | None = None
    RdsDbInstance: GuardDutyRdsDbInstance | None = None
    RdsDbUser: GuardDutyRdsDbUser | None = None
    EksCluster: GuardDutyInvestigationEksCluster | None = None
    EcsCluster: GuardDutyInvestigationEcsCluster | None = None
