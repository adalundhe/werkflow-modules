from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AppRunnerListObservabilityConfigurationsRequest(BaseModel):
    ObservabilityConfigurationName: StrictStr | None = None
    LatestOnly: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
