import re
txt="The rain in Spain"
x=re.findall("[a-d]",txt)
print(x)




import re
txt="The rain in Spain"
x=re.findall("[^a-z]",txt)
print(x)



import re
txt="The rain in Spain"
x=re.findall("[^a-zA-Z]",txt)
print(x)


import re
txt="The ra16283in in Sp4a9i6n"
x=re.findall("[0-9][0-9]",txt)
print(x)



import re
txt="The ra16283in in Sp4a95872i6n"
x=re.findall("[0-9][0-9]",txt)
print(x)

import re
txt="The ra16283in in Sp4a9i6n"
x=re.findall("[0-7]",txt)
print(x)


import re
txt="The ra169in in Sp4a95872i6n"
x=re.findall("[0-9]{3}",txt)
print(x)



import re
txt="The ra169in in Sp4a95872i6n"
x=re.findall("[0-9]+",txt)
print(x)


import re
txt="The ra169in in Sp4a95872i6n"
x=re.findall("[0-9]*",txt)
print(x)

import re
txt="The ra169in in Sp4a95872i6n"
x=re.findall("[0-9]?",txt)
print(x)