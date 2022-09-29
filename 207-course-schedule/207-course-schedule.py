'''
numCourses = 2

prereq = [[1,0]] => you have to take 1 before 0

calculate the indeg for all the courses:

index[0]  = 0
indeg[1] = 1

que = deuqe <- add all with 0 indeg

while que:
    pop it out
    
    find all the courses which has this course as prereq.
        - dec their indeg.
        if the indeg == 0:
            append to que

if all the indegs == 0 then we can finish the course.


'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dic = defaultdict(list)
        indeg = [0]*numCourses
        
        for a,b in prerequisites:
            dic[a].append(b)
            indeg[b] += 1
        
        que = deque()
        done = set()
        
        
        for i in range(numCourses):
            if indeg[i] == 0:
                que.append(i)
                done.add(i)
        
        
        while que:
            curr = que.popleft()
            
            for child in dic[curr]:
                indeg[child] -= 1
                if indeg[child] == 0 and child not in done:
                    que.append(child)
                    done.add(child)
        
        return True if len(done) == numCourses else False
        
        