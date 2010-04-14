def fix_subtrees(left, right):
    li, ri, diff, loffset, roffset, lo, ro \
        = contour(left, right)
    diff += 1
    diff += (right.x + diff + left.x) % 2

    right.mod = diff
    right.x += diff

    if right.children:
        roffset += diff

    if ri and not li:
        lo.thread = ri
        lo.mod = roffset - loffset
    elif li and not ri:
        ro.thread = li
        ro.mod = loffset - roffset

    return (left.x + right.x) / 2
