#proceduralnie
#def scheduleTasksProcedural(tasks):
#    tasks.sort(key=lambda x: x[1])
#    
#    maxReward = 0
#    scheduledTasks = []
#    lastEndTime = 0
#
#    for task in tasks:
#        start, end, reward = task
#        if start >= lastEndTime:
#            scheduledTasks.append(task)
#            maxReward += reward
#            lastEndTime = end
#
#    return maxReward, scheduledTasks
#
#tasks = [(1, 3, 50), (2, 5, 20), (4, 6, 60), (6, 7, 30), (5, 8, 25), (8, 9, 55)]
#print(scheduleTasksProcedural(tasks))

from functools import reduce

def scheduleTasksFunctional(tasks):
    sortedTasks = sorted(tasks, key=lambda task: task[1])

    result = reduce(
        lambda acc, task: (
            acc[0] + [task] if task[0] >= acc[1] else acc[0],
            task[1] if task[0] >= acc[1] else acc[1],
            acc[2] + task[2] if task[0] >= acc[1] else acc[2]
        ),
        sortedTasks,
        ([], 0, 0)
    )

    maxReward, scheduledTasks = result[2], result[0]
    return maxReward, scheduledTasks

tasks = [(1, 3, 50), (2, 5, 20), (4, 6, 60), (6, 7, 30), (5, 8, 25), (8, 9, 55)]
print(scheduleTasksFunctional(tasks))