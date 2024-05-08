def amount(A, S):
    A.sort()
    results = []

    def backtrack(comb, next_index, current_sum):
        if current_sum == S:
            results.append(list(comb))
            return
        if current_sum > S:
            return

        for i in range(next_index, len(A)):
            if i > next_index and A[i] == A[i-1]:
                continue
            comb.append(A[i])
            backtrack(comb, i + 1, current_sum + A[i])
            comb.pop()

    backtrack([], 0, 0)
    return results

