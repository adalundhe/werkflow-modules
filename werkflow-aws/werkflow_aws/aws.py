from werkflow.modules.base import Module
from .parsers import AWSConfigParser
from .services import (
    AWSCredentials,
    AWSCodeArtifact,
    AWSCostExplorer,
    AWSElastiCache,
    AWSSTS,
)


class AWS(Module):

    def __init__(self) -> None:
        super().__init__()

        self.config = AWSConfigParser()
        self.credentials = AWSCredentials()
        self.code_artifact = AWSCodeArtifact()
        self.cost_explorer = AWSCostExplorer()
        self.elasticache = AWSElastiCache()
        self.sts = AWSSTS()

    async def close(self):
        await self.credentials.close()
        await self.code_artifact.close()
        await self.cost_explorer.close()
        await self.elasticache.close()

    def abort(self):
        self.credentials.abort()
        self.code_artifact.abort()
        self.cost_explorer.abort()
        self.elasticache.abort()

    

