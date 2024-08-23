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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PlatformTerm(BaseModel):
    """
    An ontology term from Experimental Factor Ontology (EFO) for platforms and instruments used in assays.
    """ # noqa: E501
    release_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was released.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the metadata object.")
    schema_version: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The version of the JSON schema that the server uses to validate the object.")
    uuid: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with every object.")
    notes: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="DACC internal notes.")
    aliases: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Lab specific identifiers to reference an object.")
    creation_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was created.")
    submitted_by: Optional[StrictStr] = Field(default=None, description="The user who submitted the object.")
    submitter_comment: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Additional information specified by the submitter to be displayed as a comment on the portal.")
    description: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A plain text description of the object.")
    term_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="An ontology term identifier describing a platform.")
    term_name: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Ontology term describing a biological sample, assay, trait, or disease.")
    deprecated_ntr_terms: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="A list of deprecated NTR terms previously associated with this ontology term.")
    is_a: Optional[List[StrictStr]] = Field(default=None, description="A list of ontology terms which are the nearest ancestor to this ontology term.")
    company: Optional[StrictStr] = Field(default=None, description="The company that developed and sells the instrument.")
    sequencing_kits: Optional[List[StrictStr]] = Field(default=None, description="The available sequencing kits for this platform.")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[List[StrictStr]] = Field(default=None, alias="@type")
    summary: Optional[StrictStr] = Field(default=None, description="A summary of the ontology term.")
    name: Optional[StrictStr] = Field(default=None, description="A unique identifier for the ontology term, reformatted from the original term ID.")
    synonyms: Optional[List[StrictStr]] = Field(default=None, description="Synonyms for the term that have been recorded in an ontology.")
    ancestors: Optional[List[StrictStr]] = Field(default=None, description="List of term names of ontological terms that precede the given term in the ontological tree. These ancestor terms are typically more general ontological terms under which the term is classified.")
    ontology: Optional[StrictStr] = Field(default=None, description="The ontology in which the term is recorded.")
    __properties: ClassVar[List[str]] = ["release_timestamp", "status", "schema_version", "uuid", "notes", "aliases", "creation_timestamp", "submitted_by", "submitter_comment", "description", "term_id", "term_name", "deprecated_ntr_terms", "is_a", "company", "sequencing_kits", "@id", "@type", "summary", "name", "synonyms", "ancestors", "ontology"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['archived', 'deleted', 'in progress', 'released']):
            raise ValueError("must be one of enum values ('archived', 'deleted', 'in progress', 'released')")
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

    @field_validator('term_id')
    def term_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(EFO|NTR):[0-9]{2,8}$", value):
            raise ValueError(r"must validate the regular expression /^(EFO|NTR):[0-9]{2,8}$/")
        return value

    @field_validator('term_name')
    def term_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(?![\s\"\'])[\S|\s]*[^\s\"\']$", value):
            raise ValueError(r"must validate the regular expression /^(?![\s\"'])[\S|\s]*[^\s\"']$/")
        return value

    @field_validator('company')
    def company_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['10X Genomics', 'Illumina', 'Life Technologies', 'Oxford Nanopore Technologies', 'Pacific Biosciences', 'Parse Biosciences', 'Roche']):
            raise ValueError("must be one of enum values ('10X Genomics', 'Illumina', 'Life Technologies', 'Oxford Nanopore Technologies', 'Pacific Biosciences', 'Parse Biosciences', 'Roche')")
        return value

    @field_validator('sequencing_kits')
    def sequencing_kits_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['HiSeq SBS Kit v4', 'HiSeq SR Cluster Kit v4-cBot-HS', 'HiSeq PE Cluster Kit v4-cBot-HS', 'HiSeq SR Rapid Cluster Kit v2', 'HiSeq PE Rapid Cluster Kit v2', 'HiSeq Rapid SBS Kit v2', 'HiSeq 3000/4000 SBS Kit', 'HiSeq 3000/4000 SR Cluster Kit', 'HiSeq 3000/4000 PE Cluster Kit', 'MiSeq Reagent Kit v2', 'NextSeq 500 Mid Output Kit', 'NextSeq 500 High Output Kit', 'NextSeq 500 Mid Output v2 Kit', 'NextSeq 500 High Output v2 Kit', 'NextSeq 500/550 Mid-Output v2.5 Kit', 'NextSeq 500/550 High-Output v2.5 Kit', 'TG NextSeq 500/550 Mid-Output Kit v2.5', 'TG NextSeq 500/550 High-Output Kit v2.5', 'NextSeq 1000/2000 P1 Reagent Kit', 'NextSeq 1000/2000 P2 Reagent Kit', 'NextSeq 1000/2000 P3 Reagent Kit', 'NextSeq 1000/2000 P1 XLEAP-SBS Reagent Kit', 'NextSeq 1000/2000 P2 XLEAP-SBS Reagent Kit', 'NextSeq 2000 P3 XLEAP-SBS Reagent Kit', 'NextSeq 2000 P4 XLEAP-SBS Reagent Kit', 'NovaSeq 6000 SP Reagent Kit v1.5', 'NovaSeq 6000 S1 Reagent Kit v1.5', 'NovaSeq 6000 S2 Reagent Kit v1.5', 'NovaSeq 6000 S4 Reagent Kit v1.5', 'NovaSeq X Series 1.5B Reagent Kit', 'NovaSeq X Series 10B Reagent Kit', 'NovaSeq X Series 25B Reagent Kit', 'ONT Ligation Sequencing Kit V14', 'Sequel sequencing kit 3.0', 'Sequel II sequencing kit 2.0']):
                raise ValueError("each list item must be one of ('HiSeq SBS Kit v4', 'HiSeq SR Cluster Kit v4-cBot-HS', 'HiSeq PE Cluster Kit v4-cBot-HS', 'HiSeq SR Rapid Cluster Kit v2', 'HiSeq PE Rapid Cluster Kit v2', 'HiSeq Rapid SBS Kit v2', 'HiSeq 3000/4000 SBS Kit', 'HiSeq 3000/4000 SR Cluster Kit', 'HiSeq 3000/4000 PE Cluster Kit', 'MiSeq Reagent Kit v2', 'NextSeq 500 Mid Output Kit', 'NextSeq 500 High Output Kit', 'NextSeq 500 Mid Output v2 Kit', 'NextSeq 500 High Output v2 Kit', 'NextSeq 500/550 Mid-Output v2.5 Kit', 'NextSeq 500/550 High-Output v2.5 Kit', 'TG NextSeq 500/550 Mid-Output Kit v2.5', 'TG NextSeq 500/550 High-Output Kit v2.5', 'NextSeq 1000/2000 P1 Reagent Kit', 'NextSeq 1000/2000 P2 Reagent Kit', 'NextSeq 1000/2000 P3 Reagent Kit', 'NextSeq 1000/2000 P1 XLEAP-SBS Reagent Kit', 'NextSeq 1000/2000 P2 XLEAP-SBS Reagent Kit', 'NextSeq 2000 P3 XLEAP-SBS Reagent Kit', 'NextSeq 2000 P4 XLEAP-SBS Reagent Kit', 'NovaSeq 6000 SP Reagent Kit v1.5', 'NovaSeq 6000 S1 Reagent Kit v1.5', 'NovaSeq 6000 S2 Reagent Kit v1.5', 'NovaSeq 6000 S4 Reagent Kit v1.5', 'NovaSeq X Series 1.5B Reagent Kit', 'NovaSeq X Series 10B Reagent Kit', 'NovaSeq X Series 25B Reagent Kit', 'ONT Ligation Sequencing Kit V14', 'Sequel sequencing kit 3.0', 'Sequel II sequencing kit 2.0')")
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
        """Create an instance of PlatformTerm from a JSON string"""
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
        """Create an instance of PlatformTerm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "release_timestamp": obj.get("release_timestamp"),
            "status": obj.get("status"),
            "schema_version": obj.get("schema_version"),
            "uuid": obj.get("uuid"),
            "notes": obj.get("notes"),
            "aliases": obj.get("aliases"),
            "creation_timestamp": obj.get("creation_timestamp"),
            "submitted_by": obj.get("submitted_by"),
            "submitter_comment": obj.get("submitter_comment"),
            "description": obj.get("description"),
            "term_id": obj.get("term_id"),
            "term_name": obj.get("term_name"),
            "deprecated_ntr_terms": obj.get("deprecated_ntr_terms"),
            "is_a": obj.get("is_a"),
            "company": obj.get("company"),
            "sequencing_kits": obj.get("sequencing_kits"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "summary": obj.get("summary"),
            "name": obj.get("name"),
            "synonyms": obj.get("synonyms"),
            "ancestors": obj.get("ancestors"),
            "ontology": obj.get("ontology")
        })
        return _obj


