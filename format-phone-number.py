import re
def convert_phone_number(phone):
  phonenum = re.search(r'(\d){3}-?\s?(\d){3}-?\s?(\d){4}', phone)
  phonegroup = re.split(r'-|\s', phonenum[0])
  result = re.sub(r'(\d){3}-?\s?(\d){3}-?\s?(\d){4}', f'({phonegroup[0]}) {phonegroup[1]}-{phonegroup[2]}', phone)
  return result

print(convert_phone_number("Phone number of Buckingham Palace is 303 123 7300"))
