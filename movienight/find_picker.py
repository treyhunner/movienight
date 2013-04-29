def find_picker(attenders):
    attendees = set(attenders)
    counted = [x for x in attendees if x.score != 'N/A']
    if len(counted) == 1:
        return counted[0]
    S = set(counted[0].events)
    for i in counted:
        S = S & set(i.events)
    for i in S:
        if i.picker_id not in [x.id for x in S]:
            S -= i
    if S == set():
        low_score = counted[0]
        for x in counted:
            if x.score < low_score.score:
                low_score = x
        counted.remove(low_score)
        picker = find_picker(counted)
    else:
        relative_scores = {x:-len(set(x.picks) & S)*100 for x in counted}
        picker = counted[0]
        for x in counted:
            if relative_scores[x] > relative_scores[picker]:
                picker = x
    return picker
