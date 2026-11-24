from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_evaluation_answer_output import ConnectEvaluationAnswerOutput
from .connect_evaluation_metadata import ConnectEvaluationMetadata
from .connect_evaluation_note import ConnectEvaluationNote
from .connect_evaluation_resolved_source import ConnectEvaluationResolvedSource
from .connect_evaluation_score import ConnectEvaluationScore


class ConnectEvaluation(BaseModel):
    EvaluationId: StrictStr | None = None
    EvaluationArn: StrictStr | None = None
    Metadata: ConnectEvaluationMetadata | None = None
    Answers: dict[StrictStr, ConnectEvaluationAnswerOutput] | None = None
    Notes: dict[StrictStr, ConnectEvaluationNote] | None = None
    Status: StrictStr | None = None
    Scores: dict[StrictStr, ConnectEvaluationScore] | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    EvaluationType: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ItemEnablementStatus: dict[StrictStr, StrictStr] | None = None
    SourceResolutionStatus: StrictStr | None = None
    SourceValues: list[ConnectEvaluationResolvedSource] | None = None
