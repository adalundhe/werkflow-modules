from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .target_classification import TargetClassification
from .target_mandatory_fields import TargetMandatoryFields
from .target_status import TargetStatus


class TargetToSourcesMapping(BaseModel):
    inferClassificationDefaults: StrictBool | None = None
    inferFieldDefaults: StrictBool | None = None
    inferStatusDefaults: StrictBool | None = None
    inferSubtaskTypeDefault: StrictBool | None = None
    issueIdsOrKeys: list[StrictStr] | None = None
    targetClassification: list[TargetClassification] | None = None
    targetMandatoryFields: list[TargetMandatoryFields] | None = None
    targetStatus: list[TargetStatus] | None = None
