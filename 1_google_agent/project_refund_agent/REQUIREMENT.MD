# 🏗️ Mini-Project: Refund Agent for Ed-Tech Platform
## Context and Problem
- Ed-tech companies manually process refund requests.
- Refunds depend on policy: 
    - full refund if requested within 7 days of purchase and 
    - less than 20% of the course watched.

## Setup
- Dummy SQLite database student.db with three tables:
- students (5 students)
- courses (3 courses)
- enrollments (10 entries linking students and courses, purchase dates, completion %, refund status, refund reason)


## Tools Created (6 Function Tools)



| Tool Name                  | Purpose                                                                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------|
| `identify_student`         | Validate student existence by email.                                                               |
| `get_my_enrollments`       | List courses the student has enrolled in.                                                          |
| `get_refund_policy`        | Retrieve refund policy details externally.                                                         |
| `check_refund_eligibility` | Check eligibility based on purchase date and course completion.                                     |
| `place_refund_request`     | Save the refund request and reason, and change the status to "refund requested."                    |
| `get_refund_status`        | Check the current refund request status ("Refunded" or "Refund Requested").                       |

## Workflow

- Student requests refund.
- Agent asks for registered email and verifies student.
- Agent lists enrolled courses and asks which course refund is requested for.
- Agent checks refund eligibility.
- If ineligible, agent explains the reason.
- If eligible, agent requests refund reason from student.
- Agent confirms refund request, updates database.
- Student can later query refund status.