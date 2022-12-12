class MathTables:
    def __init__(self, no_of_table, end_value):
        self.no_of_table = no_of_table
        self.end_value = end_value

    def multiplication_table(self):
        for i in range(1, self.no_of_table + 1):
            print('Multiplication table of ', i)
            for j in range(1, self.end_value +1): 
                print(f'{j} * {i} = {i * j}')

n = int(input('number of tables: '))        
m1 = MathTables(n, 10)

m1.multiplication_table()
