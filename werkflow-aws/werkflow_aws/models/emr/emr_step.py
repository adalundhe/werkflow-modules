from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_hadoop_step_config import EMRHadoopStepConfig
from .emr_step_additional_info import EMRStepAdditionalInfo
from .emr_step_status import EMRStepStatus


class EMRStep(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Config: EMRHadoopStepConfig | None = None
    ActionOnFailure: StrictStr | None = None
    Status: EMRStepStatus | None = None
    ExecutionRoleArn: StrictStr | None = None
    LogUri: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
    AdditionalInfo: EMRStepAdditionalInfo | None = None
