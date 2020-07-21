# scores_list = [["Bobby","87"],
# ["Charles","100"],
# ["Eric","64"],
# ["Charles","22"]]

#Ouput: 87


def avgScore(scores_list):
    dicts = {}
    dicts_score = {}
    max_avg =0
    for ele in scores_list:
        if ele[0] not in dicts:
            dicts[ele[0]] = 1
            dicts_score[ele[0]]  = int(ele[1])
        else:
            dicts[ele[0]] += 1
            dicts_score[ele[0]]  += int(ele[1])

    
    for k in dicts:
        if k in dicts_score:
            avg = dicts_score[k]/dicts[k]
            max_avg =max(avg,max_avg)
    print "The max average score is", max_avg
    return max_avg
        
avgScore(scores_list)



#scores_list = [["Bobby",87],
#["Charles",100],
#["Eric",64],
#["Charles",22]]

def avgScoreN(scores_list):
    dicts = {}
    mx =0 
    for i in range(len(scores_list)): 
        inp_arr = scores_list[i]
        key = inp_arr[0]
        if key not in dicts:
            dicts[key] = {"val":0, "ln":0}
        dicts[key]["val"] += inp_arr[1] 
        dicts[key]["ln"] += 1 
        
    print dicts
        
    for k,v in dicts.items():
        
        mx = max(mx,v['val']/v['ln'])
    print mx
        
