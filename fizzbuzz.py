class FizzBuzz():
    def is_mod_by_3(self, number):
        return number % 3 == 0

    def is_mod_by_5(self, number):
        return number % 5 == 0

    def is_mod_by_15(self, number):
        return self.is_mod_by_3(number) and self.is_mod_by_5(number)

    def count(self, number):
        if self.is_mod_by_15(number):
            return 'fizzbuzz'

        if self.is_mod_by_3(number):
            return 'fizz'

        if self.is_mod_by_5(number):
            return 'buzz'

        return str(number)
