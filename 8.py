def task1():
    trees = [[x for x in line.rstrip()] for line in open("8-test.txt")]
    visible_trees = len(trees) * 2 + len(trees[0]) * 2 - 4

    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            current_tree = trees[y][x]
            # Check horizontal
            if max(trees[y][:x]) < current_tree or max(trees[y][x + 1:]) < current_tree:
                visible_trees += 1
                continue

            col = []
            # Check vertical
            for y2 in range(len(trees)):
                col.append(trees[y2][x])

            if max(col[:y]) < current_tree or max(col[y + 1:]) < current_tree:
                visible_trees += 1
    print(visible_trees)


def task2():
    trees = [[x for x in line.rstrip()] for line in open("8.txt")]
    visible_trees = len(trees) * 2 + len(trees[0]) * 2 - 4
    best_score = 0
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            current_tree = trees[y][x]

            col = []
            # Check vertical
            for y2 in range(len(trees)):
                col.append(trees[y2][x])

            left = trees[y][:x]
            left.reverse()
            right = trees[y][x + 1:]
            top = col[:y]
            top.reverse()
            bottom = col[y + 1:]

            score = []
            for i in range(len(left)):
                if left[i] < current_tree:
                    if i == len(left) - 1:
                        score.append(int(i + 1))
                    continue
                score.append(int(i + 1))
                break

            for i in range(len(right)):
                if right[i] < current_tree:
                    if i == len(right) - 1:
                        score.append(int(i + 1))
                    continue
                score.append(int(i + 1))
                break

            for i in range(len(top)):
                if top[i] < current_tree:
                    if i == len(top) - 1:
                        score.append(int(i + 1))
                    continue
                score.append(int(i + 1))
                break

            for i in range(len(bottom)):
                if bottom[i] < current_tree:
                    if i == len(bottom) - 1:
                        score.append(int(i + 1))
                    continue
                score.append(int(i + 1))
                break

            this_score = 1
            for i in score:
                this_score *= int(i)
            if this_score > best_score:
                best_score = this_score
    print(best_score)


task2()
