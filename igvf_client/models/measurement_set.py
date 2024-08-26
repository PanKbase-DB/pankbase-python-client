# coding: utf-8

"""
    IGVF Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 46.1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class MeasurementSet(BaseModel):
    """
    Measurement set is a file set that hosts raw data files (e.g. FASTQs) resulting from sequencing of a library prepared from the nucleic acids of the sample that is the main target of the assay. For example sequencing of accessible regions in the genome, or sequencing of the transcriptome of the sample. The assay can either be bulk or single cell type. The sample specific raw sequencing results will be captured in the measurement sets. The files in the measurement sets are specific to the sample being investigated. See auxiliary sets for files that are not a direct result of sequencing the sample under investigation.
    """ # noqa: E501
    release_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was released.")
    publications: Optional[List[StrictStr]] = Field(default=None, description="The publications associated with this object.")
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
    dbxrefs: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Identifiers from external resources that may have 1-to-1 or 1-to-many relationships with IGVF file sets.")
    samples: Optional[List[StrictStr]] = Field(default=None, description="The sample(s) associated with this file set.")
    donors: Optional[List[StrictStr]] = Field(default=None, description="The donors of the samples associated with this measurement set.")
    file_set_type: Optional[StrictStr] = Field(default=None, description="The category that best describes this measurement set.")
    assay_term: Optional[StrictStr] = Field(default=None, description="The assay used to produce data in this measurement set.")
    protocols: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Links to the protocol(s) for conducting the assay on Protocols.io.")
    preferred_assay_title: Optional[StrictStr] = Field(default=None, description="The custom lab preferred label for the experiment performed in this measurement set.")
    multiome_size: Optional[Annotated[int, Field(strict=True, ge=2)]] = Field(default=None, description="The number of datasets included in the multiome experiment this measurement set is a part of.")
    control_file_sets: Optional[List[StrictStr]] = Field(default=None, description="File sets that can serve as scientific controls for this measurement_set.")
    sequencing_library_types: Optional[List[StrictStr]] = Field(default=None, description="Description of the libraries sequenced in this measurement set.")
    auxiliary_sets: Optional[List[StrictStr]] = Field(default=None, description="The auxiliary sets of files produced alongside raw data from this measurement set.")
    external_image_url: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Links to the external site where images produced by this measurement are stored.")
    targeted_genes: Optional[List[StrictStr]] = Field(default=None, description="A list of genes targeted in this assay. For example, TF ChIP-seq attempts to identify binding sites of a protein encoded by a specific gene. In CRISPR FlowFISH, the modified samples are sorted based on expression of a specific gene. This property differs from small_scale_gene_list in Construct Library Set, which describes genes targeted by the content integrated in the constructs (such as guide RNAs.)")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[List[StrictStr]] = Field(default=None, alias="@type")
    summary: Optional[StrictStr] = None
    files: Optional[List[StrictStr]] = Field(default=None, description="The files associated with this file set.")
    control_for: Optional[List[StrictStr]] = Field(default=None, description="The file sets for which this file set is a control.")
    submitted_files_timestamp: Optional[StrictStr] = Field(default=None, description="The timestamp the first file object in the file_set or associated auxiliary sets was created.")
    input_file_set_for: Optional[List[StrictStr]] = Field(default=None, description="The file sets that use this file set as an input.")
    related_multiome_datasets: Optional[List[StrictStr]] = Field(default=None, description="Related datasets included in the multiome experiment this measurement set is a part of.")
    __properties: ClassVar[List[str]] = ["release_timestamp", "publications", "documents", "lab", "award", "accession", "alternate_accessions", "collections", "status", "revoke_detail", "schema_version", "uuid", "notes", "aliases", "creation_timestamp", "submitted_by", "submitter_comment", "description", "dbxrefs", "samples", "donors", "file_set_type", "assay_term", "protocols", "preferred_assay_title", "multiome_size", "control_file_sets", "sequencing_library_types", "auxiliary_sets", "external_image_url", "targeted_genes", "@id", "@type", "summary", "files", "control_for", "submitted_files_timestamp", "input_file_set_for", "related_multiome_datasets"]

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

    @field_validator('file_set_type')
    def file_set_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['experimental data']):
            raise ValueError("must be one of enum values ('experimental data')")
        return value

    @field_validator('preferred_assay_title')
    def preferred_assay_title_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['10x multiome', '10x multiome with MULTI-seq', 'AAV-MPRA', 'ATAC-seq', 'CERES-seq', 'Cell painting', 'CRISPR FlowFISH', 'DOGMA-seq', 'Histone ChIP-seq', 'Hi-C', 'HT-recruit', 'lentiMPRA', 'MERFISH', 'MIAA', 'mN2H', 'MPRA', 'MPRA (scQer)', 'MULTI-seq', 'Parse SPLiT-seq', 'Perturb-seq', 'RNA-seq', 'SGE', 'scATAC-seq', 'scNT-seq', 'scNT-seq2', 'scRNA-seq', 'semi-qY2H', 'SHARE-seq', 'smFISH', 'snATAC-seq', 'snmC-Seq2', 'snMCT-seq', 'snM3C-seq', 'snRNA-seq', 'Spatial transcriptomics', 'SUPERSTARR', 'TAP-seq', 'TF ChIP-seq', 'VAMP-seq', 'Variant FlowFISH', 'Variant painting', 'Y2H', 'yN2H']):
            raise ValueError("must be one of enum values ('10x multiome', '10x multiome with MULTI-seq', 'AAV-MPRA', 'ATAC-seq', 'CERES-seq', 'Cell painting', 'CRISPR FlowFISH', 'DOGMA-seq', 'Histone ChIP-seq', 'Hi-C', 'HT-recruit', 'lentiMPRA', 'MERFISH', 'MIAA', 'mN2H', 'MPRA', 'MPRA (scQer)', 'MULTI-seq', 'Parse SPLiT-seq', 'Perturb-seq', 'RNA-seq', 'SGE', 'scATAC-seq', 'scNT-seq', 'scNT-seq2', 'scRNA-seq', 'semi-qY2H', 'SHARE-seq', 'smFISH', 'snATAC-seq', 'snmC-Seq2', 'snMCT-seq', 'snM3C-seq', 'snRNA-seq', 'Spatial transcriptomics', 'SUPERSTARR', 'TAP-seq', 'TF ChIP-seq', 'VAMP-seq', 'Variant FlowFISH', 'Variant painting', 'Y2H', 'yN2H')")
        return value

    @field_validator('sequencing_library_types')
    def sequencing_library_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['direct RNA', 'exome capture', 'mRNA enriched', 'rRNA depleted', 'polyA depleted', 'polyA enriched']):
                raise ValueError("each list item must be one of ('direct RNA', 'exome capture', 'mRNA enriched', 'rRNA depleted', 'polyA depleted', 'polyA enriched')")
        return value

    @field_validator('external_image_url')
    def external_image_url_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^https:\/\/cellpainting-gallery\.s3\.amazonaws\.com(\S+)$", value):
            raise ValueError(r"must validate the regular expression /^https:\/\/cellpainting-gallery\.s3\.amazonaws\.com(\S+)$/")
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
        """Create an instance of MeasurementSet from a JSON string"""
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
        """Create an instance of MeasurementSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "release_timestamp": obj.get("release_timestamp"),
            "publications": obj.get("publications"),
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
            "dbxrefs": obj.get("dbxrefs"),
            "samples": obj.get("samples"),
            "donors": obj.get("donors"),
            "file_set_type": obj.get("file_set_type"),
            "assay_term": obj.get("assay_term"),
            "protocols": obj.get("protocols"),
            "preferred_assay_title": obj.get("preferred_assay_title"),
            "multiome_size": obj.get("multiome_size"),
            "control_file_sets": obj.get("control_file_sets"),
            "sequencing_library_types": obj.get("sequencing_library_types"),
            "auxiliary_sets": obj.get("auxiliary_sets"),
            "external_image_url": obj.get("external_image_url"),
            "targeted_genes": obj.get("targeted_genes"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "summary": obj.get("summary"),
            "files": obj.get("files"),
            "control_for": obj.get("control_for"),
            "submitted_files_timestamp": obj.get("submitted_files_timestamp"),
            "input_file_set_for": obj.get("input_file_set_for"),
            "related_multiome_datasets": obj.get("related_multiome_datasets")
        })
        return _obj


