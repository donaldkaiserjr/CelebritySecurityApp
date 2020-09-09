class Incident:
    
    def __init__(self, offender_sex, incident_location, inc_city, inc_state, 
    incident_type, date, celeb_fname, celeb_lname, offender_fname, offender_lname, 
    offender_age, d_license, police_disp, officer_fname, officer_lname, police_dept):
        self.offender_sex = offender_sex
        self.incident_location = incident_location
        self.inc_city = inc_city
        self.inc_state = inc_state
        self.incident_type = incident_type
        self.date = date
        self.celeb_fname = celeb_fname
        self.celeb_lname = celeb_lname
        self.offender_fname = offender_fname
        self.offender_lname = offender_lname
        self.offender_age = offender_age
        self.d_license = d_license
        #boolean: True if police were dispatched
        self.police_disp = police_disp
        self.officer_fname = officer_fname
        self.officer_lname = officer_lname
        self.police_dept = police_dept

    @property
    def offender_full_name(self):
        return '{} {}'.format(self.offender_fname, self.offender_lname)

    @property
    def celebrity_full_name(self):
        return '{} {}'.format(self.celeb_fname, self.celeb_lname)
    
    @property
    def officer_full_name(self):
        return '{} {}'.format(self.officer_fname, self.officer_lname)

    def __repr__(self):
        return "Incident('{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', {}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.offender_sex, self.incident_location, self.inc_city, self.inc_state, self.incident_type, self.date, self.celeb_fname, self.celeb_lname, self.offender_fname, self.offender_lname, self.offender_age, self.d_license, self.police_disp, self.officer_fname, self.officer_lname, self.police_dept)

    def __str__(self):
        return 'On {} {} {} was involved in {} by offender: {} {} at  LOCATION: {}   CITY: {}   STATE: {}'.format(self.date, self.celeb_fname, self.celeb_lname, self.incident_type, self.offender_fname, self.offender_lname, self.incident_location, self.inc_city, self.inc_state)

    def __len__(self):
        return len(self.offender_full_name)

    def __len__(self):
        return len(self.celebrity_full_name)

    def __len__(self):
        return len(self.officer_full_name)
 
class Celebrity(Incident):

    def __init__(self, offender_sex, incident_location, inc_city, inc_state, 
    incident_type, date, celeb_fname, celeb_lname, offender_fname, offender_lname, 
    offender_age, d_license, police_disp, officer_fname, officer_lname, police_dept):
        
        Incident.__init__(self, offender_sex, incident_location, inc_city, 
        inc_state, incident_type, date, celeb_fname, celeb_lname, 
        offender_fname, offender_lname, offender_age, d_license, police_disp, 
        officer_fname, officer_lname, police_dept)
