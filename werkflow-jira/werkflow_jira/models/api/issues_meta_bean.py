from __future__ import annotations
from pydantic import BaseModel
from .issues_jql_meta_data_bean import IssuesJqlMetaDataBean


class IssuesMetaBean(BaseModel):
    jql: IssuesJqlMetaDataBean | None = None
