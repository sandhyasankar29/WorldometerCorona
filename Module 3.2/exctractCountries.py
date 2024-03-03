import sys
import os

current_directory = os.getcwd()
directory_components = current_directory.split(os.sep)
new_directory_components = directory_components[:-1]
new_directory = os.sep.join(new_directory_components)
rel_path=os.path.join(new_directory,f'./Module 2/Module 2.3')
sys.path.insert(1, rel_path)
rel_path=os.path.join(new_directory,f'./Module 2/Module 2.3/India')
sys.path.insert(1, rel_path)

from Australia import getLinksAustralia
from England import getLinksEngland
from India import ProcessPage
from Malaysia import getLinksMalaysia
from Singapore import getLinksSingapore

ProcessPage.getTimelineData()
countries = ['Australia', 'England', 'India', 'Malaysia', 'Singapore']

getLinksAustralia.main()
getLinksEngland.main()

getLinksMalaysia.main()
getLinksSingapore.main()