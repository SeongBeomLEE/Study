def solution(info, query):
    DB = {}
    langs = ["cpp", "java", "python", "-"]
    jobs = ["backend", "frontend", "-"]
    careers = ["junior", "senior", "-"]
    foods = ["chicken", "pizza", "-"]
    for lang in langs:
        for job in jobs:
            for career in careers:
                for food in foods:
                    DB[lang + " and " + job + " and " + career + " and " + food] = []

    for user_info in info:
        lang, job, career, food, score = user_info.split()
        langs = [lang, "-"]
        jobs = [job, "-"]
        careers = [career, "-"]
        foods = [food, "-"]
        for lang in langs:
            for job in jobs:
                for career in careers:
                    for food in foods:
                        DB[lang + " and " + job + " and " + career + " and " + food].append(int(score))

    for key in DB.keys():
        DB[key].sort()

    answer = []
    for q in query:
        target = int(q.replace("and", "").split()[-1])
        q = q.replace(f"{target}", "").strip()
        scores = DB[q]

        start_index = 0
        end_index = len(scores) - 1
        while start_index <= end_index:
            mid_index = int((start_index + end_index) / 2)
            mid = scores[mid_index]
            if mid < target:
                start_index = mid_index + 1
            if mid >= target:
                end_index = mid_index - 1
        answer.append(len(scores) - start_index)
    return answer
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 0","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 50"]
print(solution(info, query))