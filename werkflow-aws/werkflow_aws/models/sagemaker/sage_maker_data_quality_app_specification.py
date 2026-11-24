from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDataQualityAppSpecification(BaseModel):
    ImageUri: StrictStr | None = None
    ContainerEntrypoint: list[StrictStr] | None = None
    ContainerArguments: list[StrictStr] | None = None
    RecordPreprocessorSourceUri: StrictStr | None = None
    PostAnalyticsProcessorSourceUri: StrictStr | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
