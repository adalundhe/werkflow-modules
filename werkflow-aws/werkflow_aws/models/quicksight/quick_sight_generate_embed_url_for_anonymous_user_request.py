from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_anonymous_user_embedding_experience_configuration import QuickSightAnonymousUserEmbeddingExperienceConfiguration
from .quick_sight_session_tag import QuickSightSessionTag


class QuickSightGenerateEmbedUrlForAnonymousUserRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr
    AuthorizedResourceArns: list[StrictStr]
    ExperienceConfiguration: QuickSightAnonymousUserEmbeddingExperienceConfiguration
    SessionLifetimeInMinutes: StrictInt | None = None
    SessionTags: list[QuickSightSessionTag] | None = None
    AllowedDomains: list[StrictStr] | None = None
