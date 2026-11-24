from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecr_list_image_referrers_filter import ECRListImageReferrersFilter
from .ecr_subject_identifier import ECRSubjectIdentifier


class ECRListImageReferrersRequest(BaseModel):
    repositoryName: StrictStr
    subjectId: ECRSubjectIdentifier
    registryId: StrictStr | None = None
    filter: ECRListImageReferrersFilter | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
