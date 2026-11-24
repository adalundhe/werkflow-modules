from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .connect_evaluation_form_item_enablement_configuration import ConnectEvaluationFormItemEnablementConfiguration
from .connect_evaluation_form_score_threshold import ConnectEvaluationFormScoreThreshold

if TYPE_CHECKING:
    from .connect_evaluation_form_item import ConnectEvaluationFormItem


class ConnectEvaluationFormSection(BaseModel):
    Title: StrictStr | None = None
    RefId: StrictStr | None = None
    Instructions: StrictStr | None = None
    Items: list[ConnectEvaluationFormItem] | None = None
    Weight: StrictFloat | StrictInt | None = None
    IsExcludedFromScoring: StrictBool | None = None
    ScoreThresholds: list[ConnectEvaluationFormScoreThreshold] | None = None
    Enablement: ConnectEvaluationFormItemEnablementConfiguration | None = None
