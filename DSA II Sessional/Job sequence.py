#greedy approach
class job:
    def __init__(self,jobid,deadline,profit):
        self.jobid = jobid
        self.deadline = deadline
        self.profit = profit

def jobSequence(jobs):
    jobs.sort(key = lambda x : x.profit,reverse = True)


    maxdeadline = 0
    for job in jobs:
        if job.deadline >maxdeadline:
            maxdeadline = job.deadline

    slots = [None]*maxdeadline
    totalprofit = 0

    for job in jobs:
        for j in range(job.deadline-1,-1,-1):
            if slots[j] is None:
                slots[j]=job
                totalprofit +=job.profit
                break
    print("Total Profit",totalprofit)



jobs = [
    job("J1",2,100),
    job("J2",1,19),
    job("J3",2,27),
    job("J4",1,25),
    job("J5",3,15)
]

jobSequence(jobs)


