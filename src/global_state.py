class GlobalState:
    def __init__(self):
        
        self.user = {
            "login": None,
            "password": None,
            "fio": None,
            "email": None,
            "phone_number": None,
        }
        
        self.current_target = {
            "name": None,
            "latitude_max": None,
            "longitude_min": None,
            "latitude_min": None,
            "longitude_max": None,
        }

        self.targets_list = []

global_state = GlobalState()