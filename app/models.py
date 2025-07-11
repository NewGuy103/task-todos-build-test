import uuid
from pydantic import BaseModel, AwareDatetime
from enum import IntEnum


class SortByComboBoxEnum(IntEnum):
    closest_to_deadline = 0
    farthest_to_deadline = 1
    subjects_a_to_z = 2


class SubjectBase(BaseModel):
    subject: str
    deadline: AwareDatetime
    task: str


class EditedSubjectTask(SubjectBase):
    pass


class EditedTaskWithID(SubjectBase):
    completed: bool
    task_id: uuid.UUID


class SubjectTask(SubjectBase):
    completed: bool
    task_id: uuid.UUID


# State models
class SortAndFilterState(BaseModel):
    subject_filter: str | None = None
    include_all_subjects: bool = True
    sort_filter: SortByComboBoxEnum = SortByComboBoxEnum.closest_to_deadline
