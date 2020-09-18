class Offender:
    def __init__(self, offender_fname, offender_lname, off_sex, off_age, off_d_license, date):
        self.offender_fname = offender_fname
        self.offender_lname = offender_lname
        self.off_sex = off_sex
        self.off_age = off_age
        self.off_d_license = off_d_license
        self.date = date

    @property
    def offender_full_name(self):
        return '{} {}'.format(self.offender_fname, self.offender_lname)

    def __repr__(self):
        return "Offender('{}', '{}', '{}', '{}', '{}', '{}')".format(self.offender_fname, self.offender_lname, self.off_sex, self.off_age, self.off_d_license, self.date)

class Security(Offender):
    
    def __init__(self, offender_fname, offender_lname, off_sex, off_age, 
    off_d_license, date, officer_fname, officer_lname, officer_id, company, celebrity, incident_type, 
    incident_location, incident_city, incident_state, police_disp):
        
        super().__init__(offender_fname, offender_lname, off_sex, off_age, off_d_license, date)
        self.officer_fname = officer_fname
        self.officer_lname = officer_lname
        self.officer_id = officer_id
        self.company = company
        self.celebrity = celebrity
        self.incident_type = incident_type
        self.incident_location = incident_location
        self.incident_city = incident_city
        self.incident_state = incident_state
        #boolean: True if police were dispatched
        self.police_disp = police_disp

    @property
    def officer_full_name(self):
        return '{} {}'.format(self.officer_fname, self.officer_lname)

    def __repr__(self):
        return "Security('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.officer_fname, self.officer_lname, self.officer_id, self.company, self.celebrity, self.incident_type, self.incident_location, self.incident_city, self.incident_state, self.police_disp)
        
    def __str__(self):
        return 'On {} {} was involved in {} by offender: {} {} at  LOCATION: {}   CITY: {}   STATE: {}'.format(self.date, self.celebrity, self.incident_type, self.offender_fname, self.offender_lname, self.incident_location, self.incident_city, self.incident_state)

    def __len__(self):
        return len(self.officer_full_name)


    
ricky_martin1 = Security("Justin", "Newton", "male", 24, "B111233", 20190904, "Gary", "Lang", 9933448, "A1 Security", "Justin Bieber", "Stage Trespass", "Staples", "Los Angeles", "CA", True)
print(repr(ricky_martin1))
