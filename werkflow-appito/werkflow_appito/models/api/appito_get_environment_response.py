from pydantic import BaseModel
from werkflow_appito.models.environment.appito_environment import AppitoEnvironment


class AppitoGetEnvironmentResponse(BaseModel):
    environments: list[AppitoEnvironment]