from __future__ import annotations
from pydantic import BaseModel, StrictBool


class KendraGitHubDocumentCrawlProperties(BaseModel):
    CrawlRepositoryDocuments: StrictBool | None = None
    CrawlIssue: StrictBool | None = None
    CrawlIssueComment: StrictBool | None = None
    CrawlIssueCommentAttachment: StrictBool | None = None
    CrawlPullRequest: StrictBool | None = None
    CrawlPullRequestComment: StrictBool | None = None
    CrawlPullRequestCommentAttachment: StrictBool | None = None
