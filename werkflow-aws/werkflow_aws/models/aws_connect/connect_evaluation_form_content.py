from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_evaluation_form_auto_evaluation_configuration import ConnectEvaluationFormAutoEvaluationConfiguration
from .connect_evaluation_form_item import ConnectEvaluationFormItem
from .connect_evaluation_form_language_configuration import ConnectEvaluationFormLanguageConfiguration
from .connect_evaluation_form_scoring_strategy import ConnectEvaluationFormScoringStrategy
from .connect_evaluation_form_target_configuration import ConnectEvaluationFormTargetConfiguration
from .connect_evaluation_review_configuration import ConnectEvaluationReviewConfiguration


class ConnectEvaluationFormContent(BaseModel):
    EvaluationFormVersion: StrictInt | None = None
    EvaluationFormId: StrictStr | None = None
    EvaluationFormArn: StrictStr | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    Items: list[ConnectEvaluationFormItem] | None = None
    ScoringStrategy: ConnectEvaluationFormScoringStrategy | None = None
    AutoEvaluationConfiguration: ConnectEvaluationFormAutoEvaluationConfiguration | None = None
    TargetConfiguration: ConnectEvaluationFormTargetConfiguration | None = None
    LanguageConfiguration: ConnectEvaluationFormLanguageConfiguration | None = None
    ReviewConfiguration: ConnectEvaluationReviewConfiguration | None = None
    AIVersion: StrictStr | None = None
