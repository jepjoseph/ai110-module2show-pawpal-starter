from scheduler import Owner, Pet, Scheduler, Task
import streamlit as st

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 180

if st.button("Add task"):
    if st.session_state.remaining_time <= 30:
        st.warning("No more tasks can be added. Remaining time is 30 minutes or less.")
    else:
        if int(duration) > st.session_state.remaining_time:
            st.warning("This task is too long for the remaining time.")
        else:
            st.session_state.tasks.append(
                {
                    "title": task_title,
                    "duration_minutes": int(duration),
                    "priority": priority,
                }
            )
            st.session_state.remaining_time -= int(duration)

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

if "available_minutes" not in st.session_state:
    st.session_state.available_minutes = 180

st.subheader("Build Schedule")

display_value = max(st.session_state.remaining_time, 30)

st.session_state.available_minutes = st.number_input(
    "Available minutes",
    min_value=30,
    max_value=600,
    value=display_value,
)

st.session_state.remaining_time = st.session_state.available_minutes

if st.button("Generate schedule"):
    if not st.session_state.tasks:
        st.warning("Add at least one task before generating a schedule.")
    else:
        owner = Owner(owner_id=1, name=owner_name)
        pet = Pet(pet_id=1, name=pet_name, species=species)

        tasks = [
            Task(
                task_id=index + 1,
                title=item["title"],
                duration_minutes=int(item["duration_minutes"]),
                priority=item["priority"],
            )
            for index, item in enumerate(st.session_state.tasks)
        ]

        scheduler = Scheduler(available_minutes=int(st.session_state.available_minutes))
        plan = scheduler.generate_daily_plan(owner, pet, tasks)

        st.success(f"Schedule generated for {owner.name}.")

        if plan.entries:
            for entry in plan.entries:
                st.write(
                    f"{entry.time_slot} — {entry.task.title} "
                    f"({entry.task.duration_minutes} min) [{entry.task.priority}]"
                )
                st.caption(entry.reason)
        else:
            st.info("No tasks fit into the available time.")
