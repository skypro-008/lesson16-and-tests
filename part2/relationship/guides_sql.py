guides = [
    {
        "name": "Елена",
        "surname": "Макеева"
    },
    {
        "name": "Федор",
        "surname": "Земельников"
    },
    {
        "name": "Степан",
        "surname": "Саровский"
    }
]


tours = [
    {
        "name": "Путешествие в горы",
        "days_duration": 4,
        "guide_id": 1
    },
    {
        "name": "Лесные реки",
        "days_duration": 2,
        "guide_id": 1
    },
    {
        "name": "Сказки у костра",
        "days_duration": 3,
        "guide_id": 1
    },
    {
        "name": "Мир водопадов",
        "days_duration": 7,
        "guide_id": 2
    },
    {
        "name": "Зеленые луга",
        "days_duration": 2,
        "guide_id": 2
    },
    {
        "name": "Северная природа",
        "days_duration": 4,
        "guide_id": 2
    },
    {
        "name": "Ночной город",
        "days_duration": 1,
        "guide_id": 2
    },
    {
        "name": "Тайны Петербурга",
        "days_duration": 1,
        "guide_id": 3
    },
    {
        "name": "Три крепости",
        "days_duration": 3,
        "guide_id": 3
    },
    {
        "name": "Каньон желаний",
        "days_duration": 7,
        "guide_id": 3
    }
]


def add_guides(session, guide_model):
    with session() as ses:
        guide_instances = [guide_model(**guide) for guide in guides]
        ses.add_all(guide_instances)
        ses.commit()


def add_tours(session, tour_model):
    with session() as ses:
        tour_instances = [tour_model(**tour) for tour in tours]
        ses.add_all(tour_instances)
        ses.commit()
