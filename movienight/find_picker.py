def find_picker(attenders):
    counted = [x for x in attenders if x.score != 'N/A']
    S = set(counted[0].events)
    for i in counted:
        S = S & set(i.events)
    for i in S:
        if i.picker_id not in [x.id for x in S]:
            S -= i
    if S == set():
        picker = counted[0]
        for x in counted:
            if x.score > picker.score:
                picker = x
    else:
        relative_scores = {x:-len(set(x.picks) & S)*100 for x in counted}
        picker = counted[0]
        for x in counted:
            if relative_score[x] > relative_score[picker]:
                picker = x
    return picker
