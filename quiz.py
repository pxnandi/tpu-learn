correctAns = [9, 7, 4, 6, 3, 1, 12, 8, 5, 2] # Правильные ответы

questions = ['В зоопарке живёт столько жёлтых попугаев, сколько и голубых. Голубых столько же, сколько и красных. Cколько всего попугаев, если красных три?',
             'В доме у Кати живут четыре кота. Каждый кот утром съедает две сосиски. Сегодня Кате не хватило одной сосиски, чтобы накормить всех своих котов. Сколько сосисок было сегодня у Кати?',
             'Маше два года назад исполнилось 5 лет, а Ване через год будет 7 лет. Сколько лет было Ване, когда Маше было 5 ktn?',]
            #  'На ветке сидело несколько птичек. Потом четыре улетели, и осталось только 2 птички. Сколько их было вначале?',
            #  'За забором гуляли курицы. Я вижу, что там 6 куриных ног. Сколько там куриц?',
            #  'За забором гуляли кошки и курицы, а всего у них было 6 ног. Сколько было кошек?',
            #  'У одной машины 4 колеса. Сколько колёс у трёх машин?',
            #  'Ваня задумал число. Оно больше, чем 7, но меньше, чем 9. Какое это число?',
            #  'Гуляя в парке Катя нашла 4 дубовых листа и 1 кленовый. Сколько всего листьев нашла Катя?',
            #  'У Володи было 4 абрикоса. 2 он отдал своей сестре Вере. Сколько абрикосов осталось у Володи?']

incAns = []  # Номера вопросов на которые неправильно был дан ответ
i = 0

for i in range(len(questions)):
    print(questions[i])
    Ans = input()
    if int(Ans) != correctAns[i]:
        incAns.append(i)

while incAns:
    ia = incAns.copy()
    for i in range(len(incAns)):

        print(questions[ia[i]])
        
        Ans = input()
        if int(Ans) == correctAns[incAns[i]]:
            incAns.pop(i)




