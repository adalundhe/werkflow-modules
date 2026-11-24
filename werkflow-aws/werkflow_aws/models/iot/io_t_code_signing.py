from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_custom_code_signing import IoTCustomCodeSigning
from .io_t_start_signing_job_parameter import IoTStartSigningJobParameter


class IoTCodeSigning(BaseModel):
    awsSignerJobId: StrictStr | None = None
    startSigningJobParameter: IoTStartSigningJobParameter | None = None
    customCodeSigning: IoTCustomCodeSigning | None = None
