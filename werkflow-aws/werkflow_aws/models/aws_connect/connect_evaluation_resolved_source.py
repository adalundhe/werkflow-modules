from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_item_enablement_source import ConnectEvaluationFormItemEnablementSource
from .connect_evaluation_form_item_enablement_source_value import ConnectEvaluationFormItemEnablementSourceValue


class ConnectEvaluationResolvedSource(BaseModel):
    Source: ConnectEvaluationFormItemEnablementSource | None = None
    Status: StrictStr | None = None
    Values: list[ConnectEvaluationFormItemEnablementSourceValue] | None = None
