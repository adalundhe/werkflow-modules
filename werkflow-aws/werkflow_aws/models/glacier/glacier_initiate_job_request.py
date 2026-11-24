from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glacier_job_parameters import GlacierJobParameters


class GlacierInitiateJobRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    jobParameters: GlacierJobParameters | None = None
