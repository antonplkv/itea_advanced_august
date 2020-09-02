class Phone:

    def __init__(self, model, imei):
        self.model = model
        self.imei = imei

    def call(self, number):
        print(f'Calling to {number} from {self.model}')


class Smartphone(Phone):

    def call(self, number):
        print('Looking for number in contacts book')
        print(f'Trying to call {number} from {self.model} {self.imei}')
        print('The end of call')

    def send_message(self, number):
        print(f'Sending message to {number} from {self.model}')

    def send_message_in_telegram(self, user_id):
        print(f'Sending message in telegram to {user_id} from {self.model}')


huawei = Smartphone('huawei', 'zzzzzzzzzz')
huawei.call('+380312312312')
huawei.send_message('+380312312312')
huawei.send_message_in_telegram(312312)

nokia = Phone('Nokia', 'qweqwe12321312321')
nokia.imei = '21312312312312'
print(nokia.imei)

nokia.call('+380966666666')

siemens = Phone('siemens', 'weqweqweqweqweqw')
print(siemens.imei)
siemens.call('+380912312312')

