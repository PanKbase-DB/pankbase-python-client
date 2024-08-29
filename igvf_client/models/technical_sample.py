# coding: utf-8

"""
    IGVF Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 47.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class TechnicalSample(BaseModel):
    """
    A sample that is used as a medium to perform biological measurement without the intent to characterize the technical sample itself. For example, the solution in which RNA oligos binding experiments are performed.
    """ # noqa: E501
    release_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was released.")
    publications: Optional[List[StrictStr]] = Field(default=None, description="The publications associated with this object.")
    url: Optional[StrictStr] = Field(default=None, description="An external resource with additional information.")
    sources: Optional[List[StrictStr]] = Field(default=None, description="The originating lab(s) or vendor(s).")
    lot_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The lot identifier provided by the originating lab or vendor.")
    product_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The product identifier provided by the originating lab or vendor.")
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
    starting_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The initial quantity of samples obtained.")
    starting_amount_units: Optional[StrictStr] = Field(default=None, description="The units used to quantify the amount of samples obtained.")
    dbxrefs: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Biosample identifiers from external resources, such as Biosample database or Cellosaurus.")
    date_obtained: Optional[StrictStr] = Field(default=None, description="The date the sample was harvested, dissected or created, depending on the type of the sample.")
    sorted_from: Optional[StrictStr] = Field(default=None, description="Links to a larger sample from which this sample was obtained through sorting.")
    sorted_from_detail: Optional[StrictStr] = Field(default=None, description="Detail for sample sorted into fractions capturing information about sorting.")
    virtual: Optional[StrictBool] = Field(default=None, description="Virtual samples are not representing actual physical entities from experiments, but rather capturing metadata about hypothetical samples that the reported analysis results are relevant for.")
    construct_library_sets: Optional[List[StrictStr]] = Field(default=None, description="The construct library sets of vectors introduced to this sample prior to performing an assay.")
    moi: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The actual multiplicity of infection (MOI) for vectors introduced to this sample. At least one construct library set must be specified in order to specify MOI. This property should capture the actual MOI, and not the targeted MOI.")
    nucleic_acid_delivery: Optional[StrictStr] = Field(default=None, description="Method of introduction of nucleic acid into the cell.")
    time_post_library_delivery: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The time that elapsed past the time-point when the construct library sets were introduced.")
    time_post_library_delivery_units: Optional[StrictStr] = Field(default=None, description="The units of time that elapsed past the point when the construct library sets were introduced.")
    protocols: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Links to the protocol(s) for preparing the samples on Protocols.io.")
    sample_material: Optional[StrictStr] = None
    taxa: Optional[StrictStr] = None
    sample_terms: Optional[List[StrictStr]] = Field(default=None, description="Ontology terms identifying a technical sample.")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[List[StrictStr]] = Field(default=None, alias="@type")
    summary: Optional[StrictStr] = Field(default=None, description="A summary of this sample.")
    file_sets: Optional[List[StrictStr]] = Field(default=None, description="The file sets linked to this sample.")
    multiplexed_in: Optional[List[StrictStr]] = Field(default=None, description="The multiplexed samples in which this sample is included.")
    sorted_fractions: Optional[List[StrictStr]] = Field(default=None, description="The fractions into which this sample has been sorted.")
    origin_of: Optional[List[StrictStr]] = Field(default=None, description="The samples which originate from this sample, such as through a process of cell differentiation.")
    institutional_certificates: Optional[List[StrictStr]] = Field(default=None, description="The institutional certificates under which use of this sample is approved.")
    classifications: Optional[List[StrictStr]] = Field(default=None, description="The general category of this type of sample.")
    __properties: ClassVar[List[str]] = ["release_timestamp", "publications", "url", "sources", "lot_id", "product_id", "documents", "lab", "award", "accession", "alternate_accessions", "collections", "status", "revoke_detail", "schema_version", "uuid", "notes", "aliases", "creation_timestamp", "submitted_by", "submitter_comment", "description", "starting_amount", "starting_amount_units", "dbxrefs", "date_obtained", "sorted_from", "sorted_from_detail", "virtual", "construct_library_sets", "moi", "nucleic_acid_delivery", "time_post_library_delivery", "time_post_library_delivery_units", "protocols", "sample_material", "taxa", "sample_terms", "@id", "@type", "summary", "file_sets", "multiplexed_in", "sorted_fractions", "origin_of", "institutional_certificates", "classifications"]

    @field_validator('lot_id')
    def lot_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\S+(\s|\S)*\S+|\S)$", value):
            raise ValueError(r"must validate the regular expression /^(\S+(\s|\S)*\S+|\S)$/")
        return value

    @field_validator('product_id')
    def product_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\S+(\s|\S)*\S+|\S)$", value):
            raise ValueError(r"must validate the regular expression /^(\S+(\s|\S)*\S+|\S)$/")
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

    @field_validator('starting_amount_units')
    def starting_amount_units_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['cells', 'cells/ml', 'g', 'items', 'mg', 'whole animals', 'whole embryos', 'μg', 'ng']):
            raise ValueError("must be one of enum values ('cells', 'cells/ml', 'g', 'items', 'mg', 'whole animals', 'whole embryos', 'μg', 'ng')")
        return value

    @field_validator('nucleic_acid_delivery')
    def nucleic_acid_delivery_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['transfection', 'adenoviral transduction', 'lentiviral transduction']):
            raise ValueError("must be one of enum values ('transfection', 'adenoviral transduction', 'lentiviral transduction')")
        return value

    @field_validator('time_post_library_delivery_units')
    def time_post_library_delivery_units_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['minute', 'hour', 'day', 'week', 'month']):
            raise ValueError("must be one of enum values ('minute', 'hour', 'day', 'week', 'month')")
        return value

    @field_validator('sample_material')
    def sample_material_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['undefined', 'inorganic', 'synthetic', 'organic']):
            raise ValueError("must be one of enum values ('undefined', 'inorganic', 'synthetic', 'organic')")
        return value

    @field_validator('taxa')
    def taxa_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Saccharomyces cerevisiae', 'Homo sapiens']):
            raise ValueError("must be one of enum values ('Saccharomyces cerevisiae', 'Homo sapiens')")
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
        """Create an instance of TechnicalSample from a JSON string"""
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
        """Create an instance of TechnicalSample from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "release_timestamp": obj.get("release_timestamp"),
            "publications": obj.get("publications"),
            "url": obj.get("url"),
            "sources": obj.get("sources"),
            "lot_id": obj.get("lot_id"),
            "product_id": obj.get("product_id"),
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
            "starting_amount": obj.get("starting_amount"),
            "starting_amount_units": obj.get("starting_amount_units"),
            "dbxrefs": obj.get("dbxrefs"),
            "date_obtained": obj.get("date_obtained"),
            "sorted_from": obj.get("sorted_from"),
            "sorted_from_detail": obj.get("sorted_from_detail"),
            "virtual": obj.get("virtual"),
            "construct_library_sets": obj.get("construct_library_sets"),
            "moi": obj.get("moi"),
            "nucleic_acid_delivery": obj.get("nucleic_acid_delivery"),
            "time_post_library_delivery": obj.get("time_post_library_delivery"),
            "time_post_library_delivery_units": obj.get("time_post_library_delivery_units"),
            "protocols": obj.get("protocols"),
            "sample_material": obj.get("sample_material"),
            "taxa": obj.get("taxa"),
            "sample_terms": obj.get("sample_terms"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "summary": obj.get("summary"),
            "file_sets": obj.get("file_sets"),
            "multiplexed_in": obj.get("multiplexed_in"),
            "sorted_fractions": obj.get("sorted_fractions"),
            "origin_of": obj.get("origin_of"),
            "institutional_certificates": obj.get("institutional_certificates"),
            "classifications": obj.get("classifications")
        })
        return _obj


