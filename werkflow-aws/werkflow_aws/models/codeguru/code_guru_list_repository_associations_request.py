from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeGuruListRepositoryAssociationsRequest(BaseModel):
    ProviderTypes: list[Literal['CodeCommit', 'GitHub', 'Bitbucket', 'GitHubEnterpriseServer', 'S3Bucket']] | None = None
    States: list[Literal['Associated', 'Associating', 'Failed', 'Disassociating', 'Disassociated']] | None = None
    Names: list[StrictStr] | None = None
    Owners: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
