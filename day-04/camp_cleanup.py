
def get_subsets():
    overlaps = 0
    with open("day-4/input.txt") as section_assignments:
        for assignment in section_assignments:
            ranges = [ list(map(int, r.split('-'))) for r in assignment.strip().split(',')]
            if (ranges[0][0] >= ranges[1][0] and ranges[0][1] <= ranges[1][1]) \
            or (ranges[1][0] >= ranges[0][0] and ranges[1][1] <= ranges[0][1]):
                overlaps += 1
    return overlaps

def get_overlaps():
    overlaps = 0
    with open("day-4/input.txt") as section_assignments:
        for assignment in section_assignments:
            ranges = [ list(map(int, r.split('-'))) for r in assignment.strip().split(',')]
            if (ranges[1][1] >= ranges[0][0] >= ranges[1][0]) \
            or (ranges[1][1] >= ranges[0][1] >= ranges[1][0]) \
            or (ranges[0][1] >= ranges[1][0] >= ranges[0][0]) \
            or (ranges[0][1] >= ranges[1][1] >= ranges[0][0]):
                overlaps += 1
    return overlaps

print(get_overlaps())

            