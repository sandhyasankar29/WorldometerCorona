from Australia import getLinksAustralia
from England import getLinksEngland
from India import ProcessPage
from Malaysia import getLinksMalaysia
from Singapore import getLinksSingapore

countries = ['Australia', 'England', 'India', 'Malaysia', 'Singapore']
for i in range(0,5):
    print(f"{i+1}. {countries[i]}")
while(True):
    try:
        ch=int(input("Enter a choice in range 1 to 5 to select the country"))-1
        if(ch<0 or ch>4):
            raise ValueError
        break
    except:
        print("Expected value in range 1 to 5")

if(ch == 0):
    getLinksAustralia.main()
elif(ch == 1):
    getLinksEngland.main()
elif(ch == 2):
    ProcessPage.getTimelineData()
elif(ch == 3):
    getLinksMalaysia.main()
elif(ch == 4):
    getLinksSingapore.main()