from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .connect_evaluation_form_auto_evaluation_configuration import ConnectEvaluationFormAutoEvaluationConfiguration
from .connect_evaluation_form_item import ConnectEvaluationFormItem
from .connect_evaluation_form_language_configuration import ConnectEvaluationFormLanguageConfiguration
from .connect_evaluation_form_scoring_strategy import ConnectEvaluationFormScoringStrategy
from .connect_evaluation_form_target_configuration import ConnectEvaluationFormTargetConfiguration
from .connect_evaluation_review_configuration import ConnectEvaluationReviewConfiguration


class ConnectCreateEvaluationFormRequest(BaseModel):
    InstanceId: StrictStr
    Title: StrictStr
    Items: list[ConnectEvaluationFormItem]
    Description: StrictStr | None = None
    ScoringStrategy: ConnectEvaluationFormScoringStrategy | None = None
    AutoEvaluationConfiguration: ConnectEvaluationFormAutoEvaluationConfiguration | None = None
    ClientToken: StrictStr | None = None
    AsDraft: StrictBool | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ReviewConfiguration: ConnectEvaluationReviewConfiguration | None = None
    TargetConfiguration: ConnectEvaluationFormTargetConfiguration | None = None
    LanguageConfiguration: ConnectEvaluationFormLanguageConfiguration | None = None
    AIVersion: StrictStr | None = None
