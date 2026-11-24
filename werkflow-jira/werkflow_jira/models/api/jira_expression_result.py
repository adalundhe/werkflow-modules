from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .jira_expression_evaluation_meta_data_bean import JiraExpressionEvaluationMetaDataBean


class JiraExpressionResult(BaseModel):
    meta: JiraExpressionEvaluationMetaDataBean | None = None
    value: Any = None
