from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_rule_declaration import CodePipelineRuleDeclaration


class CodePipelineCondition(BaseModel):
    result: StrictStr | None = None
    rules: list[CodePipelineRuleDeclaration] | None = None
