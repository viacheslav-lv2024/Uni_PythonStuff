total_assignm_pts = int(input())

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
print(grade)