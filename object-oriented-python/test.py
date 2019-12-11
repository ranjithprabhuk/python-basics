class Customer:
    def __init__(self):
        self.__cust_id = None
        self.__cust_name = None

    def get_cust_id(self):
        print("Normal customer")

    def get_cust_name(self):
        return self.__cust_name

    def set_cust_id(self, value):
        self.__cust_id = value

    def set_cust_name(self, value):
        self.__cust_name = value

class PrivilegedCustomer(Customer):
    def __init__(self):
        super().__init__()
        self.__overdraft_limit = None

    def get_overdraft_limit(self):
        return self.__overdraft_limit

    def set_overdraft_limit(self, value):
        self.__overdraft_limit = value

    def get_cust_id(self):
        print("Privileged Customer")

class RegularCustomer(Customer):
    def __init__(self):
        super().__init__()
        self.__min_balance = None

    def get_min_balance(self):
        return self.__min_balance

    def set_min_balance(self, value):
        self.__min_balance = value

r=RegularCustomer()
p=PrivilegedCustomer()
r.get_cust_id()
p.get_cust_id()