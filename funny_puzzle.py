import copy
import heapq

def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    distance = 0
    for i in range(len(from_state)):
        if from_state[i]!=0:
            distance += abs(int(i/3) - int((from_state[i] - 1) / 3)) + abs(i%3 - (from_state[i] - 1) % 3)
    return distance




def print_succ(state):
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    succ_states, pos = [], [-3,3,1,-1]
    for i in range (len(state)):
        for j in pos:
            temp = copy.deepcopy(state)
            if (i+j>=0 and i+j<=8) and not (((i+1)%3==0 and j == 1) or ((i+1)%3==1 and j == -1)):
                if temp[i+j] == 0 and temp[i] != 0:
                    temp[i+j] = state[i]
                    temp[i] = 0
                    succ_states.append(temp)

    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    open, close = [], []
    h, count = get_manhattan_distance(state), 0
    heapq.heappush(open, (h, state, (0, h, -1)))
    while open:
        min = heapq.heappop(open)
        close.append(min)
        count += len(min)
        h1 = min[2][1]
        if h1 == 0:  # Goal node, exit
            print_solve(min, close)
            print("Max queue length:", count)
            return
        pos = get_succ(min[1])
        move = min[2][0] + 1

        for x in pos:
            n = False
            gh = get_manhattan_distance(x)
            for y in open:
                if x == y[1]:
                    n = True
                    if move < y[2][0]:
                        open.pop(open.index(y))
                        heapq.heappush(open, (move + gh, x, (move, gh, min[2][2] + 1)))
                    break

            for y in close:
                if x == y[1]:
                    n = True
                    if move < y[2][0]:
                        open.pop(open.index(y))
                        heapq.heappush(open, (move + gh, x, (move, gh, min[2][2] + 1)))
                    break

            if not n:
                heapq.heappush(open, (move + gh, x, (move, gh, min[2][2] + 1)))
    return

def print_solve(m, c):
    move = 0
    for x in c:
        if x[2][2] == m[2][2] - 1:
            move = print_solve(x, c)
            break
    h = get_manhattan_distance(m[1])
    print(m[1], "h={}".format(h), "moves:", move)
    return move+1

if __name__ == "__main__":
    solve([5, 2, 3, 0, 6, 4, 7, 1, 0])
