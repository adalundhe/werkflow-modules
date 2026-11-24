from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_commit_approval_rule_event_metadata import CodeCommitApprovalRuleEventMetadata
from .code_commit_approval_rule_overridden_event_metadata import CodeCommitApprovalRuleOverriddenEventMetadata
from .code_commit_approval_state_changed_event_metadata import CodeCommitApprovalStateChangedEventMetadata
from .code_commit_pull_request_created_event_metadata import CodeCommitPullRequestCreatedEventMetadata
from .code_commit_pull_request_merged_state_changed_event_metadata import CodeCommitPullRequestMergedStateChangedEventMetadata
from .code_commit_pull_request_source_reference_updated_event_metadata import CodeCommitPullRequestSourceReferenceUpdatedEventMetadata
from .code_commit_pull_request_status_changed_event_metadata import CodeCommitPullRequestStatusChangedEventMetadata


class CodeCommitPullRequestEvent(BaseModel):
    pullRequestId: StrictStr | None = None
    eventDate: datetime.datetime | StrictStr | None = None
    pullRequestEventType: StrictStr | None = None
    actorArn: StrictStr | None = None
    pullRequestCreatedEventMetadata: CodeCommitPullRequestCreatedEventMetadata | None = None
    pullRequestStatusChangedEventMetadata: CodeCommitPullRequestStatusChangedEventMetadata | None = None
    pullRequestSourceReferenceUpdatedEventMetadata: CodeCommitPullRequestSourceReferenceUpdatedEventMetadata | None = None
    pullRequestMergedStateChangedEventMetadata: CodeCommitPullRequestMergedStateChangedEventMetadata | None = None
    approvalRuleEventMetadata: CodeCommitApprovalRuleEventMetadata | None = None
    approvalStateChangedEventMetadata: CodeCommitApprovalStateChangedEventMetadata | None = None
    approvalRuleOverriddenEventMetadata: CodeCommitApprovalRuleOverriddenEventMetadata | None = None
