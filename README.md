# Scraping-ngodarpan.gov.in-with-Beautiful-Soup
The NGO-DARPAN is a platform that provides space for interface between VOs/NGOs and key Government Ministries / Departments / Government Bodies, to start with. Later it is proposed to cover all Central Ministries / Departments / Government Bodies.
This is a free facility offered by the NITI Aayog in association with National Informatics Centre to bring about greater partnership between government & voluntary sector and foster better transparency, efficiency and accountability.
The NGO-DARPAN started out as an initiative of the Prime Minister's Office, to create and promote a healthy partnership between VOs/NGOs and the Government of India. The Portal is managed at present by NITI Aayog.There are 77553 ngos registered in this portal 

The url is https://ngodarpan.gov.in/index.php/search/. You have to install some open-source external libraries like BeautifulSoup,requests,csv etc.I have implemented the code in such a way that we can extract the data of 77553 ngos by running the code once.If anyone want to extract data based on preferences like state-wise,sector-wise,just edit the data variable in the code accordingly.The Data is given in the repository.

## Package install
sudo pip3 install package-name

## Run the code
python3 ngo_new.py
