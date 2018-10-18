import init
import api_calls as api
import pprint


def remove_none_elements_from_list(list):
    return [e for e in list if e is not None]


def fix_question_groups():
    quizzes = api.get_all_quizzes()
    pprint.pprint('We have ' + str(len(quizzes)) + ' quizzes')
    for quiz in quizzes:
        payload = []
        quiz_title = quiz['title']
        print('We are currently looking at the quiz: ' + quiz_title)
        quiz_id = quiz['id']
        quiz_questions = api.get_quiz_questions(quiz_id)
        print('There are ' + str(len(quiz_questions)) + ' questions in this quiz')
        quiz_questions_group_array = []
        quiz_questions.sort(key=lambda x: x['id'], reverse=False)
        for quiz_question in quiz_questions:
            quiz_questions_group_array.append(quiz_question['quiz_group_id'])
        print(quiz_questions_group_array)
        # filter out for question groups with one question
        quiz_questions_group_array = [x for x in quiz_questions_group_array if quiz_questions_group_array.count(x) == 1]
        # remove nones from question group array (for questions that didnt have a group)
        quiz_questions_group_array = remove_none_elements_from_list(quiz_questions_group_array)
        pprint.pprint(quiz_questions_group_array)
        for quiz_question in quiz_questions:
            if quiz_question['quiz_group_id'] in quiz_questions_group_array:

                group_points = api.get_quiz_group(quiz_id, quiz_question['quiz_group_id'])['question_points']
                print(group_points)
                print('Moving single question "' + quiz_question['question_name'] + '" outside of its question group')


                api.fix_question(quiz_id, quiz_question['id'])
                api.fix_question_points(quiz_id, quiz_question['id'], group_points)

                data = {}
                pprint.pprint(quiz_question['question_name'] + ' has an id ' + str(quiz_question['id']))
                data["type"] = "question"
                data["id"] = str(quiz_question['id'])
                payload.append(data)

        print('Deleting empty single question groups in ' + quiz_title)
        for quiz_question_group in quiz_questions_group_array:
            api.delete_quiz_group(str(quiz_id), str(quiz_question_group))
        if len(quiz_questions_group_array) > 0:
            print('Reordering questions in ' + quiz_title)
            pprint.pprint(payload)
            api.fix_question_order(quiz_id, payload)
