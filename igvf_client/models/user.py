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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    A user of IGVF data portal who is a member or affiliate member of IGVF.
    """ # noqa: E501
    status: Optional[StrictStr] = Field(default=None, description="The status of the metadata object.")
    schema_version: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The version of the JSON schema that the server uses to validate the object.")
    uuid: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with every object.")
    notes: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="DACC internal notes.")
    aliases: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Lab specific identifiers to reference an object.")
    creation_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was created.")
    submitted_by: Optional[StrictStr] = Field(default=None, description="The user who submitted the object.")
    submitter_comment: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Additional information specified by the submitter to be displayed as a comment on the portal.")
    description: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A plain text description of the object.")
    email: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The email associated with the user's account.")
    first_name: Optional[StrictStr] = Field(default=None, description="The user's first (given) name.")
    last_name: Optional[StrictStr] = Field(default=None, description="The user's last (family) name.")
    lab: Optional[StrictStr] = Field(default=None, description="Lab user is primarily associated with.")
    submits_for: Optional[List[StrictStr]] = Field(default=None, description="Labs user is authorized to submit data for.")
    groups: Optional[List[StrictStr]] = Field(default=None, description="Additional access control groups")
    viewing_groups: Optional[List[StrictStr]] = Field(default=None, description="The group that determines which set of data the user has permission to view.")
    job_title: Optional[StrictStr] = Field(default=None, description="The role of the user in their lab or organization.")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[List[StrictStr]] = Field(default=None, alias="@type")
    summary: Optional[StrictStr] = Field(default=None, description="A summary of the object.")
    title: Optional[StrictStr] = Field(default=None, description="The full name of the user.")
    __properties: ClassVar[List[str]] = ["status", "schema_version", "uuid", "notes", "aliases", "creation_timestamp", "submitted_by", "submitter_comment", "description", "email", "first_name", "last_name", "lab", "submits_for", "groups", "viewing_groups", "job_title", "@id", "@type", "summary", "title"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['current', 'deleted', 'disabled']):
            raise ValueError("must be one of enum values ('current', 'deleted', 'disabled')")
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

    @field_validator('email')
    def email_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", value):
            raise ValueError(r"must validate the regular expression /^[^\s@]+@[^\s@]+\.[^\s@]+$/")
        return value

    @field_validator('groups')
    def groups_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['admin', 'read-only-admin', 'verified']):
                raise ValueError("each list item must be one of ('admin', 'read-only-admin', 'verified')")
        return value

    @field_validator('viewing_groups')
    def viewing_groups_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['community', 'IGVF']):
                raise ValueError("each list item must be one of ('community', 'IGVF')")
        return value

    @field_validator('job_title')
    def job_title_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Principal Investigator', 'Co-Investigator', 'Project Manager', 'Submitter', 'Post Doc', 'Data Wrangler', 'Scientist', 'Computational Scientist', 'Software Developer', 'NHGRI staff member', 'Other']):
            raise ValueError("must be one of enum values ('Principal Investigator', 'Co-Investigator', 'Project Manager', 'Submitter', 'Post Doc', 'Data Wrangler', 'Scientist', 'Computational Scientist', 'Software Developer', 'NHGRI staff member', 'Other')")
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
        """Create an instance of User from a JSON string"""
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
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "schema_version": obj.get("schema_version"),
            "uuid": obj.get("uuid"),
            "notes": obj.get("notes"),
            "aliases": obj.get("aliases"),
            "creation_timestamp": obj.get("creation_timestamp"),
            "submitted_by": obj.get("submitted_by"),
            "submitter_comment": obj.get("submitter_comment"),
            "description": obj.get("description"),
            "email": obj.get("email"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "lab": obj.get("lab"),
            "submits_for": obj.get("submits_for"),
            "groups": obj.get("groups"),
            "viewing_groups": obj.get("viewing_groups"),
            "job_title": obj.get("job_title"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "summary": obj.get("summary"),
            "title": obj.get("title")
        })
        return _obj


