from scheduler import Owner, Pet, Scheduler, Task


def test_scheduler_prioritizes_high_priority_tasks():
    owner = Owner(owner_id=1, name="Jordan")
    pet = Pet(pet_id=1, name="Mochi", species="dog")

    tasks = [
        Task(task_id=1, title="Feed", duration_minutes=15, priority="low"),
        Task(task_id=2, title="Walk", duration_minutes=20, priority="high"),
        Task(task_id=3, title="Medicine", duration_minutes=10, priority="medium"),
    ]

    scheduler = Scheduler(available_minutes=60)
    plan = scheduler.generate_daily_plan(owner, pet, tasks)

    assert plan.entries[0].task.title == "Walk"
    assert plan.entries[0].task.priority == "high"


def test_scheduler_skips_tasks_that_do_not_fit():
    owner = Owner(owner_id=1, name="Jordan")
    pet = Pet(pet_id=1, name="Mochi", species="dog")

    tasks = [
        Task(task_id=1, title="Walk", duration_minutes=20, priority="high"),
        Task(task_id=2, title="Treat", duration_minutes=20, priority="medium"),
        Task(task_id=3, title="Brush", duration_minutes=15, priority="low"),
    ]

    scheduler = Scheduler(available_minutes=30)
    plan = scheduler.generate_daily_plan(owner, pet, tasks)

    assert len(plan.entries) == 1
    assert plan.entries[0].task.title == "Walk"


def test_plan_entry_includes_reason_and_time_slot():
    owner = Owner(owner_id=1, name="Jordan")
    pet = Pet(pet_id=1, name="Mochi", species="dog")

    task = Task(task_id=1, title="Walk", duration_minutes=20, priority="high")
    scheduler = Scheduler(available_minutes=60)

    plan = scheduler.generate_daily_plan(owner, pet, [task])

    assert plan.entries[0].reason
    assert " - " in plan.entries[0].time_slot