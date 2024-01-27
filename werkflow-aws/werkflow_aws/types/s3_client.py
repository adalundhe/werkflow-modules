from __future__ import annotations
import datetime
from abc import ABC, abstractmethod
from io import FileIO
from typing import (
    Dict, 
    Optional, 
    Literal, 
    Union, 
    List,
    TextIO,
    BinaryIO,
    TypedDict,
    Callable,
    Any
)
from .s3_multipart_upload_part import s3MultipartUploadPart
from .s3_tag import s3Tag


class s3Client(ABC):

    @abstractmethod
    def list_buckets(self) -> Dict[str, str]:
        pass

    @abstractmethod
    def list_objects_v2(
        self,
        Bucket: str=None,
        Delimiter: Optional[str]=None,
        EncodingType: Optional[str]=None,
        MaxKeys: Optional[int]=None,
        Prefix: Optional[str]=None,
        ContinuationToken: Optional[str]=None,
        FetchOwner: Optional[bool]=None,
        StartAfter: Optional[str]=None,
        ExpectedBucketOwner: Optional[str]=None,
        OptionalObjectAttributes: Optional[
            List[str]
        ]=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def get_object(
        self,
        Bucket: str=None,
        IfMatch: Optional[str]=None,
        IfModifiedSince: Optional[datetime.datetime]=None,
        IfNoneMatch: Optional[str]=None,
        IfUnmodifiedSince: Optional[datetime.datetime]=None,
        Key: str=None,
        Range: Optional[str]=None,
        ResponseCacheControl: Optional[str]=None,
        ResponseContentDisposition: Optional[str]=None,
        ResponseContentEncoding: Optional[str]=None,
        ResponseContentLanguage: Optional[str]=None,
        ResponseContentType: Optional[str]=None,
        ResponseExpires: Optional[datetime.datetime]=None,
        VersionId: Optional[str]=None,
        SSECustomerAlgorithm: Optional[str]=None,
        SSECustomerKey: Optional[str]=None,
        PartNumber: Optional[int]=None,
        ExpectedBucketOwner: Optional[str]=None,
        ChecksumMode: Union[
            Optional[Literal['ENABLED']],
            Optional[Literal['DISABLED']]
        ]=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def put_object(
        self,
        ACL: Union[
            Optional[Literal['private']],
            Optional[Literal['public-read']],
            Optional[Literal['public-read-write']],
            Optional[Literal['authenticated-read']],
            Optional[Literal['aws-exec-read']],
            Optional[Literal['bucket-owner-read']],
            Optional[Literal['bucket-owner-full-control']]
        ]=None,
        Body: Union[bytes, TextIO, BinaryIO]=None,
        Bucket: str=None,
        CacheControl: Optional[str]=None,
        ContentDisposition: Optional[str]=None,
        ContentEncoding: Optional[str]=None,
        ContentLanguage: Optional[str]=None,
        ContentLength: Optional[int]=None,
        ContentMD5: Optional[str]=None,
        ContentType: Optional[str]=None,
        ChecksumAlgorithm: Union[
            Optional[Literal['CRC32']],
            Optional[Literal['CRC32C']],
            Optional[Literal['SHA1']],
            Optional[Literal['SHA256']]
        ]=None,
        ChecksumCRC32: Optional[str]=None,
        ChecksumCRC32C: Optional[str]=None,
        ChecksumSHA1: Optional[str]=None,
        ChecksumSHA256: Optional[str]=None,
        Expires: Optional[datetime.datetime]=None,
        GrantFullControl: Optional[str]=None,
        GrantRead: Optional[str]=None,
        GrantReadACP: Optional[str]=None,
        GrantWriteACP: Optional[str]=None,
        Key: str=None,
        Metadata: Optional[Dict[str, str]]=None,
        ServerSideEncryption: Union[
            Optional[Literal['AES256']],
            Optional[Literal['aws:kms']],
            Optional[Literal['aws:kms:dsse']]
        ]=None,
        StorageClass: Union[
            Optional[Literal['STANDARD']],
            Optional[Literal['REDUCED_REDUNDANCY']],
            Optional[Literal['STANDARD_IA']],
            Optional[Literal['ONEZONE_IA']],
            Optional[Literal['INTELLIGENT_TIERING']],
            Optional[Literal['GLACIER']],
            Optional[Literal['DEEP_ARCHIVE']],
            Optional[Literal['OUTPOSTS']],
            Optional[Literal['GLACIER_IR']],
            Optional[Literal['SNOW']]
        ]=None,
        WebsiteRedirectLocation: Optional[str]=None,
        SSECustomerAlgorithm: Optional[str]=None,
        SSECustomerKey: Optional[str]=None,
        SSEKMSKeyId: Optional[str]=None,
        SSEKMSEncryptionContext: Optional[str]=None,
        BucketKeyEnabled: Optional[bool]=None,
        Tagging: Optional[str]=None,
        ObjectLockMode: Union[
            Optional[Literal['GOVERNANCE']],
            Optional[Literal['COMPLIANCE']]
        ]=None,
        ObjectLockRetainUntilDate: Optional[datetime.datetime]=None,
        ObjectLockLegalHoldStatus: Union[
            Optional[Literal['ON']],
            Optional[Literal['OFF']]
        ]=None,
        ExpectedBucketOwner: Optional[str]=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def delete_bucket(
        self,
        Bucket='string',
        ExpectedBucketOwner='string'
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def delete_object(
        self,
        Bucket: str=None,
        Key: str=None,
        MFA: Optional[str]=None,
        VersionId: Optional[str]=None,
        BypassGovernanceRetention: Optional[bool]=None,
        ExpectedBucketOwner: Optional[str]=None
    ) -> Dict[str, str]:
        pass
    
    @abstractmethod
    def list_multipart_uploads(
        self,
        Bucket: str=None,
        Delimiter: Optional[str]=None,
        EncodingType: Optional[str]=None,
        KeyMarker: Optional[str]=None,
        MaxUploads: Optional[int]=None,
        Prefix: Optional[str]=None,
        UploadIdMarker: Optional[str]=None,
        ExpectedBucketOwner: Optional[str]=None
    ) -> Dict[str, str]:
        pass
    
    @abstractmethod
    def list_parts(
        self,
        Bucket: str=None,
        Key: str=None,
        MaxParts: Optional[int]=None,
        PartNumberMarker: Optional[int]=None,
        UploadId: Optional[str]=None,
        ExpectedBucketOwner: Optional[str]=None,
        SSECustomerAlgorithm: Optional[str]=None,
        SSECustomerKey: Optional[str]=None,
    ) -> Dict[str, str]:
        pass
    
    @abstractmethod
    def complete_multipart_upload(
        self,
        Bucket: str=None,
        Key: str=None,
        MultipartUpload: Dict[
             Literal['Parts'],
             List[s3MultipartUploadPart]
        ]=None,
        UploadId: str=None,
        ChecksumCRC32: Optional[str]=None,
        ChecksumCRC32C: Optional[str]=None,
        ChecksumSHA1: Optional[str]=None,
        ChecksumSHA256: Optional[str]=None,
        ExpectedBucketOwner: Optional[str]=None,
        SSECustomerAlgorithm: Optional[str]=None,
        SSECustomerKey: Optional[str]=None,
    ) -> Dict[str, str]:
        pass
    
    @abstractmethod
    def abort_multipart_upload(
        self,
        Bucket: str=None,
        Key: str=None,
        UploadId: str=None,
        ExpectedBucketOwner: Optional[str]=None
    ) -> Dict[str, str]:
        pass
    
    @abstractmethod
    def create_multipart_upload(
        self,
        ACL: Union[
            Optional[Literal['private']],
            Optional[Literal['public-read']],
            Optional[Literal['public-read-write']],
            Optional[Literal['authenticated-read']],
            Optional[Literal['aws-exec-read']],
            Optional[Literal['bucket-owner-read']],
            Optional[Literal['bucket-owner-full-control']]
        ]=None,
        Body: Union[bytes, TextIO, BinaryIO]=None,
        Bucket: str=None,
        CacheControl: Optional[str]=None,
        ContentDisposition: Optional[str]=None,
        ContentEncoding: Optional[str]=None,
        ContentLanguage: Optional[str]=None,
        ContentType: Optional[str]=None,
        Expires: Optional[datetime.datetime]=None,
        GrantFullControl: Optional[str]=None,
        GrantRead: Optional[str]=None,
        GrantReadACP: Optional[str]=None,
        GrantWriteACP: Optional[str]=None,
        Key: str=None,
        Metadata: Optional[Dict[str, str]]=None,
        ServerSideEncryption: Union[
            Optional[Literal['AES256']],
            Optional[Literal['aws:kms']],
            Optional[Literal['aws:kms:dsse']]
        ]=None,
        StorageClass: Union[
            Optional[Literal['STANDARD']],
            Optional[Literal['REDUCED_REDUNDANCY']],
            Optional[Literal['STANDARD_IA']],
            Optional[Literal['ONEZONE_IA']],
            Optional[Literal['INTELLIGENT_TIERING']],
            Optional[Literal['GLACIER']],
            Optional[Literal['DEEP_ARCHIVE']],
            Optional[Literal['OUTPOSTS']],
            Optional[Literal['GLACIER_IR']],
            Optional[Literal['SNOW']]
        ]=None,
        WebsiteRedirectLocation: Optional[str]=None,
        SSECustomerAlgorithm: Optional[str]=None,
        SSECustomerKey: Optional[str]=None,
        SSEKMSKeyId: Optional[str]=None,
        SSEKMSEncryptionContext: Optional[str]=None,
        BucketKeyEnabled: Optional[bool]=None,
        Tagging: Optional[str]=None,
        ObjectLockMode: Union[
            Optional[Literal['GOVERNANCE']],
            Optional[Literal['COMPLIANCE']]
        ]=None,
        ObjectLockRetainUntilDate: Optional[datetime.datetime]=None,
        ObjectLockLegalHoldStatus: Union[
            Optional[Literal['ON']],
            Optional[Literal['OFF']]
        ]=None,
        ExpectedBucketOwner: Optional[str]=None,
        ChecksumAlgorithm: Union[
             Optional[Literal['CRC32']],
             Optional[Literal['CRC32C']],
             Optional[Literal['SHA1']],
             Optional[Literal['SHA256']]
        ]=None
    ) -> Dict[str, str]:
        pass
    
    @abstractmethod
    def upload_part(
        self,
        Body: Union[
             bytes,
             TextIO,
             BinaryIO
        ]=None,
        Bucket: Optional[str]=None,
        ContentLength: Optional[int]=None,
        ContentMD5: Optional[str]=None,
        ContentType: Optional[str]=None,
        ChecksumAlgorithm: Union[
            Optional[Literal['CRC32']],
            Optional[Literal['CRC32C']],
            Optional[Literal['SHA1']],
            Optional[Literal['SHA256']]
        ]=None,
        ChecksumCRC32: Optional[str]=None,
        ChecksumCRC32C: Optional[str]=None,
        ChecksumSHA1: Optional[str]=None,
        ChecksumSHA256: Optional[str]=None,
        Key: str=None,
        PartNumber: int=None,
        UploadId: str=None,
        SSECustomerAlgorithm: Optional[str]=None,
        SSECustomerKey: Optional[str]=None,
        RequestPayer: Optional[
            Literal['requester']
        ]=None,
        ExpectedBucketOwner: Optional[str]=None,
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def upload_part_copy(
        self,
        Bucket: str=None,
        CopySource: str | TypedDict[
            Literal['Bucket','Key','VersionId'],
            str
        ]=None,
        Key: str=None,
        PartNumber: int=None,
        UploadId: str=None,
        SSECustomerAlgorithm: Optional[str]=None,
        SSECustomerKey: Optional[str]=None,
        RequestPayer: Optional[
            Literal['requester']
        ]=None,
        ExpectedBucketOwner: Optional[str]=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def get_bucket_tagging(
        self,
        Bucket: str=None,
        ExpectedBucketOwner: Optional[str]=None,
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def get_object_tagging(
        self,
        Bucket: str=None,
        Key: str=None,
        VersionId: Optional[str]=None,
        ExpectedBucketOwner: Optional[str]=None,
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def put_bucket_tagging(
        self,
        Bucket: str=None,
        ChecksumAlgorithm: Union[
            Optional[Literal['CRC32']],
            Optional[Literal['CRC32C']],
            Optional[Literal['SHA1']],
            Optional[Literal['SHA256']]
        ]=None,
        Tagging: Dict[
            Literal['TagSet'],
            List[s3Tag]
        ]=None,
        ExpectedBucketOwner: Optional[str]=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def put_object_tagging(
        self,
        Bucket: str=None,
        Key: str=None,
        VersionId: Optional[str]=None,
        ContentMD5: Optional[str]=None,
        ChecksumAlgorithm: Optional[
            Literal[
                'CRC32',
                'CRC32C',
                'SHA1',
                'SHA256'
            ]
        ]=None,
        Tagging: Dict[
            Literal['TagSet'],
            List[s3Tag]
        ]=None,
        ExpectedBucketOwner: Optional[str]=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def delete_bucket_tagging(
        self,
        Bucket: str=None,
        ExpectedBucketOwner: Optional[str]=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def delete_object_tagging(
        self,
        Bucket: str=None,
        Key: str=None,
        VersionId: Optional[str]=None,
        ExpectedBucketOwner: Optional[str]=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def upload_fileobj(
        self,
        Fileobj: FileIO,
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, str],
        Callback: Callable[..., Any],
        Config: Dict[str, str]
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def upload_file(
        self,
        Fileobj: FileIO,
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, str],
        Callback: Callable[..., Any],
        Config: Dict[str, str]
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def list_directory_buckets(
        self,
        ContinuationToken: str=None,
        MaxDirectoryBuckets: int=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def list_object_versions(
        Bucket: str=None,
        Delimiter: str=None,
        EncodingType: Literal['url']=None,
        KeyMarker: str=None,
        MaxKeys: int=None,
        Prefix: str=None,
        VersionIdMarker: str=None,
        ExpectedBucketOwner: str=None,
        RequestPayer: Literal['requester']=None,
        OptionalObjectAttributes: List[str]=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def delete_objects(
        self,
        Bucket: str=None,
        Delete: Dict[
            Literal['Objects', 'Quiet'],
            List[
                Dict[
                    Literal['Key', 'VersionId'],
                    str
                ]
            ] | bool
        ]=None,
        MFA: str=None,
        RequestPayer: Literal['requester']=None,
        BypassGovernanceRetention: bool=None,
        ExpectedBucketOwner: str=None,
        ChecksumAlgorithm: Literal[
            'CRC32',
            'CRC32C',
            'SHA1',
            'SHA256'
        ]=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def download_file(
        self,
        Bucket: str,
        Key: str,
        Filename: str,
        ExtraArgs: Dict[str, str],
        Callback: Callable[..., Any],
        Config: str
    ) -> None:
        pass

    @abstractmethod
    def download_fileobj(
        self,
        Bucket: str,
        Key: str,
        Fileobj: FileIO,
        ExtraArgs: Dict[str, str],
        Callback: Callable[..., Any],
        Config: str
    ) -> None:
        pass

    @abstractmethod
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, str]=None,
        ExpiresIn: int=None,
        HttpMethod: str=None
    )-> str:
        pass

    @abstractmethod
    def generate_presigned_post(
        self,
        Bucket: str,
        Key: str,
        Fields: Dict[str, str]=None,
        Conditions: List[Dict[str, str] | List[str]]=None,
        ExpiresIn: int=None
    ) -> Dict[str, str]:
        pass
    
    @abstractmethod
    def copy_object(
        self,
        ACL: Literal[
            'private',
            'public-read',
            'public-read-write',
            'authenticated-read',
            'aws-exec-read',
            'bucket-owner-read',
            'bucket-owner-full-control'
        ]=None,
        Bucket: str=None,
        CacheControl: str=None,
        ChecksumAlgorithm: Literal[
            'CRC32',
            'CRC32C',
            'SHA1',
            'SHA256'
        ]=None,
        ContentDisposition: str=None,
        ContentEncoding: str=None,
        ContentLanguage: str=None,
        ContentType: str=None,
        CopySource: str | Dict[
            Literal['Bucket', 'Key', 'VersionId'],
            str
        ]=None,
        CopySourceIfMatch: str=None,
        CopySourceIfModifiedSince: datetime.datetime=None,
        CopySourceIfNoneMatch: str=None,
        CopySourceIfUnmodifiedSince: datetime.datetime=None,
        Expires: datetime.datetime=None,
        GrantFullControl: str=None,
        GrantRead: str=None,
        GrantReadACP: str=None,
        GrantWriteACP: str=None,
        Key: str=None,
        Metadata: Dict[str, str]=None,
        MetadataDirective: Literal['COPY', 'REPLACE']=None,
        TaggingDirective: Literal['COPY', 'REPLACE']=None,
        ServerSideEncryption: Literal[
            'AES256',
            'aws:kms',
            'aws:kms:dsse'
        ]=None,
        StorageClass: Literal[
            'STANDARD',
            'REDUCED_REDUNDANCY',
            'STANDARD_IA',
            'ONEZONE_IA',
            'INTELLIGENT_TIERING',
            'GLACIER',
            'DEEP_ARCHIVE',
            'OUTPOSTS',
            'GLACIER_IR',
            'SNOW',
            'EXPRESS_ONEZONE'
        ]=None,
        WebsiteRedirectLocation: str=None,
        SSECustomerAlgorithm: str=None,
        SSECustomerKey: str=None,
        SSEKMSKeyId: str=None,
        SSEKMSEncryptionContext: str=None,
        BucketKeyEnabled: bool=None,
        CopySourceSSECustomerAlgorithm: str=None,
        CopySourceSSECustomerKey: str=None,
        RequestPayer: Literal['requester']=None,
        Tagging: str= None,
        ObjectLockMode: Literal['GOVERNANCE', 'COMPLIANCE']=None,
        ObjectLockRetainUntilDate: datetime.datetime=None,
        ObjectLockLegalHoldStatus: Literal['ON', 'OFF']=None,
        ExpectedBucketOwner: str=None,
        ExpectedSourceBucketOwner: str=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def copy(
        self,
        copy_source: Dict[
            Literal[
                'Bucket',
                'Key',
                'VersionId'
            ],
            str
        ],
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, str]=None,
        Callback: Callable[..., Any]=None,
        SourceClient: s3Client=None,
        Config: Dict[str, str]=None
    ) -> None:
        pass

    @abstractmethod
    def put_bucket_versioning(
        self,
        Bucket: str=None,
        ChecksumAlgorithm: Literal[
            'CRC32',
            'CRC32C',
            'SHA1',
            'SHA256'
        ]=None,
        MFA: str=None,
        VersioningConfiguration: Dict[
            Literal['MFADelete', 'Status'],
            Literal['Enabled', 'Disabled'] |
            Literal['Enabled', 'Suspended']
        ]=None,
        ExpectedBucketOwner: str=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def close(self):
        pass