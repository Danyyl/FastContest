from typing import List, Optional

from tasks.schemas import Solution
from utils.resolver import resolve
from utils.mongo_helper import MongoHelper


class SolutionManager:

    def __init__(self):
        self.helper = MongoHelper()

    async def get_by_task_id(self, task_id: int) -> Optional[List[Solution]]:
        solutions = await self.helper.get_objects("solution", {"task_id": task_id})
        return solutions

    async def resolve_task(self, solution) -> Solution:
        try:
            data = resolve(
                code=solution.code,
                func_name=solution.func_name,
                input_data=solution.input_data,
                output_data=solution.output_data,
            )
        except AssertionError as e:
            result = {
                "task_id": solution.task_id,
                "code": solution.code,
                "resolved": False,
                "time": 0,
                "error_type": "Wrong answer",
                "error_value": str(e),
                "score": 0,
            }
        except Exception as e:
            result = {
                "task_id": solution.task_id,
                "code": solution.code,
                "resolved": False,
                "time": 0,
                "error_type": "Compilation Error",
                "error_value": str(e),
                "score": 0,
            }
        else:
            result = {
                "task_id": solution.task_id,
                "code": solution.code,
                "resolved": True,
                "time": data["time"],
                "error_type": None,
                "error_value": None,
                "score": 10,
            }
        id = await self.helper.insert_one("solution", result)
        solution = await self.helper.get_object("solution", {"_id": id})
        return solution
