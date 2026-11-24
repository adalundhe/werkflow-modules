from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_registered_user_embedding_experience_configuration import QuickSightRegisteredUserEmbeddingExperienceConfiguration


class QuickSightGenerateEmbedUrlForRegisteredUserWithIdentityRequest(BaseModel):
    AwsAccountId: StrictStr
    ExperienceConfiguration: QuickSightRegisteredUserEmbeddingExperienceConfiguration
    SessionLifetimeInMinutes: StrictInt | None = None
    AllowedDomains: list[StrictStr] | None = None
