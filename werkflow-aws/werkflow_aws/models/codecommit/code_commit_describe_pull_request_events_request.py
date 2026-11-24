from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitDescribePullRequestEventsRequest(BaseModel):
    pullRequestId: StrictStr
    pullRequestEventType: Literal['PULL_REQUEST_CREATED', 'PULL_REQUEST_STATUS_CHANGED', 'PULL_REQUEST_SOURCE_REFERENCE_UPDATED', 'PULL_REQUEST_MERGE_STATE_CHANGED', 'PULL_REQUEST_APPROVAL_RULE_CREATED', 'PULL_REQUEST_APPROVAL_RULE_UPDATED', 'PULL_REQUEST_APPROVAL_RULE_DELETED', 'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN', 'PULL_REQUEST_APPROVAL_STATE_CHANGED'] | None = None
    actorArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
