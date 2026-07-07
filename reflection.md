# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
 * My initial UML design includes six main classes: Owner, Pet, Task, Scheduler, DailyPlan, and PlanEntry. The Owner class stores user information, including preferences and available times, and manages their pets. The Pet class represents each pet and stores its basic details along with related care tasks. The Task class defines individual pet care activities such as feeding, walking, or medication, including attributes like duration, priority, and scheduling preferences. The Scheduler class is the core logic component that organizes, filters, and sorts tasks into a structured daily plan based on constraints. The DailyPlan class represents the final schedule for a specific day, grouping all planned activities. The PlanEntry class represents each scheduled item in the plan, linking a task to a time slot and providing context for why it was selected. Overall, this design keeps the system modular, organized, and easy to extend.


- What classes did you include, and what responsibilities did you assign to each?
* These are the classes included and their responsibilities:
1) Owner: stores the owner’s information, such as name, preferred times, and preferences.

2) Pet: stores the pet’s information, such as name, species, age, and energy level, and keeps track of its tasks.

3) Task: represents a care activity like walking, feeding, grooming, or medication, including its duration, priority, and timing preferences.

4) Scheduler: handles the scheduling logic by sorting, filtering, and organizing tasks into a daily plan based on constraints and priorities.

5) PlanEntry: represents one scheduled item in the daily plan, including the time slot, the task, and a reason for inclusion.

6) DailyPlan: holds the full set of planned activities for the day and can add entries and summarize the schedule.


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
 * Yes, my design changed during implementation. One important change was that the UI now updates the available minutes dynamically as tasks are added, so users can see the remaining time left in real time. I also allowed users to override the default available minutes value in the schedule section with their own input. I made these changes because the initial design was more static, and this improved the app’s usability by making the scheduling constraints more visible and interactive.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
* The scheduler considers time and priority as its main constraints. It checks whether a task fits within the available minutes and then sorts tasks by priority in the order high, medium, and low. I decided these constraints mattered most because the app is meant to help users plan important care tasks first while still staying within their available time.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
* A tradeoff is that the scheduler favors high-priority tasks over lower-priority ones when time is limited. This is reasonable because in a real pet-care routine, important tasks like medication or feeding should be completed first, even if some less urgent tasks are left out.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
* I used AI tools to help with design brainstorming, debugging, and refactoring. It was especially useful when I was deciding how to structure the classes and when I ran into issues with the Streamlit UI and pytest import errors. The most helpful prompts were ones that asked for explanations of errors or suggestions for organizing the scheduler and its related classes.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
* One moment where I did not accept an AI suggestion as-is was when I was trying to connect the “Add task” flow to the “Available minutes” value in the schedule section. The AI suggestion kept using the default 180-minute value instead of the user’s custom input, and the remaining-time display also calculated incorrectly by subtracting the total duration of all tasks each time. I verified the suggestion by testing the app manually in Streamlit, checking the displayed remaining time after each task, and comparing it against the expected math. I then fixed the logic so the remaining time is based on the new task’s duration instead of the full accumulated total.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
* I tested that high-priority tasks are scheduled first, that tasks that exceed the available time are skipped, and that the app generates a clear daily plan with time slots and reasons. These behaviors were important because they ensure the scheduler is practical and that the UI behaves as expected.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
* I am reasonably confident in the core scheduling behavior, especially for simple cases with clear priority and time constraints. If I had more time, I would test edge cases such as tasks that exactly match the available time, very long tasks, equal-priority tasks, and recurring or conflicting tasks.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
* I am most satisfied with the custom available time feature, where users can enter their own available time. It made the scheduling experience more practical and personalized.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
* If I had another iteration, I would improve the UI design, especially the starting screen, to make it feel more polished and visually appealing, perhaps with a more 3D-style appearance.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
* One important thing I learned is that AI can be very useful, but it can also be stubborn and is not always reliable when it comes to math and logic-heavy programming tasks. Its suggestions still need to be tested and verified carefully.