import os


class Vehicle:

    def __int__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def add_vehicle(self):
        inventory_file = open('inventory.txt', 'a+')
        make = input('Enter make:')
        model = input('Enter model:')
        color = input('Enter color:')
        while True:
            year = input('Enter year (Must be numerical):')
            try:
                val = int(year)
                break
            except ValueError:
                print('You can only enter numbers! Try again!')

        while True:
            mileage = input('Enter mileage:')
            try:
                val = int(mileage)
                break
            except ValueError:
                print('You can only enter numbers! Try again!')

        with open('inventory.txt') as f:
            line_count = 0
            for line in f:
                line_count += 1
        line_count += 1

        inventory_file.write(make + ', ' + model + ', ' + color + ', ' + str(year) + ', ' + str(mileage) + '\n')
        inventory_file.close()

        print('Vehicle successfully added')

    def update_vehicle(self):

        with open('inventory.txt') as f:
            line_count = 0
            for line in f:
                line_count += 1
                print(str(line_count) + ': ' + line)

        del_vehicle = int(input('Enter number of the record you would like to update: '))

        new_data = open('inventory.txt', 'r')
        remove = new_data.readlines()
        new_data.close()

        del remove[del_vehicle - 1]
        new_file = open('inventory.txt', 'w+')
        for line in remove:
            new_file.write(line)
        new_file.close()

        Vehicle.add_vehicle(Vehicle)

        inventory_file = open('inventory.txt', 'r')

    def view_vehicle(self):
        inventory_file = open('inventory.txt', 'r')
        output = inventory_file.read()

        print(output)
        inventory_file.close()

    def remove_vehicle(self):
        with open('inventory.txt') as f:
            line_count = 0
            for line in f:
                line_count += 1
                print(str(line_count) + ': ' + line)

        del_vehicle = int(input('Enter number of the record you would like to delete:'))

        new_data = open('inventory.txt', 'r')
        remove = new_data.readlines()
        new_data.close()

        del remove[del_vehicle - 1]
        new_file = open('inventory.txt', 'w+')
        for line in remove:
            new_file.write(line)
        new_file.close()


        print('Vehicle record successfully removed')


def main():
    user = True
    while user:
        print("1. Add vehicle\n"
              "2. Remove vehicle\n"
              "3. Update vehicle\n"
              "4. View Contents of inventory file\n"
              "5. Export inventory file\n"
              "6. Quit")

        command = input("Please make a selection:")
        print()

        if command == '1':
            Vehicle.add_vehicle(Vehicle)
        elif command == '2':
            Vehicle.remove_vehicle(Vehicle)
        elif command == '3':
            Vehicle.update_vehicle(Vehicle)
        elif command == '4':
            Vehicle.view_vehicle(Vehicle)
        elif command == '5':
            directory = os.getcwd()
            print('Inventory record exported to ' + directory + '\\' + 'inventory.txt')
        elif command == '6':
            print('Goodbye!')
            user = False
        else:
            print('That is not a valid input, please try again!')


if __name__ == '__main__':
    main()
