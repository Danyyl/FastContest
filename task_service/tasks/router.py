from typing import List, Optional

from fastapi import APIRouter, Depends

from tasks.schemas import Solution, SolutionCreate
from tasks.managers import SolutionManager
from utils.dependencies import check_token


router = APIRouter(
    prefix="",
    tags=[],
)


@router.get("/solutions/{task_id}", response_model=Optional[List[Solution]])
async def get_solutions(task_id: int, token: bool = Depends(check_token)) -> Optional[List[Solution]]:
    manager = SolutionManager()
    solutions = await manager.get_by_task_id(task_id)
    return solutions


@router.post("/solutions/create", response_model=Solution)
async def create_task(solution: SolutionCreate, token: bool = Depends(check_token)) -> Solution:
    manager = SolutionManager()
    return await manager.resolve_task(solution)



