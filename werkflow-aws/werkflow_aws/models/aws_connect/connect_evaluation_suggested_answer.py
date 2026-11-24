from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_answer_data import ConnectEvaluationAnswerData
from .connect_evaluation_question_answer_analysis_details import ConnectEvaluationQuestionAnswerAnalysisDetails
from .connect_evaluation_question_input_details import ConnectEvaluationQuestionInputDetails


class ConnectEvaluationSuggestedAnswer(BaseModel):
    Value: ConnectEvaluationAnswerData | None = None
    Status: StrictStr | None = None
    Input: ConnectEvaluationQuestionInputDetails | None = None
    AnalysisType: StrictStr | None = None
    AnalysisDetails: ConnectEvaluationQuestionAnswerAnalysisDetails | None = None
