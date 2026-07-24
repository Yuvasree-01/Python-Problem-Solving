class Solution:
    def average(self, salary: List[int]) -> float:
        total=sum(salary)
        maximum=max(salary)
        minimum=min(salary)
        average=(total-minimum-maximum)/(len(salary)-2)
        return average
        