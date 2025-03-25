# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
Thread = namedtuple("Thread", ["thread", "next_free_time"])


def assign_jobs_(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

def assign_jobs(n_workers: int, jobs: list[int]) -> list[AssignedJob]:
    # should the heap be of size n_workers?
    H = [(0, i) for i in range(n_workers)]
    result = []
    # define pq functions
    # Parent
    def Parent(i: int) -> int:
        return (i-1) // 2
    # LeftChild
    def LeftChild(i: int) -> int:
        return (i * 2) + 1
    # RightChild
    def RightChild(i: int) -> int:
        return (i * 2) + 2
    # SiftUp
    def SiftUp(i: int) -> None:
        """
        Sift ith node up to correct position in min heap tree
        """
        # do until i is the root or i is greater than it's parent
        while i > 0 and H[Parent(i)] > H[i]:
            # swap the location of i and parent
            H[Parent(i)], H[i] = H[i], H[Parent(i)]
            # set parent to i to check if this new node is in the correct place
            i = Parent(i)       
    # SiftDown
    def SiftDown(i: int) -> None:
        # track minimum index
        minIndex = i
        left = LeftChild(i)
        # if there is child and it is less than parent and ajust minIndex
        if left < len(H) and H[left] < H[minIndex]:
            minIndex = left
        right = RightChild(i)
        if right < len(H) and H[right] < H[minIndex]:
            minIndex = right
        # if i isn't the smallest value
        if i != minIndex:
            # swap it with the smallest and shift down the larger if needed
            H[i], H[minIndex] = H[minIndex], H[i]
            SiftDown(minIndex)
    # Insert
    def Insert(p: tuple[int,int]) -> None:
        # add the freed thread
        H.append(p)
        # sift up the thread to the correct position in priority queue
        SiftUp(len(H) - 1)

    # ExtractMin
    def ExtractMin() -> tuple[int,int]:
        result = H[0]
        H[0] = H[-1]
        H.pop()
        SiftDown(0)
        return result
    
    for job in jobs:
        # get the next available thread for the job
        free_time, thread = ExtractMin()
        # "assign" the job by adding to the results list
        assignment = AssignedJob(thread, free_time)
        result.append(assignment)
        # insert thread back into priority queue with its available time
        Insert((free_time + job, thread))
        assert len(H) == n_workers
    
    return result


    

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
