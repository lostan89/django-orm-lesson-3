from datacenter import models

COMMENDATIONS = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
    ]

def find_schoolkid(child_name):
    try:
        return Schoolkid.objects.get(full_name__contains=child_name)
    except Schoolkid.DoesNotExist:
        return "Такого ученика не существует"
    except Schoolkid.MultipleObjectsReturned:
        return "По вашему запросу существует более одного ученика"


def create_commendation(child, lesson):
    import random

    one_random_lesson = (
        Lesson.objects.filter(year_of_study=6, group_letter="А", subject__title=lesson)
        .order_by("?")
        .first()
    )
    if not one_random_lesson:
        return "Уроков не найдено"
    Commendation.objects.create(
        text=random.choice(COMMENDATIONS),
        created=one_random_lesson.date,
        schoolkid=find_schoolkid(child),
        subject=one_random_lesson.subject,
        teacher=one_random_lesson.teacher,
    )


def remove_chastisements(child):
    schoolkid = Chastisement.objects.filter(schoolkid=find_schoolkid(child))
    schoolkid.delete()
    return "Замечания удалены"


def fix_marks(child):
    schoolkid = Marks.objects.filter(points__lt=4, schoolkid=find_schoolkid(child))
    schoolkid.update(points=5)
    return "Оценки исправлены"

def main():
    
if __name__ == "__main__":
    main()
