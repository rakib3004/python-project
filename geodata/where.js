myData = [
[50.06688579999999,19.9136192, 'aleja Adama Mickiewicza 30, 30-059 Kraków, Poland'],
[52.2394019,21.0150792, 'Krakowskie Przedmieście 5, 00-068 Warszawa, Poland'],
[30.0189275,31.499707, 'AUC Avenue، Road، First New Cairo, Cairo Governorate 11835, Egypt'],
[33.4532165,-112.0719833, 'Phoenix, AZ 85004, USA'],
[39.3301047,-82.1076022, 'Athens, OH 45701, USA'],
[28.3588163,75.58802039999999, 'Vidya Vihar, Pilani, Rajasthan 333031, India'],
[6.8939569,3.7187158, 'Ilishan-Remo, Nigeria'],
[25.2677203,82.99125819999999, 'Ajagara, Varanasi, Uttar Pradesh 221005, India'],
[12.9503878,77.5022224, 'Mysore Rd, Jnana Bharathi, Bengaluru, Karnataka 560056, India'],
[31.5488923,-97.1130573, '1311 S 5th St, Waco, TX 76706, USA'],
[39.9619537,116.3662615, '19 Xinjiekou Outer St, Bei Tai Ping Zhuang, Haidian Qu, Beijing Shi, China, 100875'],
[53.8938988,27.5460609, 'praspiekt Niezaliežnasci 4, Minsk, Belarus'],
[44.8184518,20.4575913, 'Studentski trg 1, Beograd, Serbia'],
[42.5030333,-89.0309048, '700 College St, Beloit, WI 53511, USA'],
[53.8938988,27.5460609, 'praspiekt Niezaliežnasci 4, Minsk, Belarus'],
[43.76908419999999,-79.4692584, '1000 Finch Ave W, North York, ON M3J 2V5, Canada'],
[10.6779085,78.74454879999999, 'Palkalaiperur, Tiruchirappalli, Tamil Nadu 620024, India'],
[42.3504997,-71.1053991, 'Boston, MA 02215, USA'],
[35.3050053,-120.6624942, 'San Luis Obispo, CA 93407, USA'],
[34.1813584,-117.3231875, '5500 University Pkwy, San Bernardino, CA 92407, USA'],
[51.5210038,-0.1746353, '25 Paddington Green, London W2 1NB, UK'],
[40.8075355,-73.9625727, 'New York, NY 10027, USA'],
[52.0746136,-0.6282833, 'College Rd, Cranfield, Wharley End, Bedford MK43 0AL, UK'],
[50.1030364,14.3912841, '166 36 Prague 6, Czechia'],
[43.7044406,-72.2886935, 'Hanover, NH 03755, USA'],
[37.3192827,-122.0447913, '21250 Stevens Creek Blvd, Cupertino, CA 95014, USA'],
[51.377114,7.494838999999999, 'Universitätsstraße 11, 58097 Hagen, Germany'],
[48.4331922,35.0427966, 'Haharina Ave, 72, Dnipropetrovsk, Dnipropetrovska oblast, Ukraine, 49000'],
[38.430691,27.13692, 'No: 144 35210, Alsancak, Cumhuriyet Blv, 35220 Konak/İzmir, Turkey'],
[39.9566127,-75.18994409999999, '3141 Chestnut St, Philadelphia, PA 19104, USA'],
[30.2849185,-97.7340567, 'Austin, TX 78712, USA'],
[36.0014258,-78.9382286, 'Durham, NC 27708, USA'],
[45.7864448,4.7641329, '23 Avenue Guy de Collongue, 69130 Écully, France'],
[48.709445,2.1661629, 'CentraleSupélec, 3 Rue Joliot Curie, 91190 Gif-sur-Yvette, France'],
[36.1026877,-79.5023313, '50 Campus Drive, Elon, NC 27244, USA'],
[55.4877012,8.4469108, 'Spangsbjerg Kirkevej 103, 6700 Esbjerg, Denmark'],
[-2.1480702,-79.9644896, 'Vía Perimetral 5, Guayaquil, Ecuador'],
[51.24683899999999,6.7916647, 'Münsterstraße 156, 40476 Düsseldorf, Germany'],
[47.7233835,13.0871253, 'Urstein Süd 1, 5412 Puch bei Hallein, Austria'],
[-23.6956191,-46.5469041, 'Av. Pereira Barreto, 400 - Vila Baeta Neves - Centro, São Bernardo do Campo - SP, 09751-000, Brazil'],
[45.2461012,19.8516968, 'Trg Dositeja Obradovića 6, Novi Sad 106314, Serbia'],
[40.7529512,-73.4267093, '2350 NY-110, Farmingdale, NY 11735, USA'],
[-19.870682,-43.9677359, 'Av. Pres. Antônio Carlos, 6627 - Pampulha, Belo Horizonte - MG, 31270-901, Brazil'],
[26.3749876,-80.10106329999999, '777 Glades Rd, Boca Raton, FL 33431, USA'],
[42.7789743,-72.05553929999999, '40 University Dr, Rindge, NH 03461, USA'],
[26.1562123,91.66148539999999, 'Gopinath Bordoloi Nagar, Jalukbari, Guwahati, Assam 781014, India'],
[38.8298118,-77.3073606, '4400 University Dr, Fairfax, VA 22030, USA'],
[38.8977953,-77.0129087, '600 New Jersey Ave NW, Washington, DC 20001, USA'],
[33.753068,-84.38528190000001, 'Atlanta, GA 30302, USA'],
[42.9097484,-85.7630885, 'Grandville, MI, USA'],
[50.87485419999999,4.7077677, 'Andreas Vesaliusstraat 13, 3000 Leuven, Belgium'],
[21.005603,105.8434525, '1 Đại Cồ Việt, Bách Khoa, Hai Bà Trưng, Hà Nội, Vietnam'],
[31.7945578,35.2414009, 'Jerusalem'],
[17.4448649,78.34981379999999, 'Professor CR Rao Rd, Gachibowli, Hyderabad, Telangana 500032, India'],
[26.5123388,80.2329, 'Kalyanpur, Kanpur, Uttar Pradesh 208016, India'],
[59.3954004,24.6641777, 'Raja 4, 12616 Tallinn, Estonia'],
[39.1754487,-86.512627, '107 S Indiana Ave, Bloomington, IN 47405, USA'],
[45.4377574,12.3223297, 'Santa Croce, 191, 30135 Venezia VE, Italy'],
[41.8348731,-87.6270059, '10 W 35th St, Chicago, IL 60616, USA'],
[40.5120479,-88.9931683, '100 N University St, Normal, IL 61761, USA'],
[28.5449756,77.19262839999999, 'IIT Campus, Hauz Khas, New Delhi, Delhi 110016, India'],
[22.3149274,87.31053109999999, 'Kharagpur, West Bengal 721302, India'],
[23.8142953,86.44118069999999, 'Police Line Road, Main Campus IIT (ISM, near Rani Bandh, IIT (ISM, Hirapur, Sardar Patel Nagar, Dhanbad, Jharkhand 826004, India'],
[39.1754487,-86.512627, '107 S Indiana Ave, Bloomington, IN 47405, USA'],
[39.1754487,-86.512627, '107 S Indiana Ave, Bloomington, IN 47405, USA'],
[45.4948236,-73.5623366, '1100 Rue Notre-Dame Ouest, Montréal, QC H3C 1K3, Canada'],
[39.106401,-76.95158099999999, '15319 Briarcliff Manor Way, Burtonsville, MD 20866, USA'],
[18.4880037,-69.96249499999999, 'Av. de Los Próceres 49, Santo Domingo 10602, Dominican Republic'],
[17.4448649,78.34981379999999, 'Professor CR Rao Rd, Gachibowli, Hyderabad, Telangana 500032, India'],
[52.2766643,104.2777445, 'Karl Marx St, 1, Irkutsk, Irkutskaya oblast, Russia, 664003'],
[22.5811617,88.3905995, '1, 12, CIT Rd, Bidhannagar, Kolkata, West Bengal 700054, India'],
[17.4932682,78.3913929, 'Ashok Nagar, Kukatpally Housing Board Colony, Kukatpally, Hyderabad, Telangana 500085, India'],
[28.5402232,77.1662154, 'New Mehrauli Road, JNU Ring Rd, New Delhi, Delhi 110067, India'],
[32.4950392,35.9912257, 'Ar Ramtha 3030، Ar-Ramtha, Jordan'],
[39.1974437,-96.5847249, 'Manhattan, KS 66506, USA'],
[35.723988,46.707924, 'Kol, Kurdistan Province, Iran'],
[42.290035,-85.598145, '1200 Academy St, Kalamazoo, MI 49006, USA'],
[54.898991,23.912825, 'K. Donelaičio g. 73, Kaunas 44249, Lithuania'],
[54.898991,23.912825, 'K. Donelaičio g. 73, Kaunas 44249, Lithuania'],
[55.790447,49.1214349, 'Kremlyovskaya St, 18, Kazan, Respublika Tatarstan, Russia, 420008'],
[41.1455594,-81.33928829999999, '800 E Summit St, Kent, OH 44240, USA'],
[49.9958165,36.241777, 'Marshala Bazhanova St, 17, Kharkiv, Kharkivska oblast, Ukraine, 61000'],
[13.65117,100.4966439, '126 Pracha Uthit Rd, Khwaeng Bang Mot, Khet Thung Khru, Krung Thep Maha Nakhon 10140, Thailand'],
[53.285023,69.3695728, 'Kokshetau 020000, Kazakhstan'],
[50.4491699,30.4561487, 'Peremohy Ave, 37, Kyiv, Ukraine, 03056'],
[50.4491699,30.4561487, 'Peremohy Ave, 37, Kyiv, Ukraine, 03056'],
[50.4420868,30.5104023, 'Volodymyrska St, 60, Kyiv, Ukraine, 01033'],
[46.4702636,-80.9734288, '935 Ramsey Lake Rd, Sudbury, ON P3E 2C6, Canada'],
[34.068921,-118.4451811, 'Los Angeles, CA 90095, USA'],
[51.7537146,19.4517176, 'Stefana Żeromskiego 116, 90-924 Łódź, Poland'],
[49.8406108,24.0225099, 'Universytetska St, 1, Lviv, Lvivska oblast, Ukraine, 79000'],
[42.701848,-84.4821719, 'Michigan, USA'],
[13.0660293,80.28317190000001, 'Navalar Nagar, Chepauk, Triplicane, Chennai, Tamil Nadu 600005, India'],
[53.4222397,58.9824868, 'Prospekt Lenina, 38, Magnitogorsk, Chelyabinskaya oblast, Russia, 455000'],
[34.304073,48.8452846, 'Hamadan Province, Malayer, University Blvd, Iran'],
[39.4164811,-81.4498947, '215 5th St, Marietta, OH 45750, USA'],
[24.4326227,54.6184724, 'Near Home WTC AUH, Airport Road - مدينة مصدر - أبو ظبي - United Arab Emirates'],
[44.8199188,20.4587075, 'Studentski trg 16, Beograd 105104, Serbia'],
[42.701848,-84.4821719, 'Michigan, USA'],
[39.88983820000001,32.780086, 'Üniversiteler, Dumlupinar Bulvari 1/6-133, 06800 Çankaya/Ankara, Turkey'],
[37.9537078,-91.7756271, '106, Parker Hall, 300 W 13th St, Rolla, MO 65409, USA'],
[-37.9109574,145.1371751, 'Wellington Rd, Clayton VIC 3800, Australia'],
[-37.9109574,145.1371751, 'Wellington Rd, Clayton VIC 3800, Australia'],
[-38.311211,146.429409, 'Northways Rd, Churchill VIC 3842, Australia'],
[25.6515649,-100.28954, 'Av. Eugenio Garza Sada 2501 Sur, Tecnológico, 64849 Monterrey, N.L., Mexico'],
[55.6502051,37.6643098, 'Kashira Hwy, 31, Moskva, Russia, 115409'],
[55.9297243,37.5199434, 'Institutskiy Pereulok, 9, Dolgoprudny, Moskovskaya oblast, Russia, 141701'],
[55.70393490000001,37.5286696, 'Ulitsa Kolmogorova, 1, Moskva, Russia, 119991'],
[22.253537,84.90182639999999, 'Bisra Rd, National Institute of Technology, Jindal Colony, Udit Nagar, Rourkela, Odisha 769001, India'],
[40.72951339999999,-73.9964609, 'New York, NY 10003, USA'],
[21.1468555,79.050062, 'Amravati Rd, Ram Nagar, Nagpur, Maharashtra 440033, India'],
[1.3483099,103.6831347, '50 Nanyang Ave, Singapore 639798'],
[31.3958746,75.5358439, 'Grand Trunk Road, Barnala - Amritsar Bypass Rd, Jalandhar, Punjab 144011, India'],
[25.0173405,121.5397518, 'No. 1, Section 4, Roosevelt Rd, Da’an District, Taipei City, Taiwan 10617'],
[-12.0231787,-77.04763009999999, 'Av. Túpac Amaru 210, Rímac 15333, Peru'],
[41.772663,-88.1440142, '30 N Brainard St, Naperville, IL 60540, USA'],
[42.3398067,-71.0891717, '360 Huntington Ave, Boston, MA 02115, USA'],
[42.0564594,-87.67526699999999, '633 Clark St, Evanston, IL 60208, USA'],
[55.13719099999999,36.6070589, 'Obninsk, Kaluga Oblast, Russia, 249034'],
[36.8858594,-76.3057051, '5115 Hampton Blvd, Norfolk, VA 23529, USA'],
[42.2573474,-121.7849109, '3201 Campus Dr, Klamath Falls, OR 97601, USA'],
[19.4436005,-70.6843785, 'Autopista Duarte Km 1 1/2, Santiago De Los Caballeros 51000, Dominican Republic'],
[35.8012314,51.5028533, 'Tehran Province, Tehran, اتوبان ارتش کوی نفت, Nakhl St, Iran'],
[40.7982133,-77.8599084, 'State College, PA 16801, USA'],
[45.4784315,9.228342399999999, 'Piazza Leonardo da Vinci, 32, 20133 Milano MI, Italy'],
[44.4386064,26.0494925, 'Splaiul Independenței 313, București 060042, Romania'],
[45.7536393,21.2251615, 'Piața Victoriei 2, Timișoara 300006, Romania'],
[12.0182619,79.8568461, 'Pondicherry University, Chinna Kalapet, Kalapet, Puducherry 605014, India'],
[-33.44180680000001,-70.6399544, 'Av Libertador Bernardo OHiggins 340, Santiago, Región Metropolitana, Chile'],
[45.5111471,-122.6834235, '1825 SW Broadway, Portland, OR 97201, USA'],
[39.7743174,-86.1764194, '420 University Blvd, Indianapolis, IN 46202, USA'],
[12.9237228,77.4987012, 'Mysore Rd, RV Vidyaniketan, Post, Bengaluru, Karnataka 560059, India'],
[42.7297628,-73.67888839999999, '110 8th St, Troy, NY 12180, USA'],
[41.081015,-74.1745057, '505 Ramapo Valley Rd, Mahwah, NJ 07430, USA'],
[43.0844955,-77.6749311, '1 Lomb Memorial Dr, Rochester, NY 14623, USA'],
[10.7285131,79.0184111, 'Trichy-Tanjore Road, Thirumalaisamudram, Thanjavur, Tamil Nadu 613401, India'],
[59.941894,30.2989199, 'University Embankment, 7/9, Sankt-Peterburg, Russia, 199034'],
[59.929491,30.2966081, 'Bolshaya Morskaya Ulitsa, 67, Sankt-Peterburg, Russia, 190000'],
[60.0076235,30.3731954, 'Politekhnicheskaya Ulitsa, 29, Sankt-Peterburg, Russia, 195251'],
[37.7241492,-122.4799405, '1600 Holloway Ave, San Francisco, CA 94132, USA']
];
