from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class Owner:
    owner_id: int
    name: str
    preferred_times: List[str] = field(default_factory=list)
    preferences: List[str] = field(default_factory=list)
    pets: List["Pet"] = field(default_factory=list)

    def add_pet(self, pet: "Pet") -> None:
        self.pets.append(pet)


@dataclass
class Pet:
    pet_id: int
    name: str
    species: str
    age: int = 0
    energy_level: str = "medium"
    tasks: List["Task"] = field(default_factory=list)

    def add_task(self, task: "Task") -> None:
        self.tasks.append(task)


@dataclass
class Task:
    task_id: int
    title: str
    category: str = "general"
    duration_minutes: int = 0
    priority: str = "medium"
    preferred_time: Optional[str] = None
    is_recurring: bool = False

    def get_priority_score(self) -> int:
        return {"low": 1, "medium": 2, "high": 3}.get(self.priority.lower(), 2)


@dataclass
class PlanEntry:
    time_slot: str
    task: Task
    reason: str

    def to_string(self) -> str:
        return f"{self.time_slot} - {self.task.title} ({self.task.duration_minutes} min)"


@dataclass
class DailyPlan:
    date: str
    entries: List[PlanEntry] = field(default_factory=list)

    def add_entry(self, entry: PlanEntry) -> None:
        self.entries.append(entry)

    def summarize(self) -> str:
        if not self.entries:
            return "No tasks scheduled."
        lines = [f"Daily plan for {self.date}:"]
        for entry in self.entries:
            lines.append(f"- {entry.to_string()}")
        return "\n".join(lines)


@dataclass
class Scheduler:
    available_minutes: int = 240
    start_time: str = "08:00"
    end_time: str = "20:00"

    def generate_daily_plan(self, owner: Owner, pet: Pet, tasks: List[Task]) -> DailyPlan:
        plan = DailyPlan(date="Today")
        remaining_minutes = self.available_minutes
        current_time = datetime.strptime(self.start_time, "%H:%M")

        sorted_tasks = self.sort_tasks(tasks)
        for task in self.filter_tasks(sorted_tasks):
            if task.duration_minutes > remaining_minutes:
                continue

            end_time = current_time + timedelta(minutes=task.duration_minutes)
            time_slot = f"{current_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}"
            reason = self._build_reason(task, remaining_minutes)

            plan.add_entry(PlanEntry(time_slot=time_slot, task=task, reason=reason))

            remaining_minutes -= task.duration_minutes
            current_time = end_time

        return plan

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        return sorted(
            tasks,
            key=lambda task: (
                -task.get_priority_score(),
                task.duration_minutes,
                task.title.lower(),
            ),
        )

    def filter_tasks(self, tasks: List[Task]) -> List[Task]:
        return [
            task
            for task in tasks
            if task.duration_minutes > 0 and task.duration_minutes <= self.available_minutes
        ]

    def resolve_conflicts(self, plan: DailyPlan) -> DailyPlan:
        return plan

    def _build_reason(self, task: Task, remaining_minutes: int) -> str:
        priority_text = {
            1: "lower priority",
            2: "medium priority",
            3: "high priority",
        }.get(task.get_priority_score(), "medium priority")

        return f"Added because it is a {priority_text} task and it fits within the remaining {remaining_minutes} minutes."