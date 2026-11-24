from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .compute_optimizer_export_destination import ComputeOptimizerExportDestination


class ComputeOptimizerRecommendationExportJob(BaseModel):
    jobId: StrictStr | None = None
    destination: ComputeOptimizerExportDestination | None = None
    resourceType: StrictStr | None = None
    status: StrictStr | None = None
    creationTimestamp: datetime.datetime | StrictStr | None = None
    lastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
