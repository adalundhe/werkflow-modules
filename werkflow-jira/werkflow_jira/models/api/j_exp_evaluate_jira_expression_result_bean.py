from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .j_exp_evaluate_meta_data_bean import JExpEvaluateMetaDataBean


class JExpEvaluateJiraExpressionResultBean(BaseModel):
    meta: JExpEvaluateMetaDataBean | None = None
    value: Any = None
