class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_fails = 0
        x = 0
        while sandwiches:
            if sandwiches[0] == students[0]:
                sandwiches.pop(x)
                students.pop(x)
                num_fails = 0
            elif num_fails < len(students):
                students.append(students.pop(0))
                num_fails += 1
            else:
                break
        return len(students)


