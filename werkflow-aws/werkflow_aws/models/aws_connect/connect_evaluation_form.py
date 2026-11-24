from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .connect_evaluation_form_auto_evaluation_configuration import ConnectEvaluationFormAutoEvaluationConfiguration
from .connect_evaluation_form_item import ConnectEvaluationFormItem
from .connect_evaluation_form_language_configuration import ConnectEvaluationFormLanguageConfiguration
from .connect_evaluation_form_scoring_strategy import ConnectEvaluationFormScoringStrategy
from .connect_evaluation_form_target_configuration import ConnectEvaluationFormTargetConfiguration
from .connect_evaluation_review_configuration import ConnectEvaluationReviewConfiguration


class ConnectEvaluationForm(BaseModel):
    EvaluationFormId: StrictStr | None = None
    EvaluationFormVersion: StrictInt | None = None
    Locked: StrictBool | None = None
    EvaluationFormArn: StrictStr | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    Items: list[ConnectEvaluationFormItem] | None = None
    ScoringStrategy: ConnectEvaluationFormScoringStrategy | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: StrictStr | None = None
    AutoEvaluationConfiguration: ConnectEvaluationFormAutoEvaluationConfiguration | None = None
    ReviewConfiguration: ConnectEvaluationReviewConfiguration | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    TargetConfiguration: ConnectEvaluationFormTargetConfiguration | None = None
    LanguageConfiguration: ConnectEvaluationFormLanguageConfiguration | None = None
    LatestValidationStatus: StrictStr | None = None
    LastValidationTime: datetime.datetime | StrictStr | None = None
    AIVersion: StrictStr | None = None
