from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .emr_bootstrap_action_detail import EMRBootstrapActionDetail
from .emr_job_flow_execution_status_detail import EMRJobFlowExecutionStatusDetail
from .emr_job_flow_instances_detail import EMRJobFlowInstancesDetail
from .emr_step_detail import EMRStepDetail


class EMRJobFlowDetail(BaseModel):
    JobFlowId: StrictStr | None = None
    Name: StrictStr | None = None
    LogUri: StrictStr | None = None
    LogEncryptionKmsKeyId: StrictStr | None = None
    AmiVersion: StrictStr | None = None
    ExecutionStatusDetail: EMRJobFlowExecutionStatusDetail | None = None
    Instances: EMRJobFlowInstancesDetail | None = None
    Steps: list[EMRStepDetail] | None = None
    BootstrapActions: list[EMRBootstrapActionDetail] | None = None
    SupportedProducts: list[StrictStr] | None = None
    VisibleToAllUsers: StrictBool | None = None
    JobFlowRole: StrictStr | None = None
    ServiceRole: StrictStr | None = None
    AutoScalingRole: StrictStr | None = None
    ScaleDownBehavior: StrictStr | None = None
