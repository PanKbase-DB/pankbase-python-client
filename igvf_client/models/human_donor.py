# coding: utf-8

"""
    PanKbase Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 41.0.0
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

class HumanDonor(BaseModel):
    """
    A human donor of any biosample, including cell lines. Submission of any sample originating from a human donor requires submission of information about the relevant donor. For example, submission of the donor of K562 is a prerequisite for submission of any K562 cell line samples. The following fields are **required**: `award`, `lab`, `rrid`, `living_donor`, `bmi`, `diabetes_status`, `diabetes_status_description`, and `taxa`. These fields must be included for the schema to be valid. Additionally, the following fields are **desired**: `center_donor_id`, `ethnicities`, `hba1c`, `diabetes_status_hba1c`, `glucose_loweing_theraphy`, `hospital_stay`, `donation_type`, and `cause_of_death`. While these fields are not mandatory, their inclusion is highly recommended for a more comprehensive data submission.
    """ # noqa: E501
    release_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was released.")
    taxa: Optional[StrictStr] = Field(default=None, description="The species of the organism.")
    publication_identifiers: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="The publication identifiers that provide more information about the object.")
    url: Optional[StrictStr] = Field(default=None, description="An external resource with additional information.")
    documents: Optional[List[StrictStr]] = Field(default=None, description="Documents that provide additional information (not data file).")
    lab: Optional[StrictStr] = Field(default=None, description="Lab associated with the submission.")
    award: Optional[StrictStr] = Field(default=None, description="Grant associated with the submission.")
    accession: Optional[StrictStr] = Field(default=None, description="A unique identifier to be used to reference the object prefixed with PKB.")
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
    dbxrefs: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Identifiers from external resources that may have 1-to-1 or 1-to-many relationships with IGVF donors.")
    sex: Optional[StrictStr] = Field(default=None, description="Self-Reported sex of the donor.")
    phenotypic_features: Optional[List[StrictStr]] = Field(default=None, description="A list of associated phenotypic features of the donor.")
    virtual: Optional[StrictBool] = Field(default=None, description="Virtual donors are not representing actual human or model organism donors, samples coming from which were used in experiments, but rather capturing metadata about hypothetical donors that the reported analysis results are relevant for.")
    ethnicities: Optional[List[StrictStr]] = Field(default=None, description="Self-Reported Ethnicity of the donor.")
    genetic_ethnicities: Optional[List[StrictStr]] = Field(default=None, description="Inferred ancestry of the donor from genetic analysis")
    living_donor: Optional[StrictBool] = Field(default=None, description="Living Donor")
    family_history_of_diabetes: Optional[StrictStr] = Field(default=None, description="Family History of Diabetes")
    family_history_of_diabetes_relationship: Optional[List[StrictStr]] = Field(default=None, description="Family History of Diabetes Relationship.")
    rrid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Research Unique Identifier. PanKbase will only take donors with RRID")
    pancreas_tissue_available: Optional[StrictBool] = Field(default=None, description="Pancreas tissue is available for research or analysis")
    center_donor_id: Optional[StrictStr] = Field(default=None, description="Donor center ID identifier for cross-referencing")
    biological_sex: Optional[StrictStr] = Field(default=None, description="Inferred biological sex derived from genomic data")
    age: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Age in years")
    bmi: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Body mass index (Kg/m2)")
    diabetes_duration: Optional[StrictStr] = Field(default=None, description="Diabetes Duration in years")
    diabetes_status: Optional[List[StrictStr]] = Field(default=None, description="Diabetes status T1D,T2D,MODY, etc. MONDO ontology term")
    diabetes_status_description: Optional[StrictStr] = Field(default=None, description="Description of diabetes status")
    hba1c: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The percentage measurement of HbA1c, which reflects the average blood glucose levels over the past 2-3 months.  If not available, 'NA'")
    diabetes_status_hba1c: Optional[StrictStr] = Field(default=None, description="A categorization of diabetes status based on adjusted HbA1C levels, considering factors such as age, race, or other clinical conditions that might influence HbA1C measurements")
    donation_type: Optional[StrictStr] = Field(default=None, description="The type of organ donation, categorized as DCD, NDD, or MAID")
    cause_of_death: Optional[StrictStr] = Field(default=None, description="The primary medical condition or event that led to the patient’s death")
    c_peptide: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The concentration of C-Peptide in the blood, a marker used to assess insulin production and pancreatic function")
    aab_gada: Optional[StrictBool] = Field(default=None, description="The presence of Autoantibodies against GADA")
    aab_gada_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="AAB GADA value (unit/ml)")
    aab_ia2: Optional[StrictBool] = Field(default=None, description="The presence of Autoantibodies against IA2")
    aab_ia2_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="AAB IA2 value (unit/ml)")
    aab_znt8: Optional[StrictBool] = Field(default=None, description="The presence of Autoantibodies against ZNT8")
    aab_znt8_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="AAB ZNT8 value (unit/ml)")
    hla_typing: Optional[List[StrictStr]] = Field(default=None, description="Series of comma-separated values describing HLA types as: class, locus, allele1, allele2, method")
    other_tissues_available: Optional[List[StrictStr]] = Field(default=None, description="Tissues obtained from the donor")
    hospital_stay: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total number of days the patient was hospitalized")
    glucose_loweing_theraphy: Optional[List[StrictStr]] = Field(default=None, description="Details the type of therapy or medication regimen the patient is on to manage blood glucose levels, including oral medications, insulin, or other treatments.")
    human_donor_identifiers: Optional[List[StrictStr]] = Field(default=None, description="Identifiers of this human donor.")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[List[StrictStr]] = Field(default=None, alias="@type")
    summary: Optional[StrictStr] = Field(default=None, description="A summary of the human donor.")
    __properties: ClassVar[List[str]] = ["release_timestamp", "taxa", "publication_identifiers", "url", "documents", "lab", "award", "accession", "alternate_accessions", "collections", "status", "revoke_detail", "schema_version", "uuid", "notes", "aliases", "creation_timestamp", "submitted_by", "submitter_comment", "description", "dbxrefs", "sex", "phenotypic_features", "virtual", "ethnicities", "genetic_ethnicities", "living_donor", "family_history_of_diabetes", "family_history_of_diabetes_relationship", "rrid", "pancreas_tissue_available", "center_donor_id", "biological_sex", "age", "bmi", "diabetes_duration", "diabetes_status", "diabetes_status_description", "hba1c", "diabetes_status_hba1c", "donation_type", "cause_of_death", "c_peptide", "aab_gada", "aab_gada_value", "aab_ia2", "aab_ia2_value", "aab_znt8", "aab_znt8_value", "hla_typing", "other_tissues_available", "hospital_stay", "glucose_loweing_theraphy", "human_donor_identifiers", "@id", "@type", "summary"]

    @field_validator('taxa')
    def taxa_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Homo sapiens']):
            raise ValueError("must be one of enum values ('Homo sapiens')")
        return value

    @field_validator('collections')
    def collections_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ClinGen', 'ENCODE', 'GREGoR', 'IGVF_catalog_beta_v0.1', 'IGVF_catalog_beta_v0.2', 'IGVF_catalog_beta_v0.3', 'IGVF_catalog_beta_v0.4', 'MaveDB', 'IIDP', 'HPAP', 'PanKbase', 'IsletCore', 'MPRAbase', 'Vista']):
                raise ValueError("each list item must be one of ('ClinGen', 'ENCODE', 'GREGoR', 'IGVF_catalog_beta_v0.1', 'IGVF_catalog_beta_v0.2', 'IGVF_catalog_beta_v0.3', 'IGVF_catalog_beta_v0.4', 'MaveDB', 'IIDP', 'HPAP', 'PanKbase', 'IsletCore', 'MPRAbase', 'Vista')")
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

    @field_validator('sex')
    def sex_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['male', 'female', 'other']):
            raise ValueError("must be one of enum values ('male', 'female', 'other')")
        return value

    @field_validator('ethnicities')
    def ethnicities_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['African American', 'African Caribbean', 'Arab', 'Asian', 'Black', 'Black African', 'Caucasian', 'Chinese', 'Colombian', 'Dai Chinese', 'Esan', 'Eskimo', 'European', 'Gambian', 'Han Chinese', 'Hispanic', 'Indian', 'Japanese', 'Kinh Vietnamese', 'Luhya', 'Maasai', 'Mende', 'Native Hawaiian', 'Pacific Islander', 'Puerto Rican', 'Yoruba']):
                raise ValueError("each list item must be one of ('African American', 'African Caribbean', 'Arab', 'Asian', 'Black', 'Black African', 'Caucasian', 'Chinese', 'Colombian', 'Dai Chinese', 'Esan', 'Eskimo', 'European', 'Gambian', 'Han Chinese', 'Hispanic', 'Indian', 'Japanese', 'Kinh Vietnamese', 'Luhya', 'Maasai', 'Mende', 'Native Hawaiian', 'Pacific Islander', 'Puerto Rican', 'Yoruba')")
        return value

    @field_validator('genetic_ethnicities')
    def genetic_ethnicities_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['African American', 'African Caribbean', 'Arab', 'Asian', 'Black', 'Black African', 'Caucasian', 'Chinese', 'Colombian', 'Dai Chinese', 'Esan', 'Eskimo', 'European', 'Gambian', 'Han Chinese', 'Hispanic', 'Indian', 'Japanese', 'Kinh Vietnamese', 'Luhya', 'Maasai', 'Mende', 'Native Hawaiian', 'Pacific Islander', 'Puerto Rican', 'Yoruba']):
                raise ValueError("each list item must be one of ('African American', 'African Caribbean', 'Arab', 'Asian', 'Black', 'Black African', 'Caucasian', 'Chinese', 'Colombian', 'Dai Chinese', 'Esan', 'Eskimo', 'European', 'Gambian', 'Han Chinese', 'Hispanic', 'Indian', 'Japanese', 'Kinh Vietnamese', 'Luhya', 'Maasai', 'Mende', 'Native Hawaiian', 'Pacific Islander', 'Puerto Rican', 'Yoruba')")
        return value

    @field_validator('family_history_of_diabetes')
    def family_history_of_diabetes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true', 'false', 'NA', 'unknown']):
            raise ValueError("must be one of enum values ('true', 'false', 'NA', 'unknown')")
        return value

    @field_validator('rrid')
    def rrid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^RRID:[A-Z]{4}\d{8}$", value):
            raise ValueError(r"must validate the regular expression /^RRID:[A-Z]{4}\d{8}$/")
        return value

    @field_validator('biological_sex')
    def biological_sex_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['male', 'female']):
            raise ValueError("must be one of enum values ('male', 'female')")
        return value

    @field_validator('diabetes_status_description')
    def diabetes_status_description_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['type 1 diabetes', 'type 2 diabetes', 'gestational diabetes', 'maturity onset diabetes of the young (MODY)', 'neonatal diabetes', 'wolfram syndrome', 'alström syndrome', 'latent autoimmune diabetes in adults (LADA)', 'type 3c diabetes', 'steroid-induced diabetes', 'cystic fibrosis diabetes', 'non-diabetic']):
            raise ValueError("must be one of enum values ('type 1 diabetes', 'type 2 diabetes', 'gestational diabetes', 'maturity onset diabetes of the young (MODY)', 'neonatal diabetes', 'wolfram syndrome', 'alström syndrome', 'latent autoimmune diabetes in adults (LADA)', 'type 3c diabetes', 'steroid-induced diabetes', 'cystic fibrosis diabetes', 'non-diabetic')")
        return value

    @field_validator('diabetes_status_hba1c')
    def diabetes_status_hba1c_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['type 1 diabetes', 'type 2 diabetes', 'gestational diabetes', 'maturity onset diabetes of the young (MODY)', 'neonatal diabetes', 'wolfram syndrome', 'alström syndrome', 'latent autoimmune diabetes in adults (LADA)', 'type 3c diabetes', 'steroid-induced diabetes', 'cystic fibrosis diabetes', 'non-diabetic']):
            raise ValueError("must be one of enum values ('type 1 diabetes', 'type 2 diabetes', 'gestational diabetes', 'maturity onset diabetes of the young (MODY)', 'neonatal diabetes', 'wolfram syndrome', 'alström syndrome', 'latent autoimmune diabetes in adults (LADA)', 'type 3c diabetes', 'steroid-induced diabetes', 'cystic fibrosis diabetes', 'non-diabetic')")
        return value

    @field_validator('donation_type')
    def donation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DCD', 'DBD', 'NDD', 'MAID']):
            raise ValueError("must be one of enum values ('DCD', 'DBD', 'NDD', 'MAID')")
        return value

    @field_validator('glucose_loweing_theraphy')
    def glucose_loweing_theraphy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Oral medications', 'Insulin', 'Other treatment', 'Metformin', 'Glipizide', 'Glimeperide', 'Ozempic', 'Pills of unknown name', 'Lantus', 'Trulicity', 'Oral meds', 'Unknown pills', 'Glyxambi', 'Unknown medication', 'Unknown', 'No treatment', 'NA']):
                raise ValueError("each list item must be one of ('Oral medications', 'Insulin', 'Other treatment', 'Metformin', 'Glipizide', 'Glimeperide', 'Ozempic', 'Pills of unknown name', 'Lantus', 'Trulicity', 'Oral meds', 'Unknown pills', 'Glyxambi', 'Unknown medication', 'Unknown', 'No treatment', 'NA')")
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
        """Create an instance of HumanDonor from a JSON string"""
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
        """Create an instance of HumanDonor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "release_timestamp": obj.get("release_timestamp"),
            "taxa": obj.get("taxa"),
            "publication_identifiers": obj.get("publication_identifiers"),
            "url": obj.get("url"),
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
            "sex": obj.get("sex"),
            "phenotypic_features": obj.get("phenotypic_features"),
            "virtual": obj.get("virtual"),
            "ethnicities": obj.get("ethnicities"),
            "genetic_ethnicities": obj.get("genetic_ethnicities"),
            "living_donor": obj.get("living_donor"),
            "family_history_of_diabetes": obj.get("family_history_of_diabetes"),
            "family_history_of_diabetes_relationship": obj.get("family_history_of_diabetes_relationship"),
            "rrid": obj.get("rrid"),
            "pancreas_tissue_available": obj.get("pancreas_tissue_available"),
            "center_donor_id": obj.get("center_donor_id"),
            "biological_sex": obj.get("biological_sex"),
            "age": obj.get("age"),
            "bmi": obj.get("bmi"),
            "diabetes_duration": obj.get("diabetes_duration"),
            "diabetes_status": obj.get("diabetes_status"),
            "diabetes_status_description": obj.get("diabetes_status_description"),
            "hba1c": obj.get("hba1c"),
            "diabetes_status_hba1c": obj.get("diabetes_status_hba1c"),
            "donation_type": obj.get("donation_type"),
            "cause_of_death": obj.get("cause_of_death"),
            "c_peptide": obj.get("c_peptide"),
            "aab_gada": obj.get("aab_gada"),
            "aab_gada_value": obj.get("aab_gada_value"),
            "aab_ia2": obj.get("aab_ia2"),
            "aab_ia2_value": obj.get("aab_ia2_value"),
            "aab_znt8": obj.get("aab_znt8"),
            "aab_znt8_value": obj.get("aab_znt8_value"),
            "hla_typing": obj.get("hla_typing"),
            "other_tissues_available": obj.get("other_tissues_available"),
            "hospital_stay": obj.get("hospital_stay"),
            "glucose_loweing_theraphy": obj.get("glucose_loweing_theraphy"),
            "human_donor_identifiers": obj.get("human_donor_identifiers"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "summary": obj.get("summary")
        })
        return _obj


