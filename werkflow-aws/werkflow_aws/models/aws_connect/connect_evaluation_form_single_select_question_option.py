from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .connect_automatic_fail_configuration import ConnectAutomaticFailConfiguration
from .connect_question_option_points_configuration import ConnectQuestionOptionPointsConfiguration


class ConnectEvaluationFormSingleSelectQuestionOption(BaseModel):
    RefId: StrictStr | None = None
    Text: StrictStr | None = None
    Score: StrictInt | None = None
    AutomaticFail: StrictBool | None = None
    AutomaticFailConfiguration: ConnectAutomaticFailConfiguration | None = None
    PointsConfiguration: ConnectQuestionOptionPointsConfiguration | None = None
