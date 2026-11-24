from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_evaluation_context import ConfigServiceEvaluationContext
from .config_service_evaluation_status import ConfigServiceEvaluationStatus
from .config_service_resource_details import ConfigServiceResourceDetails


class ConfigServiceGetResourceEvaluationSummaryResponse(BaseModel):
    ResourceEvaluationId: StrictStr | None = None
    EvaluationMode: StrictStr | None = None
    EvaluationStatus: ConfigServiceEvaluationStatus | None = None
    EvaluationStartTimestamp: datetime.datetime | StrictStr | None = None
    Compliance: StrictStr | None = None
    EvaluationContext: ConfigServiceEvaluationContext | None = None
    ResourceDetails: ConfigServiceResourceDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
