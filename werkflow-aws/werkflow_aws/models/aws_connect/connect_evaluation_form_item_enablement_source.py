from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluationFormItemEnablementSource(BaseModel):
    Type: StrictStr | None = None
    RefId: StrictStr | None = None
    ContactField: StrictStr | None = None
    ContactAttributeKey: StrictStr | None = None
    SegmentAttributeKey: StrictStr | None = None
    EvaluationMetadataField: StrictStr | None = None
    AiMetricsField: StrictStr | None = None
