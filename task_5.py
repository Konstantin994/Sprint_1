class TestCase:
    def __init__(self):
        self.steps = {}
        self.result = None
    
    def set_step(self,step_number,step_next):
        self.steps[step_number] = step_next
    
    def delete_step(self,step_number):
        self.steps.pop(step_number)

    def set_result(self,result):
        self.result = result

    def get_test_case(self):
        string = str(self.__dict__)
        new_string = string.replace('steps','Шаги').replace('result','Ожидаемый результат')
        print(new_string)

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 