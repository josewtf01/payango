class official_document:
    """docstring for [object Object]."""
    def __init__(self, name = "walter", email ='ya@gmail.com',
        card_number= '3333-4444-2222-1111', direction = 'Verde Valle, 44550 Guadalajara, Jal.',
        curp = 'EIAG850616HMSNGV06'):
        self.name = name
        self.email = email
        self.card_number = card_number
        self.direction = direction
        self.curp = curp
    def show_name(self):
        return self.name
    def show_email(self):
        return self.email
    def show_card_num(self):
        return self.card_number
    def show_direction(self):
        return self.direction
    def show_curp(self):
        return self.curp
