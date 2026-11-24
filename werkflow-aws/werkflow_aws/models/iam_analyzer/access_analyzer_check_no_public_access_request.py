from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AccessAnalyzerCheckNoPublicAccessRequest(BaseModel):
    policyDocument: StrictStr
    resourceType: Literal['AWS::DynamoDB::Table', 'AWS::DynamoDB::Stream', 'AWS::EFS::FileSystem', 'AWS::OpenSearchService::Domain', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::S3::Bucket', 'AWS::S3::AccessPoint', 'AWS::S3Express::DirectoryBucket', 'AWS::S3::Glacier', 'AWS::S3Outposts::Bucket', 'AWS::S3Outposts::AccessPoint', 'AWS::SecretsManager::Secret', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::IAM::AssumeRolePolicyDocument', 'AWS::S3Tables::TableBucket', 'AWS::ApiGateway::RestApi', 'AWS::CodeArtifact::Domain', 'AWS::Backup::BackupVault', 'AWS::CloudTrail::Dashboard', 'AWS::CloudTrail::EventDataStore', 'AWS::S3Tables::Table', 'AWS::S3Express::AccessPoint']
