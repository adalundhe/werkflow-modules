from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_auto_evaluation_configuration import ConnectAutoEvaluationConfiguration


class ConnectStartContactEvaluationRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    EvaluationFormId: StrictStr
    AutoEvaluationConfiguration: ConnectAutoEvaluationConfiguration | None = None
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
