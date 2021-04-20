#Calculate the subject using the prefix


def findSubject(prefix):
  if prefix == 'ACC':
    subject = 'Accounting'
  if prefix == 'ANTHC':
    subject = 'Anthropology Culture'
  if prefix == 'ANTH':
    subject = 'Anthropology'
  if prefix == 'AFPRL':
    subject = 'Africana/PR/Latino St'
  if prefix == 'ARB':
    subject = 'Arabic'
  if prefix == 'WGSA':
    subject = 'Gender Literature and Arts'
  if prefix == 'IMA':
    subject = 'Arts Integrated Media'
  if prefix == 'ARTCR':
    subject = 'Art Creative'
  if prefix == 'ARTH':
    subject = 'Art History'
  if prefix == 'ARTLA':
    subject = 'Art Liberal Arts'
  if prefix == 'ASIAN':
    subject = 'Asian/Asian American Studies'
  if prefix == 'ASTRO':
    subject = 'Astronomy'
  if prefix == 'BIOCH':
    subject = 'Bio-Chemistry'
  if prefix == 'BIOL':
    subject = 'Biological Sciences'
  if prefix == 'BUS':
    subject = 'Business'
  if prefix == 'CLA':
    subject = 'Classical Culture/Archaeology'
  if prefix == 'CHEM':
    subject = 'Chemistry'
  if prefix == 'CHIN':
    subject = 'Chinese'
  if prefix == 'CSCI':
    subject = 'Computer Science'
  if prefix == 'COMPL':
    subject = 'Comparative Literature'
  if prefix == 'COMSC':
    subject = 'Communication Science'
  if prefix == 'COCO':
    subject = 'Counseling'
  if prefix == 'ADSUP' or prefix == 'CEDC' or prefix == 'SEDC':
    subject = 'Curriculum and Teaching'
  if prefix == 'DAN':
    subject = 'Dance'
  if prefix == 'ACSK':
    subject = 'Developmental Skills'
  if prefix == 'ECO':
    subject = 'Economics'
  if prefix == 'EDABA':
    subject = 'Education Applied Behavior'
  if prefix == 'ARTED':
    subject = 'Education Art'
  if prefix == 'BILED':
    subject = 'Education Bilingual'
  if prefix == 'CHND':
    subject = 'Education Chinese'
  if prefix == 'DANED':
    subject = 'Education Dance'
  if prefix == 'ECC' or prefix == 'SPEDE':
    subject = 'Education Early Childhood'
  if prefix == 'EDESL':
    subject = 'Educ English as Second Lang'
  if prefix == 'CEDF' or prefix == 'ECF' or prefix == 'EDPS' or prefix == 'SEDF':
    subject = 'Educational Foundation'
  if prefix == 'HED':
    subject = 'Health And Physical Education'
  if prefix == 'EDLIT':
    subject = 'Literacy Education'
  if prefix == 'LATED':
    subject = 'Education Latin'
  if prefix == 'COUNM':
    subject = 'Education Mental Health'
  if prefix == 'COUNR':
    subject = 'Education Rehab Counseling'
  if prefix == 'SPED':
    subject = 'Education Specialized'
  if prefix == 'SEDCP':
    subject = 'Education'
  if prefix == 'ENGL':
    subject = 'English'
  if prefix == 'WGST':
    subject = 'Feminist Thought and Theory'
  if prefix == 'FILM' or prefix == 'FILMP' or prefix == 'FILPL':
    subject = 'Film Studies'
  if prefix == 'FREN':
    subject = 'French'
  if prefix == 'PGEOG':
    subject = 'Geology and Geography'
  if prefix == 'GEOG':
    subject = 'Geography'
  if prefix == 'GEOL':
    subject = 'Geology'
  if prefix == 'WGSP':
    subject = 'Gender and Public Policy'
  if prefix == 'GERMN':
    subject = 'German'
  if prefix == 'GTECH':
    subject = 'Geography Technology'
  if prefix == 'GRK':
    subject = 'Greek'
  if prefix == 'GSR':
    subject = 'Graduate Social Research'
  if prefix == 'HEBR':
    subject = 'Hebrew'
  if prefix == 'HIST':
    subject = 'History'
  if prefix == 'HONS':
    subject = 'Honors Seminar'
  if prefix == 'HMBIO':
    subject = 'Human Biology'
  if prefix == 'HUM':
    subject = 'Humanities'
  if prefix == 'HR':
    subject = 'Human Rights'
  if prefix == 'ILBAK' or prefix == 'WGSI':
    subject = 'Independent Study'
  if prefix == 'ITAL':
    subject = 'Italian'
  if prefix == 'JPN':
    subject = 'Japanese'
  if prefix == 'JS':
    subject = 'Jewish Studies'
  if prefix == 'LACS':
    subject = 'Latin Amer/Caribbean Studi'
  if prefix == 'WGSL':
    subject = 'Labor, Migration/Globalization'
  if prefix == 'LAT':
    subject = 'Latin'
  if prefix == 'LING':
    subject = 'Linguistics'
  if prefix == 'LIBR':
    subject = 'Library Science'
  if prefix == 'ENRT':
    subject = 'Enroute Master'
  if prefix == 'MHC':
    subject = 'Macaulay Honors College'
  if prefix == 'MAM':
    subject = 'Maintenance of Matriculation'
  if prefix == 'MATH':
    subject = 'Mathematics'
  if prefix == 'MLS' or prefix == 'MLSP':
    subject = 'Medical Lab Science'
  if prefix == 'MEDIA' or prefix == 'MEDP' or prefix == 'MEDPL':
    subject = 'Media Studies'
  if prefix == 'MUSHL':
    subject = 'Music History And Literature'
  if prefix == 'MUSIN':
    subject = 'Music'
  if prefix == 'MUSPF':
    subject = 'Music Performance'
  if prefix == 'MUSTH':
    subject = 'Music Theory'
  if prefix == 'NFS':
    subject = 'Nutrition and Food Science'
  if prefix == 'NURS':
    subject = 'Nursing'
  if prefix == 'NUTR':
    subject = 'Nutrition'
  if prefix == 'ONFIL':
    subject = 'On File'
  if prefix == 'PERM':
    subject = 'Permit'
  if prefix == 'PHILO':
    subject = 'Philosophy'
  if prefix == 'PT':
    subject = 'Physical Therapy'
  if prefix == 'PHYS':
    subject = 'Physics'
  if prefix == 'POL':
    subject = 'Polish'
  if prefix == 'PORT':
    subject = 'Portuguese'
  if prefix == 'POLSC':
    subject = 'Political Science'
  if prefix == 'PSYCH':
    subject = 'Psychology'
  if prefix == 'PH':
    subject = 'Public Health'
  if prefix == 'PUPOL':
    subject = 'Public Policy'
  if prefix == 'REL':
    subject = 'Religion Studies'
  if prefix == 'RAS':
    subject = 'Russian Area Studies'
  if prefix == 'RUSS':
    subject = 'Russian'
  if prefix == 'SCI':
    subject = 'Science'
  if prefix == 'SSW':
    subject = 'School of Social Work'
  if prefix == 'WGSS':
    subject = 'Sexuality'
  if prefix == 'SOC':
    subject = 'Sociology'
  if prefix == 'SOSCI':
    subject = 'Social Science'
  if prefix == 'SW':
    subject = 'Social Work'
  if prefix == 'SPAN':
    subject = 'Spanish'
  if prefix == 'STABD':
    subject = 'Study Abroad'
  if prefix == 'STAT':
    subject = 'Statistics'
  if prefix == 'THEA':
    subject = 'Theatre And Cinema'
  if prefix == 'THC':
    subject = 'Theatre And Film'
  if prefix == 'TRN':
    subject = 'Translation'
  if prefix == 'URBG':
    subject = 'Urban Affairs'
  if prefix == 'URBP':
    subject = 'Urban Planning'
  if prefix == 'URBS':
    subject = 'Urban Studies'
  if prefix == 'WGSC':
    subject = 'Women/Gender Across Cultures'
  if prefix == 'WGS':
    subject = 'Women and Gender Studies'

  return subject