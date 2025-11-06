def create_commendation(child, lesson):
    import random

    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=child)
    except Schoolkid.DoesNotExist:
        return "Такого ученика не существует"
    except Schoolkid.MultipleObjectsReturned:
        return "По вашему запросу существует более одного ученика"
    one_random_lesson = (
        Lesson.objects.filter(year_of_study=6, group_letter="А", subject__title=lesson)
        .order_by("?")
        .first()
    )
    commendation_list = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
    ]
    Commendation.objects.create(
        text=random.choice(commendation_list),
        created=one_random_lesson.date,
        schoolkid=schoolkid,
        subject=one_random_lesson.subject,
        teacher=one_random_lesson.teacher,
    )


def remove_chastisements(schoolkid):
    from datacenter import models

    for bad_chastisement in schoolkid:
        bad_chastisement.delete()
    return "Замечания удалены"


def fix_marks(schoolkid):
    from datacenter import models

    for bad_point in schoolkid:
        bad_point.points = 5
        bad_point.save()
    return "Оценки исправлены"
