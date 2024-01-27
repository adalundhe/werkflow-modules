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
    ):
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
    ):
        pass

    @abstractmethod
    def close(self):
        pass