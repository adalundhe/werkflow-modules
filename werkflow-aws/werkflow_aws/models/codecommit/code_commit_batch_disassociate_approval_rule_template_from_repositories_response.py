from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_batch_disassociate_approval_rule_template_from_repositories_error import CodeCommitBatchDisassociateApprovalRuleTemplateFromRepositoriesError


class CodeCommitBatchDisassociateApprovalRuleTemplateFromRepositoriesResponse(BaseModel):
    disassociatedRepositoryNames: list[StrictStr] | None = None
    errors: list[CodeCommitBatchDisassociateApprovalRuleTemplateFromRepositoriesError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
