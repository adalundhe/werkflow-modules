from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_registered_user_embedding_experience_configuration import QuickSightRegisteredUserEmbeddingExperienceConfiguration


class QuickSightGenerateEmbedUrlForRegisteredUserRequest(BaseModel):
    AwsAccountId: StrictStr
    UserArn: StrictStr
    ExperienceConfiguration: QuickSightRegisteredUserEmbeddingExperienceConfiguration
    SessionLifetimeInMinutes: StrictInt | None = None
    AllowedDomains: list[StrictStr] | None = None
