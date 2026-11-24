from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_hadoop_jar_step_config import EMRHadoopJarStepConfig
from .emr_step_monitoring_configuration import EMRStepMonitoringConfiguration


class EMRStepConfig(BaseModel):
    Name: StrictStr | None = None
    ActionOnFailure: StrictStr | None = None
    HadoopJarStep: EMRHadoopJarStepConfig | None = None
    StepMonitoringConfiguration: EMRStepMonitoringConfiguration | None = None
