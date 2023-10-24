import sys
from decimal import Decimal

from assertpy import assert_that


class Calculator:
    @staticmethod
    def calculator(firstOperand, secondOperand, operator):
        result = 0
        match operator:
          case '+':
            result = firstOperand + secondOperand
          case '-':
            result = firstOperand - secondOperand
          case '*':
            result = firstOperand * secondOperand
          case '/':
            if secondOperand != 0:
                result = firstOperand/secondOperand
            else:
                raise ZeroDivisionError ('ошибка деление на 0 запрещено' )
          case _:
            raise Exception ('Неккорректный ввод')
        return result


    def calculate_discount(self, purchaseAmount, discountAmount) ->float:
        res = 0
        discount =0
        s = str(purchaseAmount).split('.')

        if type(purchaseAmount) != float or type(discountAmount) != int or  purchaseAmount <= 0 or discountAmount < 0\
                or discountAmount >= 100:
            raise ArithmeticError('Ошибка!Некорректный ввод данных')

        elif len(s[1]) > 2 or purchaseAmount < 0:
            raise ArithmeticError('Ошибка!Цена товара должна быть положительным числом с точностью до 2 знака')
        else:
            discount = Calculator.calculator(purchaseAmount,float(discountAmount),'*')
            discount = Calculator.calculator(discount, 100,'/')
            res = Calculator.calculator(purchaseAmount,discount,'-')
            res = (Decimal(res).quantize(Decimal('1.00')))
        return res



if __name__ == '__main__':


 def test_calculate_discount(purchaseAmount,discountAmount):
     assert_that(purchaseAmount).is_instance_of(float)
     assert_that(discountAmount).is_instance_of(int)
     assert_that(purchaseAmount).is_true()
     assert_that(discountAmount).is_true()
     assert_that(discountAmount < 100).is_true()
     assert_that(purchaseAmount > 0).is_true()
def test_calculate_discount2():
    assert_that(Calculator.calculate_discount(Calculator, 30.00, 50)).is_equal_to(15.00)




test_calculate_discount(115.9,14)

test_calculate_discount2()








