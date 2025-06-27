from aiogram.types import BotCommand


START_COMMAND = 'start'
START_COMMAND_TEXT = 'Начать работу'
FPM_ABOUT_COMMAND = 'fpm_about'
FPM_ABOUT_COMMAND_TEXT = 'Информация о факультете'
TEST_COMMAND = 'test'
TEST_COMMAND_TEXT = 'Тест для выбора направления'
DEPARTMENT_COMMAND = 'department'
DEPARTMENT_COMMAND_TEXT = 'Кафедры факультета'
DEK_COM = 'dekanat'
DEK_COM_TEXT = 'Информация о деканате'
FACULTY_COM = 'faculty'
FACULTY_COM_TEXT = 'Сайт факультета'
GRADES_SCORES = 'stats'
GRADES_SCORES_TEXT = 'Минимальный балл для поступления по годам'
COMMANDS_LIST = [
    BotCommand(command=START_COMMAND, description=START_COMMAND_TEXT),
    BotCommand(command=FPM_ABOUT_COMMAND, description=FPM_ABOUT_COMMAND_TEXT),
    BotCommand(command=DEPARTMENT_COMMAND, description=DEPARTMENT_COMMAND_TEXT),
    BotCommand(command=TEST_COMMAND, description=TEST_COMMAND_TEXT),
    BotCommand(command=DEK_COM, description=DEK_COM_TEXT),
    BotCommand(command=FACULTY_COM, description=FACULTY_COM_TEXT),
    BotCommand(command=GRADES_SCORES, description=GRADES_SCORES_TEXT)
]
