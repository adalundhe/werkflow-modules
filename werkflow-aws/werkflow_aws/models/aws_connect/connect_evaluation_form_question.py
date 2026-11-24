from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .connect_evaluation_form_item_enablement_configuration import ConnectEvaluationFormItemEnablementConfiguration
from .connect_evaluation_form_metric_configuration import ConnectEvaluationFormMetricConfiguration
from .connect_evaluation_form_question_scoring_configuration import ConnectEvaluationFormQuestionScoringConfiguration
from .connect_evaluation_form_question_type_properties import ConnectEvaluationFormQuestionTypeProperties


class ConnectEvaluationFormQuestion(BaseModel):
    Title: StrictStr | None = None
    Instructions: StrictStr | None = None
    RefId: StrictStr | None = None
    NotApplicableEnabled: StrictBool | None = None
    QuestionType: StrictStr | None = None
    QuestionTypeProperties: ConnectEvaluationFormQuestionTypeProperties | None = None
    Enablement: ConnectEvaluationFormItemEnablementConfiguration | None = None
    Weight: StrictFloat | StrictInt | None = None
    ScoringConfiguration: ConnectEvaluationFormQuestionScoringConfiguration | None = None
    MetricConfiguration: ConnectEvaluationFormMetricConfiguration | None = None
