from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AccessAnalyzerListAnalyzedResourcesRequest(BaseModel):
    analyzerArn: StrictStr
    resourceType: Literal['AWS::S3::Bucket', 'AWS::IAM::Role', 'AWS::SQS::Queue', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::KMS::Key', 'AWS::SecretsManager::Secret', 'AWS::EFS::FileSystem', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBClusterSnapshot', 'AWS::SNS::Topic', 'AWS::S3Express::DirectoryBucket', 'AWS::DynamoDB::Table', 'AWS::DynamoDB::Stream', 'AWS::IAM::User'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
