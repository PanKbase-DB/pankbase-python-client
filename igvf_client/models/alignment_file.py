# coding: utf-8

"""
    IGVF Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 46.1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class AlignmentFile(BaseModel):
    """
    A file containing alignment data in bam format.
    """ # noqa: E501
    controlled_access: Optional[StrictBool] = Field(default=None, description="Boolean value, indicating the file being controlled access, if true.")
    anvil_url: Optional[StrictStr] = Field(default=None, description="URL linking to the controlled access file that has been deposited at AnVIL workspace.")
    transcriptome_annotation: Optional[StrictStr] = Field(default=None, description="The annotation and version of the reference resource.")
    assembly: Optional[StrictStr] = Field(default=None, description="Genome assembly applicable for the annotation data.")
    release_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was released.")
    reference_files: Optional[List[StrictStr]] = Field(default=None, description="Link to the reference files used to generate this file.")
    documents: Optional[List[StrictStr]] = Field(default=None, description="Documents that provide additional information (not data file).")
    lab: Optional[StrictStr] = Field(default=None, description="Lab associated with the submission.")
    award: Optional[StrictStr] = Field(default=None, description="Grant associated with the submission.")
    accession: Optional[StrictStr] = Field(default=None, description="A unique identifier to be used to reference the object prefixed with IGVF.")
    alternate_accessions: Optional[List[StrictStr]] = Field(default=None, description="Accessions previously assigned to objects that have been merged with this object.")
    collections: Optional[List[StrictStr]] = Field(default=None, description="Some samples are part of particular data collections.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the metadata object.")
    revoke_detail: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Explanation of why an object was transitioned to the revoked status.")
    schema_version: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The version of the JSON schema that the server uses to validate the object.")
    uuid: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with every object.")
    notes: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="DACC internal notes.")
    aliases: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Lab specific identifiers to reference an object.")
    creation_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was created.")
    submitted_by: Optional[StrictStr] = Field(default=None, description="The user who submitted the object.")
    submitter_comment: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Additional information specified by the submitter to be displayed as a comment on the portal.")
    description: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A plain text description of the object.")
    analysis_step_version: Optional[StrictStr] = Field(default=None, description="The analysis step version of the file.")
    content_md5sum: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, description="The MD5sum of the uncompressed file.")
    content_type: Optional[StrictStr] = Field(default=None, description="The type of content in the file.")
    dbxrefs: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Identifiers from external resources that may have 1-to-1 or 1-to-many relationships with IGVF file objects.")
    derived_from: Optional[List[StrictStr]] = Field(default=None, description="The files participating as inputs into software to produce this output file.")
    file_format: Optional[StrictStr] = Field(default=None, description="The file format or extension of the file.")
    file_format_specifications: Optional[List[StrictStr]] = Field(default=None, description="Document that further explains the file format.")
    file_set: Optional[StrictStr] = Field(default=None, description="The file set that this file belongs to.")
    file_size: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="File size specified in bytes.")
    md5sum: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, description="The md5sum of the file being transferred.")
    submitted_file_name: Optional[StrictStr] = Field(default=None, description="Original name of the file.")
    upload_status: Optional[StrictStr] = Field(default=None, description="The upload/validation status of the file.")
    validation_error_detail: Optional[StrictStr] = Field(default=None, description="Explanation of why the file failed the automated content checks.")
    redacted: Optional[StrictBool] = Field(default=None, description="Indicates whether the alignments data have been sanitized (redacted) to prevent leakage of private and potentially identifying genomic information.")
    filtered: Optional[StrictBool] = Field(default=None, description="Indicates whether reads that did not pass a filtering step, such as PCR duplicates, have been removed from the file.")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[List[StrictStr]] = Field(default=None, alias="@type")
    summary: Optional[StrictStr] = Field(default=None, description="A summary of the alignment file.")
    integrated_in: Optional[List[StrictStr]] = Field(default=None, description="Construct library set(s) that this file was used for in insert design.")
    input_file_for: Optional[List[StrictStr]] = Field(default=None, description="The files which are derived from this file.")
    gene_list_for: Optional[List[StrictStr]] = Field(default=None, description="File Set(s) that this file is a gene list for.")
    loci_list_for: Optional[List[StrictStr]] = Field(default=None, description="File Set(s) that this file is a loci list for.")
    href: Optional[StrictStr] = Field(default=None, description="The download path to obtain file.")
    s3_uri: Optional[StrictStr] = Field(default=None, description="The S3 URI of public file object.")
    upload_credentials: Optional[Dict[str, Any]] = Field(default=None, description="The upload credentials for S3 to submit the file content.")
    content_summary: Optional[StrictStr] = Field(default=None, description="A summary of the data in the alignment file.")
    __properties: ClassVar[List[str]] = ["controlled_access", "anvil_url", "transcriptome_annotation", "assembly", "release_timestamp", "reference_files", "documents", "lab", "award", "accession", "alternate_accessions", "collections", "status", "revoke_detail", "schema_version", "uuid", "notes", "aliases", "creation_timestamp", "submitted_by", "submitter_comment", "description", "analysis_step_version", "content_md5sum", "content_type", "dbxrefs", "derived_from", "file_format", "file_format_specifications", "file_set", "file_size", "md5sum", "submitted_file_name", "upload_status", "validation_error_detail", "redacted", "filtered", "@id", "@type", "summary", "integrated_in", "input_file_for", "gene_list_for", "loci_list_for", "href", "s3_uri", "upload_credentials", "content_summary"]

    @field_validator('transcriptome_annotation')
    def transcriptome_annotation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['GENCODE 40', 'GENCODE 41', 'GENCODE 42', 'GENCODE 43', 'GENCODE 44', 'GENCODE 45', 'GENCODE M30', 'GENCODE M31', 'GENCODE M32', 'GENCODE M33', 'GENCODE M34']):
            raise ValueError("must be one of enum values ('GENCODE 40', 'GENCODE 41', 'GENCODE 42', 'GENCODE 43', 'GENCODE 44', 'GENCODE 45', 'GENCODE M30', 'GENCODE M31', 'GENCODE M32', 'GENCODE M33', 'GENCODE M34')")
        return value

    @field_validator('assembly')
    def assembly_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['GRCh38', 'GRCm39']):
            raise ValueError("must be one of enum values ('GRCh38', 'GRCm39')")
        return value

    @field_validator('collections')
    def collections_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ClinGen', 'ENCODE', 'GREGoR', 'IGVF_catalog_beta_v0.1', 'IGVF_catalog_beta_v0.2', 'IGVF_catalog_beta_v0.3', 'IGVF_catalog_beta_v0.4', 'MaveDB', 'MPRAbase', 'Vista']):
                raise ValueError("each list item must be one of ('ClinGen', 'ENCODE', 'GREGoR', 'IGVF_catalog_beta_v0.1', 'IGVF_catalog_beta_v0.2', 'IGVF_catalog_beta_v0.3', 'IGVF_catalog_beta_v0.4', 'MaveDB', 'MPRAbase', 'Vista')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['in progress', 'released', 'deleted', 'replaced', 'revoked', 'archived']):
            raise ValueError("must be one of enum values ('in progress', 'released', 'deleted', 'replaced', 'revoked', 'archived')")
        return value

    @field_validator('revoke_detail')
    def revoke_detail_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\S+(\s|\S)*\S+|\S)$", value):
            raise ValueError(r"must validate the regular expression /^(\S+(\s|\S)*\S+|\S)$/")
        return value

    @field_validator('schema_version')
    def schema_version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+(\.\d+)*$", value):
            raise ValueError(r"must validate the regular expression /^\d+(\.\d+)*$/")
        return value

    @field_validator('notes')
    def notes_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\S+(\s|\S)*\S+|\S)$", value):
            raise ValueError(r"must validate the regular expression /^(\S+(\s|\S)*\S+|\S)$/")
        return value

    @field_validator('submitter_comment')
    def submitter_comment_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\S+(\s|\S)*\S+|\S)$", value):
            raise ValueError(r"must validate the regular expression /^(\S+(\s|\S)*\S+|\S)$/")
        return value

    @field_validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\S+(\s|\S)*\S+|\S)$", value):
            raise ValueError(r"must validate the regular expression /^(\S+(\s|\S)*\S+|\S)$/")
        return value

    @field_validator('content_md5sum')
    def content_md5sum_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-f\d]{32}|[A-F\d]{32}", value):
            raise ValueError(r"must validate the regular expression /[a-f\d]{32}|[A-F\d]{32}/")
        return value

    @field_validator('file_format')
    def file_format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['bam']):
            raise ValueError("must be one of enum values ('bam')")
        return value

    @field_validator('md5sum')
    def md5sum_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-f\d]{32}|[A-F\d]{32}", value):
            raise ValueError(r"must validate the regular expression /[a-f\d]{32}|[A-F\d]{32}/")
        return value

    @field_validator('upload_status')
    def upload_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['pending', 'file not found', 'invalidated', 'validated']):
            raise ValueError("must be one of enum values ('pending', 'file not found', 'invalidated', 'validated')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AlignmentFile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlignmentFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "controlled_access": obj.get("controlled_access"),
            "anvil_url": obj.get("anvil_url"),
            "transcriptome_annotation": obj.get("transcriptome_annotation"),
            "assembly": obj.get("assembly"),
            "release_timestamp": obj.get("release_timestamp"),
            "reference_files": obj.get("reference_files"),
            "documents": obj.get("documents"),
            "lab": obj.get("lab"),
            "award": obj.get("award"),
            "accession": obj.get("accession"),
            "alternate_accessions": obj.get("alternate_accessions"),
            "collections": obj.get("collections"),
            "status": obj.get("status"),
            "revoke_detail": obj.get("revoke_detail"),
            "schema_version": obj.get("schema_version"),
            "uuid": obj.get("uuid"),
            "notes": obj.get("notes"),
            "aliases": obj.get("aliases"),
            "creation_timestamp": obj.get("creation_timestamp"),
            "submitted_by": obj.get("submitted_by"),
            "submitter_comment": obj.get("submitter_comment"),
            "description": obj.get("description"),
            "analysis_step_version": obj.get("analysis_step_version"),
            "content_md5sum": obj.get("content_md5sum"),
            "content_type": obj.get("content_type"),
            "dbxrefs": obj.get("dbxrefs"),
            "derived_from": obj.get("derived_from"),
            "file_format": obj.get("file_format"),
            "file_format_specifications": obj.get("file_format_specifications"),
            "file_set": obj.get("file_set"),
            "file_size": obj.get("file_size"),
            "md5sum": obj.get("md5sum"),
            "submitted_file_name": obj.get("submitted_file_name"),
            "upload_status": obj.get("upload_status"),
            "validation_error_detail": obj.get("validation_error_detail"),
            "redacted": obj.get("redacted"),
            "filtered": obj.get("filtered"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "summary": obj.get("summary"),
            "integrated_in": obj.get("integrated_in"),
            "input_file_for": obj.get("input_file_for"),
            "gene_list_for": obj.get("gene_list_for"),
            "loci_list_for": obj.get("loci_list_for"),
            "href": obj.get("href"),
            "s3_uri": obj.get("s3_uri"),
            "upload_credentials": obj.get("upload_credentials"),
            "content_summary": obj.get("content_summary")
        })
        return _obj


