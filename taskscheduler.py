class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_freq = max(task_count.values())
        maxtask = list(task_count.values()).count(max_freq)
        internal_needed = (max_freq-1)*(n+1)+ maxtask
        return max(internal_needed,len(tasks))

        
        

        