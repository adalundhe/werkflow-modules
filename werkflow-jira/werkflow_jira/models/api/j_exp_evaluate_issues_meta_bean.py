from __future__ import annotations
from pydantic import BaseModel
from .j_exp_evaluate_issues_jql_meta_data_bean import JExpEvaluateIssuesJqlMetaDataBean


class JExpEvaluateIssuesMetaBean(BaseModel):
    jql: JExpEvaluateIssuesJqlMetaDataBean | None = None
