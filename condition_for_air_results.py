# The value for air quality index is taken to let you know about the results of safety
class Calc:
    def __init__(self,air_quality_index):
        self.x=air_quality_index

    def is_air_safe(self):
        want_to_know = input(
            "Do you want to know if the air is fit for inhalation? Type 'Y' for Yes and 'N' for 'No:\n").upper()
        if want_to_know=='Y':
            if self.x>301:
                print("---> The 'Quality Of Air' around you is Hazardous.")
            elif self.x>201:
                print("---> The 'Quality Of Air' around you is Very Unhealthy.")
            elif self.x>151:
                print("---> The 'Quality Of Air' around you is Unhealthy.")
            elif self.x>101:
                print("---> The 'Quality Of Air' around you is Unhealthy for sensitive groups.")
            elif self.x>51:
                print("---> The 'Quality Of Air' around you is Moderately Bad.")
            elif self.x>0:
                print("---> The 'Quality Of Air' around you is Good.")
