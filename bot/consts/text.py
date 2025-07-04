
FACULTY_ABOUT = '''Факультет готовит ведущих IT-специалистов и математиков региона 📈. 
Выпускники работают в администрации Краснодарского края, правоохранительных органах 
(ФСБ, МВД), вузах (КубГУ, КубГАУ), банках («Сбербанк», «Альфа-банк»), а также в компаниях: «Роснефть», 
«МТС», «МегаФон», «Тандер», ZTE и других 💼.

Преподавательский состав включает академика РАН, 10 докторов и 34 кандидата наук. 
Студенты обучаются в 9 компьютерных классах. Более 60% выпускников поступают в магистратуру. 
Есть стипендиаты Президента РФ, фондов Потанина и «Вольное дело».

Факультет ведет научные исследования (объем — 200 млн руб. за 5 лет), публикует работы (500+ статей) и участвует в международных конференциях 📖. 
В 2002 году академик В.А. Бабешко получил Государственную премию РФ.'''

DEPARTMENT_INFO = f'На факультете есть 5 основных кафедр, выбери из списка, интересующую тебя'

START_TEXT = '''Привет,  @{username} 👋🏻 Это бот для абитуриента Факультета Компьютерных Технологий и Прикладной 
Математики. Наш бот поможет тебе определиться с выбором направления, на основе пройденного теста ⚖️. Так же в нашем боте 
ты сможешь узнать много полезной информации о факультете.'''

TEST_START_TEXT = (f'Чтобы помочь тебе определиться с выбором наиболее подходящего направления необходимо пройти тест. '
                   f'Для улучшения работы бота все ответы записываются, необходимо дать подтверждение на обработку '
                   f'ваших ответов.')
TEST_NO_CONFIRM = ('Для того, чтобы пройти тест необходимо подтвердить, что вы даёте согласие на обработку ваших '
                   'ответов.')

ADMIN_CREATED = 'Пользователь с id {tg_id} теперь администратор'
ADMIN_TO_CREATE = 'Введите id пользователя, которого хотите сделать администратором'
QUESTION_TO_CREATE = 'Напишите вопрос для его добавления'
ANSWER_TO_CREATE = 'Напишите вариант ответа на вопрос выше'
WEIGHTS_TO_CREATE = ('Напишите веса, которые будут учитываться при финальном результате в формате 0.1;0.1;0.2 и т.д., '
                     'вес может быть не больше 1\nПорядок весов для каждого направления 01.03.02; 01.03.02; 01.03.02; '
                     '02.03.03; 02.03.02; 09.03.03')
QUESTION_CREATED = 'Ваш вопрос добавлен в тест'
QUESTIONS_ADDED = 'Все вопросы успешно внесены'

RESULT = 'Наиболее подходящие направление для вас - {speciality}'
RESTART = 'Начните тест заново'

DEPARTMENTS = [
    "КИТ - изучает применение и разработку нейросетевых технологий, системы передачи и защиты информации",
    "КВТ - изучает семантические технологии, алгоритмы оптимизации, криптографию, машинное зрение",
    "КММ - изучает информационные сисетмы в образовании, базы данных и знаний, динамические задачи механики",
    "КАДИИ - изучает системы искусственного интеллекта, анализ данных, информационную безопастность",
    "КПМ - изучает математическое моделирование в экономике, электромембранные системы, анализ краевых задач"
]

DEK = 'Деканат ФКТиПМ имеет собственную страницу в Вконтакте, где публикуется все последние новости нашего факультета. ✉️'
FACULTY = 'Факультет имеет собственную страницу на сайте КубГу, там можно ннайти много полезной информации о факлуьтете и его преподавателях'
CHOOSE_DEP_FOR_GRADE_STATS = 'Выберите интересующее вас направление'
