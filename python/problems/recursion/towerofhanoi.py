def tower_of_hanoi(n):
    answer = []
    tower_of_hanoi_utils(n, 1, 3, 2, answer)
    return answer
    
def tower_of_hanoi_utils(n, from_peg, to_peg, aux_peg, answer):
    if n == 1:
        temp = [from_peg, to_peg]
        answer.append(temp)
        return
    
    tower_of_hanoi_utils(n - 1, from_peg, aux_peg, to_peg, answer)
    
    temp = [from_peg, to_peg]
    answer.append(temp)
    
    tower_of_hanoi_utils(n - 1, aux_peg, to_peg, from_peg, answer)
    