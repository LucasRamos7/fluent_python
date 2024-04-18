if __name__ == '__main__':
    # Latitude and longitude of the Los Angeles International Airport
    lax_coordinates = (33.9425, -118.408056)
    # Data about Tokyo
    city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
    # A list of tuples of the form (country_code, passport_number)
    traveler_ids = [('USA', 31195855), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for passport in sorted(traveler_ids):
        # The % formatting operator understands tuples and treats each item as a separate field
        print('%s/%s' % passport)

    for country, _ in traveler_ids:
        print(country)