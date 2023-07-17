from typing import Optional

from pydantic import BaseModel, Field, validator


class Solution(BaseModel):
    task_id: int
    code: str
    resolved: bool
    time: int
    error_type: Optional[str]
    error_value: Optional[str]
    score: int


class SolutionCreate(BaseModel):
    task_id: int
    code: str
    func_name: str
    input_data: str
    output_data: str

    @validator("code")
    def is_valid_code(cls, value=None):
        """
            Validate code
        """
        return value
