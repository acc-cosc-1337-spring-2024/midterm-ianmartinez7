#write functions here, don't add input('') statements here!



def get_assessment_value(assessment_value):
    assessment_value *= 0.60
    return assessment_value

def get_tax_assessement_value(assessment_value):
    tax_rate_per_hundred = 0.72
    property_tax_value = (assessment_value / 100) * tax_rate_per_hundred
    rounded_tax_value = round(property_tax_value, 2)
    return rounded_tax_value


