from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeGuruListCodeReviewsRequest(BaseModel):
    Type: Literal['PullRequest', 'RepositoryAnalysis']
    ProviderTypes: list[Literal['CodeCommit', 'GitHub', 'Bitbucket', 'GitHubEnterpriseServer', 'S3Bucket']] | None = None
    States: list[Literal['Completed', 'Pending', 'Failed', 'Deleting']] | None = None
    RepositoryNames: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
