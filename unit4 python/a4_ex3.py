def grade_calculator(
        assignments: list,
        bonus_assignment: int,
        exam: int) -> tuple[bool, int]:
    is_graded = True
    cnt_of_failed_assignments = 0
    total_assignm_pts = 0
    grade = None

    for i in range(len(assignments)):
        if assignments[i] is None or assignments[i] < 25:  # If assignments[i] == None is true,
            cnt_of_failed_assignments += 1  # then comparison (<) further is skipped due to how Python
        if assignments[i] is not None:      # handles "or" operation and thereby we don't get an error
            total_assignm_pts += assignments[i]
    
    if bonus_assignment is not None:
        total_assignm_pts += bonus_assignment

    if bonus_assignment is not None and bonus_assignment >= 25:
        cnt_of_failed_assignments -= 1

    if cnt_of_failed_assignments > 2:
        is_graded = False

    if total_assignm_pts < 500:
        is_graded = False

    if exam is None or exam < 50:
        is_graded = False
    
    if not is_graded:  # written to not execute excessive amount of code and to avoid misgrading
        return is_graded, 5
    
    total_assignm_pts += exam

    match total_assignm_pts:
        case _ if total_assignm_pts >= (0.875 * 1100):
            grade = 1
        case _ if total_assignm_pts >= (0.75 * 1100):
            grade = 2
        case _ if total_assignm_pts >= (0.625 * 1100):
            grade = 3
        case _ if total_assignm_pts >= (0.5 * 1100):
            grade = 4
        case _:  # we don't need "_ if total_assignm_pts <= (0.5 * 1100)" because
            grade = 5  # we already wrote all other possible options upper

    return is_graded, grade
