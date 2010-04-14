def contour(left,
            right,
            max_offset=None,
            loffset=0,
            roffset=0,
            left_outer=None, 
            right_outer=None):
    delta = left.x + loffset - (right.x + roffset)
    if not max_offset or delta > max_offset:
        max_offset = delta

    if not left_outer:
        left_outer = left
    if not right_outer:
        right_outer = right

    lo = nextleft(left_outer)
    li = nextright(left)
    ri = nextleft(right)
    ro = nextright(right_outer)

    if li and ri:
        loffset += left.offset
        roffset += right.offset
        return contour(li, ri, max_offset,
                       loffset, roffset, lo, ro)

    return (li, ri, max_offset,
            loffset, roffset, left_outer, right_outer
            )
