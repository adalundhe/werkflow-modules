from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .batch_service_job_preempted_attempt import BatchServiceJobPreemptedAttempt


class BatchServiceJobPreemptionSummary(BaseModel):
    preemptedAttemptCount: StrictInt | None = None
    recentPreemptedAttempts: list[BatchServiceJobPreemptedAttempt] | None = None
