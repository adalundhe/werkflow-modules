from werkflow_core import Module
from .parsers import AWSConfigParser
from .services import (
    AWSCloudwatch,
    AWSCredentials,
    AWSCodeArtifact,
    AWSCostExplorer,
    AWSEC2,
    AWSElastiCache,
    AWSOrganizations,
    AWSSTS,
)


class AWS(Module):

    def __init__(self) -> None:
        super().__init__()

        self.cloudwatch = AWSCloudwatch()
        self.config = AWSConfigParser()
        self.credentials = AWSCredentials()
        self.code_artifact = AWSCodeArtifact()
        self.cost_explorer = AWSCostExplorer()
        self.ec2 = AWSEC2()
        self.elasticache = AWSElastiCache()
        self.organizations = AWSOrganizations()
        self.sts = AWSSTS()

    async def close(self):
        await self.cloudwatch.close()
        await self.credentials.close()
        await self.code_artifact.close()
        await self.cost_explorer.close()
        await self.ec2.close()
        await self.elasticache.close()

    def abort(self):
        self.cloudwatch.abort()
        self.credentials.abort()
        self.code_artifact.abort()
        self.cost_explorer.abort()
        self.ec2.abort()
        self.elasticache.abort()

    

